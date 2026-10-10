"""Fenced, read-only process coverage for retained legacy installation state.

This module is deliberately a *collector*, not a process controller.  A
provider may report an empty roster only after completing its own bounded live
query.  Missing receipt/state files, a caller supplied boolean, or an empty
list from a caller therefore cannot manufacture legacy-process absence.

The installation publication lock supplied as ``fence`` remains owned by the
publisher.  The publisher supplies the raw, physically reopened predecessor
selector while holding that lock; this module derives its selector digest and
revalidates the same lock before and after every provider query.  Process
command, release, generation, and start facts are deliberately *not*
admission inputs: zero processes have no truthful values for them, and a live
process must prove them independently in its own observation.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys
import time
from collections.abc import Callable, Mapping, Sequence
from typing import Any

from legacy_process_coverage import LegacyProcessCoverageError as OpaqueCoverageError
from legacy_process_coverage import ProviderCoverageEvidence


PROVIDERS = ("project_mcp", "mcp_hot_reload", "workflow_orchestrator")
_DIGEST = re.compile(r"[0-9a-f]{64}\Z")
_MAX_QUERY_SECONDS = 30.0
_TOOLS = Path(__file__).resolve().parent
_PROVIDER_PATHS = {
    "project_mcp": _TOOLS.parent / "203_APPS/WORKFLOW_ORCHESTRATOR/docker/project_mcp_launcher.py",
    "mcp_hot_reload": _TOOLS.parent / "204_MCP/hot_reload.py",
    "workflow_orchestrator": _TOOLS.parent / "203_APPS/WORKFLOW_ORCHESTRATOR/workflow_process_inspection.py",
}


class LegacyProcessCoverageError(RuntimeError):
    """The typed coverage request itself is not safe to issue."""


def _sha256(value: object, *, name: str) -> str:
    if not isinstance(value, str) or _DIGEST.fullmatch(value) is None:
        raise LegacyProcessCoverageError(f"{name} must be a SHA-256 digest")
    return value


def _is_sha256(value: object) -> bool:
    return isinstance(value, str) and _DIGEST.fullmatch(value) is not None


def _canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)


def _digest(value: object) -> str:
    return hashlib.sha256(_canonical(value).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class LegacyProcessAdmission:
    """The sealed predecessor identity shared by all three provider queries.

    ``selection`` is intentionally not evidence and is omitted from the
    fingerprint.  It gives providers the already-admitted ProjectSelection
    object required to perform a Project-local query without rediscovery.
    """

    project_root: Path | str
    project_instance_id: str
    target_context_sha256: str
    prior_target_context_sha256: str
    prior_selector_bytes: bytes
    fence: object
    selection: object | None = field(default=None, compare=False, repr=False)

    def __post_init__(self) -> None:
        try:
            root = Path(self.project_root).absolute()
            observed = root.lstat()
        except (TypeError, ValueError, OSError) as error:
            raise LegacyProcessCoverageError("project root is unavailable") from error
        if root.is_symlink() or not root.is_dir():
            raise LegacyProcessCoverageError("project root must be a real directory")
        object.__setattr__(self, "project_root", root)
        _sha256(self.project_instance_id, name="project instance")
        _sha256(self.target_context_sha256, name="target context")
        _sha256(self.prior_target_context_sha256, name="prior target context")
        if not isinstance(self.prior_selector_bytes, bytes) or not self.prior_selector_bytes:
            raise LegacyProcessCoverageError("prior selector must be reopened raw bytes")
        revalidate = getattr(self.fence, "revalidate", None)
        if not callable(revalidate):
            raise LegacyProcessCoverageError("a revalidatable admission fence is required")
        if self.selection is not None:
            selection_root = getattr(self.selection, "root", None)
            selection_instance = getattr(self.selection, "instance_id", None)
            if selection_root != root or selection_instance != self.project_instance_id:
                raise LegacyProcessCoverageError("Project selection contradicts the admission")

    @property
    def fingerprint(self) -> str:
        return _digest({
            "project_root": str(self.project_root),
            "project_instance_id": self.project_instance_id,
            "target_context_sha256": self.target_context_sha256,
            "prior_target_context_sha256": self.prior_target_context_sha256,
            "prior_selector_sha256": self.prior_selector_sha256,
        })

    @property
    def prior_selector_sha256(self) -> str:
        """Digest the exact raw predecessor selector admitted under the lock."""
        return hashlib.sha256(self.prior_selector_bytes).hexdigest()

    def revalidate(self) -> None:
        self.fence.revalidate()


ProviderQuery = Callable[[LegacyProcessAdmission, float], Mapping[str, object]]


def _unknown(provider: str, admission: LegacyProcessAdmission, reason: str) -> dict[str, object]:
    return {
        "provider": provider,
        "state": "unknown",
        "admission_sha256": admission.fingerprint,
        "reason": reason,
        "processes": [],
    }


def _provider_query(provider: str) -> ProviderQuery | None:
    path = _PROVIDER_PATHS[provider]
    try:
        if str(path.parent) not in sys.path:
            sys.path.insert(0, str(path.parent))
        spec = importlib.util.spec_from_file_location(f"_legacy_process_provider_{provider}", path)
        if spec is None or spec.loader is None:
            return None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        query = getattr(module, "collect_legacy_processes", None)
        return query if callable(query) else None
    except Exception:
        # Import failure is a provider-query refusal, never absence.
        return None


def _open_provider_fence(provider: str, admission: LegacyProcessAdmission, deadline: float):
    """Open one provider-owned writer fence; callers cannot supply this seam."""
    path = _PROVIDER_PATHS[provider]
    if str(path.parent) not in sys.path:
        sys.path.insert(0, str(path.parent))
    spec = importlib.util.spec_from_file_location(f"_legacy_process_fence_{provider}", path)
    if spec is None or spec.loader is None:
        raise LegacyProcessCoverageError("provider fence is unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    opener = getattr(module, "open_legacy_process_fence", None)
    if not callable(opener):
        raise LegacyProcessCoverageError("provider fence is unavailable")
    return opener(admission, deadline)


def _shutdown_is_verified(value: object) -> bool:
    return (
        isinstance(value, Mapping)
        and value.get("requested") is True
        and value.get("response") == "acknowledged"
        and value.get("deadline_status") == "within-deadline"
        and value.get("verified_exit") is True
    )


def _nested_observation(
    provider: str,
    record: object,
    admission: LegacyProcessAdmission,
) -> dict[str, object] | None:
    """Accept only a provider-observed quiescence proof for one live process.

    No provider currently promotes a raw Docker row or process-table candidate
    into this shape.  Such data is useful only to refuse absence.  Should a
    provider later support an observed predecessor, its *own* query must have
    obtained every nested command, release, start, and shutdown fact below.
    The predecessor release binds the prior context and raw-selector digest;
    it must never be compared to the prospective replacement context.
    """

    if not isinstance(record, Mapping):
        return None
    required = {
        "owned_subtree", "pid", "state_generation", "observed_start_token",
        "command", "release", "shutdown",
    }
    if set(record) != required or record.get("owned_subtree") != provider:
        return None
    if type(record.get("pid")) is not int or record["pid"] <= 0:
        return None
    if not isinstance(record.get("state_generation"), str) or not record["state_generation"]:
        return None
    if not isinstance(record.get("observed_start_token"), str) or not record["observed_start_token"]:
        return None

    command = record.get("command")
    if not isinstance(command, Mapping):
        return None
    command_required = {"sha256", "environment_sha256", "wrapper_sha256", "argv", "invocation_nonce"}
    if set(command) != command_required or not all(
        _is_sha256(command.get(field))
        for field in ("sha256", "environment_sha256", "wrapper_sha256")
    ):
        return None
    argv = command.get("argv")
    if (not isinstance(argv, list) or not argv
            or any(not isinstance(value, str) or Path(value).is_absolute() or ".." in Path(value).parts
                   for value in argv)
            or not isinstance(command.get("invocation_nonce"), str) or not command["invocation_nonce"]):
        return None

    release = record.get("release")
    if not isinstance(release, Mapping):
        return None
    release_required = {
        "package_manifest_sha256", "framework_version", "version_carrier_sha256",
        "source_catalog_sha256", "full_gate_receipt_sha256", "image_digest",
        "target_context_sha256", "selector_sha256",
    }
    if set(release) != release_required or not all(
        _is_sha256(release.get(field))
        for field in (
            "package_manifest_sha256", "version_carrier_sha256", "source_catalog_sha256",
            "full_gate_receipt_sha256", "target_context_sha256", "selector_sha256",
        )
    ):
        return None
    image = release.get("image_digest")
    if (not isinstance(image, str) or not image.startswith("sha256:")
            or not _is_sha256(image[7:])
            or not isinstance(release.get("framework_version"), str) or not release["framework_version"]
            or release["target_context_sha256"] != admission.prior_target_context_sha256
            or release["selector_sha256"] != admission.prior_selector_sha256):
        return None
    if not _shutdown_is_verified(record.get("shutdown")):
        return None
    return {
        "owned_subtree": provider,
        "pid": record["pid"],
        "state_generation": record["state_generation"],
        "observed_start_token": record["observed_start_token"],
        "command": {field: command[field] for field in sorted(command_required)},
        "release": {field: release[field] for field in sorted(release_required)},
        "shutdown": {
            "requested": True,
            "response": "acknowledged",
            "deadline_status": "within-deadline",
            "verified_exit": True,
        },
    }


def _coverage_from_result(
    provider: str,
    admission: LegacyProcessAdmission,
    result: object,
) -> dict[str, object]:
    """Refuse partial/provider-shaped data; only a completed roster is absence."""

    if not isinstance(result, Mapping) or set(result) != {"outcome", "records"}:
        return _unknown(provider, admission, "provider-query-invalid")
    if result.get("outcome") != "complete" or not isinstance(result.get("records"), list):
        return _unknown(provider, admission, "provider-query-incomplete")
    records = result["records"]
    checked = [_nested_observation(provider, record, admission) for record in records]
    if any(record is None for record in checked):
        return _unknown(provider, admission, "provider-process-identity-unverified")
    processes = [record for record in checked if record is not None]
    if len({(record["pid"], record["observed_start_token"]) for record in processes}) != len(processes):
        return _unknown(provider, admission, "provider-process-identity-ambiguous")
    return {
        "provider": provider,
        "state": "absent" if not processes else "observed",
        "admission_sha256": admission.fingerprint,
        "reason": "complete-owned-query",
        "processes": processes,
    }


def collect_provider_coverage(
    admission: LegacyProcessAdmission,
    *,
    providers: Mapping[str, ProviderQuery] | None = None,
    timeout_seconds: float = _MAX_QUERY_SECONDS,
) -> tuple[dict[str, object], ...]:
    """Query every owned namespace in order while its admission fence is held.

    Providers are called with a monotonic deadline and must make no process
    action.  Any failure, refusal, unexpected shape, stale fence, or expired
    budget is represented as ``unknown`` for that provider.  The function
    never promotes an untrusted caller observation into coverage evidence.
    """

    if not isinstance(admission, LegacyProcessAdmission):
        raise LegacyProcessCoverageError("collector requires a typed admission")
    if (isinstance(timeout_seconds, bool) or not isinstance(timeout_seconds, (int, float))
            or not 0 < float(timeout_seconds) <= _MAX_QUERY_SECONDS):
        raise LegacyProcessCoverageError("provider query timeout is invalid")
    deadline = time.monotonic() + float(timeout_seconds)
    supplied = providers or {}
    if any(name not in PROVIDERS for name in supplied):
        raise LegacyProcessCoverageError("provider mapping contains an unknown namespace")
    rows: list[dict[str, object]] = []
    for provider in PROVIDERS:
        query = supplied.get(provider) if providers is not None else _provider_query(provider)
        try:
            admission.revalidate()
            if not callable(query) or time.monotonic() >= deadline:
                rows.append(_unknown(provider, admission, "provider-query-unavailable"))
                continue
            rows.append(_coverage_from_result(provider, admission, query(admission, deadline)))
            # The same fence must still name the caller after the provider's
            # live query; otherwise even a truthful empty roster is stale.
            admission.revalidate()
        except Exception:
            rows.append(_unknown(provider, admission, "provider-query-refused"))
    return tuple(rows)


def dormant_predecessor_is_absent(
    coverage: Sequence[Mapping[str, object]], admission: LegacyProcessAdmission,
) -> bool:
    """Admit zero predecessors only after all three real providers say absent."""

    if not isinstance(admission, LegacyProcessAdmission) or len(coverage) != len(PROVIDERS):
        return False
    for expected, row in zip(PROVIDERS, coverage):
        if not isinstance(row, Mapping) or set(row) != {
            "provider", "state", "admission_sha256", "reason", "processes",
        }:
            return False
        if (row.get("provider") != expected or row.get("state") != "absent"
                or row.get("admission_sha256") != admission.fingerprint
                or row.get("reason") != "complete-owned-query" or row.get("processes") != []):
            return False
    try:
        admission.revalidate()
    except Exception:
        return False
    return True


def recollect_provider_coverage(
    admission: LegacyProcessAdmission,
    coverage: Sequence[Mapping[str, object]],
    *,
    providers: Mapping[str, ProviderQuery] | None = None,
    timeout_seconds: float = _MAX_QUERY_SECONDS,
) -> tuple[dict[str, object], ...]:
    """Reopen provider evidence before copy/switch and reject a changed roster."""

    previous = tuple(dict(row) for row in coverage if isinstance(row, Mapping))
    if len(previous) != len(PROVIDERS):
        raise LegacyProcessCoverageError("prior coverage is incomplete")
    current = collect_provider_coverage(admission, providers=providers, timeout_seconds=timeout_seconds)
    if current != previous:
        raise LegacyProcessCoverageError("provider coverage changed during retained migration")
    return current


class _ProviderHandle:
    """A retained provider query: no status file is trusted between snapshots."""

    def __init__(self, provider: "FencedLegacyProcessProvider", physical_fence: object) -> None:
        self._provider = provider
        self.owned_subtree = provider.owned_subtree
        self.provider_namespace = provider.provider_namespace
        self._physical_fence = physical_fence
        self._closed = False

    def snapshot(self) -> ProviderCoverageEvidence:
        if self._closed:
            raise OpaqueCoverageError("coverage-closed", "provider handle is closed")
        admission = self._provider.admission
        deadline = time.monotonic() + _MAX_QUERY_SECONDS
        try:
            admission.revalidate()
            snapshot = getattr(self._physical_fence, "snapshot", None)
            if not callable(snapshot):
                return self._provider._evidence("unknown", (), "provider-fence-invalid")
            result = snapshot(deadline)
            admission.revalidate()
        except Exception:
            return self._provider._evidence("unknown", (), "provider-query-refused")
        row = _coverage_from_result(self.owned_subtree, admission, result)
        state = row["state"]
        if state == "unknown":
            return self._provider._evidence("unknown", (), str(row["reason"]))
        processes = tuple(dict(item) for item in row["processes"] if isinstance(item, Mapping))
        return self._provider._evidence(str(state), processes, str(row["reason"]))

    def close(self) -> None:
        close = getattr(self._physical_fence, "close", None)
        if callable(close):
            close()
        self._closed = True


class _UnavailableProviderFence:
    """A refusal carrier: it can block absence, but never manufacture it."""

    def snapshot(self, _deadline: float) -> Mapping[str, object]:
        return {"outcome": "unavailable", "records": []}

    def close(self) -> None:
        return None


class FencedLegacyProcessProvider:
    """Adapter from an actual provider query to the D607 opaque-handle seam.

    Instances are constructed only from a sealed ``LegacyProcessAdmission``.
    The shared coverage library owns their lifetime; every ``snapshot`` makes
    a fresh bounded provider query and revalidates the original admission
    fence on both sides.  No provider path signals or stops a process.
    """

    def __init__(
        self,
        owned_subtree: str,
        admission: LegacyProcessAdmission,
    ) -> None:
        if owned_subtree not in PROVIDERS:
            raise LegacyProcessCoverageError("owned provider namespace is invalid")
        if not isinstance(admission, LegacyProcessAdmission):
            raise LegacyProcessCoverageError("provider requires a typed admission")
        self.owned_subtree = owned_subtree
        self.provider_namespace = f"caprmedio://legacy-process/{owned_subtree}"
        self.admission = admission

    def _evidence(
        self,
        state: str,
        observations: tuple[Mapping[str, object], ...],
        reason: str,
    ) -> ProviderCoverageEvidence:
        return ProviderCoverageEvidence(
            state=state,
            namespace=self.provider_namespace,
            evidence={
                "provider": self.owned_subtree,
                "admission_sha256": self.admission.fingerprint,
                "query": "bounded-live-reopen",
                "reason": reason,
            },
            observations=observations,
        )

    def open_legacy_process_evidence(
        self,
        *,
        target_context_sha256: str,
        prior_target_context_sha256: str,
        prior_selector_sha256: str,
    ) -> _ProviderHandle:
        if (
            target_context_sha256 != self.admission.target_context_sha256
            or prior_target_context_sha256 != self.admission.prior_target_context_sha256
            or prior_selector_sha256 != self.admission.prior_selector_sha256
        ):
            raise OpaqueCoverageError("coverage-binding-stale", "provider admission belongs to another replacement")
        self.admission.revalidate()
        deadline = time.monotonic() + _MAX_QUERY_SECONDS
        try:
            physical_fence = _open_provider_fence(self.owned_subtree, self.admission, deadline)
        except Exception:
            # A busy or unavailable physical writer fence is not an opaque
            # coverage-construction failure.  Preserve its per-provider
            # unknown result so the installation boundary can refuse zero
            # predecessors without losing the other namespaces' evidence.
            physical_fence = _UnavailableProviderFence()
        return _ProviderHandle(self, physical_fence)


def fenced_legacy_process_providers(
    admission: LegacyProcessAdmission,
) -> tuple[FencedLegacyProcessProvider, ...]:
    """Return real adapters only while the reopened prior binding stays fenced."""

    if not isinstance(admission, LegacyProcessAdmission):
        raise LegacyProcessCoverageError("provider factory requires a typed admission")
    admission.revalidate()
    return tuple(FencedLegacyProcessProvider(name, admission) for name in PROVIDERS)


__all__ = [
    "LegacyProcessAdmission",
    "LegacyProcessCoverageError",
    "PROVIDERS",
    "collect_provider_coverage",
    "dormant_predecessor_is_absent",
    "FencedLegacyProcessProvider",
    "fenced_legacy_process_providers",
    "recollect_provider_coverage",
]
