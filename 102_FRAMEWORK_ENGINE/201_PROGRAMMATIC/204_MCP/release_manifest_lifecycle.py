"""Trusted source publication with independent plain Journal logging.

This module owns neither a Workflow Run nor a private lifecycle ledger.  It
adapts the publisher to the existing generic Work Journal and to the opaque,
host-created publication authorization context.
"""
from __future__ import annotations

from contextlib import contextmanager
import re
import datetime as dt
import hashlib
import json
from pathlib import Path
import sys
from typing import Any, Mapping

MCP = Path(__file__).resolve().parent
TOOLS = MCP.parent / "201_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import work_journal  # noqa: E402
from release_manifest_authorization import (  # noqa: E402
    PublicationAuthorizationContext,
    ReleaseManifestAuthorizationError,
    validate_candidate_payload,
    validate_public_manifest_candidate_payload,
    validate_refresh_candidate_payload,
    validate_public_manifest_context,
    validate_publication_context,
    validate_refresh_context,
)
from selected_routes import SELECTED_ROUTE_NAMES  # noqa: E402
from engine_publication_lock import engine_publication_lock  # noqa: E402


ACTION_ID = "MCP_RELEASE_MANIFEST_PUBLICATION"
STRUCTURAL_SCOPE = "MCP"
_REFRESH_ROUTE_NAMES = (*SELECTED_ROUTE_NAMES, "release_version")
_O030_REFRESH_ROUTE_NAMES = (*_REFRESH_ROUTE_NAMES, "public.release")
_O030_REFRESH_PLAN_FIELDS = frozenset({
    "source_refresh_schema_version", "source_refresh_registration_id",
})
_O030_REFRESH_SCHEMA_VERSIONS = frozenset({4, 5})


class ReleaseManifestLifecycleError(RuntimeError):
    """The trusted Release manifest lifecycle could not continue truthfully."""


