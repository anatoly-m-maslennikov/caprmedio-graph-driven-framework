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
from typing import Protocol, TypeAlias, runtime_checkable


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


def _raw_bytes(value: object, *, label: str) -> bytes:
    if not isinstance(value, bytes) or not value:
        raise LegacyProcessCoverageError("coverage-binding-invalid", f"{label} must be non-empty raw bytes")
    return value


def _image_digest(value: object, *, label: str) -> str:
    if (not isinstance(value, str) or not value.startswith("sha256:")
            or _SHA256.fullmatch(value.removeprefix("sha256:")) is None):
        raise LegacyProcessCoverageError("coverage-binding-invalid", f"{label} must be an immutable image digest")
    return value


@dataclass(frozen=True)
class NativeTargetContextProof:
    """Raw native execution selector plus the prior D600 context identity."""

    execution_selector_bytes: bytes
    prior_target_context_sha256: str

    def __post_init__(self) -> None:
        _raw_bytes(self.execution_selector_bytes, label="native execution selector")
        _sha256(self.prior_target_context_sha256, label="native prior target context")

    @property
    def execution_selector_sha256(self) -> str:
        return hashlib.sha256(self.execution_selector_bytes).hexdigest()

    def evidence_binding(self) -> dict[str, str]:
        return {
            "kind": "native_target_context",
            "execution_selector_sha256": self.execution_selector_sha256,
            "prior_target_context_sha256": self.prior_target_context_sha256,
        }


@dataclass(frozen=True)
class LegacyBootstrapSourceProof:
    """Authenticated bootstrap proof for a predecessor without D600 context.

    The publisher obtains these bytes from the retained bootstrap-image reader
    while its installation lock is held.  This boundary retains only their
    digests in provider evidence; it never accepts an already-rendered map as
    a substitute for those raw carriers.
    """

    framework_selector_bytes: bytes
    tool_selector_bytes: bytes
    package_manifest_sha256: str
    source_context_sha256: str
    image_digest: str
    bootstrap_proof_key: str
    raw_receipt_bytes: bytes

    def __post_init__(self) -> None:
        _raw_bytes(self.framework_selector_bytes, label="legacy Framework selector")
        _raw_bytes(self.tool_selector_bytes, label="legacy Tool selector")
        _sha256(self.package_manifest_sha256, label="legacy package manifest")
        _sha256(self.source_context_sha256, label="legacy source context")
        _image_digest(self.image_digest, label="legacy image")
        _sha256(self.bootstrap_proof_key, label="legacy bootstrap proof key")
        _raw_bytes(self.raw_receipt_bytes, label="legacy bootstrap raw receipt")

    @property
    def framework_selector_sha256(self) -> str:
        return hashlib.sha256(self.framework_selector_bytes).hexdigest()

    @property
    def tool_selector_sha256(self) -> str:
        return hashlib.sha256(self.tool_selector_bytes).hexdigest()

    @property
    def raw_receipt_sha256(self) -> str:
        return hashlib.sha256(self.raw_receipt_bytes).hexdigest()

    def evidence_binding(self) -> dict[str, str]:
        return {
            "kind": "legacy_bootstrap_source_proof",
            "framework_selector_sha256": self.framework_selector_sha256,
            "tool_selector_sha256": self.tool_selector_sha256,
            "package_manifest_sha256": self.package_manifest_sha256,
            "source_context_sha256": self.source_context_sha256,
            "image_digest": self.image_digest,
            "bootstrap_proof_key": self.bootstrap_proof_key,
            "raw_receipt_sha256": self.raw_receipt_sha256,
        }


PredecessorProof: TypeAlias = NativeTargetContextProof | LegacyBootstrapSourceProof


def _proof_binding(value: object) -> dict[str, str] | None:
    if isinstance(value, (NativeTargetContextProof, LegacyBootstrapSourceProof)):
        return value.evidence_binding()
    return None


