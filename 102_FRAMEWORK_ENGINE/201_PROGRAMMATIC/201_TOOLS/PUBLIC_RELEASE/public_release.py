#!/usr/bin/env python3
"""Native, source-bound public-release workflow contract.

This module is deliberately a binding, not a GitHub client.  A selected
executor supplies the native subprocess/Git bindings after normal admission;
this module owns the public-release sequencing, exact evidence shape, and
schema-v5 Workflow/Step/Action lineage.  It never invents a PR URL, secret,
credential, or Tool Run kind.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import sys
import tomllib
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Any, Callable, Mapping, Protocol
from urllib.parse import urlparse


TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

import work_journal  # noqa: E402
from workflow_run_support import RunExecutionSession, RunTracker, SelectedRunError  # noqa: E402
from retained_full_gate_packet import RetainedNativeFullGatePacket  # noqa: E402


TOOL_ID = "PUBLIC_RELEASE"
TOOL_SCHEMA_VERSION = 1
WORKFLOW_ID = "CA-O-188"
STEPS = (
    ("discover_matching_pr", "CA-O-189", "CA-O-190"),
    ("prepare_public_materials", "CA-O-191", "CA-O-192"),
    ("freeze_and_gate", "CA-O-193", "CA-O-194"),
    ("push_and_upsert_pr", "CA-O-195", "CA-O-196"),
    ("finalize_history_link", "CA-O-197", "CA-O-198"),
)
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_VERSION = re.compile(r"^v?(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:[-+][0-9A-Za-z.-]+)?$")
_COMMIT = re.compile(r"^[0-9a-f]{7,64}$")
_GITHUB_SEGMENT = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]{0,99}$")
_MAX_SOURCE_BYTES = 1024 * 1024


class PublicReleaseError(ValueError):
    """Stable contract refusal before an unproven public effect."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(f"{code}: {message}")


class PublicReleaseInterrupted(PublicReleaseError):
    """An external effect was started but no terminal proof is available."""


@dataclass(frozen=True)
class ToolCallEvidence:
    """Evidence attached to the parent Step/Action Run, never a Tool Run."""

    input_ref: str
    result_ref: str
    effect_refs: tuple[str, ...] = ()
    report_refs: tuple[str, ...] = ()
    outcome: str = "completed"


@dataclass(frozen=True)
class SourceProof:
    candidate_snapshot_manifest_sha256: str
    framework_version: str
    version_toml_sha256: str
    readme_ref: str
    readme_sha256: str
    pr_body_ref: str
    pr_body_sha256: str
    version_history_ref: str
    version_history_sha256: str
    version_history_summary: str
    version_history_pr_url: str | None
    version_history_pr_number: int | None
    public_document_closure_sha256: str = field(init=False)

    def __post_init__(self) -> None:
        # This is derived evidence, never a request field or a caller-supplied
        # replacement for physically rereading the source carriers in _source.
        object.__setattr__(self, "public_document_closure_sha256", document_closure_digest(self))


def document_closure_record(source: SourceProof) -> dict[str, Any]:
    """Return R1922's exact closed, non-self-referential document binding."""
    if not isinstance(source, SourceProof):
        raise PublicReleaseError("invalid-source-proof", "document closure requires a typed SourceProof")
    return {
        "schema": "caprmedio.public_release.document_closure.v1",
        "candidate_snapshot_manifest_sha256": source.candidate_snapshot_manifest_sha256,
        "framework_version": source.framework_version,
        "version_toml_sha256": source.version_toml_sha256,
        "readme_ref": source.readme_ref,
        "readme_sha256": source.readme_sha256,
        "pr_body_ref": source.pr_body_ref,
        "pr_body_sha256": source.pr_body_sha256,
        "version_history_ref": source.version_history_ref,
        "version_history_sha256": source.version_history_sha256,
        "version_history_summary": source.version_history_summary,
        "version_history_pr_url": source.version_history_pr_url,
        "version_history_pr_number": source.version_history_pr_number,
    }