def _root(value: str | Path) -> Path:
    try:
        root = Path(value).resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise ReleaseManifestLifecycleError("project root is unavailable") from error
    if root.is_symlink() or not root.is_dir():
        raise ReleaseManifestLifecycleError("project root is unavailable")
    return root


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _safe_ref(value: object, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise ReleaseManifestLifecycleError(f"{label} must be a non-empty repository-relative reference")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ReleaseManifestLifecycleError(f"{label} must be repository-relative")
    return value


def _digest(value: object, label: str) -> str:
    if not isinstance(value, str) or re.fullmatch(r"[0-9a-f]{64}", value) is None:
        raise ReleaseManifestLifecycleError(f"{label} must be a lowercase SHA-256 digest")
    return value


def _normalized_plan(plan: Mapping[str, Any]) -> dict[str, Any]:
    required = {
        "manifest_ref", "observed_input_sha256", "current_route_names", "candidate_route_names",
        "candidate_canonical_manifest_sha256", "added_route", "added_admission_route", "candidate_byte_count",
    }
    if (
        not isinstance(plan, Mapping)
        or not required <= set(plan)
        or set(plan) - required - {"mode"}
        or ("mode" in plan and plan["mode"] != "plan")
    ):
        raise ReleaseManifestLifecycleError("publication plan has missing or unsupported fields")
    result = {key: plan[key] for key in required}
    result["manifest_ref"] = _safe_ref(result["manifest_ref"], "plan.manifest_ref")
    result["observed_input_sha256"] = _digest(result["observed_input_sha256"], "plan.observed_input_sha256")
    result["candidate_canonical_manifest_sha256"] = _digest(
        result["candidate_canonical_manifest_sha256"], "plan.candidate_canonical_manifest_sha256"
    )
    if result["current_route_names"] != list(SELECTED_ROUTE_NAMES) or result["candidate_route_names"] != [*SELECTED_ROUTE_NAMES, "release_version"]:
        raise ReleaseManifestLifecycleError("publication plan does not describe the admitted fifteen-to-sixteen route successor")
    if result["added_route"] != "release_version" or result["added_admission_route"] != "release_version":
        raise ReleaseManifestLifecycleError("publication plan does not describe the admitted Release addition")
    if type(result["candidate_byte_count"]) is not int or result["candidate_byte_count"] < 1:
        raise ReleaseManifestLifecycleError("publication plan has invalid candidate byte count")
    return result


def _normalized_refresh_plan(plan: Mapping[str, Any]) -> dict[str, Any]:
    required = {
        "publication_operation", "manifest_ref", "observed_input_sha256", "current_route_names",
        "candidate_route_names", "candidate_canonical_manifest_sha256", "added_route",
        "added_admission_route", "candidate_byte_count",
    }
    if (
        not isinstance(plan, Mapping)
        or not required <= set(plan)
        or set(plan) - required - {"mode", *_O030_REFRESH_PLAN_FIELDS}
        or plan.get("publication_operation") != "refresh"
        or ("mode" in plan and plan["mode"] != "plan")
    ):
        raise ReleaseManifestLifecycleError("refresh plan has missing or unsupported fields")
    result = {key: plan[key] for key in required}
    result["manifest_ref"] = _safe_ref(result["manifest_ref"], "refresh plan.manifest_ref")
    result["observed_input_sha256"] = _digest(result["observed_input_sha256"], "refresh plan.observed_input_sha256")
    result["candidate_canonical_manifest_sha256"] = _digest(
        result["candidate_canonical_manifest_sha256"], "refresh plan.candidate_canonical_manifest_sha256"
    )
    expected_names = list(_REFRESH_ROUTE_NAMES)
    expected_o030_names = list(_O030_REFRESH_ROUTE_NAMES)
    if (result["current_route_names"] != result["candidate_route_names"]
            or result["current_route_names"] not in (expected_names, expected_o030_names)):
        raise ReleaseManifestLifecycleError(
            "refresh plan does not retain the exact sixteen-route projection or the exact O030 seventeen-route projection"
        )
    is_o030_repair = result["current_route_names"] == expected_o030_names
    if is_o030_repair:
        schema_version = plan.get("source_refresh_schema_version")
        if (type(schema_version) is not int
                or schema_version not in _O030_REFRESH_SCHEMA_VERSIONS):
            raise ReleaseManifestLifecycleError("O030 refresh plan must name the exact schema-4 or schema-5 registration")
        registration_id = plan.get("source_refresh_registration_id")
        if (not isinstance(registration_id, str) or not registration_id
                or "\n" in registration_id or "\r" in registration_id):
            raise ReleaseManifestLifecycleError("O030 refresh plan registration identifier is invalid")
        result.update(
            source_refresh_schema_version=schema_version,
            source_refresh_registration_id=registration_id,
        )
    elif _O030_REFRESH_PLAN_FIELDS & set(plan):
        raise ReleaseManifestLifecycleError("sixteen-route refresh plan must not claim O030 registration metadata")
    if result["added_route"] != "release_version" or result["added_admission_route"] != "release_version":
        raise ReleaseManifestLifecycleError("refresh plan does not identify the Release row")
    if type(result["candidate_byte_count"]) is not int or result["candidate_byte_count"] < 1:
        raise ReleaseManifestLifecycleError("refresh plan has invalid candidate byte count")
    return result


def _normalized_public_plan(plan: Mapping[str, Any]) -> dict[str, Any]:
    required = {
        "publication_operation", "manifest_ref", "observed_input_sha256", "current_route_names",
        "candidate_route_names", "candidate_canonical_manifest_sha256", "added_route",
        "added_admission_route", "candidate_byte_count",
    }
    if (
        not isinstance(plan, Mapping)
        or not required <= set(plan)
        or set(plan) - required - {"mode"}
        or plan.get("publication_operation") != "public"
        or ("mode" in plan and plan["mode"] != "plan")
    ):
        raise ReleaseManifestLifecycleError("public publication plan has missing or unsupported fields")
    result = {key: plan[key] for key in required}
    result["manifest_ref"] = _safe_ref(result["manifest_ref"], "public plan.manifest_ref")
    result["observed_input_sha256"] = _digest(result["observed_input_sha256"], "public plan.observed_input_sha256")
    result["candidate_canonical_manifest_sha256"] = _digest(
        result["candidate_canonical_manifest_sha256"], "public plan.candidate_canonical_manifest_sha256"
    )
    expected_current = [*SELECTED_ROUTE_NAMES, "release_version"]
    expected_candidate = [*expected_current, "public.release"]
    if result["current_route_names"] != expected_current or result["candidate_route_names"] != expected_candidate:
        raise ReleaseManifestLifecycleError("public publication plan does not describe the admitted sixteen-to-seventeen route successor")
    if result["added_route"] != "public.release" or result["added_admission_route"] != "public.release":
        raise ReleaseManifestLifecycleError("public publication plan does not describe the public Release addition")
    if type(result["candidate_byte_count"]) is not int or result["candidate_byte_count"] < 1:
        raise ReleaseManifestLifecycleError("public publication plan has invalid candidate byte count")
    return result


def _normalized_any_plan(plan: Mapping[str, Any]) -> dict[str, Any]:
    if isinstance(plan, Mapping) and plan.get("publication_operation") == "refresh":
        return _normalized_refresh_plan(plan)
    if isinstance(plan, Mapping) and plan.get("publication_operation") == "public":
        return _normalized_public_plan(plan)
    return _normalized_plan(plan)


def _intent_base(plan: Mapping[str, Any], context: PublicationAuthorizationContext) -> dict[str, Any]:
    normalized = _normalized_any_plan(plan)
    return {
        "plan": normalized,
        "source_frontier_digest": _digest(context.source_frontier_digest, "context.source_frontier_digest"),
        "authority_digest": _digest(context.authority_digest, "context.authority_digest"),
    }


def _canonical_intent(plan: Mapping[str, Any], context: PublicationAuthorizationContext, payload: bytes) -> dict[str, Any]:
    if not isinstance(payload, bytes):
        raise ReleaseManifestLifecycleError("candidate publication payload must be bytes")
    return {**_intent_base(plan, context), "candidate_payload_sha256": _sha256(payload)}






def _event_id(root: Path, intent: Mapping[str, Any]) -> str:
    return "release-manifest:" + work_journal.canonical_json_digest(
        {"action_id": ACTION_ID, "root": str(root), "intent": dict(intent)})


def _now() -> dt.datetime:
    return dt.datetime.now().astimezone()


class ReleaseManifestLifecycle:
    """One trusted lifecycle adapter injected into the manifest publisher."""

    def __init__(self, project_root: str | Path, context: PublicationAuthorizationContext) -> None:
        self.root = _root(project_root)
        self.context = context
        self._held_carrier_lock: str | None = None

    def authorize_release_manifest_publication(self, plan: Mapping[str, Any], authorization: object) -> bool:
        """Refresh opaque host authority; caller data cannot self-grant access."""
        if authorization is not self.context:
            return False
        try:
            normalized = _normalized_any_plan(plan)
            operation = normalized.get("publication_operation")
            validator = (
                validate_refresh_context if operation == "refresh"
                else validate_public_manifest_context if operation == "public"
                else validate_publication_context
            )
            validator(self.context, self.root, dict(normalized))
        except (ReleaseManifestAuthorizationError, ReleaseManifestLifecycleError, OSError, TypeError, ValueError):
            return False
        return True

    @contextmanager
    def release_manifest_publication_lock(self, plan: Mapping[str, Any]):
        """Serialize the actual manifest effect independently of plain logging."""
        manifest_ref = _normalized_any_plan(plan)["manifest_ref"]
        if self._held_carrier_lock is not None:
            raise ReleaseManifestLifecycleError("a Release manifest publication lock is already held")
        with engine_publication_lock(self.root):
            self._held_carrier_lock = manifest_ref
            try:
                yield
            finally:
                self._held_carrier_lock = None

    def prepare_release_manifest_publication(self, plan: Mapping[str, Any], payload: bytes) -> str:
        """Revalidate the exact authorized source effect without a log prerequisite."""
        self._validate_payload(plan, payload)
        self._validate_candidate_payload(plan, payload)
        intent = _canonical_intent(plan, self.context, payload)
        path = self.root / intent["plan"]["manifest_ref"]
        if _sha256(path.read_bytes()) != intent["plan"]["observed_input_sha256"]:
            raise ReleaseManifestLifecycleError("selected manifest input changed before publication")
        return _event_id(self.root, intent)


    def record_release_manifest_publication(self, result: Mapping[str, Any]) -> dict[str, str]:
        """Append the actual published observation; never gate its operation status."""
        plan = self._plan_from_result(result)
        payload = (self.root / plan["manifest_ref"]).read_bytes()
        intent = _canonical_intent(plan, self.context, payload)
        event = self._successor_event(intent, payload)
        occurred = dt.datetime.fromisoformat(event["occurred_at"])
        value = {"candidate_canonical_manifest_sha256": plan["candidate_canonical_manifest_sha256"]}
        try:
            work_journal.append_sealed_events(self.root, [event], author=self.context.journal_author,
                                             local_date=occurred.date().isoformat(), timezone=occurred.tzname())
        except (OSError, RuntimeError, TypeError, ValueError) as error:
            return {**value, "recording_error": str(error)}
        return {**value, "recording_ref": "journal:" + event["event_id"]}

    def _plan_from_result(self, result: Mapping[str, Any]) -> dict[str, Any]:
        if not isinstance(result, Mapping) or result.get("mode") != "execute" or result.get("published") is not True:
            raise ReleaseManifestLifecycleError("publication result is not a verified execute result")
        plan = {key: result[key] for key in (
            "manifest_ref", "observed_input_sha256", "current_route_names", "candidate_route_names",
            "candidate_canonical_manifest_sha256", "added_route", "added_admission_route", "candidate_byte_count",
        ) if key in result}
        if "publication_operation" in result:
            plan["publication_operation"] = result["publication_operation"]
        for field in _O030_REFRESH_PLAN_FIELDS:
            if field in result:
                plan[field] = result[field]
        return _normalized_any_plan(plan)


    def _validate_payload(self, plan: Mapping[str, Any], payload: bytes) -> None:
        if not isinstance(payload, bytes) or not payload:
            raise ReleaseManifestLifecycleError("candidate publication payload must be non-empty bytes")
        if len(payload) != _normalized_any_plan(plan)["candidate_byte_count"]:
            raise ReleaseManifestLifecycleError("candidate publication payload has a different byte count from the plan")
        try:
            document = json.loads(payload)
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise ReleaseManifestLifecycleError("candidate publication payload is not JSON") from error
        if not isinstance(document, dict) or document.get("canonical_manifest_sha256") != plan.get("candidate_canonical_manifest_sha256"):
            raise ReleaseManifestLifecycleError("candidate publication payload is not bound to the exact plan")

    def _validate_candidate_payload(self, plan: Mapping[str, Any], payload: bytes) -> None:
        try:
            normalized = _normalized_any_plan(plan)
            operation = normalized.get("publication_operation")
            validator = (
                validate_refresh_candidate_payload if operation == "refresh"
                else validate_public_manifest_candidate_payload if operation == "public"
                else validate_candidate_payload
            )
            validator(self.context, self.root, dict(normalized), payload)
        except (ReleaseManifestAuthorizationError, OSError, TypeError, ValueError) as error:
            raise ReleaseManifestLifecycleError("candidate publication payload is not bound to trusted authority") from error



    def _successor_event(self, intent: Mapping[str, Any], payload: bytes) -> dict[str, Any]:
        return {"event_id": _event_id(self.root, intent), "action_id": ACTION_ID,
                "event": "completed", "author": self.context.journal_author,
                "occurred_at": self._occurred_at(), "llm_session": dict(self.context.llm_session),
                "structural_scope": STRUCTURAL_SCOPE, "action_type": "UPDATE",
                "result": {"path": intent["plan"]["manifest_ref"], "sha256": _sha256(payload)}}




    def _occurred_at(self) -> str:
        moment = _now()
        return moment.isoformat(timespec="seconds")




__all__ = ["ReleaseManifestLifecycle", "ReleaseManifestLifecycleError"]