def _checked_evidence_proof(value: object, *, legacy: bool | None = None) -> dict[str, str] | None:
    """Validate the hash-only proof retained inside provider ``evidence_json``."""

    if not isinstance(value, Mapping):
        return None
    binding = dict(value)
    kind = binding.get("kind")
    if kind == "native_target_context":
        expected = {
            "kind", "execution_selector_sha256", "prior_target_context_sha256",
        }
        if set(binding) != expected:
            return None
        for field in expected - {"kind"}:
            if _SHA256.fullmatch(binding.get(field, "")) is None:
                return None
        if legacy is True:
            return None
    elif kind == "legacy_bootstrap_source_proof":
        expected = {
            "kind", "framework_selector_sha256", "tool_selector_sha256", "package_manifest_sha256",
            "source_context_sha256", "image_digest", "bootstrap_proof_key", "raw_receipt_sha256",
        }
        if set(binding) != expected:
            return None
        for field in expected - {"kind", "image_digest"}:
            if _SHA256.fullmatch(binding.get(field, "")) is None:
                return None
        if (not isinstance(binding.get("image_digest"), str)
                or _SHA256.fullmatch(binding["image_digest"].removeprefix("sha256:")) is None
                or not binding["image_digest"].startswith("sha256:")):
            return None
        if legacy is False:
            return None
    else:
        return None
    return {key: binding[key] for key in sorted(binding)}


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
        prior_target_context_sha256: str | None,
        prior_selector_sha256: str,
        predecessor_proof: Mapping[str, str] | None = None,
    ) -> LegacyProcessEvidenceHandle: ...


@dataclass
class _Lifecycle:
    closed: bool = False


def _retained_row(
    *,
    owned_subtree: str,
    provider_namespace: str,
    target_context_sha256: str,
    prior_target_context_sha256: str | None,
    prior_selector_sha256: str,
    predecessor_proof: PredecessorProof | None,
    evidence: ProviderCoverageEvidence,
) -> dict[str, object]:
    if evidence.state not in _STATES:
        raise LegacyProcessCoverageError("coverage-state-invalid", "provider coverage state is invalid")
    if _namespace(evidence.namespace, label="queried namespace") != provider_namespace:
        raise LegacyProcessCoverageError("coverage-namespace-stale", "provider queried a different namespace")
    if not isinstance(evidence.evidence, Mapping) or not evidence.evidence:
        raise LegacyProcessCoverageError("coverage-evidence-invalid", "provider evidence must be a non-empty table")
    evidence_table = dict(evidence.evidence)
    expected_proof = _proof_binding(predecessor_proof)
    retained_proof = _checked_evidence_proof(
        evidence_table.get("predecessor_proof"),
        legacy=isinstance(predecessor_proof, LegacyBootstrapSourceProof),
    )
    if expected_proof is not None and retained_proof != expected_proof:
        raise LegacyProcessCoverageError(
            "coverage-predecessor-proof-invalid",
            "provider evidence does not bind the authenticated predecessor proof",
        )
    if expected_proof is None and retained_proof is not None:
        if (
            retained_proof.get("kind") != "native_target_context"
            or retained_proof.get("prior_target_context_sha256") != prior_target_context_sha256
            or retained_proof.get("execution_selector_sha256") != prior_selector_sha256
        ):
            raise LegacyProcessCoverageError(
                "coverage-predecessor-proof-invalid",
                "optional native predecessor proof contradicts coverage bindings",
            )
    if expected_proof is None and "predecessor_proof" in evidence_table and retained_proof is None:
        raise LegacyProcessCoverageError("coverage-predecessor-proof-invalid", "provider predecessor proof is malformed")
    try:
        evidence_json = _canonical_json(evidence_table)
        observations_json = _canonical_json([dict(item) for item in evidence.observations])
    except (TypeError, ValueError) as error:
        raise LegacyProcessCoverageError("coverage-evidence-invalid", "provider evidence is not canonical JSON") from error
    if evidence.state == "absent" and evidence.observations:
        raise LegacyProcessCoverageError("coverage-state-invalid", "an absent namespace cannot include observations")
    if evidence.state == "observed" and not evidence.observations:
        raise LegacyProcessCoverageError("coverage-state-invalid", "an observed namespace requires observations")
    if evidence.state == "unknown" and evidence.observations:
        raise LegacyProcessCoverageError("coverage-state-invalid", "unknown coverage cannot claim process observations")
    row: dict[str, object] = {
        "owned_subtree": owned_subtree,
        "provider_namespace": provider_namespace,
        "target_context_sha256": target_context_sha256,
        "prior_selector_sha256": prior_selector_sha256,
        "state": evidence.state,
        "evidence_sha256": hashlib.sha256(evidence_json.encode("utf-8")).hexdigest(),
        "evidence_json": evidence_json,
        "observations_json": observations_json,
    }
    # Historical native rows retain their original top-level shape.  A legacy
    # bootstrap predecessor has no D600 context and must not synthesize one.
    if prior_target_context_sha256 is not None:
        row["prior_target_context_sha256"] = prior_target_context_sha256
    else:
        row["predecessor_kind"] = "legacy_bootstrap_source_proof"
    return row