def document_closure_digest(source: SourceProof) -> str:
    encoded = json.dumps(document_closure_record(source), sort_keys=True,
                         separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


@dataclass(frozen=True)
class PullRequest:
    url: str
    number: int
    head: str
    base: str
    state: str = "open"


@dataclass(frozen=True)
class PRDiscovery:
    call: ToolCallEvidence
    matches: tuple[PullRequest, ...]


@dataclass(frozen=True)
class PrepareResult:
    call: ToolCallEvidence
    source: SourceProof


@dataclass(frozen=True)
class FullGateBinding:
    """Exact local candidate/gate/promotion chain, reopened before publication."""

    candidate: object
    compilation: object
    suite: object
    build: object
    verification: object
    e2e: object
    evidence: object
    promotion: object


@dataclass(frozen=True)
class DetachedNativeFullGateBinding:
    """One original portable Full Gate packet reopened without live selection."""

    packet: RetainedNativeFullGatePacket


@dataclass(frozen=True)
class GateResult:
    call: ToolCallEvidence
    binding: FullGateBinding | DetachedNativeFullGateBinding


@dataclass(frozen=True)
class VerifiedPushReceipt:
    """Durable observation that an exact selected remote branch received a commit."""

    owner: str
    repository: str
    branch: str
    commit_sha: str
    receipt_ref: str


@dataclass(frozen=True)
class CommitPushResult:
    call: ToolCallEvidence
    commit_sha: str
    receipt: VerifiedPushReceipt


@dataclass(frozen=True)
class PRUpsertResult:
    call: ToolCallEvidence
    pull_request: PullRequest


@dataclass(frozen=True)
class FinalizationResult:
    call: ToolCallEvidence
    source: SourceProof
    changed: bool


@dataclass(frozen=True)
class _FullGateInterface:
    """Late-bound concrete RELEASE_VERSION reader types and functions."""

    legacy_evidence_type: type
    native_evidence_type: type
    retained_candidate_type: type
    portable_suite_type: type
    portable_build_type: type
    portable_verification_type: type
    portable_e2e_type: type
    verify_bound: Callable[..., Path]
    verify_detached_native: Callable[..., object]
    verify_promotion: Callable[..., Path]


class PublicReleaseBindings(Protocol):
    """Injected native bindings; implementations may use Git/subprocess APIs."""

    def discover_matching_pr(self, parameters: Mapping[str, Any]) -> PRDiscovery: ...

    def prepare_public_materials(self, parameters: Mapping[str, Any], pr_url: str | None) -> PrepareResult: ...

    def run_full_gate(self, parameters: Mapping[str, Any], source: SourceProof, phase: str) -> GateResult: ...

    def commit_and_push(self, parameters: Mapping[str, Any], source: SourceProof, phase: str) -> CommitPushResult: ...

    def upsert_main_pr(self, parameters: Mapping[str, Any], source: SourceProof,
                       known_url: str | None, phase: str) -> PRUpsertResult: ...

    def finalize_history_link(self, parameters: Mapping[str, Any], source: SourceProof,
                              pull_request: PullRequest) -> FinalizationResult: ...


def _safe_ref(value: object, label: str) -> str:
    if not isinstance(value, str) or not value or "\x00" in value:
        raise PublicReleaseError("invalid-input", f"{label} must be a non-empty repository-relative reference")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts or "\\" in value:
        raise PublicReleaseError("invalid-input", f"{label} must be repository-relative and traversal-free")
    if any(part.startswith(".env") or part.endswith(".env") for part in path.parts):
        raise PublicReleaseError("invalid-input", f"{label} must not address an environment carrier")
    return value


def _sha(value: object, label: str) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise PublicReleaseError("invalid-input", f"{label} must be a lowercase SHA-256")
    return value


def _segment(value: object, label: str) -> str:
    if not isinstance(value, str) or _GITHUB_SEGMENT.fullmatch(value) is None:
        raise PublicReleaseError("invalid-remote-binding", f"{label} must be one GitHub owner/repository segment")
    return value


def _url(value: object, label: str, *, owner: str, repository: str, number: int) -> str:
    if not isinstance(value, str) or not value or any(char in value for char in "\r\n\x00"):
        raise PublicReleaseError("invalid-pr-url", f"{label} must be a non-empty HTTPS URL")
    parsed = urlparse(value)
    expected_path = f"/{owner}/{repository}/pull/{number}"
    if (parsed.scheme != "https" or parsed.netloc != "github.com" or parsed.path != expected_path
            or parsed.params or parsed.query or parsed.fragment):
        raise PublicReleaseError("invalid-pr-url", f"{label} must bind selected github.com/{owner}/{repository} PR #{number}")
    return value


def _call(value: object, label: str) -> ToolCallEvidence:
    if not isinstance(value, ToolCallEvidence):
        raise PublicReleaseError("invalid-tool-evidence", f"{label} must return ToolCallEvidence")
    _safe_ref(value.input_ref, f"{label}.input_ref")
    _safe_ref(value.result_ref, f"{label}.result_ref")
    if value.outcome not in {"completed", "no_op", "interrupted_pending"}:
        raise PublicReleaseError("invalid-tool-evidence", f"{label} has an unsupported outcome")
    for field, rows in (("effect_refs", value.effect_refs), ("report_refs", value.report_refs)):
        if not isinstance(rows, tuple) or len(set(rows)) != len(rows):
            raise PublicReleaseError("invalid-tool-evidence", f"{label}.{field} must be a unique tuple")
        for row in rows:
            _safe_ref(row, f"{label}.{field}")
    if value.outcome == "interrupted_pending":
        error = PublicReleaseInterrupted("external-effect-uncertain", f"{label} has no terminal effect proof")
        error.call = value
        raise error
    return value


def _read_source_file(project_root: Path, ref: str, label: str) -> tuple[str, str]:
    root = project_root.resolve(strict=True)
    _safe_ref(ref, label)
    target = root / ref
    current = root
    for part in Path(ref).parts:
        current /= part
        if current.is_symlink():
            raise PublicReleaseError("source-proof-unavailable", f"{label} has a symlinked carrier ancestor")
    if target.is_symlink() or not target.is_file():
        raise PublicReleaseError("source-proof-unavailable", f"{label} is not a regular source file")
    try:
        resolved = target.resolve(strict=True)
        resolved.relative_to(root)
    except (OSError, ValueError) as error:
        raise PublicReleaseError("source-proof-unavailable", f"{label} escapes the selected Project") from error
    if resolved.stat().st_size > _MAX_SOURCE_BYTES:
        raise PublicReleaseError("source-proof-unavailable", f"{label} exceeds the source-proof size limit")
    try:
        payload = resolved.read_bytes()
        return payload.decode("utf-8"), hashlib.sha256(payload).hexdigest()
    except (OSError, UnicodeDecodeError) as error:
        raise PublicReleaseError("source-proof-unavailable", f"{label} cannot be reopened as UTF-8") from error


def _complete_section(markdown: str, heading: str) -> bool:
    match = re.search(rf"(?mi)^#{{1,6}}\s+{re.escape(heading)}\s*$", markdown)
    if match is None:
        return False
    following = re.search(r"(?m)^#{1,6}\s+", markdown[match.end():])
    body = markdown[match.end():match.end() + following.start() if following else len(markdown)]
    return bool(body.strip())


def _source(value: object, label: str, *, project_root: Path, release: Mapping[str, Any]) -> SourceProof:
    if not isinstance(value, SourceProof):
        raise PublicReleaseError("invalid-source-proof", f"{label} must return SourceProof")
    _sha(value.candidate_snapshot_manifest_sha256, f"{label}.candidate_snapshot_manifest_sha256")
    if not isinstance(value.framework_version, str) or _VERSION.fullmatch(value.framework_version) is None:
        raise PublicReleaseError("invalid-source-proof", f"{label}.framework_version must be a semantic version")
    _sha(value.version_toml_sha256, f"{label}.version_toml_sha256")
    for field in ("readme_ref", "pr_body_ref", "version_history_ref"):
        _safe_ref(getattr(value, field), f"{label}.{field}")
    for field in ("readme_sha256", "pr_body_sha256", "version_history_sha256"):
        _sha(getattr(value, field), f"{label}.{field}")
    if (not isinstance(value.version_history_summary, str) or not value.version_history_summary.strip()
            or "\n" in value.version_history_summary or "\r" in value.version_history_summary
            or len(value.version_history_summary) > 160):
        raise PublicReleaseError("invalid-source-proof", f"{label}.version_history_summary must be one concise line")
    root = Path(project_root)
    try:
        readme, readme_sha = _read_source_file(root, value.readme_ref, f"{label}.readme_ref")
        pr_body, pr_body_sha = _read_source_file(root, value.pr_body_ref, f"{label}.pr_body_ref")
        history, history_sha = _read_source_file(root, value.version_history_ref, f"{label}.version_history_ref")
        version_toml, version_toml_sha = _read_source_file(root, "version.toml", f"{label}.version.toml")
    except FileNotFoundError as error:
        raise PublicReleaseError("source-proof-unavailable", f"{label} Project root is unavailable") from error
    if (readme_sha != value.readme_sha256 or pr_body_sha != value.pr_body_sha256
            or history_sha != value.version_history_sha256):
        raise PublicReleaseError("source-proof-stale", f"{label} document bytes differ from its asserted source proof")
    if value.public_document_closure_sha256 != document_closure_digest(value):
        raise PublicReleaseError("source-proof-stale", f"{label} document closure differs from local canonical recomputation")
    try:
        actual_version = tomllib.loads(version_toml)["framework"]["version"]
    except (KeyError, TypeError, tomllib.TOMLDecodeError) as error:
        raise PublicReleaseError("source-proof-invalid", f"{label} cannot bind root version.toml [framework].version") from error
    selected_version = release["selected_version"].removeprefix("v")
    if (value.framework_version != selected_version or actual_version != selected_version
            or value.version_toml_sha256 != version_toml_sha):
        raise PublicReleaseError("new-local-cycle-required", f"{label} version.toml differs from the selected version; a fresh local release cycle is required")
    if not readme.strip() or not _complete_section(pr_body, "What's new") or not _complete_section(pr_body, "What's fixed"):
        raise PublicReleaseError("source-proof-invalid", f"{label} must reopen README and complete What's new/What's fixed PR sections")
    if value.version_history_pr_url is None:
        if value.version_history_pr_number is not None:
            raise PublicReleaseError("history-link-invalid", f"{label} has a PR number without an actual PR URL")
    else:
        if type(value.version_history_pr_number) is not int or value.version_history_pr_number < 1:
            raise PublicReleaseError("history-link-invalid", f"{label} must bind an actual positive PR number")
        _url(value.version_history_pr_url, f"{label}.version_history_pr_url",
             owner=release["remote"]["owner"], repository=release["remote"]["repository"],
             number=value.version_history_pr_number)
        matches = [line for line in history.splitlines() if value.version_history_pr_url in line]
        if (len(matches) != 1 or value.version_history_summary not in matches[0]
                or matches[0].count("http") != 1 or len(matches[0].strip()) > 240):
            raise PublicReleaseError("history-link-invalid", f"{label} must retain one concise summary with its actual PR hyperlink")
    return value


def _pr(value: object, label: str, *, release: Mapping[str, Any]) -> PullRequest:
    if not isinstance(value, PullRequest):
        raise PublicReleaseError("invalid-pr-evidence", f"{label} must return PullRequest")
    if type(value.number) is not int or value.number < 1:
        raise PublicReleaseError("invalid-pr-evidence", f"{label}.number must be positive")
    _url(value.url, f"{label}.url", owner=release["remote"]["owner"],
         repository=release["remote"]["repository"], number=value.number)
    if value.head != release["release_branch"] or value.base != release["target_branch"] or value.state != "open":
        raise PublicReleaseError("invalid-pr-evidence", f"{label} does not bind the selected open {release['release_branch']}->{release['target_branch']} PR")
    return value


def _full_gate_interface() -> _FullGateInterface:
    release_root = TOOLS_ROOT / "RELEASE_VERSION"
    if str(release_root) not in sys.path:
        sys.path.insert(0, str(release_root))
    try:
        from release_e2e_gate import PortableCandidateE2EGateEvidence
        from release_full_gate import (FullGateEvidence, NativeFullGateEvidence,
                                       verify_bound_full_gate_evidence,
                                       verify_detached_native_full_gate_evidence)
        from release_image import PortableImageBuildEvidence, PortableImageVerificationEvidence
        from release_promotion import verify_bound_promotion_evidence
        from release_retained_candidate import RetainedCandidateIdentity
        from release_suite import PortableSuiteGateEvidence
    except ImportError as error:  # pragma: no cover - protected installation boundary
        raise PublicReleaseError("full-gate-interface-unavailable", "current RELEASE_VERSION full-gate interface is unavailable") from error
    return _FullGateInterface(
        legacy_evidence_type=FullGateEvidence,
        native_evidence_type=NativeFullGateEvidence,
        retained_candidate_type=RetainedCandidateIdentity,
        portable_suite_type=PortableSuiteGateEvidence,
        portable_build_type=PortableImageBuildEvidence,
        portable_verification_type=PortableImageVerificationEvidence,
        portable_e2e_type=PortableCandidateE2EGateEvidence,
        verify_bound=verify_bound_full_gate_evidence,
        verify_detached_native=verify_detached_native_full_gate_evidence,
        verify_promotion=verify_bound_promotion_evidence,
    )


def _reopen_full_gate_binding(binding: FullGateBinding) -> Path:
    interface = _full_gate_interface()
    root = interface.verify_bound(binding.candidate, binding.compilation, binding.suite, binding.build,
                                  binding.verification, binding.e2e, binding.evidence)
    promotion_root = interface.verify_promotion(binding.candidate, binding.compilation, binding.suite,
                                                binding.build, binding.verification, binding.promotion,
                                                e2e=binding.e2e, full_gate=binding.evidence)
    if root != promotion_root:
        raise PublicReleaseError("full-gate-unproven", "retained gate and promotion proofs do not reopen one Project")
    return root


def _native_packet_receipt_ref(packet: RetainedNativeFullGatePacket) -> str:
    """Return the verified aggregate receipt as an artifact-root-relative ref."""

    root = packet.artifact_root
    evidence_root = getattr(packet.evidence, "evidence_root", None)
    if not isinstance(root, Path) or not root.is_absolute() or not isinstance(evidence_root, str):
        raise PublicReleaseError("invalid-full-gate", "detached native Full Gate packet has no safe artifact-root receipt")
    relative = PurePosixPath(evidence_root)
    if (not evidence_root or "\\" in evidence_root or relative.is_absolute()
            or relative.as_posix() != evidence_root or any(part in {"", ".", ".."} for part in relative.parts)):
        raise PublicReleaseError("invalid-full-gate", "detached native Full Gate receipt root is unsafe")
    receipt = root.joinpath(*relative.parts, "receipt.json")
    try:
        receipt.relative_to(root)
    except ValueError as error:  # pragma: no cover - lexical construction above is exhaustive
        raise PublicReleaseError("invalid-full-gate", "detached native Full Gate receipt escapes its artifact root") from error
    ref = receipt.relative_to(root).as_posix()
    _safe_ref(ref, "detached native Full Gate receipt")
    return ref


def _reopen_detached_native_full_gate(binding: DetachedNativeFullGateBinding) -> tuple[object, str]:
    """Read one retained-native aggregate without reconstructing live candidate state."""

    packet = binding.packet
    interface = _full_gate_interface()
    if not isinstance(packet, RetainedNativeFullGatePacket):
        raise PublicReleaseError("invalid-full-gate", "detached native Full Gate binding needs a typed retained packet")
    if not (
        isinstance(packet.retained_candidate, interface.retained_candidate_type)
        and isinstance(packet.suite, interface.portable_suite_type)
        and isinstance(packet.build, interface.portable_build_type)
        and isinstance(packet.verification, interface.portable_verification_type)
        and isinstance(packet.e2e, interface.portable_e2e_type)
        and isinstance(packet.evidence, interface.native_evidence_type)
    ):
        raise PublicReleaseError("invalid-full-gate", "detached native Full Gate packet has untrusted typed carriers")
    try:
        interface.verify_detached_native(
            packet.artifact_root,
            packet.retained_candidate,
            packet.suite,
            packet.build,
            packet.verification,
            packet.e2e,
            packet.evidence,
        )
    except PublicReleaseError:
        raise
    except Exception as error:
        raise PublicReleaseError("full-gate-unproven", "detached native Full Gate packet cannot be reopened") from error
    return packet.evidence, _native_packet_receipt_ref(packet)


def _full_gate_receipt_ref(binding: FullGateBinding | DetachedNativeFullGateBinding) -> str:
    """Obtain the aggregate receipt ref only after its binding has been reopened."""

    if isinstance(binding, DetachedNativeFullGateBinding):
        return _native_packet_receipt_ref(binding.packet)
    if isinstance(binding, FullGateBinding):
        evidence_root = getattr(binding.evidence, "evidence_root", None)
        if not isinstance(evidence_root, str):
            raise PublicReleaseError("invalid-full-gate", "Full Gate evidence has no receipt root")
        ref = f"{evidence_root}/receipt.json"
        _safe_ref(ref, "Full Gate receipt")
        return ref
    raise PublicReleaseError("invalid-full-gate", "Full Gate binding has no exact receipt")


def _gate(value: object, label: str, source: SourceProof, *, project_root: Path,
          selected_version: str) -> GateResult:
    if not isinstance(value, GateResult):
        raise PublicReleaseError("invalid-full-gate", f"{label} must return GateResult")
    _call(value.call, f"{label}.call")
    if isinstance(value.binding, DetachedNativeFullGateBinding):
        evidence, _receipt_ref = _reopen_detached_native_full_gate(value.binding)
        if not getattr(evidence, "passed", False):
            raise PublicReleaseError("full-gate-unproven", f"{label} requires a passed retained native Full Gate")
        if evidence.candidate_snapshot_manifest_sha256 != source.candidate_snapshot_manifest_sha256:
            raise PublicReleaseError("stale-full-gate", f"{label} does not bind the exact public source snapshot")
        if (not isinstance(evidence.receipt_sha256, str) or _SHA256.fullmatch(evidence.receipt_sha256) is None
                or evidence.framework_version != selected_version
                or _SHA256.fullmatch(evidence.version_toml_sha256 or "") is None
                or evidence.framework_version != source.framework_version
                or evidence.version_toml_sha256 != source.version_toml_sha256):
            raise PublicReleaseError("new-local-cycle-required", f"{label} version or version.toml binding changed; a fresh local release cycle is required")
        return value

    if not isinstance(value.binding, FullGateBinding):
        raise PublicReleaseError("invalid-full-gate", f"{label} must return an exact local or retained-native Full Gate binding")
    interface = _full_gate_interface()
    evidence = value.binding.evidence
    if not isinstance(evidence, interface.legacy_evidence_type) or not evidence.passed:
        raise PublicReleaseError("full-gate-unproven", f"{label} requires current typed passed FullGateEvidence")
    manifest = getattr(value.binding.candidate, "manifest", None)
    candidate_sha = getattr(manifest, "sha256", None)
    candidate_version = getattr(manifest, "framework_version", None)
    candidate_version_toml_sha = getattr(manifest, "version_toml_sha256", None)
    if evidence.candidate_snapshot_manifest_sha256 != source.candidate_snapshot_manifest_sha256:
        raise PublicReleaseError("stale-full-gate", f"{label} does not bind the exact public source snapshot")
    if candidate_sha != source.candidate_snapshot_manifest_sha256:
        raise PublicReleaseError("stale-full-gate", f"{label} candidate does not bind the exact public source snapshot")
    if (not isinstance(evidence.receipt_sha256, str) or _SHA256.fullmatch(evidence.receipt_sha256) is None
            or evidence.framework_version != selected_version
            or candidate_version != selected_version
            or _SHA256.fullmatch(evidence.version_toml_sha256 or "") is None
            or evidence.version_toml_sha256 != candidate_version_toml_sha
            or evidence.framework_version != source.framework_version
            or evidence.version_toml_sha256 != source.version_toml_sha256):
        raise PublicReleaseError("new-local-cycle-required", f"{label} version or version.toml binding changed; a fresh local release cycle is required")
    try:
        root = _reopen_full_gate_binding(value.binding)
    except PublicReleaseError:
        raise
    except Exception as error:
        raise PublicReleaseError("full-gate-unproven", f"{label} cannot reopen its retained local gate/promotion evidence") from error
    if root.resolve() != Path(project_root).resolve():
        raise PublicReleaseError("full-gate-unproven", f"{label} reopens evidence outside the selected Project")
    return value


def _parameters(value: object) -> dict[str, Any]:
    if not isinstance(value, Mapping) or set(value) != {"release", "source", "recovery"}:
        raise PublicReleaseError("invalid-input", "parameters must contain exactly release, source, and recovery")
    release = value["release"]
    source = value["source"]
    recovery = value["recovery"]
    if not isinstance(release, Mapping) or set(release) != {"selected_version", "release_branch", "target_branch", "remote"}:
        raise PublicReleaseError("invalid-input", "release must contain selected_version, release_branch, target_branch, and remote")
    version = release.get("selected_version")
    if not isinstance(version, str) or _VERSION.fullmatch(version) is None:
        raise PublicReleaseError("invalid-version", "selected_version must be a semantic version")
    if release.get("release_branch") != "amm/dev" or release.get("target_branch") != "main":
        raise PublicReleaseError("unsafe-branch", "public release is bound only from amm/dev to main")
    remote = release.get("remote")
    if not isinstance(remote, Mapping) or set(remote) != {"scope", "name", "owner", "repository"}:
        raise PublicReleaseError("invalid-input", "remote must contain scope, name, owner, and repository")
    if remote.get("scope") != "personal" or not isinstance(remote.get("name"), str) or not remote["name"]:
        raise PublicReleaseError("unsafe-remote", "public release requires an explicit personal remote identity")
    _segment(remote.get("owner"), "remote.owner")
    _segment(remote.get("repository"), "remote.repository")
    if not isinstance(source, Mapping) or set(source) != {"candidate_snapshot_manifest_sha256", "readme_ref", "pr_body_ref", "version_history_ref", "version_history_summary"}:
        raise PublicReleaseError("invalid-input", "source must contain exact documentation and snapshot bindings")
    _sha(source.get("candidate_snapshot_manifest_sha256"), "source.candidate_snapshot_manifest_sha256")
    for field in ("readme_ref", "pr_body_ref", "version_history_ref"):
        _safe_ref(source.get(field), f"source.{field}")
    summary = source.get("version_history_summary")
    if (not isinstance(summary, str) or not summary.strip() or "\n" in summary or "\r" in summary
            or len(summary) > 160):
        raise PublicReleaseError("invalid-input", "version_history_summary must be one concise non-empty line")
    if not isinstance(recovery, Mapping) or set(recovery) != {"prior_push", "prior_pr"}:
        raise PublicReleaseError("invalid-input", "recovery must contain prior_push and prior_pr")
    if any(recovery.get(key) not in {"not_started", "confirmed", "unknown"} for key in recovery):
        raise PublicReleaseError("invalid-input", "recovery values must be not_started, confirmed, or unknown")
    if "unknown" in recovery.values():
        raise PublicReleaseError("unknown-remote-effect", "recovery must discover an uncertain push or PR; it cannot replay it")
    return {"release": dict(release), "source": dict(source), "recovery": dict(recovery)}


def _expected_runs(request: Mapping[str, Any]) -> None:
    rows = request.get("requested_runs")
    if not isinstance(rows, list) or len(rows) != 11:
        raise PublicReleaseError("invalid-run-graph", "public release requires one Workflow and five Step/Action pairs")
    expected = [(WORKFLOW_ID, "workflow", None)]
    for _, step, action in STEPS:
        expected.extend(((step, "step", WORKFLOW_ID), (action, "action", step)))
    found: list[tuple[str, str, str | None]] = []
    identifiers: dict[str, str] = {}
    for row in rows:
        if not isinstance(row, Mapping) or not isinstance(row.get("definition"), Mapping):
            raise PublicReleaseError("invalid-run-graph", "requested runs must carry definition bindings")
        definition = row["definition"]
        atom_id, kind = definition.get("atom_id"), row.get("kind")
        parent = row.get("parent_requested_run_id")
        if not isinstance(atom_id, str) or kind not in {"workflow", "step", "action"} or not isinstance(row.get("requested_run_id"), str):
            raise PublicReleaseError("invalid-run-graph", "requested runs have malformed identities")
        identifiers[atom_id] = row["requested_run_id"]
        found.append((atom_id, kind, parent if isinstance(parent, str) else None))
    required_ids = [item[0] for item in expected]
    if sorted(item[0] for item in found) != sorted(required_ids):
        raise PublicReleaseError("invalid-run-graph", "requested runs must bind exactly CA-O-188 through CA-O-198")
    workflow_requested = identifiers.get(WORKFLOW_ID)
    for step_name, step_id, action_id in STEPS:
        step_requested, action_requested = identifiers.get(step_id), identifiers.get(action_id)
        if (step_id, "step", workflow_requested) not in found or (action_id, "action", step_requested) not in found:
            raise PublicReleaseError("invalid-run-graph", f"{step_name} lacks the required Workflow->Step->Action parentage")
        if action_requested is None:
            raise PublicReleaseError("invalid-run-graph", f"{step_name} action is absent")


def _append_call(trace: list[dict[str, Any]], *, operation: str, call: ToolCallEvidence,
                 step_run_id: str, action_run_id: str) -> None:
    trace.append({
        "operation": operation,
        "parent_step_run_id": step_run_id,
        "parent_action_run_id": action_run_id,
        "input_ref": call.input_ref,
        "result_ref": call.result_ref,
        "effect_refs": list(call.effect_refs),
        "report_refs": list(call.report_refs),
    })


def _finish(session: Any, run: Mapping[str, Any], *, outcome: str, result_ref: str,
            effect_refs: list[str], report_ref: str) -> None:
    recorded = session.finish_run(run["run_id"], outcome=outcome, result_ref=result_ref,
                                  effect_refs=effect_refs, report_ref=report_ref)
    if recorded.get("disposition") == "recording_pending":
        raise SelectedRunError("recording-pending", "Run terminal evidence could not be durably recorded")


def _is_terminal(session: RunExecutionSession, run: Mapping[str, Any]) -> bool:
    run_id = run["run_id"]
    return any(record.get("run_id") == run_id for record in (*session.terminal.values(), *session.interrupted.values()))


def _safe_run_evidence_directory(root: Path) -> Path:
    """Create the selected-Run evidence directory without following aliases."""
    try:
        root_status = root.lstat()
    except OSError as error:
        raise PublicReleaseError("run-evidence-unavailable", "selected Project root is unavailable") from error
    if root.is_symlink() or not stat.S_ISDIR(root_status.st_mode):
        raise PublicReleaseError("run-evidence-unavailable", "selected Project root is aliased")
    relative = work_journal.configured_runtime_root(root) / "state" / "work_journal" / "selected_runs" / "evidence"
    current = root
    for component in relative.parts:
        current /= component
        try:
            current.mkdir(mode=0o700)
        except FileExistsError:
            pass
        try:
            status = current.lstat()
        except OSError as error:
            raise PublicReleaseError("run-evidence-unavailable", "Run evidence directory is unavailable") from error
        if current.is_symlink() or not stat.S_ISDIR(status.st_mode):
            raise PublicReleaseError("run-evidence-unavailable", "Run evidence directory is aliased")
    return current


def _run_evidence_ref(session: RunExecutionSession, run: Mapping[str, Any], *, outcome: str) -> str:
    """Write one immutable terminal payload beside selected-Run dispatch evidence."""
    root = Path(session.tracker.root)
    run_id = run.get("run_id")
    definition = run.get("definition")
    if not isinstance(run_id, str) or not run_id or not isinstance(definition, Mapping):
        raise PublicReleaseError("invalid-run-evidence", "started Run lacks a stable identity")
    payload = {
        "schema_version": 1,
        "request_id": session.request["request_id"],
        "run_id": run_id,
        "kind": run["kind"],
        "atom_id": definition["atom_id"],
        "outcome": outcome,
    }
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"
    digest = hashlib.sha256(encoded).hexdigest()
    directory = _safe_run_evidence_directory(root)
    path = directory / f"{digest}.json"
    try:
        descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0), 0o600)
    except FileExistsError:
        try:
            status = path.lstat()
            if path.is_symlink() or not stat.S_ISREG(status.st_mode) or status.st_nlink != 1:
                raise PublicReleaseError("run-evidence-unavailable", "immutable Run evidence is aliased")
            descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0))
            with os.fdopen(descriptor, "rb") as handle:
                existing = handle.read()
            if existing != encoded:
                raise PublicReleaseError("run-evidence-conflict", "immutable Run evidence bytes conflict")
        except OSError as error:
            raise PublicReleaseError("run-evidence-unavailable", "immutable Run evidence cannot be reopened") from error
    else:
        try:
            with os.fdopen(descriptor, "wb") as handle:
                handle.write(encoded)
                handle.flush()
                os.fsync(handle.fileno())
        except OSError as error:
            raise PublicReleaseError("run-evidence-unavailable", "immutable Run evidence cannot be written") from error
    return path.relative_to(root).as_posix()


