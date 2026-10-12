"""Opt-in, source-admitted publication of the seventeenth public-release route.

This is deliberately separate from ``release_manifest_publisher``: D572 owns
the existing fifteen-to-sixteen successor, while D613 owns only the additive
sixteen-to-seventeen public-release admission.  Planning is read-only.  The
single replacement is available only through the existing opaque operator
capability and Journal lifecycle.
"""
from __future__ import annotations

import copy
import hashlib
import os
from pathlib import Path
import sys
import tempfile
from typing import Any, Mapping

from selected_routes import (
    SELECTED_ROUTE_NAMES,
    SelectedRouteError,
    _public_release_workflow_edges,
    canonical_digest,
    canonical_json,
    load_selected_manifest,
    selected_manifest_ref,
)


_RELEASE_ROUTE = "release_version"
_PUBLIC_ROUTE = "public.release"
_CURRENT_NAMES = [*SELECTED_ROUTE_NAMES, _RELEASE_ROUTE]
_CANDIDATE_NAMES = [*_CURRENT_NAMES, _PUBLIC_ROUTE]


class PublicManifestPublishError(ValueError):
    """The bounded public-release manifest successor cannot be published."""


def _root(value: str | Path) -> Path:
    try:
        root = Path(value).resolve(strict=True)
    except (OSError, TypeError, ValueError) as error:
        raise PublicManifestPublishError("project root is unavailable") from error
    if root.is_symlink() or not root.is_dir():
        raise PublicManifestPublishError("project root is unavailable")
    return root


def _public_admission(project_root: Path) -> dict[str, Any]:
    public_release = Path(__file__).resolve().parents[1] / "201_TOOLS" / "PUBLIC_RELEASE"
    if str(public_release) not in sys.path:
        sys.path.insert(0, str(public_release))
    try:
        from selected_admission import (
            PublicReleaseSourceAdmissionError,
            derive_public_release_source_admission,
            validate_public_release_source_admission,
        )
        derived = derive_public_release_source_admission(project_root)
        validated = validate_public_release_source_admission(project_root, derived)
    except (ImportError, OSError, TypeError, ValueError) as error:
        raise PublicManifestPublishError(f"public Release source admission is not current: {error}") from error
    if not isinstance(derived, Mapping) or not isinstance(validated, Mapping) or dict(derived) != dict(validated):
        raise PublicManifestPublishError("public Release source admission returned an invalid contract")
    return copy.deepcopy(dict(validated))


def _public_route(project_root: Path, admission: Mapping[str, Any]) -> dict[str, Any]:
    steps, actions = admission.get("ordered_steps"), admission.get("ordered_actions")
    if (not isinstance(steps, list) or not steps or not isinstance(actions, list)
            or len(steps) != len(actions)):
        raise PublicManifestPublishError("public Release source admission has an invalid ordered definition")
    try:
        edges = _public_release_workflow_edges(project_root, admission)
    except (OSError, TypeError, ValueError, SelectedRouteError) as error:
        raise PublicManifestPublishError(f"public Release source workflow is not current: {error}") from error
    return {
        "route": _PUBLIC_ROUTE,
        "workflow": copy.deepcopy(admission["workflow"]),
        "ordered_steps": [
            {"step": copy.deepcopy(step), "action": copy.deepcopy(action)}
            for step, action in zip(steps, actions, strict=True)
        ],
        "ordered_actions": copy.deepcopy(actions),
        "native_action_calls": copy.deepcopy(admission["native_action_calls"]),
        "entry_step": steps[0]["atom_id"],
        "on_result": copy.deepcopy(edges),
        "mutation_capable": admission["mutation_capable"],
    }