@dataclass(frozen=True, init=False)
class LegacyProcessCoverage:
    """Opaque frozen snapshot backed by still-open provider evidence handles."""

    _target_context_sha256: str
    _prior_target_context_sha256: str | None
    _prior_selector_sha256: str
    _predecessor_proof: PredecessorProof | None = field(repr=False, compare=False)
    _handles: tuple[LegacyProcessEvidenceHandle, ...] = field(repr=False, compare=False)
    _rows: tuple[dict[str, object], ...] = field(repr=False)
    _lifecycle: _Lifecycle = field(repr=False, compare=False)

    @classmethod
    def _create(
        cls,
        *,
        target_context_sha256: str,
        prior_target_context_sha256: str | None,
        prior_selector_sha256: str,
        predecessor_proof: PredecessorProof | None,
        handles: tuple[LegacyProcessEvidenceHandle, ...],
        rows: tuple[dict[str, object], ...],
    ) -> "LegacyProcessCoverage":
        instance = object.__new__(cls)
        object.__setattr__(instance, "_target_context_sha256", target_context_sha256)
        object.__setattr__(instance, "_prior_target_context_sha256", prior_target_context_sha256)
        object.__setattr__(instance, "_prior_selector_sha256", prior_selector_sha256)
        object.__setattr__(instance, "_predecessor_proof", predecessor_proof)
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
        prior_target_context_sha256: str | None = None,
        prior_selector_sha256: str,
        predecessor_proof: PredecessorProof | None = None,
    ) -> None:
        self._require_open()
        supplied_proof = _proof_binding(predecessor_proof)
        retained_proof = _proof_binding(self._predecessor_proof)
        if (
            self._target_context_sha256 != _sha256(target_context_sha256, label="target context")
            or self._prior_selector_sha256 != _sha256(prior_selector_sha256, label="prior selector")
            or retained_proof != supplied_proof
        ):
            raise LegacyProcessCoverageError("coverage-binding-stale", "coverage belongs to a different replacement")
        if self._prior_target_context_sha256 is None:
            if prior_target_context_sha256 is not None:
                raise LegacyProcessCoverageError("coverage-binding-stale", "legacy bootstrap coverage has no prior D600 context")
        elif self._prior_target_context_sha256 != _sha256(prior_target_context_sha256, label="prior target context"):
            raise LegacyProcessCoverageError("coverage-binding-stale", "coverage belongs to a different replacement")

    def revalidate(self) -> None:
        """Physically reopen each still-fenced provider and require exact stability."""

        self._require_open()
        current = _snapshot_rows(
            self._handles,
            target_context_sha256=self._target_context_sha256,
            prior_target_context_sha256=self._prior_target_context_sha256,
            prior_selector_sha256=self._prior_selector_sha256,
            predecessor_proof=self._predecessor_proof,
        )
        if current != self._rows:
            raise LegacyProcessCoverageError("coverage-changed", "provider coverage changed before replacement")