def _require_prepared_source(expected: Mapping[str, Any], actual: SourceProof, *, pr: PullRequest | None,
                             project_root: Path, release: Mapping[str, Any], require_selected_candidate: bool) -> None:
    _source(actual, "material source", project_root=project_root, release=release)
    if (actual.readme_ref != expected["readme_ref"] or actual.pr_body_ref != expected["pr_body_ref"]
            or actual.version_history_ref != expected["version_history_ref"]):
        raise PublicReleaseError("source-proof-mismatch", "material preparation changed a selected document carrier")
    if actual.version_history_summary != expected["version_history_summary"]:
        raise PublicReleaseError("history-link-invalid", "Version History must retain the requested concise summary")
    if require_selected_candidate and actual.candidate_snapshot_manifest_sha256 != expected["candidate_snapshot_manifest_sha256"]:
        raise PublicReleaseError("source-proof-mismatch", "material preparation does not bind the selected candidate snapshot")
    if pr is None:
        if actual.version_history_pr_url is not None or actual.version_history_pr_number is not None:
            raise PublicReleaseError("history-link-invalid", "Version History cannot name a PR before its identity is verified")
    elif actual.version_history_pr_url != pr.url or actual.version_history_pr_number != pr.number:
        raise PublicReleaseError("history-link-invalid", "Version History must bind the exact verified matching PR")