def _public_parts(project_root: Path) -> tuple[dict[str, Any], bytes, dict[str, Any], bytes, Path, dict[str, Any]]:
    """Derive the exact D613 successor without mutating the selected carrier.

    This is intentionally shared with the opaque authorizer so it never trusts
    route, admission, manifest, or source digests supplied by a caller.
    """
    try:
        current = load_selected_manifest(project_root)
    except (OSError, TypeError, ValueError, SelectedRouteError) as error:
        raise PublicManifestPublishError(f"current selected manifest is unavailable: {error}") from error
    if [row.get("route") for row in current.get("routes", [])] != _CURRENT_NAMES:
        raise PublicManifestPublishError("public publication requires the current exact sixteen-route manifest")
    if "public_release_source_admissions" in current:
        raise PublicManifestPublishError("public publication requires a manifest without public Release admission")
    admission = _public_admission(project_root)
    candidate = copy.deepcopy(current)
    candidate.pop("manifest_ref", None)
    candidate["routes"].append(_public_route(project_root, admission))
    candidate["public_release_source_admissions"] = [copy.deepcopy(admission)]
    candidate["source_freshness"]["selected_binding_digest"] = canonical_digest(candidate["routes"])
    candidate.pop("canonical_manifest_sha256", None)
    candidate["canonical_manifest_sha256"] = canonical_digest(candidate)
    path = project_root / selected_manifest_ref(project_root)
    try:
        observed = path.read_bytes()
    except OSError as error:
        raise PublicManifestPublishError("current selected manifest bytes are unavailable") from error
    payload = (canonical_json(candidate) + "\n").encode("utf-8")
    plan = {
        "publication_operation": "public",
        "manifest_ref": path.relative_to(project_root).as_posix(),
        "observed_input_sha256": hashlib.sha256(observed).hexdigest(),
        "current_route_names": [row["route"] for row in current["routes"]],
        "candidate_route_names": [row["route"] for row in candidate["routes"]],
        "candidate_canonical_manifest_sha256": candidate["canonical_manifest_sha256"],
        "added_route": _PUBLIC_ROUTE,
        "added_admission_route": _PUBLIC_ROUTE,
        "candidate_byte_count": len(payload),
    }
    return plan, observed, current, payload, path, admission


def plan_public_manifest_publish(project_root: str | Path) -> dict[str, Any]:
    """Return the read-only, exact D613 public-release publication plan."""
    root = _root(project_root)
    plan, _, _, _, _, _ = _public_parts(root)
    return {"mode": "plan", **plan}


def _atomic_write(path: Path, payload: bytes) -> None:
    if path.is_symlink() or not path.parent.is_dir():
        raise PublicManifestPublishError("selected manifest carrier is unavailable")
    temporary: str | None = None
    try:
        descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except OSError as error:
        raise PublicManifestPublishError("could not atomically publish selected manifest") from error
    finally:
        if temporary is not None:
            try:
                Path(temporary).unlink(missing_ok=True)
            except OSError:
                pass