def _snapshot_rows(
    handles: Sequence[LegacyProcessEvidenceHandle],
    *,
    target_context_sha256: str,
    prior_target_context_sha256: str | None,
    prior_selector_sha256: str,
    predecessor_proof: PredecessorProof | None,
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
                predecessor_proof=predecessor_proof,
                evidence=evidence,
            )
        )
    return tuple(rows)


def open_legacy_process_coverage(
    providers: Sequence[LegacyProcessEvidenceProvider],
    *,
    target_context_sha256: str,
    prior_target_context_sha256: str | None = None,
    prior_selector_sha256: str | None = None,
    predecessor_proof: PredecessorProof | None = None,
) -> LegacyProcessCoverage:
    """Acquire all provider fences and freeze a physically queried D607 view.

    The input is a sequence of provider objects, never caller-supplied process
    mappings.  On failure, every already-opened provider handle is closed and
    no coverage object is returned.
    """

    target = _sha256(target_context_sha256, label="target context")
    proof = predecessor_proof if isinstance(
        predecessor_proof, (NativeTargetContextProof, LegacyBootstrapSourceProof),
    ) else None
    if predecessor_proof is not None and proof is None:
        raise LegacyProcessCoverageError("coverage-predecessor-proof-invalid", "predecessor proof is not typed")
    if isinstance(proof, NativeTargetContextProof):
        prior_target = proof.prior_target_context_sha256
        prior_selector = proof.execution_selector_sha256
        if (prior_target_context_sha256 is not None and prior_target_context_sha256 != prior_target) or (
                prior_selector_sha256 is not None and prior_selector_sha256 != prior_selector):
            raise LegacyProcessCoverageError("coverage-binding-stale", "native proof contradicts caller bindings")
    elif isinstance(proof, LegacyBootstrapSourceProof):
        if prior_target_context_sha256 is not None:
            raise LegacyProcessCoverageError(
                "coverage-predecessor-proof-invalid", "legacy bootstrap proof must omit prior D600 context",
            )
        prior_target = None
        # The Framework selector is the predecessor's execution carrier;
        # the Tool selector is independently retained in its proof binding.
        prior_selector = proof.framework_selector_sha256
        if prior_selector_sha256 is not None and prior_selector_sha256 != prior_selector:
            raise LegacyProcessCoverageError("coverage-binding-stale", "legacy proof contradicts caller selector")
    else:
        # Retain the historical native API and row schema.  New callers use a
        # typed proof above, which carries both raw selector hashes.
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
                opening = {
                    "target_context_sha256": target,
                    "prior_selector_sha256": prior_selector,
                }
                if prior_target is not None:
                    opening["prior_target_context_sha256"] = prior_target
                if proof is not None:
                    opening["predecessor_proof"] = proof.evidence_binding()
                handle = provider.open_legacy_process_evidence(**opening)
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
            predecessor_proof=proof,
        )
        return LegacyProcessCoverage._create(
            target_context_sha256=target,
            prior_target_context_sha256=prior_target,
            prior_selector_sha256=prior_selector,
            predecessor_proof=proof,
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
    prior_target_context_sha256: str | None = None,
    prior_selector_sha256: str | None = None,
    predecessor_proof: PredecessorProof | None = None,
) -> tuple[dict[str, object], ...]:
    """Validate serialized coverage only; it deliberately cannot prove it live."""

    target = _sha256(target_context_sha256, label="target context")
    proof = predecessor_proof if isinstance(
        predecessor_proof, (NativeTargetContextProof, LegacyBootstrapSourceProof),
    ) else None
    if predecessor_proof is not None and proof is None:
        raise LegacyProcessCoverageError("coverage-predecessor-proof-invalid", "predecessor proof is not typed")
    if isinstance(proof, NativeTargetContextProof):
        prior_target = proof.prior_target_context_sha256
        prior_selector = proof.execution_selector_sha256
        if (prior_target_context_sha256 is not None and prior_target_context_sha256 != prior_target) or (
                prior_selector_sha256 is not None and prior_selector_sha256 != prior_selector):
            raise LegacyProcessCoverageError("coverage-binding-stale", "native proof contradicts retained bindings")
    elif isinstance(proof, LegacyBootstrapSourceProof):
        if prior_target_context_sha256 is not None:
            raise LegacyProcessCoverageError(
                "coverage-predecessor-proof-invalid", "legacy bootstrap proof must omit prior D600 context",
            )
        prior_target = None
        prior_selector = proof.framework_selector_sha256
        if prior_selector_sha256 is not None and prior_selector_sha256 != prior_selector:
            raise LegacyProcessCoverageError("coverage-binding-stale", "legacy proof contradicts retained selector")
    else:
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
        is_legacy = row.get("predecessor_kind") == "legacy_bootstrap_source_proof"
        expected_keys = {
            "owned_subtree", "provider_namespace", "target_context_sha256", "prior_selector_sha256",
            "state", "evidence_sha256", "evidence_json", "observations_json",
        }
        if is_legacy:
            expected_keys.add("predecessor_kind")
        else:
            expected_keys.add("prior_target_context_sha256")
        if set(row) != expected_keys:
            raise LegacyProcessCoverageError("coverage-evidence-invalid", "retained coverage row has an invalid shape")
        if row.get("target_context_sha256") != target or row.get("prior_selector_sha256") != prior_selector:
            raise LegacyProcessCoverageError("coverage-binding-stale", "retained coverage belongs to another replacement")
        if prior_target is None:
            if not is_legacy:
                raise LegacyProcessCoverageError("coverage-binding-stale", "legacy retained coverage has a native context field")
        elif is_legacy or row.get("prior_target_context_sha256") != prior_target:
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
        retained_proof = _checked_evidence_proof(evidence.get("predecessor_proof"), legacy=is_legacy)
        if proof is not None and retained_proof != proof.evidence_binding():
            raise LegacyProcessCoverageError(
                "coverage-predecessor-proof-invalid", "retained coverage does not bind the authenticated predecessor proof",
            )
        if is_legacy and retained_proof is None:
            raise LegacyProcessCoverageError(
                "coverage-predecessor-proof-invalid", "legacy retained coverage has no authenticated bootstrap proof",
            )
        if not is_legacy and "predecessor_proof" in evidence and retained_proof is None:
            raise LegacyProcessCoverageError("coverage-predecessor-proof-invalid", "retained predecessor proof is malformed")
        if not is_legacy and retained_proof is not None and (
                retained_proof.get("kind") != "native_target_context"
                or retained_proof.get("prior_target_context_sha256") != prior_target
                or retained_proof.get("execution_selector_sha256") != prior_selector):
            raise LegacyProcessCoverageError(
                "coverage-predecessor-proof-invalid",
                "retained native predecessor proof contradicts coverage bindings",
            )
        if row.get("evidence_sha256") != hashlib.sha256(evidence_json.encode("utf-8")).hexdigest():
            raise LegacyProcessCoverageError("coverage-tampered", "retained coverage digest differs")
        if (state == "absent" and observations) or (state == "observed" and not observations) or (
            state == "unknown" and observations
        ):
            raise LegacyProcessCoverageError("coverage-state-invalid", "retained coverage state and observations differ")
        retained = {
            "owned_subtree": expected,
            "provider_namespace": namespace,
            "target_context_sha256": target,
            "prior_selector_sha256": prior_selector,
            "state": state,
            "evidence_sha256": row["evidence_sha256"],
            "evidence_json": evidence_json,
            "observations_json": observations_json,
        }
        if is_legacy:
            retained["predecessor_kind"] = "legacy_bootstrap_source_proof"
        else:
            retained["prior_target_context_sha256"] = prior_target
        checked.append(retained)
    return tuple(checked)


__all__ = [
    "LegacyBootstrapSourceProof",
    "LegacyProcessCoverage",
    "LegacyProcessCoverageError",
    "LegacyProcessEvidenceHandle",
    "LegacyProcessEvidenceProvider",
    "NativeTargetContextProof",
    "OWNED_PROCESS_NAMESPACES",
    "PredecessorProof",
    "ProviderCoverageEvidence",
    "open_legacy_process_coverage",
    "validate_retained_coverage_rows",
]
