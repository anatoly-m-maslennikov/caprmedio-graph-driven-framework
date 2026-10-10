"""Opaque, provider-held evidence for D607 legacy-process coverage.

This module deliberately does not discover, signal, or stop processes.  A
provider opens its own admission fence, returns a handle that can physically
reopen its namespace, and keeps that handle alive until the installation
facade closes the coverage.  Callers cannot turn a mapping, checksum, or
boolean into coverage evidence.
"""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
import hashlib
import json
import re
from typing import Protocol, runtime_checkable


OWNED_PROCESS_NAMESPACES = (
    "project_mcp",
    "mcp_hot_reload",
    "workflow_orchestrator",
)
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_STATES = frozenset(("absent", "observed", "unknown"))


class LegacyProcessCoverageError(RuntimeError):
    """A provider did not give a complete, stable D607 coverage view."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


def _canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def _digest(value: object) -> str:
    return hashlib.sha256(_canonical_json(value).encode("utf-8")).hexdigest()


def _sha256(value: object, *, label: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise LegacyProcessCoverageError("coverage-binding-invalid", f"{label} must be a SHA-256 digest")
    return value


def _namespace(value: object, *, label: str) -> str:
    if not isinstance(value, str) or not value or len(value) > 512 or any(ord(char) < 32 for char in value):
        raise LegacyProcessCoverageError("coverage-namespace-invalid", f"{label} is not a safe provider namespace")
    return value


@dataclass(frozen=True)
class ProviderCoverageEvidence:
    """One physical query result returned only by an opened provider handle."""

    state: str
    namespace: str
    evidence: Mapping[str, object]
    observations: tuple[Mapping[str, object], ...] = ()


@runtime_checkable
class LegacyProcessEvidenceHandle(Protocol):
    """A provider-held fence plus a fresh namespace query."""

    owned_subtree: str
    provider_namespace: str

    def snapshot(self) -> ProviderCoverageEvidence: ...

    def close(self) -> None: ...


@runtime_checkable
class LegacyProcessEvidenceProvider(Protocol):
    """Provider-owned admission and discovery seam.

    Implementations must acquire their provider's start/admission fence before
    returning the handle and retain it until ``handle.close()``.  The handle's
    ``snapshot`` must perform a real bounded re-open of that provider's
    namespace; a cached status file is not sufficient absence evidence.
    """

    owned_subtree: str
    provider_namespace: str

    def open_legacy_process_evidence(
        self,
        *,
        target_context_sha256: str,
        prior_target_context_sha256: str,
        prior_selector_sha256: str,
    ) -> LegacyProcessEvidenceHandle: ...


@dataclass
class _Lifecycle:
    closed: bool = False


def _retained_row(
    *,
    owned_subtree: str,
    provider_namespace: str,
    target_context_sha256: str,
    prior_target_context_sha256: str,
    prior_selector_sha256: str,
    evidence: ProviderCoverageEvidence,
) -> dict[str, object]:
    if evidence.state not in _STATES:
        raise LegacyProcessCoverageError("coverage-state-invalid", "provider coverage state is invalid")
    if _namespace(evidence.namespace, label="queried namespace") != provider_namespace:
        raise LegacyProcessCoverageError("coverage-namespace-stale", "provider queried a different namespace")
    if not isinstance(evidence.evidence, Mapping) or not evidence.evidence:
        raise LegacyProcessCoverageError("coverage-evidence-invalid", "provider evidence must be a non-empty table")
    try:
        evidence_json = _canonical_json(dict(evidence.evidence))
        observations_json = _canonical_json([dict(item) for item in evidence.observations])
    except (TypeError, ValueError) as error:
        raise LegacyProcessCoverageError("coverage-evidence-invalid", "provider evidence is not canonical JSON") from error
    if evidence.state == "absent" and evidence.observations:
        raise LegacyProcessCoverageError("coverage-state-invalid", "an absent namespace cannot include observations")
    if evidence.state == "observed" and not evidence.observations:
        raise LegacyProcessCoverageError("coverage-state-invalid", "an observed namespace requires observations")
    if evidence.state == "unknown" and evidence.observations:
        raise LegacyProcessCoverageError("coverage-state-invalid", "unknown coverage cannot claim process observations")
    return {
        "owned_subtree": owned_subtree,
        "provider_namespace": provider_namespace,
        "target_context_sha256": target_context_sha256,
        "prior_target_context_sha256": prior_target_context_sha256,
        "prior_selector_sha256": prior_selector_sha256,
        "state": evidence.state,
        "evidence_sha256": hashlib.sha256(evidence_json.encode("utf-8")).hexdigest(),
        "evidence_json": evidence_json,
        "observations_json": observations_json,
    }


@dataclass(frozen=True, init=False)
class LegacyProcessCoverage:
    """Opaque frozen snapshot backed by still-open provider evidence handles."""

    _target_context_sha256: str
    _prior_target_context_sha256: str
    _prior_selector_sha256: str
    _handles: tuple[LegacyProcessEvidenceHandle, ...] = field(repr=False, compare=False)
    _rows: tuple[dict[str, object], ...] = field(repr=False)
    _lifecycle: _Lifecycle = field(repr=False, compare=False)

    @classmethod
    def _create(
        cls,
        *,
        target_context_sha256: str,
        prior_target_context_sha256: str,
        prior_selector_sha256: str,
        handles: tuple[LegacyProcessEvidenceHandle, ...],
        rows: tuple[dict[str, object], ...],
    ) -> "LegacyProcessCoverage":
        instance = object.__new__(cls)
        object.__setattr__(instance, "_target_context_sha256", target_context_sha256)
        object.__setattr__(instance, "_prior_target_context_sha256", prior_target_context_sha256)
        object.__setattr__(instance, "_prior_selector_sha256", prior_selector_sha256)
        object.__setattr__(instance, "_handles", handles)
        object.__setattr__(instance, "_rows", rows)
        object.__setattr__(instance, "_lifecycle", _Lifecycle())
        return instance

    def __enter__(self) -> "LegacyProcessCoverage":
        self._require_open()
        return self

    def __exit__(self, *_unused: object) -> None:
        self.close()

    def _require_open(self) -> None:
        if self._lifecycle.closed:
            raise LegacyProcessCoverageError("coverage-closed", "provider admission fences have been released")

    def close(self) -> None:
        if self._lifecycle.closed:
            return
        self._lifecycle.closed = True
        errors: list[Exception] = []
        for handle in reversed(self._handles):
            try:
                handle.close()
            except Exception as error:  # Provider cleanup must not mask the primary migration outcome.
                errors.append(error)
        if errors:
            raise LegacyProcessCoverageError("coverage-fence-release-failed", "a provider admission fence did not close")

    def retained_rows(self) -> tuple[dict[str, object], ...]:
        self._require_open()
        return tuple(dict(row) for row in self._rows)

    def observations(self) -> tuple[dict[str, object], ...]:
        self._require_open()
        result: list[dict[str, object]] = []
        for row in self._rows:
            try:
                decoded = json.loads(str(row["observations_json"]))
            except (TypeError, ValueError, json.JSONDecodeError) as error:  # Defensive: rows were generated locally.
                raise LegacyProcessCoverageError("coverage-evidence-invalid", "stored observations are invalid") from error
            if not isinstance(decoded, list) or any(not isinstance(item, dict) for item in decoded):
                raise LegacyProcessCoverageError("coverage-evidence-invalid", "stored observations are invalid")
            result.extend(dict(item) for item in decoded)
        return tuple(result)

    def assert_binding(
        self,
        *,
        target_context_sha256: str,
        prior_target_context_sha256: str,
        prior_selector_sha256: str,
    ) -> None:
        self._require_open()
        if (
            self._target_context_sha256 != _sha256(target_context_sha256, label="target context")
            or self._prior_target_context_sha256 != _sha256(prior_target_context_sha256, label="prior target context")
            or self._prior_selector_sha256 != _sha256(prior_selector_sha256, label="prior selector")
        ):
            raise LegacyProcessCoverageError("coverage-binding-stale", "coverage belongs to a different replacement")

    def revalidate(self) -> None:
        """Physically reopen each still-fenced provider and require exact stability."""

        self._require_open()
        current = _snapshot_rows(
            self._handles,
            target_context_sha256=self._target_context_sha256,
            prior_target_context_sha256=self._prior_target_context_sha256,
            prior_selector_sha256=self._prior_selector_sha256,
        )
        if current != self._rows:
            raise LegacyProcessCoverageError("coverage-changed", "provider coverage changed before replacement")


def _snapshot_rows(
    handles: Sequence[LegacyProcessEvidenceHandle],
    *,
    target_context_sha256: str,
    prior_target_context_sha256: str,
    prior_selector_sha256: str,
) -> tuple[dict[str, object], ...]:
    if len(handles) != len(OWNED_PROCESS_NAMESPACES):
        raise LegacyProcessCoverageError("coverage-incomplete", "coverage requires every owned namespace")
    rows: list[dict[str, object]] = []
    for expected, handle in zip(OWNED_PROCESS_NAMESPACES, handles, strict=True):
        owner = getattr(handle, "owned_subtree", expected)
        namespace = getattr(handle, "provider_namespace", None)
        # Handles are returned by an already-bound provider.  Carry these two
        # attributes to make a swapped handle fail before it is queried.
        if owner != expected:
            raise LegacyProcessCoverageError("coverage-order-invalid", "provider handles are not in owned namespace order")
        namespace = _namespace(namespace, label="provider namespace")
        try:
            evidence = handle.snapshot()
        except LegacyProcessCoverageError:
            raise
        except Exception as error:
            raise LegacyProcessCoverageError("coverage-query-failed", "provider evidence could not be reopened") from error
        if not isinstance(evidence, ProviderCoverageEvidence):
            raise LegacyProcessCoverageError("coverage-evidence-invalid", "provider returned an untyped evidence result")
        rows.append(
            _retained_row(
                owned_subtree=expected,
                provider_namespace=namespace,
                target_context_sha256=target_context_sha256,
                prior_target_context_sha256=prior_target_context_sha256,
                prior_selector_sha256=prior_selector_sha256,
                evidence=evidence,
            )
        )
    return tuple(rows)


def open_legacy_process_coverage(
    providers: Sequence[LegacyProcessEvidenceProvider],
    *,
    target_context_sha256: str,
    prior_target_context_sha256: str,
    prior_selector_sha256: str,
) -> LegacyProcessCoverage:
    """Acquire all provider fences and freeze a physically queried D607 view.

    The input is a sequence of provider objects, never caller-supplied process
    mappings.  On failure, every already-opened provider handle is closed and
    no coverage object is returned.
    """

    target = _sha256(target_context_sha256, label="target context")
    prior_target = _sha256(prior_target_context_sha256, label="prior target context")
    prior_selector = _sha256(prior_selector_sha256, label="prior selector")
    if len(providers) != len(OWNED_PROCESS_NAMESPACES):
        raise LegacyProcessCoverageError("coverage-incomplete", "coverage requires every owned namespace")
    handles: list[LegacyProcessEvidenceHandle] = []
    try:
        for expected, provider in zip(OWNED_PROCESS_NAMESPACES, providers, strict=True):
            if getattr(provider, "owned_subtree", None) != expected:
                raise LegacyProcessCoverageError("coverage-order-invalid", "providers are not in owned namespace order")
            _namespace(getattr(provider, "provider_namespace", None), label="provider namespace")
            try:
                handle = provider.open_legacy_process_evidence(
                    target_context_sha256=target,
                    prior_target_context_sha256=prior_target,
                    prior_selector_sha256=prior_selector,
                )
            except LegacyProcessCoverageError:
                raise
            except Exception as error:
                raise LegacyProcessCoverageError("coverage-query-failed", "provider admission could not be opened") from error
            if not isinstance(handle, LegacyProcessEvidenceHandle):
                raise LegacyProcessCoverageError("coverage-handle-invalid", "provider did not return an evidence handle")
            # Bind the returned handle to the same provider before snapshotting;
            # this catches an accidentally swapped still-open handle.
            if (
                getattr(handle, "owned_subtree", None) != expected
                or getattr(handle, "provider_namespace", None) != getattr(provider, "provider_namespace")
            ):
                raise LegacyProcessCoverageError("coverage-handle-invalid", "provider returned a mismatched evidence handle")
            handles.append(handle)
        frozen_handles = tuple(handles)
        rows = _snapshot_rows(
            frozen_handles,
            target_context_sha256=target,
            prior_target_context_sha256=prior_target,
            prior_selector_sha256=prior_selector,
        )
        return LegacyProcessCoverage._create(
            target_context_sha256=target,
            prior_target_context_sha256=prior_target,
            prior_selector_sha256=prior_selector,
            handles=frozen_handles,
            rows=rows,
        )
    except BaseException:
        for handle in reversed(handles):
            try:
                handle.close()
            except Exception:
                pass
        raise


def validate_retained_coverage_rows(
    rows: object,
    *,
    target_context_sha256: str,
    prior_target_context_sha256: str,
    prior_selector_sha256: str,
) -> tuple[dict[str, object], ...]:
    """Validate serialized coverage only; it deliberately cannot prove it live."""

    target = _sha256(target_context_sha256, label="target context")
    prior_target = _sha256(prior_target_context_sha256, label="prior target context")
    prior_selector = _sha256(prior_selector_sha256, label="prior selector")
    if not isinstance(rows, list) or len(rows) != len(OWNED_PROCESS_NAMESPACES):
        raise LegacyProcessCoverageError("coverage-incomplete", "retained coverage requires every owned namespace")
    checked: list[dict[str, object]] = []
    for expected, value in zip(OWNED_PROCESS_NAMESPACES, rows, strict=True):
        if not isinstance(value, Mapping):
            raise LegacyProcessCoverageError("coverage-evidence-invalid", "retained coverage row is invalid")
        row = dict(value)
        if row.get("owned_subtree") != expected:
            raise LegacyProcessCoverageError("coverage-order-invalid", "retained coverage rows are not in owned namespace order")
        if (
            row.get("target_context_sha256") != target
            or row.get("prior_target_context_sha256") != prior_target
            or row.get("prior_selector_sha256") != prior_selector
        ):
            raise LegacyProcessCoverageError("coverage-binding-stale", "retained coverage belongs to another replacement")
        namespace = _namespace(row.get("provider_namespace"), label="provider namespace")
        state = row.get("state")
        if state not in _STATES:
            raise LegacyProcessCoverageError("coverage-state-invalid", "retained coverage state is invalid")
        evidence_json = row.get("evidence_json")
        observations_json = row.get("observations_json")
        if not isinstance(evidence_json, str) or not isinstance(observations_json, str):
            raise LegacyProcessCoverageError("coverage-evidence-invalid", "retained coverage JSON is missing")
        try:
            evidence = json.loads(evidence_json)
            observations = json.loads(observations_json)
        except json.JSONDecodeError as error:
            raise LegacyProcessCoverageError("coverage-evidence-invalid", "retained coverage JSON is malformed") from error
        if not isinstance(evidence, dict) or not evidence or not isinstance(observations, list) or any(
            not isinstance(item, dict) for item in observations
        ):
            raise LegacyProcessCoverageError("coverage-evidence-invalid", "retained coverage JSON has an invalid shape")
        if _canonical_json(evidence) != evidence_json or _canonical_json(observations) != observations_json:
            raise LegacyProcessCoverageError("coverage-evidence-invalid", "retained coverage JSON is not canonical")
        if row.get("evidence_sha256") != hashlib.sha256(evidence_json.encode("utf-8")).hexdigest():
            raise LegacyProcessCoverageError("coverage-tampered", "retained coverage digest differs")
        if (state == "absent" and observations) or (state == "observed" and not observations) or (
            state == "unknown" and observations
        ):
            raise LegacyProcessCoverageError("coverage-state-invalid", "retained coverage state and observations differ")
        checked.append(
            {
                "owned_subtree": expected,
                "provider_namespace": namespace,
                "target_context_sha256": target,
                "prior_target_context_sha256": prior_target,
                "prior_selector_sha256": prior_selector,
                "state": state,
                "evidence_sha256": row["evidence_sha256"],
                "evidence_json": evidence_json,
                "observations_json": observations_json,
            }
        )
    return tuple(checked)


__all__ = [
    "LegacyProcessCoverage",
    "LegacyProcessCoverageError",
    "LegacyProcessEvidenceHandle",
    "LegacyProcessEvidenceProvider",
    "OWNED_PROCESS_NAMESPACES",
    "ProviderCoverageEvidence",
    "open_legacy_process_coverage",
    "validate_retained_coverage_rows",
]