def publish_public_manifest(
    project_root: str | Path, *, execute: bool = False, authorization: Any = None,
) -> dict[str, Any]:
    """Publish only an exact, operator-authorized D613 successor."""
    if type(execute) is not bool:
        raise PublicManifestPublishError("execute must be a boolean")
    root = _root(project_root)
    plan, observed, current, payload, path, _ = _public_parts(root)
    if not execute:
        return {"mode": "plan", **plan}
    try:
        from release_manifest_authorization import (
            PublicationAuthorizationContext,
            validate_public_manifest_context,
        )
        from release_manifest_lifecycle import ReleaseManifestLifecycle
    except ImportError as error:
        raise PublicManifestPublishError("trusted public manifest lifecycle is unavailable") from error
    if not isinstance(authorization, PublicationAuthorizationContext):
        raise PublicManifestPublishError("execute requires a trusted host-created public publication context")
    sealed_plan = {"mode": "plan", **plan}
    try:
        context = validate_public_manifest_context(authorization, root, sealed_plan)
        lifecycle = ReleaseManifestLifecycle(root, context)
        if lifecycle.authorize_release_manifest_publication(plan, context) is not True:
            raise PublicManifestPublishError("trusted public publication context was refused")
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        raise PublicManifestPublishError(f"trusted public publication context is invalid: {error}") from error
    if path.read_bytes() != observed:
        raise PublicManifestPublishError("selected manifest input changed after authorization")
    _, observed_after, current_after, payload_after, _, _ = _public_parts(root)
    if current_after != current or observed_after != observed or payload_after != payload:
        raise PublicManifestPublishError("source-derived public successor changed after authorization")
    try:
        with lifecycle.release_manifest_publication_lock(plan):
            pending_event_id = lifecycle.prepare_release_manifest_publication(plan, payload)
            if not isinstance(pending_event_id, str) or not pending_event_id:
                raise PublicManifestPublishError("trusted lifecycle did not seal a public publication intent")
            validate_public_manifest_context(context, root, sealed_plan, manifest_state="input")
            if path.read_bytes() != observed:
                raise PublicManifestPublishError("selected manifest input changed after intent sealing")
            _, observed_final, current_final, payload_final, _, _ = _public_parts(root)
            if current_final != current or observed_final != observed or payload_final != payload:
                raise PublicManifestPublishError("source-derived public successor changed after intent sealing")
            _atomic_write(path, payload)
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        pending_event_id = locals().get("pending_event_id")
        result = {
            "mode": "execute", "published": False,
            "disposition": "pending_publication" if isinstance(pending_event_id, str) and pending_event_id else "blocked",
            "publication_requirement": str(error), **plan,
        }
        if isinstance(pending_event_id, str) and pending_event_id:
            result["pending_event_id"] = pending_event_id
        return result
    try:
        published = path.read_bytes()
        if published != payload:
            raise PublicManifestPublishError("published manifest bytes differ from the sealed public candidate")
        loaded = load_selected_manifest(root)
    except (OSError, TypeError, ValueError, SelectedRouteError) as error:
        return {
            "mode": "execute", "published": True, "disposition": "readback_required",
            "pending_event_id": pending_event_id, "readback_requirement": str(error), **plan,
        }
    names = [row["route"] for row in loaded["routes"]]
    if names != _CANDIDATE_NAMES:
        return {
            "mode": "execute", "published": True, "disposition": "readback_required",
            "pending_event_id": pending_event_id,
            "readback_requirement": "published manifest does not discover the additive public Release route", **plan,
        }
    try:
        validate_public_manifest_context(context, root, sealed_plan, manifest_state="candidate")
    except (OSError, TypeError, ValueError) as error:
        return {
            "mode": "execute", "published": True, "disposition": "readback_required",
            "pending_event_id": pending_event_id, "readback_requirement": str(error), **plan,
        }
    evidence = {"mode": "execute", "published": True, "published_route_names": names, **plan}
    try:
        receipt = lifecycle.record_release_manifest_publication(dict(evidence))
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        return {
            **evidence, "disposition": "recording_required", "pending_event_id": pending_event_id,
            "recording_requirement": str(error),
        }
    if (not isinstance(receipt, Mapping) or set(receipt) != {"recording_ref", "candidate_canonical_manifest_sha256"}
            or not isinstance(receipt["recording_ref"], str) or not receipt["recording_ref"]
            or receipt["candidate_canonical_manifest_sha256"] != plan["candidate_canonical_manifest_sha256"]):
        return {
            **evidence, "disposition": "recording_required", "pending_event_id": pending_event_id,
            "recording_requirement": "trusted internal lifecycle recording is incomplete",
        }
    return {**evidence, "disposition": "published", "recording_ref": receipt["recording_ref"]}


def recover_public_manifest_publish(
    project_root: str | Path, *, pending_event_id: str, authorization: Any,
) -> dict[str, Any]:
    """Finalize one already-written D613 successor; never rewrite its carrier."""
    root = _root(project_root)
    if not isinstance(pending_event_id, str) or not pending_event_id:
        raise PublicManifestPublishError("recovery requires one sealed pending event identity")
    try:
        from release_manifest_authorization import (
            PublicationAuthorizationContext,
            validate_public_manifest_recovery_context,
        )
        from release_manifest_lifecycle import ReleaseManifestLifecycle
    except ImportError as error:
        raise PublicManifestPublishError("trusted public manifest lifecycle is unavailable") from error
    if not isinstance(authorization, PublicationAuthorizationContext):
        raise PublicManifestPublishError("recovery requires a trusted host-created public publication context")
    try:
        validate_public_manifest_recovery_context(authorization, root, pending_event_id)
        recovered = ReleaseManifestLifecycle(root, authorization).recover_release_manifest_publication(pending_event_id)
    except (OSError, RuntimeError, TypeError, ValueError) as error:
        return {
            "mode": "recover", "disposition": "recording_required", "pending_event_id": pending_event_id,
            "recording_requirement": str(error),
        }
    return {"mode": "recover", "pending_event_id": pending_event_id, **dict(recovered)}


__all__ = [
    "PublicManifestPublishError", "plan_public_manifest_publish", "publish_public_manifest",
    "recover_public_manifest_publish",
]