def _push(value: object, label: str, *, release: Mapping[str, Any]) -> CommitPushResult:
    if not isinstance(value, CommitPushResult) or _COMMIT.fullmatch(value.commit_sha) is None:
        raise PublicReleaseError("invalid-push-proof", f"{label} commit/push must return an immutable commit proof")
    call = _call(value.call, label)
    if not call.effect_refs:
        raise PublicReleaseError("invalid-push-proof", f"{label} commit/push has no remote effect reference")
    receipt = value.receipt
    if (not isinstance(receipt, VerifiedPushReceipt) or receipt.owner != release["remote"]["owner"]
            or receipt.repository != release["remote"]["repository"]
            or receipt.branch != release["release_branch"] or receipt.commit_sha != value.commit_sha):
        raise PublicReleaseError("invalid-push-proof", f"{label} lacks an exact selected-remote push receipt")
    _safe_ref(receipt.receipt_ref, f"{label}.receipt_ref")
    return value


def describe() -> dict[str, Any]:
    return {
        "schema_version": TOOL_SCHEMA_VERSION,
        "tool": TOOL_ID,
        "entrypoint": "TOOLS/PUBLIC_RELEASE/public_release.py",
        "admission": "descriptive prototype only; a native selected-run adapter must be admitted before execution",
        "workflow": WORKFLOW_ID,
        "steps": [{"name": name, "step": step, "action": action} for name, step, action in STEPS],
        "effects": ["planned only: prepare_repository_documents", "planned only: run_current_full_gate", "planned only: git_commit_push", "planned only: find_create_update_main_pr"],
        "limits": [
            "Operator authorization is required for execute admission.",
            "The injected executor is a test/prototype seam, not a CLI-native executor.",
            "Full gate/promotion evidence must reopen durable RELEASE_VERSION files, not pass JSON.",
            "Only personal remote amm/dev to main is in scope; this workflow never merges.",
            "Tool calls are evidence on parent Step/Action Runs, never Tool Runs.",
            "An unknown prior push or PR is discovered, not replayed.",
        ],
    }


def _executor(project_root: Path, bindings: PublicReleaseBindings, trace: list[dict[str, Any]],
              parsed_parameters: Mapping[str, Any]) -> Callable[[dict[str, Any], RunExecutionSession], None]:
    def execute(_request: dict[str, Any], session: RunExecutionSession) -> None:
        workflow = session.start_run(next(row["requested_run_id"] for row in _request["requested_runs"] if row["definition"]["atom_id"] == WORKFLOW_ID))
        effect_refs: list[str] = []
        report_refs: list[str] = []
        source: SourceProof | None = None
        discovered: PullRequest | None = None
        final_pr: PullRequest | None = None
        step: Mapping[str, Any] | None = None
        action: Mapping[str, Any] | None = None
        action_effects: list[str] = []
        action_reports: list[str] = []
        action_result_ref: str | None = None
        try:
            for name, step_id, action_id in STEPS:
                step_requested = next(row["requested_run_id"] for row in _request["requested_runs"] if row["definition"]["atom_id"] == step_id)
                action_requested = next(row["requested_run_id"] for row in _request["requested_runs"] if row["definition"]["atom_id"] == action_id)
                step = session.start_run(step_requested)
                action = session.start_run(action_requested)
                action_effects = []
                action_reports = []
                action_result_ref = None
                if name == "discover_matching_pr":
                    result = bindings.discover_matching_pr(parsed_parameters)
                    call = _call(result.call if isinstance(result, PRDiscovery) else None, name)
                    if not isinstance(result, PRDiscovery) or len(result.matches) > 1:
                        raise PublicReleaseError("duplicate-matching-pr", "discovery must find zero or one matching open main PR")
                    if result.matches:
                        discovered = _pr(result.matches[0], name, release=parsed_parameters["release"])
                    _append_call(trace, operation=name, call=call, step_run_id=step["run_id"], action_run_id=action["run_id"])
                    action_reports.extend(call.report_refs)
                    action_result_ref = call.result_ref
                elif name == "prepare_public_materials":
                    result = bindings.prepare_public_materials(parsed_parameters, discovered.url if discovered else None)
                    if not isinstance(result, PrepareResult):
                        raise PublicReleaseError("invalid-tool-evidence", "prepare_public_materials must return PrepareResult")
                    call = _call(result.call, name)
                    source = _source(result.source, name, project_root=Path(project_root), release=parsed_parameters["release"])
                    _require_prepared_source(parsed_parameters["source"], source, pr=discovered,
                                             project_root=Path(project_root), release=parsed_parameters["release"],
                                             require_selected_candidate=True)
                    _append_call(trace, operation=name, call=call, step_run_id=step["run_id"], action_run_id=action["run_id"])
                    action_effects.extend(call.effect_refs)
                    action_reports.extend(call.report_refs)
                    action_result_ref = call.result_ref
                elif name == "freeze_and_gate":
                    if source is None:
                        raise PublicReleaseError("missing-source-proof", "public materials must be prepared before the full gate")
                    result = _gate(bindings.run_full_gate(parsed_parameters, source, "initial"), name, source,
                                   project_root=Path(project_root), selected_version=parsed_parameters["release"]["selected_version"].removeprefix("v"))
                    _append_call(trace, operation=name, call=result.call, step_run_id=step["run_id"], action_run_id=action["run_id"])
                    action_reports.extend((*result.call.report_refs, _full_gate_receipt_ref(result.binding)))
                    action_result_ref = result.call.result_ref
                elif name == "push_and_upsert_pr":
                    if source is None:
                        raise PublicReleaseError("missing-source-proof", "public materials must be prepared before push")
                    pushed = _push(bindings.commit_and_push(parsed_parameters, source, "initial"), "initial push",
                                   release=parsed_parameters["release"])
                    push_call = pushed.call
                    _append_call(trace, operation="commit_and_push_initial", call=push_call, step_run_id=step["run_id"], action_run_id=action["run_id"])
                    action_effects.extend(push_call.effect_refs)
                    action_reports.extend(push_call.report_refs)
                    action_result_ref = push_call.result_ref
                    upserted = bindings.upsert_main_pr(parsed_parameters, source, discovered.url if discovered else None, "initial")
                    if not isinstance(upserted, PRUpsertResult):
                        raise PublicReleaseError("invalid-pr-evidence", "upsert_main_pr must return PRUpsertResult")
                    pr_call = _call(upserted.call, "initial PR")
                    final_pr = _pr(upserted.pull_request, "initial PR", release=parsed_parameters["release"])
                    if discovered is not None and final_pr.url != discovered.url:
                        raise PublicReleaseError("duplicate-matching-pr", "PR upsert changed the early-discovered matching PR identity")
                    _append_call(trace, operation="find_create_update_main_pr", call=pr_call, step_run_id=step["run_id"], action_run_id=action["run_id"])
                    action_effects.extend(pr_call.effect_refs)
                    action_reports.extend(pr_call.report_refs)
                    action_result_ref = pr_call.result_ref
                else:
                    if final_pr is None:
                        raise PublicReleaseError("missing-pr-proof", "a final PR proof is required before Version History finalization")
                    result = bindings.finalize_history_link(parsed_parameters, source, final_pr)
                    if not isinstance(result, FinalizationResult):
                        raise PublicReleaseError("invalid-tool-evidence", "finalize_history_link must return FinalizationResult")
                    final_call = _call(result.call, name)
                    if source is None:
                        raise PublicReleaseError("missing-source-proof", "public materials must be prepared before history finalization")
                    final_source = _source(result.source, name, project_root=Path(project_root), release=parsed_parameters["release"])
                    if result.changed:
                        if discovered is not None:
                            raise PublicReleaseError("history-link-invalid", "existing PR history finalization cannot report an unbound source change")
                        _require_prepared_source(parsed_parameters["source"], final_source, pr=final_pr,
                                                 project_root=Path(project_root), release=parsed_parameters["release"],
                                                 require_selected_candidate=False)
                        if final_source.candidate_snapshot_manifest_sha256 == source.candidate_snapshot_manifest_sha256:
                            raise PublicReleaseError("history-link-invalid", "new PR history finalization needs its actual URL and a new source snapshot")
                        _append_call(trace, operation="finalize_version_history", call=final_call, step_run_id=step["run_id"], action_run_id=action["run_id"])
                        action_effects.extend(final_call.effect_refs)
                        action_reports.extend(final_call.report_refs)
                        action_result_ref = final_call.result_ref
                        renewed = _gate(bindings.run_full_gate(parsed_parameters, final_source, "history_link_final"), "renewed full gate", final_source,
                                        project_root=Path(project_root), selected_version=parsed_parameters["release"]["selected_version"].removeprefix("v"))
                        _append_call(trace, operation="renewed_full_gate", call=renewed.call, step_run_id=step["run_id"], action_run_id=action["run_id"])
                        action_reports.extend((*renewed.call.report_refs, _full_gate_receipt_ref(renewed.binding)))
                        action_result_ref = renewed.call.result_ref
                        pushed = _push(bindings.commit_and_push(parsed_parameters, final_source, "history_link_final"), "final push",
                                       release=parsed_parameters["release"])
                        push_call = pushed.call
                        _append_call(trace, operation="commit_and_push_history_link", call=push_call, step_run_id=step["run_id"], action_run_id=action["run_id"])
                        action_effects.extend(push_call.effect_refs)
                        action_reports.extend(push_call.report_refs)
                        action_result_ref = push_call.result_ref
                        refreshed = bindings.upsert_main_pr(parsed_parameters, final_source, final_pr.url, "history_link_final")
                        if not isinstance(refreshed, PRUpsertResult):
                            raise PublicReleaseError("invalid-pr-evidence", "final PR refresh must return PRUpsertResult")
                        refresh_call = _call(refreshed.call, "final PR refresh")
                        refreshed_pr = _pr(refreshed.pull_request, "final PR refresh", release=parsed_parameters["release"])
                        if refreshed_pr.url != final_pr.url:
                            raise PublicReleaseError("duplicate-matching-pr", "final PR refresh changed the created PR identity")
                        _append_call(trace, operation="refresh_main_pr", call=refresh_call, step_run_id=step["run_id"], action_run_id=action["run_id"])
                        action_effects.extend(refresh_call.effect_refs)
                        action_reports.extend(refresh_call.report_refs)
                        action_result_ref = refresh_call.result_ref
                        source = final_source
                    else:
                        _require_prepared_source(parsed_parameters["source"], final_source, pr=final_pr,
                                                 project_root=Path(project_root), release=parsed_parameters["release"],
                                                 require_selected_candidate=True)
                        _append_call(trace, operation="finalize_version_history", call=final_call, step_run_id=step["run_id"], action_run_id=action["run_id"])
                        action_reports.extend(final_call.report_refs)
                        action_result_ref = final_call.result_ref
                action_result_ref = _run_evidence_ref(session, action, outcome="completed")
                step_result_ref = _run_evidence_ref(session, step, outcome="completed")
                _finish(session, action, outcome="completed", result_ref=action_result_ref,
                        effect_refs=action_effects, report_ref=action_reports[0] if action_reports else action_result_ref)
                _finish(session, step, outcome="completed", result_ref=step_result_ref,
                        effect_refs=action_effects, report_ref=action_reports[0] if action_reports else step_result_ref)
                effect_refs.extend(action_effects)
                report_refs.extend(action_reports)
            workflow_result_ref = _run_evidence_ref(session, workflow, outcome="completed")
            _finish(session, workflow, outcome="completed", result_ref=workflow_result_ref,
                    effect_refs=effect_refs, report_ref=report_refs[0] if report_refs else workflow_result_ref)
        except PublicReleaseInterrupted as interrupted:
            call = getattr(interrupted, "call", None)
            if isinstance(call, ToolCallEvidence):
                action_effects.extend(call.effect_refs)
                action_reports.extend(call.report_refs)
                action_result_ref = call.result_ref
            action_result_ref = action_result_ref or _run_evidence_ref(session, action, outcome="interrupted_pending")
            step_result_ref = _run_evidence_ref(session, step, outcome="interrupted_pending")
            workflow_result_ref = _run_evidence_ref(session, workflow, outcome="interrupted_pending")
            _finish(session, action, outcome="interrupted_pending", result_ref=action_result_ref,
                    effect_refs=action_effects, report_ref=action_reports[0] if action_reports else action_result_ref)
            _finish(session, step, outcome="interrupted_pending", result_ref=step_result_ref,
                    effect_refs=action_effects, report_ref=action_reports[0] if action_reports else step_result_ref)
            _finish(session, workflow, outcome="interrupted_pending", result_ref=workflow_result_ref,
                    effect_refs=effect_refs + action_effects, report_ref=report_refs[0] if report_refs else workflow_result_ref)
        except PublicReleaseError:
            action_result_ref = _run_evidence_ref(session, action, outcome="failed")
            step_result_ref = _run_evidence_ref(session, step, outcome="failed")
            workflow_result_ref = _run_evidence_ref(session, workflow, outcome="failed")
            _finish(session, action, outcome="failed", result_ref=action_result_ref,
                    effect_refs=action_effects, report_ref=action_reports[0] if action_reports else action_result_ref)
            _finish(session, step, outcome="failed", result_ref=step_result_ref,
                    effect_refs=action_effects, report_ref=action_reports[0] if action_reports else step_result_ref)
            _finish(session, workflow, outcome="failed", result_ref=workflow_result_ref,
                    effect_refs=effect_refs + action_effects, report_ref=report_refs[0] if report_refs else workflow_result_ref)
            # The shared recorder now owns a truthful terminal result.  Do not
            # raise into RunTracker, which correctly treats uncaught failures
            # as uncertain interruption rather than an observed failed action.
            return
        except BaseException as error:
            if isinstance(error, SelectedRunError) and error.code == "recording-pending":
                raise
            if action is not None and step is not None:
                interrupted_result_ref = action_result_ref or _run_evidence_ref(session, action, outcome="interrupted_pending")
                if not _is_terminal(session, action):
                    _finish(session, action, outcome="interrupted_pending", result_ref=interrupted_result_ref,
                            effect_refs=action_effects, report_ref=action_reports[0] if action_reports else interrupted_result_ref)
                if not _is_terminal(session, step):
                    step_result_ref = _run_evidence_ref(session, step, outcome="interrupted_pending")
                    _finish(session, step, outcome="interrupted_pending", result_ref=step_result_ref,
                            effect_refs=action_effects, report_ref=action_reports[0] if action_reports else step_result_ref)
                workflow_effects = [*effect_refs, *action_effects]
                if workflow_effects and not _is_terminal(session, workflow):
                    session.note_effects(workflow["run_id"], result_ref=interrupted_result_ref,
                                         effect_refs=workflow_effects)
            raise

    return execute


def run_execution_session(project_root: Path, session: RunExecutionSession, *,
                          bindings: PublicReleaseBindings) -> list[dict[str, Any]]:
    """Execute public release inside one already-admitted shared Run session."""
    if not isinstance(session, RunExecutionSession):
        raise PublicReleaseError("invalid-run-session", "public release requires an admitted RunExecutionSession")
    try:
        selected_root = Path(project_root).resolve(strict=True)
        session_root = Path(session.tracker.root).resolve(strict=True)
    except OSError as error:
        raise PublicReleaseError("invalid-run-session", "selected Project root cannot be reopened") from error
    if selected_root != session_root:
        raise PublicReleaseError("invalid-run-session", "shared Run session belongs to a different selected Project")
    _expected_runs(session.request)
    parsed_parameters = _parameters(session.request.get("parameters"))
    trace: list[dict[str, Any]] = []
    _executor(selected_root, bindings, trace, parsed_parameters)(session.request, session)
    return trace


def run(project_root: Path, request: Mapping[str, Any], *, bindings: PublicReleaseBindings,
        source_observer: Callable[[dict[str, Any]], Mapping[str, Any]],
        journal_context: Mapping[str, str] | None = None) -> dict[str, Any]:
    """Compatibility wrapper that admits and runs one public-release session."""

    if not isinstance(request, Mapping):
        raise PublicReleaseError("invalid-input", "request must be an object")
    _expected_runs(request)
    _parameters(request.get("parameters"))
    trace: list[dict[str, Any]] = []

    def executor(_request: dict[str, Any], session: RunExecutionSession) -> None:
        trace.extend(run_execution_session(Path(project_root), session, bindings=bindings))

    tracker = RunTracker(Path(project_root), source_observer=source_observer, executor=executor,
                         journal_context=journal_context)
    try:
        result = tracker.run_selected_operation(dict(request))
    except SelectedRunError as error:
        raise PublicReleaseError(error.code, str(error)) from error
    return {**result, "tool_calls": trace, "workflow": WORKFLOW_ID}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--describe", action="store_true", help="emit the installed source contract")
    args = parser.parse_args()
    if not args.describe:
        parser.error("execution requires admitted selected-run bindings; use this entrypoint with --describe only")
    print(json.dumps(describe(), ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
