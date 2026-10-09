"""Private bounded host E2E evidence after the isolated release suite gate.

This gate deliberately has a smaller authority surface than a promotion.  It
can inspect the immutable candidate image and run exactly the three committed
host harnesses; it cannot select an image, create a Docker daemon/socket
route, retry an effect, call a public MCP route, or promote anything.  A
test-double result remains explicitly incomplete evidence.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import re
import selectors
import signal
import subprocess
import sys
import tempfile
import time
import tomllib
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, replace
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any, Literal

from release_contract import ReleaseContractError, ValidatedCandidate, canonical_json
from release_e2e_context import CANDIDATE_IMAGE_ENVIRONMENT_VARIABLE, CONTEXT_ENVIRONMENT_VARIABLE
from release_handoff import CANONICAL_SOURCE_RELATIVE, FRAMEWORK_SETTINGS_RELATIVE, PackageRow, SealedCandidateCompilation, tree_sha256
from release_image import (ImageBuildEvidence, ImageVerificationEvidence,
                           PortableImageBuildEvidence, PortableImageVerificationEvidence,
                           read_image_execution_artifacts, verify_bound_image_evidence)
from release_package_evidence import PackageEvidenceView, bind_package_evidence
from release_packaging import RUNTIME_ROOT, ReleasePackagingError, _verify_release
from release_portable_contract import SealedPortableCandidateCompilation
from release_portable_package import PreparedPortableReleasePackage
from release_retained_candidate import RetainedCandidateIdentity, reopen_retained_candidate_identity
from release_retained_package import RetainedNativePackageEvidence, read_retained_native_package_evidence
from release_suite import (PortableSuiteGateEvidence, SuiteGateEvidence, _active_n_state,
                           _active_skill_records, _safe_path, _validate_bound_inputs,
                           verify_bound_suite_evidence)
from release_test_phases import derive_test_phase_map


EVIDENCE_ROOT = ".caprmedio_runtime/release_e2e"
GRAMMAR_RELATIVE = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/release_e2e_bindings.json"
DRIVER_RELATIVE = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/run_release_e2e.py"
_ENVIRONMENT_KEYS = (
    "PATH", "TMPDIR", CONTEXT_ENVIRONMENT_VARIABLE, CANDIDATE_IMAGE_ENVIRONMENT_VARIABLE,
)
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_IMAGE_ID = re.compile(r"^sha256:[0-9a-f]{64}$")
_MAX_CONTEXT_BYTES = 256 * 1024
_N_DRIVER_RELATIVE = (
    "FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/run_release_e2e.py"
)
_DOCKER_CANDIDATES = (
    "/usr/local/bin/docker",
    "/opt/homebrew/bin/docker",
    "/usr/bin/docker",
    "/Applications/Docker.app/Contents/Resources/bin/docker",
)
DEFAULT_FRAMEWORK_SETTINGS_RELATIVE = (
    f"{CANONICAL_SOURCE_RELATIVE}/001_CORE_META_MODEL/caprmedio_framework_default_settings.toml"
)
_LIMIT_KEYS = (
    "inspect_timeout_seconds",
    "harness_timeout_seconds",
    "cleanup_timeout_seconds",
    "max_stdout_bytes",
    "max_stderr_bytes",
    "max_junit_bytes",
)
_SETTINGS_SNAPSHOT_FILENAME = "release-e2e-limits.json"
_RETAINED_GRAMMAR_FILENAME = "release-e2e-grammar.json"
_RETAINED_DEFAULT_SETTINGS_FILENAME = "release-e2e-default-settings.toml"
_RETAINED_INSTANCE_SETTINGS_FILENAME = "release-e2e-instance-settings.toml"


@dataclass(frozen=True)
class ReleaseE2ELimits:
    """The six fixed caps for one bounded E2E attempt; callers cannot override them."""

    inspect_timeout_seconds: float = 60.0
    harness_timeout_seconds: float = 900.0
    cleanup_timeout_seconds: float = 60.0
    max_stdout_bytes: int = 8 * 1024 * 1024
    max_stderr_bytes: int = 8 * 1024 * 1024
    max_junit_bytes: int = 8 * 1024 * 1024


DEFAULT_RELEASE_E2E_LIMITS = ReleaseE2ELimits()


@dataclass(frozen=True)
class FrozenReleaseE2ELimits:
    """Exact framework settings bytes and resolved limits for one attempt."""

    limits: ReleaseE2ELimits
    snapshot: bytes
    sha256: str
    default_settings: bytes
    instance_settings: bytes


@dataclass(frozen=True)
class E2EExecutionResult:
    exit_code: int | None
    stdout: bytes
    stderr: bytes
    timed_out: bool = False
    output_limited: bool = False
    cleanup_uncertain: bool = False


@dataclass(frozen=True)
class ExecutableIdentity:
    """One resolved, byte-identified executable or controller carrier."""

    role: Literal["n_host_controller", "python", "driver", "docker"]
    path: str
    sha256: str


@dataclass(frozen=True)
class FrozenHostE2ECapability:
    """N-bound host command identities, captured before E2E process effects."""

    executing_selector_sha256: str
    executing_release_package_sha256: str
    executing_skill_sha256: str
    n_host_controller: ExecutableIdentity
    python: ExecutableIdentity
    driver: ExecutableIdentity
    docker: ExecutableIdentity
    closed_path: str


class HostE2EExecutor:
    """The sole production adapter: N-bound fixed host processes, never a shell.

    It obtains the executable identities from fixed locations rather than a
    caller argument or ambient ``PATH``.  The gate freezes and reopens those
    identities around every candidate E2E attempt.
    """

    execution_kind = "host-subprocess"

    def __init__(self) -> None:
        self._frozen_limits: ReleaseE2ELimits | None = None

    @staticmethod
    def _external_identity(path: Path, *, role: Literal["python", "docker"]) -> ExecutableIdentity:
        resolved = path.resolve(strict=True)
        if (not resolved.is_absolute() or resolved.is_symlink() or not resolved.is_file()
                or not os.access(resolved, os.X_OK)):
            raise ReleaseContractError("release-e2e-host-executable-invalid", f"trusted {role} executable is unavailable")
        return ExecutableIdentity(role, str(resolved), _digest(resolved.read_bytes()))

    @classmethod
    def freeze_capability(cls, root: Path, candidate: ValidatedCandidate) -> FrozenHostE2ECapability:
        """Derive the N controller and exact host executables without PATH lookup."""

        n_state = _active_n_state(root, candidate)
        n_root = root / RUNTIME_ROOT / "releases" / candidate.authority.executing_release
        # The N copy of the fixed JUnit driver *is* the host controller.  It
        # validates the sealed context and runs the one pinned unittest phase;
        # executing it directly avoids introducing an RPC or wrapper layer.
        controller = _regular(n_root, _N_DRIVER_RELATIVE, label="frozen N host controller")
        driver = _regular(n_root, _N_DRIVER_RELATIVE, label="frozen N E2E driver")
        python = cls._external_identity(Path(sys.executable), role="python")
        docker_path = next((Path(value) for value in _DOCKER_CANDIDATES if Path(value).is_file()), None)
        if docker_path is None:
            raise ReleaseContractError("release-e2e-host-executable-missing", "trusted Docker executable is unavailable")
        docker = cls._external_identity(docker_path, role="docker")
        n_host_controller = ExecutableIdentity("n_host_controller", str(controller), _digest(controller.read_bytes()))
        n_driver = ExecutableIdentity("driver", str(driver), _digest(driver.read_bytes()))
        # Python and the N controller are always absolute argv[0:2] paths.
        # The grammar deliberately retains its literal ``docker`` token, so
        # its closed PATH contains only the byte-attested Docker directory.
        closed_path = str(Path(docker.path).parent)
        return FrozenHostE2ECapability(*n_state, n_host_controller, python, n_driver, docker, closed_path)

    @classmethod
    def revalidate_capability(cls, root: Path, candidate: ValidatedCandidate,
                              frozen: FrozenHostE2ECapability) -> None:
        """Refuse any changed current-N, controller, driver, or host executable."""

        observed = cls.freeze_capability(root, candidate)
        if observed != frozen:
            raise ReleaseContractError("release-currentness-stale", "frozen host E2E capability changed during execution")

    def _bind_frozen_limits(self, limits: ReleaseE2ELimits) -> None:
        """Gate-private binding; public callers cannot provide process limits."""

        self._frozen_limits = limits

    @staticmethod
    def _stop_process_group(process: subprocess.Popen[bytes], timeout_seconds: float) -> bool:
        """End a timed-out/over-limit command and prove its process group exited."""

        if process.poll() is not None:
            return True
        try:
            os.killpg(process.pid, signal.SIGTERM)
        except ProcessLookupError:
            return process.poll() is not None
        except OSError:
            return False
        try:
            process.wait(timeout=timeout_seconds)
            return True
        except subprocess.TimeoutExpired:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                return process.poll() is not None
            except OSError:
                return False
            try:
                process.wait(timeout=timeout_seconds)
                return True
            except subprocess.TimeoutExpired:
                return False

    @staticmethod
    def _append_bounded(buffer: bytearray, chunk: bytes, limit: int) -> bool:
        """Append at most the configured bytes and say whether the stream exceeded it."""

        remaining = limit - len(buffer)
        if remaining <= 0:
            return bool(chunk)
        if len(chunk) > remaining:
            buffer.extend(chunk[:remaining])
            return True
        buffer.extend(chunk)
        return False

    def run(self, argv: tuple[str, ...], *, cwd: Path, environment: dict[str, str], timeout_seconds: float) -> E2EExecutionResult:
        """Run one fixed command with the gate's already-frozen output limits."""

        if not argv or any(not isinstance(item, str) or not item for item in argv):
            raise ReleaseContractError("release-e2e-command-invalid", "E2E executor received an invalid fixed argv")
        limits = self._frozen_limits
        if limits is None:
            raise ReleaseContractError("release-e2e-limits-unbound", "host E2E executor has no frozen Framework settings")
        try:
            process = subprocess.Popen(
                argv, cwd=cwd, env=environment, stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False,
                start_new_session=True,
            )
        except OSError:
            raise
        assert process.stdout is not None and process.stderr is not None
        stdout, stderr = bytearray(), bytearray()
        selector = selectors.DefaultSelector()
        selector.register(process.stdout, selectors.EVENT_READ, "stdout")
        selector.register(process.stderr, selectors.EVENT_READ, "stderr")
        deadline = time.monotonic() + timeout_seconds
        timed_out = False
        output_limited = False
        cleanup_uncertain = False
        try:
            while selector.get_map():
                remaining_seconds = deadline - time.monotonic()
                if remaining_seconds <= 0:
                    timed_out = True
                    break
                events = selector.select(timeout=remaining_seconds)
                if not events:
                    timed_out = True
                    break
                for key, _event in events:
                    stream = key.fileobj
                    chunk = os.read(stream.fileno(), 64 * 1024)
                    if not chunk:
                        selector.unregister(stream)
                        continue
                    limit = limits.max_stdout_bytes if key.data == "stdout" else limits.max_stderr_bytes
                    buffer = stdout if key.data == "stdout" else stderr
                    output_limited = self._append_bounded(buffer, chunk, limit) or output_limited
                    if output_limited:
                        break
                if output_limited:
                    break
            if timed_out or output_limited:
                cleanup_uncertain = not self._stop_process_group(process, limits.cleanup_timeout_seconds)
            elif process.poll() is None:
                remaining_seconds = deadline - time.monotonic()
                if remaining_seconds <= 0:
                    timed_out = True
                    cleanup_uncertain = not self._stop_process_group(process, limits.cleanup_timeout_seconds)
                else:
                    try:
                        process.wait(timeout=remaining_seconds)
                    except subprocess.TimeoutExpired:
                        timed_out = True
                        cleanup_uncertain = not self._stop_process_group(process, limits.cleanup_timeout_seconds)
            return E2EExecutionResult(process.poll(), bytes(stdout), bytes(stderr), timed_out, output_limited, cleanup_uncertain)
        finally:
            selector.close()
            process.stdout.close()
            process.stderr.close()


@dataclass(frozen=True)
class HarnessReceipt:
    source_path: str
    source_sha256: str
    argv: tuple[str, ...]
    started_at: str
    finished_at: str
    exit_code: int | None
    timed_out: bool
    stdout_path: str
    stdout_sha256: str
    stderr_path: str
    stderr_sha256: str
    junit_path: str
    junit_sha256: str | None
    executed_tests: int
    elapsed_seconds: float
    reason: str


@dataclass(frozen=True)
class CandidateE2EGateEvidence:
    candidate_snapshot_manifest_sha256: str
    candidate_image_digest: str
    phase_map_sha256: str
    grammar_sha256: str
    outcome: Literal["passed", "failed", "timed_out", "incomplete", "stale", "recording_uncertain"]
    reason: str
    harness_receipts: tuple[HarnessReceipt, ...]
    evidence_root: str
    receipt_sha256: str | None
    settings_snapshot_path: str | None
    settings_snapshot_sha256: str | None
    host_capability_path: str | None
    host_capability_sha256: str | None
    execution_kind: Literal["host-subprocess", "test-double"]

    @property
    def passed(self) -> bool:
        return self.outcome == "passed" and self.execution_kind == "host-subprocess" and self.receipt_sha256 is not None


@dataclass(frozen=True, kw_only=True)
class PortableCandidateE2EGateEvidence(CandidateE2EGateEvidence):
    """Portable-package E2E receipt with its closed D597/D596 bindings.

    Schema-2 receipts intentionally continue to use ``CandidateE2EGateEvidence``
    and therefore retain their original canonical receipt bytes.  Portable
    receipts must carry every package identity needed by a later Full Gate;
    none of these values is inferred from a legacy carrier.
    """

    package_schema: Literal["portable-1"]
    package_manifest_sha256: str
    package_evidence_sha256: str
    package_evidence_relpath: str
    source_catalog_sha256: str
    candidate_run_id: str
    input_manifest_sha256: str
    framework_version: str
    version_toml_sha256: str


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ReleaseContractError("release-e2e-grammar-invalid", "E2E grammar has a duplicate key")
        result[key] = value
    return result


def _regular(root: Path, relative: str, *, label: str) -> Path:
    path = PurePosixPath(relative)
    if (not relative or path.is_absolute() or path.as_posix() != relative
            or any(part in {"", ".", ".."} for part in path.parts)):
        raise ReleaseContractError("release-e2e-path-unsafe", f"{label} is not a safe relative path")
    target = root.joinpath(*path.parts)
    if target.is_symlink() or not target.is_file():
        raise ReleaseContractError("release-e2e-input-missing", f"{label} is absent or unsafe")
    try:
        target.resolve(strict=True).relative_to(root.resolve(strict=True))
    except ValueError as error:
        raise ReleaseContractError("release-e2e-path-unsafe", f"{label} escapes the candidate root") from error
    return target


def _parse_grammar(raw: bytes) -> dict[str, Any]:
    if len(raw) > _MAX_CONTEXT_BYTES:
        raise ReleaseContractError("release-e2e-grammar-invalid", "E2E grammar exceeds its fixed size")
    try:
        grammar = json.loads(raw.decode("utf-8"), object_pairs_hook=_reject_duplicates)
    except (UnicodeDecodeError, json.JSONDecodeError, ReleaseContractError) as error:
        raise ReleaseContractError("release-e2e-grammar-invalid", "E2E grammar is not canonical JSON") from error
    expected_keys = {"schema_version", "environment_keys", "image_inspect_argv", "driver", "harnesses"}
    if not isinstance(grammar, dict) or set(grammar) != expected_keys or grammar.get("schema_version") != 1:
        raise ReleaseContractError("release-e2e-grammar-invalid", "E2E grammar has an unsupported schema")
    if tuple(grammar.get("environment_keys", ())) != _ENVIRONMENT_KEYS:
        raise ReleaseContractError("release-e2e-grammar-invalid", "E2E grammar environment is not closed")
    if grammar.get("driver") != DRIVER_RELATIVE:
        raise ReleaseContractError("release-e2e-grammar-invalid", "E2E grammar selects an unsupported driver")
    inspect = grammar.get("image_inspect_argv")
    if inspect != ["docker", "image", "inspect", "--format", "{{.Id}}", "{candidate_image_digest}"]:
        raise ReleaseContractError("release-e2e-grammar-invalid", "E2E grammar image inspection is not fixed")
    harnesses = grammar.get("harnesses")
    if not isinstance(harnesses, list) or len(harnesses) != 3:
        raise ReleaseContractError("release-e2e-grammar-invalid", "E2E grammar must contain exactly three harnesses")
    seen: set[str] = set()
    for row in harnesses:
        if not isinstance(row, dict) or set(row) != {"source_path", "argv", "context_optins"}:
            raise ReleaseContractError("release-e2e-grammar-invalid", "E2E harness has an unsupported shape")
        source_path, argv, optins = row["source_path"], row["argv"], row["context_optins"]
        if not isinstance(source_path, str) or source_path in seen or not source_path.startswith("102_FRAMEWORK_ENGINE/"):
            raise ReleaseContractError("release-e2e-grammar-invalid", "E2E harness source path is invalid or duplicated")
        seen.add(source_path)
        if (not isinstance(argv, list) or len(argv) != 8 or argv[0] != "{trusted_python}"
                or argv[1] != DRIVER_RELATIVE or argv[2:7] != ["--start-directory", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests", "--pattern", Path(source_path).name, "--junit"]
                or argv[7] != "{e2e_junit_path}"):
            raise ReleaseContractError("release-e2e-grammar-invalid", "E2E harness argv is not fixed to the JUnit driver")
        if not isinstance(optins, dict) or any(not isinstance(key, str) or not isinstance(value, str) for key, value in optins.items()):
            raise ReleaseContractError("release-e2e-grammar-invalid", "E2E harness opt-ins are invalid")
    required_sources = {
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_docker_e2e.py",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_workflows_docker_e2e.py",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_query_mcp_e2e.py",
    }
    if seen != required_sources:
        raise ReleaseContractError("release-e2e-grammar-invalid", "E2E grammar harness set changed")
    # The E2E phase-map is independently sealed from the candidate inventory;
    # it is never re-derived from this mutable grammar carrier.
    return grammar


def _load_grammar(root: Path) -> tuple[dict[str, Any], bytes, str, str]:
    path = _regular(root, GRAMMAR_RELATIVE, label="E2E grammar")
    raw = path.read_bytes()
    return _parse_grammar(raw), raw, _digest(raw), ""


def _executor_kind(executor: object) -> Literal["host-subprocess", "test-double"]:
    if type(executor) is HostE2EExecutor:
        return "host-subprocess"
    if getattr(executor, "execution_kind", None) == "test-double" and callable(getattr(executor, "run", None)):
        return "test-double"
    raise ReleaseContractError("release-e2e-executor-untrusted", "E2E requires HostE2EExecutor or an explicitly marked test double")


def _portable_package_view(
    candidate: ValidatedCandidate,
    compilation: SealedCandidateCompilation | SealedPortableCandidateCompilation,
    unit_suite: object,
    image_build: object,
    image: object,
    *,
    prepared_package: PreparedPortableReleasePackage | None,
) -> PackageEvidenceView | None:
    """Reopen the physical portable package and bind native predecessors.

    Package evidence owns the package re-open.  E2E only compares closed
    predecessor receipts to that fresh result; it neither reconstructs a
    schema-2 compilation nor creates a package identity.
    """

    if isinstance(compilation, SealedCandidateCompilation):
        if prepared_package is not None:
            raise ReleaseContractError(
                "release-e2e-package-schema-mismatch",
                "schema-2 candidate E2E does not accept a portable package receipt",
            )
        return None
    if not isinstance(compilation, SealedPortableCandidateCompilation):
        raise ReleaseContractError(
            "release-e2e-handoff-untrusted",
            "candidate E2E requires a sealed legacy or portable compilation",
        )
    if not isinstance(prepared_package, PreparedPortableReleasePackage):
        raise ReleaseContractError(
            "release-e2e-portable-package-required",
            "portable candidate E2E requires the typed prepared package receipt",
        )
    try:
        package = bind_package_evidence(candidate, compilation, prepared_package=prepared_package)
    except Exception as error:
        code = getattr(error, "code", "release-e2e-portable-package-invalid")
        raise ReleaseContractError(str(code), "portable package evidence could not be physically reopened") from error
    if (
        package.package_schema != "portable-1"
        or package.source_catalog_sha256 is None
        or package.candidate_run_id is None
        or package.input_manifest_sha256 is None
        or package.candidate_snapshot_manifest_sha256 != candidate.manifest.sha256
        or package.framework_version != candidate.manifest.framework_version
        or package.version_toml_sha256 != candidate.manifest.version_toml_sha256
    ):
        raise ReleaseContractError(
            "release-e2e-portable-package-mismatch",
            "reopened portable package does not bind the sealed candidate/version/catalog",
        )
    shared = {
        "source_catalog_sha256": package.source_catalog_sha256,
        "candidate_run_id": package.candidate_run_id,
        "input_manifest_sha256": package.input_manifest_sha256,
        "framework_version": package.framework_version,
        "version_toml_sha256": package.version_toml_sha256,
    }
    image_expected = {
        "package_schema": package.package_schema,
        **shared,
    }
    for label, evidence, expected in (
        ("portable Unit", unit_suite, {**shared, "input_schema": "portable-1", "phase_map_sha256": package.phase_map.sha256}),
        ("portable image build", image_build, {**image_expected, "package_manifest_sha256": package.actual_package_manifest_sha256}),
        ("portable image verification", image, {**image_expected, "package_manifest_sha256": package.actual_package_manifest_sha256}),
    ):
        for field, value in expected.items():
            if getattr(evidence, field, None) != value:
                raise ReleaseContractError(
                    "release-e2e-portable-predecessor-mismatch",
                    f"{label} does not bind the reopened portable package: {field}",
                )
    _portable_sidecar_binding(image_build, image)
    return package


def _portable_sidecar_binding(image_build: object, image: object) -> tuple[str, str]:
    """Require both native Image receipts to bind one retained package view.

    At execution time E2E must reject a missing, malformed, or disagreeing
    Image binding before it can execute any host harness. The retained-artifact
    reader reopens the sidecar later; its carrier remains Project-relative and
    is intentionally not converted into a schema-2 receipt field.
    """

    bindings: list[tuple[str, str]] = []
    for label, evidence in (("portable image build", image_build), ("portable image verification", image)):
        digest = getattr(evidence, "package_evidence_sha256", None)
        relative = getattr(evidence, "package_evidence_relpath", None)
        if not isinstance(digest, str) or _SHA256.fullmatch(digest) is None:
            raise ReleaseContractError(
                "release-e2e-portable-predecessor-mismatch",
                f"{label} lacks a retained package-evidence digest",
            )
        if not isinstance(relative, str):
            raise ReleaseContractError(
                "release-e2e-portable-predecessor-mismatch",
                f"{label} lacks a retained package-evidence carrier",
            )
        path = PurePosixPath(relative)
        if (
            not relative
            or path.is_absolute()
            or path.as_posix() != relative
            or any(part in {"", ".", ".."} for part in path.parts)
            or path.parent.name != "package_evidence"
            or path.name != f"{digest}.json"
        ):
            raise ReleaseContractError(
                "release-e2e-portable-predecessor-mismatch",
                f"{label} package-evidence carrier is not canonical",
            )
        bindings.append((digest, relative))
    if bindings[0] != bindings[1]:
        raise ReleaseContractError(
            "release-e2e-portable-predecessor-mismatch",
            "portable Image receipts bind different retained package evidence",
        )
    return bindings[0]


def _read_retained_portable_image_package(
    root: Path,
    image_build: object,
    image: object,
) -> PackageEvidenceView:
    """Reopen the native package named by Image receipts through its sidecar.

    This is the retained-artifact counterpart to ``_portable_package_view``.
    It deliberately accepts no prepared receipt and does not call the live
    package-evidence binder: original E2E proof must remain readable after
    selection or checkout changes.
    """

    if not isinstance(image_build, PortableImageBuildEvidence) or not isinstance(image, PortableImageVerificationEvidence):
        raise ReleaseContractError(
            "release-e2e-retained-package-untrusted",
            "portable retained E2E artifacts require native Image receipts",
        )
    digest, relative = _portable_sidecar_binding(image_build, image)
    # Retention preserves a content-addressed package beside the sidecar. The
    # Docker context names its copy ``PACKAGE`` and therefore cannot satisfy
    # the package verifier's content-addressed-root invariant.
    sidecar = _regular(root, relative, label="retained portable package evidence")
    candidate_root = sidecar.parent.parent
    package_root = candidate_root / "package" / image_build.package_manifest_sha256
    if package_root.is_symlink() or not package_root.is_dir():
        raise ReleaseContractError(
            "release-e2e-retained-package-untrusted",
            "portable sidecar lacks its retained content-addressed package",
        )
    try:
        retained = read_retained_native_package_evidence(
            package_root,
            sidecar,
            expected_sha256=digest,
        )
    except ReleaseContractError as error:
        raise ReleaseContractError(
            "release-e2e-retained-package-untrusted",
            "portable image package evidence cannot be reopened",
        ) from error
    view = retained.view
    expected = {
        "package_schema": "portable-1",
        "package_manifest_sha256": view.actual_package_manifest_sha256,
        "source_catalog_sha256": view.source_catalog_sha256,
        "candidate_run_id": view.candidate_run_id,
        "input_manifest_sha256": view.input_manifest_sha256,
        "framework_version": view.framework_version,
        "version_toml_sha256": view.version_toml_sha256,
        "package_evidence_sha256": retained.receipt_sha256,
        "package_evidence_relpath": relative,
    }
    for label, evidence in (("portable image build", image_build), ("portable image verification", image)):
        if any(getattr(evidence, field, None) != value for field, value in expected.items()):
            raise ReleaseContractError(
                "release-e2e-retained-package-untrusted",
                f"{label} does not bind the reopened retained package",
            )
    return view


def _reopen_predecessors(
    candidate: ValidatedCandidate,
    compilation: SealedCandidateCompilation | SealedPortableCandidateCompilation,
    unit_suite: SuiteGateEvidence,
    image_build: ImageBuildEvidence,
    image: ImageVerificationEvidence,
    *,
    prepared_package: PreparedPortableReleasePackage | None = None,
) -> tuple[Path, PackageEvidenceView | None]:
    """Reopen predecessor bytes, rather than trusting fields a caller supplies."""

    package = _portable_package_view(
        candidate, compilation, unit_suite, image_build, image, prepared_package=prepared_package,
    )
    if package is None:
        root = _validate_bound_inputs(candidate, compilation)
        suite_root = verify_bound_suite_evidence(candidate, compilation, unit_suite)
        image_attempt = verify_bound_image_evidence(candidate, compilation, unit_suite, image_build, image)
    else:
        suite_root = verify_bound_suite_evidence(candidate, compilation, unit_suite)
        image_attempt = verify_bound_image_evidence(
            candidate, compilation, unit_suite, image_build, image, prepared_package=prepared_package,
        )
        root = Path(candidate.project_root).resolve()
    expected_image_attempt = _safe_path(root, image.evidence_root)
    if suite_root != root or image_attempt != expected_image_attempt:
        raise ReleaseContractError("release-e2e-predecessor-root-mismatch", "predecessor evidence reopened outside its bound candidate carrier")
    if _IMAGE_ID.fullmatch(image.candidate_image_digest) is None:
        raise ReleaseContractError("release-e2e-image-untrusted", "reopened image evidence lacks an immutable candidate ID")
    return root, package


def _bound_phase_map(candidate: ValidatedCandidate, grammar: dict[str, Any],
                     package: PackageEvidenceView | None = None):
    """Bind grammar phases to the independently sealed candidate test map."""

    phase_map = derive_test_phase_map(candidate)
    grammar_paths = tuple(sorted(row["source_path"] for row in grammar["harnesses"]))
    if grammar_paths != phase_map.candidate_e2e_paths:
        raise ReleaseContractError("release-e2e-phase-map-mismatch", "E2E grammar paths differ from the sealed candidate phase map")
    if package is not None and package.phase_map != phase_map:
        raise ReleaseContractError("release-e2e-phase-map-mismatch", "portable package phase map differs from the sealed candidate phase map")
    return phase_map


def _utc_timestamp() -> str:
    """An unambiguous, timezone-aware wall-clock carrier for one harness."""

    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def _parse_utc_timestamp(value: object) -> datetime:
    if not isinstance(value, str) or not value.endswith("Z"):
        raise ReleaseContractError("release-e2e-evidence-untrusted", "E2E harness timestamp is not an explicit UTC value")
    try:
        parsed = datetime.fromisoformat(value.removesuffix("Z") + "+00:00")
    except ValueError as error:
        raise ReleaseContractError("release-e2e-evidence-untrusted", "E2E harness timestamp is malformed") from error
    if parsed.tzinfo != timezone.utc or parsed.isoformat(timespec="microseconds").replace("+00:00", "Z") != value:
        raise ReleaseContractError("release-e2e-evidence-untrusted", "E2E harness timestamp is not canonical UTC")
    return parsed


def _sealed_source_rows(
    compilation: SealedCandidateCompilation | SealedPortableCandidateCompilation,
) -> tuple[object, ...]:
    """Return source-bearing rows without coercing portable input to schema-2."""

    if isinstance(compilation, SealedCandidateCompilation):
        return tuple(compilation.package_rows)
    if isinstance(compilation, SealedPortableCandidateCompilation):
        return tuple(compilation.portable_package_rows)
    raise ReleaseContractError("release-e2e-handoff-untrusted", "candidate E2E compilation is not typed")


def _source_control_fingerprint(root: Path, candidate: ValidatedCandidate,
                                compilation: SealedCandidateCompilation | SealedPortableCandidateCompilation,
                                grammar: bytes) -> str:
    """Fingerprint every sealed source carrier the host driver may observe."""

    rows: dict[str, tuple[str, int]] = {}
    for row in candidate.manifest.source_inventory_rows:
        rows[row.source_path] = (row.source_sha256, row.source_mode)
    for row in _sealed_source_rows(compilation):
        source_path = getattr(row, "source_path", None)
        digest = getattr(row, "sha256", None)
        mode = getattr(row, "mode", None)
        if (
            not isinstance(source_path, str)
            or not isinstance(digest, str)
            or _SHA256.fullmatch(digest) is None
            or type(mode) is not int
            or not 0 <= mode <= 0o777
        ):
            raise ReleaseContractError("release-e2e-handoff-untrusted", "sealed candidate source row is invalid")
        prior = rows.setdefault(source_path, (digest, mode))
        if prior != (digest, mode):
            raise ReleaseContractError("release-e2e-binding-mismatch", "candidate and compilation seal conflicting source bytes")
    records: list[dict[str, object]] = []
    for relative, (expected_sha, expected_mode) in sorted(rows.items()):
        path = _regular(root, relative, label="sealed E2E source")
        observed = path.read_bytes()
        actual_mode = path.stat().st_mode & 0o777
        actual_sha = _digest(observed)
        if actual_sha != expected_sha or actual_mode != expected_mode:
            raise ReleaseContractError("release-currentness-stale", f"sealed source changed: {relative}")
        records.append({"path": relative, "sha256": actual_sha, "mode": actual_mode})
    grammar_path = _regular(root, GRAMMAR_RELATIVE, label="E2E grammar")
    if grammar_path.read_bytes() != grammar:
        raise ReleaseContractError("release-currentness-stale", "E2E grammar changed during candidate execution")
    records.append({"path": GRAMMAR_RELATIVE, "sha256": _digest(grammar), "mode": grammar_path.stat().st_mode & 0o777})
    return _digest(canonical_json(records))


def _write_new(path: Path, payload: bytes) -> None:
    with path.open("xb") as stream:
        stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())


def _freeze_release_e2e_settings(default_raw: bytes, instance_raw: bytes) -> FrozenReleaseE2ELimits:
    """Resolve the closed E2E limit set from physically supplied TOML bytes."""

    try:
        default_document = tomllib.loads(default_raw.decode("utf-8"))
        instance_document = tomllib.loads(instance_raw.decode("utf-8"))
    except (UnicodeDecodeError, tomllib.TOMLDecodeError) as error:
        raise ReleaseContractError("release-e2e-settings-invalid", "release E2E Framework settings are invalid TOML") from error
    default_table = default_document.get("release_e2e") if isinstance(default_document, dict) else None
    instance_table = instance_document.get("release_e2e", {}) if isinstance(instance_document, dict) else None
    if (not isinstance(default_table, dict) or set(default_table) != set(_LIMIT_KEYS)
            or not isinstance(instance_table, dict) or not set(instance_table).issubset(_LIMIT_KEYS)):
        raise ReleaseContractError("release-e2e-settings-invalid", "release E2E Framework settings have an unsupported shape")
    values = {key: instance_table.get(key, default_table[key]) for key in _LIMIT_KEYS}
    for key in _LIMIT_KEYS[:3]:
        value = values[key]
        if type(value) not in {int, float} or not math.isfinite(float(value)) or float(value) <= 0:
            raise ReleaseContractError("release-e2e-settings-invalid", f"release E2E setting is not finite and positive: {key}")
    for key in _LIMIT_KEYS[3:]:
        value = values[key]
        if type(value) is not int or value <= 0:
            raise ReleaseContractError("release-e2e-settings-invalid", f"release E2E setting is not a positive byte limit: {key}")
    limits = ReleaseE2ELimits(
        float(values["inspect_timeout_seconds"]),
        float(values["harness_timeout_seconds"]),
        float(values["cleanup_timeout_seconds"]),
        values["max_stdout_bytes"], values["max_stderr_bytes"], values["max_junit_bytes"],
    )
    snapshot = canonical_json({
        "schema_version": 1,
        "default_settings": {
            "path": DEFAULT_FRAMEWORK_SETTINGS_RELATIVE,
            "sha256": _digest(default_raw),
        },
        "instance_settings": {
            "path": FRAMEWORK_SETTINGS_RELATIVE,
            "sha256": _digest(instance_raw),
        },
        "limits": asdict(limits),
    })
    return FrozenReleaseE2ELimits(limits, snapshot, _digest(snapshot), default_raw, instance_raw)


def _release_e2e_settings(root: Path, candidate: ValidatedCandidate) -> FrozenReleaseE2ELimits:
    """Resolve the six D582 caps from default TOML plus the Framework Instance.

    The snapshot carries both source-byte digests and the resolved values. It
    is retained with an attempt and reopened before a later admission, rather
    than treating a caller-provided limit or a live TOML read as authoritative.
    """

    default_path = _regular(root, DEFAULT_FRAMEWORK_SETTINGS_RELATIVE, label="default E2E settings")
    instance_path = _regular(root, FRAMEWORK_SETTINGS_RELATIVE, label="Framework Instance settings")
    default_raw, instance_raw = default_path.read_bytes(), instance_path.read_bytes()
    if _digest(instance_raw) != candidate.manifest.framework_settings_digest:
        raise ReleaseContractError("release-currentness-stale", "Framework Instance settings no longer match the candidate seal")
    return _freeze_release_e2e_settings(default_raw, instance_raw)


def _reopen_release_e2e_settings(root: Path, candidate: ValidatedCandidate,
                                 evidence: CandidateE2EGateEvidence) -> ReleaseE2ELimits:
    """Require the retained snapshot and currently reopened Framework settings to agree."""

    if (not isinstance(evidence.settings_snapshot_path, str)
            or not isinstance(evidence.settings_snapshot_sha256, str)
            or _SHA256.fullmatch(evidence.settings_snapshot_sha256) is None
            or evidence.settings_snapshot_path != f"{evidence.evidence_root}/{_SETTINGS_SNAPSHOT_FILENAME}"):
        raise ReleaseContractError("release-e2e-settings-untrusted", "candidate E2E evidence lacks a bound settings snapshot")
    path = _regular(root, evidence.settings_snapshot_path, label="candidate E2E settings snapshot")
    snapshot = path.read_bytes()
    frozen = _release_e2e_settings(root, candidate)
    if _digest(snapshot) != evidence.settings_snapshot_sha256 or snapshot != frozen.snapshot:
        raise ReleaseContractError("release-e2e-settings-untrusted", "candidate E2E settings changed or snapshot is not bound")
    return frozen.limits


def _reopen_retained_release_e2e_settings(root: Path, evidence: CandidateE2EGateEvidence) -> ReleaseE2ELimits:
    """Reopen the settings bytes recorded with an original E2E attempt.

    Unlike fresh admission, this must not consult mutable Framework settings:
    the snapshot, both TOML carriers, and their resolved limits form one
    original-proof packet beneath the immutable attempt root.
    """

    if (not isinstance(evidence.settings_snapshot_path, str)
            or not isinstance(evidence.settings_snapshot_sha256, str)
            or _SHA256.fullmatch(evidence.settings_snapshot_sha256) is None
            or evidence.settings_snapshot_path != f"{evidence.evidence_root}/{_SETTINGS_SNAPSHOT_FILENAME}"):
        raise ReleaseContractError("release-e2e-settings-untrusted", "candidate E2E evidence lacks a bound settings snapshot")
    snapshot = _regular(root, evidence.settings_snapshot_path, label="candidate E2E settings snapshot").read_bytes()
    default_raw = _regular(
        root,
        f"{evidence.evidence_root}/{_RETAINED_DEFAULT_SETTINGS_FILENAME}",
        label="retained default E2E settings",
    ).read_bytes()
    instance_raw = _regular(
        root,
        f"{evidence.evidence_root}/{_RETAINED_INSTANCE_SETTINGS_FILENAME}",
        label="retained Framework Instance E2E settings",
    ).read_bytes()
    frozen = _freeze_release_e2e_settings(default_raw, instance_raw)
    if _digest(snapshot) != evidence.settings_snapshot_sha256 or snapshot != frozen.snapshot:
        raise ReleaseContractError("release-e2e-settings-untrusted", "retained E2E settings packet is incomplete or changed")
    return frozen.limits


def _reopen_retained_grammar(root: Path, evidence: CandidateE2EGateEvidence) -> tuple[dict[str, Any], bytes]:
    """Reopen the exact fixed-three-harness grammar recorded by the attempt."""

    raw = _regular(
        root,
        f"{evidence.evidence_root}/{_RETAINED_GRAMMAR_FILENAME}",
        label="retained candidate E2E grammar",
    ).read_bytes()
    if _digest(raw) != evidence.grammar_sha256:
        raise ReleaseContractError("release-e2e-evidence-untrusted", "retained E2E grammar bytes changed or are unbound")
    return _parse_grammar(raw), raw


def _cap_test_double_result(result: E2EExecutionResult, limits: ReleaseE2ELimits) -> E2EExecutionResult:
    """Prevent a test double from writing unbounded evidence bytes.

    Production subprocess reads are capped before accumulation in
    :meth:`HostE2EExecutor.run`; this branch only makes synthetic adapters
    obey the same retained-artifact bound.
    """

    stdout_limited = len(result.stdout) > limits.max_stdout_bytes
    stderr_limited = len(result.stderr) > limits.max_stderr_bytes
    return replace(
        result,
        stdout=result.stdout[:limits.max_stdout_bytes],
        stderr=result.stderr[:limits.max_stderr_bytes],
        output_limited=result.output_limited or stdout_limited or stderr_limited,
    )


def _execution_result(value: object) -> E2EExecutionResult:
    if not isinstance(value, E2EExecutionResult):
        raise TypeError("E2E executor returned an untyped result")
    if value.exit_code is not None and (type(value.exit_code) is not int or value.exit_code < 0):
        raise TypeError("E2E executor exit code is invalid")
    if (not isinstance(value.stdout, bytes) or not isinstance(value.stderr, bytes)
            or type(value.timed_out) is not bool or type(value.output_limited) is not bool
            or type(value.cleanup_uncertain) is not bool):
        raise TypeError("E2E executor result streams are invalid")
    return value


def _read_bounded_file(path: Path, limit: int) -> bytes | None:
    """Read no more than one byte beyond a retained-file limit."""

    if path.is_symlink() or not path.is_file():
        return None
    try:
        with path.open("rb") as stream:
            payload = stream.read(limit + 1)
    except OSError:
        return None
    return payload if len(payload) <= limit else None


def _observe_junit(path: Path, limit: int) -> tuple[int, str | None, str, bytes | None]:
    payload = _read_bounded_file(path, limit)
    if payload is None:
        return 0, None, "JUnit report is missing, unsafe or too large", None
    payload_sha256 = _digest(payload)
    if b"<!DOCTYPE" in payload.upper() or b"<!ENTITY" in payload.upper():
        return 0, payload_sha256, "JUnit report contains unsupported declarations", payload
    try:
        root = ET.fromstring(payload)
    except ET.ParseError:
        return 0, payload_sha256, "JUnit report is malformed", payload
    if root.tag not in {"testsuite", "testsuites"}:
        return 0, payload_sha256, "JUnit report has an unsupported root", payload
    cases = list(root.iter("testcase"))
    if not cases:
        return 0, payload_sha256, "JUnit report has zero testcases", payload
    if any(list(case.iter("failure")) or list(case.iter("error")) or list(case.iter("skipped")) for case in cases):
        return len(cases), payload_sha256, "JUnit report contains failed, errored or skipped testcases", payload
    for suite in (node for node in root.iter() if node.tag in {"testsuite", "testsuites"}):
        actual = len(list(suite.iter("testcase")))
        for key, expected in (("tests", actual), ("failures", 0), ("errors", 0), ("skipped", 0)):
            if key in suite.attrib:
                try:
                    if int(suite.attrib[key]) != expected:
                        return len(cases), payload_sha256, "JUnit summary is inconsistent", payload
                except ValueError:
                    return len(cases), payload_sha256, "JUnit summary is invalid", payload
    return len(cases), payload_sha256, "", payload


def _read_bounded_artifact(root: Path, relative: str, *, limit: int, label: str) -> bytes:
    path = _regular(root, relative, label=label)
    payload = _read_bounded_file(path, limit)
    if payload is None:
        raise ReleaseContractError("release-e2e-evidence-untrusted", f"{label} exceeds its frozen byte limit")
    return payload


def _context_bytes_for_binding(root: Path, scratch: Path, reports: Path,
                               candidate_snapshot_manifest_sha256: str,
                               candidate_image_digest: str, grammar_sha256: str,
                               phase_map_sha256: str,
                               grammar: dict[str, Any]) -> tuple[bytes, tuple[dict[str, Any], ...]]:
    """Render the immutable attempt context from already sealed identities.

    This deliberately needs only the candidate/image identities, not a live
    ``ValidatedCandidate``.  Detached retained readers use the same grammar
    and path binding without turning a descriptor back into a live candidate.
    """

    harnesses: list[dict[str, Any]] = []
    for row in grammar["harnesses"]:
        pattern = Path(row["source_path"]).name
        junit_path = reports / f"{pattern}.xml"
        harnesses.append({
            "source_path": row["source_path"],
            "start_directory": row["argv"][3],
            "pattern": pattern,
            "junit_path": str(junit_path),
            "context_optins": row["context_optins"],
        })
    payload = {
        "schema_version": 1,
        "source_root": str(root.resolve()),
        "scratch_root": str(scratch.resolve()),
        "report_root": str(reports.resolve()),
        "candidate_snapshot_manifest_sha256": candidate_snapshot_manifest_sha256,
        "candidate_image_digest": candidate_image_digest,
        "grammar_sha256": grammar_sha256,
        "phase_map_sha256": phase_map_sha256,
        "fixed_harnesses": harnesses,
        "phase_bindings": ["image-inspect", *(row["pattern"] for row in harnesses)],
    }
    encoded = canonical_json(payload)
    if len(encoded) > _MAX_CONTEXT_BYTES:
        raise ReleaseContractError("release-e2e-context-invalid", "sealed E2E context exceeds its fixed size")
    return encoded, tuple(harnesses)


def _context_bytes(root: Path, scratch: Path, reports: Path, candidate: ValidatedCandidate,
                   image: ImageVerificationEvidence, grammar_sha256: str, phase_map_sha256: str,
                   grammar: dict[str, Any]) -> tuple[bytes, tuple[dict[str, Any], ...]]:
    """Render a live-candidate context through the shared sealed binding."""

    return _context_bytes_for_binding(
        root, scratch, reports, candidate.manifest.sha256, image.candidate_image_digest,
        grammar_sha256, phase_map_sha256, grammar,
    )


@dataclass(frozen=True)
class _CapturedE2EContext:
    """Original execution paths carried as immutable identities, never read."""

    source_root: Path
    scratch_root: Path
    reports_root: Path


def _captured_absolute_path(value: object, *, label: str) -> Path:
    """Accept one canonical absolute POSIX identity without touching its target."""

    if not isinstance(value, str) or not value:
        raise ReleaseContractError("release-e2e-evidence-untrusted", f"captured {label} path is invalid")
    path = PurePosixPath(value)
    if (
        not path.is_absolute()
        or path.as_posix() != value
        or any(part in {"", ".", ".."} for part in path.parts)
    ):
        raise ReleaseContractError("release-e2e-evidence-untrusted", f"captured {label} path is unsafe")
    return Path(value)


def _reopen_relocated_e2e_context(root: Path, evidence: CandidateE2EGateEvidence,
                                  candidate_snapshot_manifest_sha256: str,
                                  image: ImageVerificationEvidence, grammar_sha256: str,
                                  phase_map_sha256: str,
                                  grammar: dict[str, Any]) -> _CapturedE2EContext:
    """Validate an unchanged original context copied below ``root``.

    The context's absolute paths identify where execution happened originally.
    They are deliberately parsed but never reopened: all evidence bytes remain
    read through ``root``.  This is the detached equivalent of Image's
    relocated command-shape validation.
    """

    context = _read_bounded_artifact(
        root, f"{evidence.evidence_root}/scratch/context.json",
        limit=_MAX_CONTEXT_BYTES, label="candidate E2E context",
    )
    try:
        document = json.loads(context.decode("utf-8"), object_pairs_hook=_reject_duplicates)
    except (UnicodeDecodeError, json.JSONDecodeError, ReleaseContractError) as error:
        raise ReleaseContractError("release-e2e-evidence-untrusted", "captured candidate E2E context is invalid") from error
    required = {
        "schema_version", "source_root", "scratch_root", "report_root",
        "candidate_snapshot_manifest_sha256", "candidate_image_digest",
        "grammar_sha256", "phase_map_sha256", "fixed_harnesses", "phase_bindings",
    }
    if not isinstance(document, dict) or set(document) != required or canonical_json(document) != context:
        raise ReleaseContractError("release-e2e-evidence-untrusted", "captured candidate E2E context is not canonical")
    source_root = _captured_absolute_path(document["source_root"], label="source root")
    scratch_root = _captured_absolute_path(document["scratch_root"], label="scratch root")
    reports_root = _captured_absolute_path(document["report_root"], label="report root")
    evidence_relative = PurePosixPath(evidence.evidence_root)
    expected_scratch = source_root.joinpath(*evidence_relative.parts, "scratch")
    expected_reports = expected_scratch / "reports"
    if scratch_root != expected_scratch or reports_root != expected_reports:
        raise ReleaseContractError("release-e2e-evidence-untrusted", "captured E2E work paths do not form the fixed attempt layout")
    expected_harnesses = []
    for row in grammar["harnesses"]:
        pattern = Path(row["source_path"]).name
        expected_harnesses.append({
            "source_path": row["source_path"],
            "start_directory": row["argv"][3],
            "pattern": pattern,
            "junit_path": str(reports_root / f"{pattern}.xml"),
            "context_optins": row["context_optins"],
        })
    if (
        type(document["schema_version"]) is not int
        or document["schema_version"] != 1
        or document["candidate_snapshot_manifest_sha256"] != candidate_snapshot_manifest_sha256
        or document["candidate_image_digest"] != image.candidate_image_digest
        or document["grammar_sha256"] != grammar_sha256
        or document["phase_map_sha256"] != phase_map_sha256
        or document["fixed_harnesses"] != expected_harnesses
        or document["phase_bindings"] != ["image-inspect", *(item["pattern"] for item in expected_harnesses)]
    ):
        raise ReleaseContractError("release-e2e-evidence-untrusted", "captured E2E context does not match its sealed grammar and identities")
    return _CapturedE2EContext(source_root, scratch_root, reports_root)


def _receipt_path(root: Path, evidence_root: str) -> Path:
    return _safe_path(root, evidence_root) / "receipt.json"


def _host_identities_bytes(capability: FrozenHostE2ECapability) -> bytes:
    return canonical_json({
        "schema_version": 1,
        "executing_selector_sha256": capability.executing_selector_sha256,
        "executing_release_package_sha256": capability.executing_release_package_sha256,
        "executing_skill_sha256": capability.executing_skill_sha256,
        "closed_path": capability.closed_path,
        "identities": [asdict(capability.n_host_controller), asdict(capability.python),
                       asdict(capability.driver), asdict(capability.docker)],
    })


def _identity_from_payload(value: object, *, role: Literal["n_host_controller", "python", "driver", "docker"]) -> ExecutableIdentity:
    if not isinstance(value, dict) or set(value) != {"role", "path", "sha256"}:
        raise ReleaseContractError("release-e2e-capability-invalid", "host capability identity has an unsupported shape")
    path, digest = value.get("path"), value.get("sha256")
    if (value.get("role") != role or not isinstance(path, str) or not Path(path).is_absolute()
            or not isinstance(digest, str) or _SHA256.fullmatch(digest) is None):
        raise ReleaseContractError("release-e2e-capability-invalid", "host capability identity is invalid")
    return ExecutableIdentity(role, path, digest)


def _reopen_host_capability(root: Path, evidence: CandidateE2EGateEvidence) -> FrozenHostE2ECapability:
    """Reopen the receipt-bound frozen host capability before later consumption."""

    if not isinstance(evidence.host_capability_path, str) or not isinstance(evidence.host_capability_sha256, str):
        raise ReleaseContractError("release-e2e-capability-untrusted", "actual E2E evidence lacks its frozen host capability carrier")
    expected = f"{evidence.evidence_root}/host-identities.json"
    if evidence.host_capability_path != expected or _SHA256.fullmatch(evidence.host_capability_sha256) is None:
        raise ReleaseContractError("release-e2e-capability-untrusted", "host capability carrier path or digest is invalid")
    path = _regular(root, evidence.host_capability_path, label="retained host capability")
    payload = path.read_bytes()
    if _digest(payload) != evidence.host_capability_sha256:
        raise ReleaseContractError("release-e2e-capability-untrusted", "retained host capability bytes changed")
    try:
        raw = json.loads(payload.decode("utf-8"), object_pairs_hook=_reject_duplicates)
    except (UnicodeDecodeError, json.JSONDecodeError, ReleaseContractError) as error:
        raise ReleaseContractError("release-e2e-capability-invalid", "retained host capability is not canonical JSON") from error
    required = {
        "schema_version", "executing_selector_sha256", "executing_release_package_sha256",
        "executing_skill_sha256", "closed_path", "identities",
    }
    if not isinstance(raw, dict) or set(raw) != required or raw.get("schema_version") != 1 or canonical_json(raw) != payload:
        raise ReleaseContractError("release-e2e-capability-invalid", "retained host capability has an unsupported schema")
    state = []
    for field in ("executing_selector_sha256", "executing_release_package_sha256", "executing_skill_sha256"):
        value = raw.get(field)
        if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
            raise ReleaseContractError("release-e2e-capability-invalid", "retained host capability has invalid N currentness")
        state.append(value)
    identities = raw.get("identities")
    if not isinstance(identities, list) or len(identities) != 4:
        raise ReleaseContractError("release-e2e-capability-invalid", "retained host capability identities are incomplete")
    controller, python, driver, docker = (
        _identity_from_payload(value, role=role)
        for value, role in zip(identities, ("n_host_controller", "python", "driver", "docker"), strict=True)
    )
    closed_path = raw.get("closed_path")
    expected_path = str(Path(docker.path).parent)
    if (not isinstance(closed_path, str) or closed_path != expected_path
            or controller.path != driver.path or controller.sha256 != driver.sha256):
        raise ReleaseContractError("release-e2e-capability-invalid", "retained host controller is not the exact executed N driver")
    return FrozenHostE2ECapability(*state, controller, python, driver, docker, closed_path)


def verify_bound_candidate_e2e_evidence(
    candidate: ValidatedCandidate,
    compilation: SealedCandidateCompilation | SealedPortableCandidateCompilation,
    unit_suite: SuiteGateEvidence,
    image: ImageVerificationEvidence,
    evidence: CandidateE2EGateEvidence,
    *,
    image_build: ImageBuildEvidence,
    prepared_package: PreparedPortableReleasePackage | None = None,
) -> Path:
    """Reopen actual candidate-E2E artifacts; this never promotes a candidate.

    The retained host capability is receipt-bound and then independently
    re-derived from frozen N.  Deleting or replacing that carrier, or changing
    the N controller/Python/driver/Docker bytes, therefore invalidates a later
    consumer instead of leaving an unauthenticated side file beside a receipt.
    """

    root, package = _reopen_predecessors(
        candidate, compilation, unit_suite, image_build, image, prepared_package=prepared_package,
    )
    capability = _read_candidate_e2e_artifacts(root, candidate, compilation, image, evidence, package=package)
    HostE2EExecutor.revalidate_capability(root, candidate, capability)
    return root


def _verify_retained_host_capability_for_release(root: Path, executing_release: str,
                                                 unit_suite: object,
                                                 capability: FrozenHostE2ECapability,
                                                 *, captured_source_root: Path | None = None) -> None:
    """Prove original N and executable bytes without consulting current selection.

    ``executing_release`` is sealed in both a live candidate manifest and a
    retained descriptor.  Keeping it explicit lets the detached path reopen
    the original host packet without reconstructing a ``ValidatedCandidate``.
    """

    expected_state = (
        unit_suite.executing_selector_sha256, unit_suite.executing_release_package_sha256,
        unit_suite.executing_skill_sha256,
    )
    actual_state = (
        capability.executing_selector_sha256, capability.executing_release_package_sha256,
        capability.executing_skill_sha256,
    )
    if actual_state != expected_state:
        raise ReleaseContractError("release-e2e-capability-untrusted", "host capability differs from the original Suite N identity")
    if not isinstance(executing_release, str) or not executing_release:
        raise ReleaseContractError("release-e2e-capability-untrusted", "retained host capability has no sealed executing release")
    package_relative = f"{RUNTIME_ROOT}/releases/{executing_release}"
    package = _safe_path(root, package_relative)
    manifest_bytes = _regular(root, f"{package_relative}/manifest.toml", label="retained N manifest").read_bytes()
    try:
        manifest_text = manifest_bytes.decode("utf-8")
        manifest = tomllib.loads(manifest_text)
        rows = [PackageRow.model_validate({
            "resource": row["resource"], "source_path": row["source_path"],
            "destination_path": row["destination"], "sha256": row["sha256"], "mode": row["mode"],
        }) for row in manifest["files"]]
        _verify_release(package, manifest_text, rows)
    except (KeyError, OSError, TypeError, ValueError, ReleasePackagingError) as error:
        raise ReleaseContractError("release-e2e-capability-untrusted", "original N package bytes or modes changed") from error
    if tree_sha256(root, package_relative) != capability.executing_release_package_sha256:
        raise ReleaseContractError("release-e2e-capability-untrusted", "original N package no longer matches the frozen host capability")
    skill_files, skill_directories = _active_skill_records(root, f"{package_relative}/SKILLS/ca")
    skill_sha = _digest(canonical_json({"files": skill_files, "directories": sorted(skill_directories)}))
    if skill_sha != capability.executing_skill_sha256:
        raise ReleaseContractError("release-e2e-capability-untrusted", "original N Skill no longer matches the frozen host capability")
    controller = _regular(root, f"{package_relative}/{_N_DRIVER_RELATIVE}", label="retained N host controller")
    if captured_source_root is not None:
        # Detached packets preserve original absolute executable paths.  Tie
        # those immutable path identities to the captured source root while
        # reopening the actual controller only from the archive root.
        expected_captured_controller = captured_source_root / package_relative / _N_DRIVER_RELATIVE
        if (
            capability.n_host_controller.path != str(expected_captured_controller)
            or capability.driver.path != str(expected_captured_controller)
            or _digest(controller.read_bytes()) != capability.n_host_controller.sha256
            or capability.driver.sha256 != capability.n_host_controller.sha256
        ):
            raise ReleaseContractError("release-e2e-capability-untrusted", "retained host controller differs from its captured execution identity")
        for identity in (capability.python, capability.docker):
            _captured_absolute_path(identity.path, label=f"{identity.role} executable")
        return
    if capability.n_host_controller.path != str(controller) or capability.driver.path != str(controller):
        raise ReleaseContractError("release-e2e-capability-untrusted", "retained host controller is outside the exact original N package")
    for identity in (capability.n_host_controller, capability.python, capability.driver, capability.docker):
        path = Path(identity.path)
        try:
            resolved = path.resolve(strict=True)
            if (resolved != path or path.is_symlink() or not path.is_file()
                    or (identity.role in {"python", "docker"} and not os.access(path, os.X_OK))
                    or _digest(path.read_bytes()) != identity.sha256):
                raise ValueError("executable bytes or carrier changed")
        except (OSError, ValueError) as error:
            raise ReleaseContractError("release-e2e-capability-untrusted", f"retained {identity.role} executable changed") from error


def _verify_retained_host_capability(root: Path, candidate: ValidatedCandidate,
                                     unit_suite: SuiteGateEvidence,
                                     capability: FrozenHostE2ECapability) -> None:
    """Live-reader compatibility wrapper for the shared retained check."""

    _verify_retained_host_capability_for_release(
        root, candidate.authority.executing_release, unit_suite, capability,
    )


def read_candidate_e2e_execution_artifacts(
    candidate: ValidatedCandidate,
    compilation: SealedCandidateCompilation | SealedPortableCandidateCompilation,
    unit_suite: SuiteGateEvidence,
    image: ImageVerificationEvidence,
    evidence: CandidateE2EGateEvidence,
    *,
    image_build: ImageBuildEvidence,
    prepared_package: PreparedPortableReleasePackage | None = None,
) -> Path:
    """Read exact original E2E proof after selection, without admitting any effect.

    The original Suite and Image receipts, frozen N package/controller and host
    executables remain byte-bound. Current selection and public Skill ownership
    are separate duties of the promotion consumer; fresh admission still uses
    ``verify_bound_candidate_e2e_evidence`` and its active-N guard.
    """

    if isinstance(compilation, SealedPortableCandidateCompilation):
        # Original-artifact consumption is intentionally independent of a
        # current checkout/package rebind. The Image reader and the helper
        # below reopen only retained private artifacts and the sidecar.
        image_attempt = read_image_execution_artifacts(
            candidate, compilation, unit_suite, image_build, image, prepared_package=prepared_package,
        )
        root = Path(candidate.project_root).resolve()
        package = _read_retained_portable_image_package(root, image_build, image)
        retained_inputs = True
    else:
        package = _portable_package_view(
            candidate, compilation, unit_suite, image_build, image, prepared_package=prepared_package,
        )
        if package is not None:  # pragma: no cover - only a typed portable compilation returns one
            raise ReleaseContractError("release-e2e-handoff-untrusted", "legacy artifact reader received portable package evidence")
        image_attempt = read_image_execution_artifacts(candidate, compilation, unit_suite, image_build, image)
        root = Path(candidate.project_root).resolve()
        retained_inputs = False
    if image_attempt != _safe_path(root, image.evidence_root):
        raise ReleaseContractError("release-e2e-predecessor-root-mismatch", "image artifacts reopened outside their bound candidate carrier")
    capability = _read_candidate_e2e_artifacts(
        root, candidate, compilation, image, evidence, package=package, retained=retained_inputs,
    )
    _verify_retained_host_capability(root, candidate, unit_suite, capability)
    return root


def _detached_artifact_root(value: Path) -> Path:
    """Open one explicit retained-artifact root without checkout authority."""

    if not isinstance(value, Path) or not value.is_absolute() or any(part == ".." for part in value.parts):
        raise ReleaseContractError("release-e2e-artifact-root-invalid", "detached candidate E2E requires an absolute artifact root")
    try:
        observed = value.lstat()
        root = value.resolve(strict=True)
    except OSError as error:
        raise ReleaseContractError("release-e2e-artifact-root-invalid", "detached artifact root is unavailable") from error
    if value.is_symlink() or not root.is_dir() or not os.path.samestat(observed, root.stat()):
        raise ReleaseContractError("release-e2e-artifact-root-invalid", "detached artifact root is unsafe")
    return root


def _reopen_detached_candidate_at_root(root: Path,
                                       retained_candidate: RetainedCandidateIdentity) -> RetainedCandidateIdentity:
    """Reopen a D597 identity and require every retained reference below ``root``."""

    if not isinstance(retained_candidate, RetainedCandidateIdentity):
        raise ReleaseContractError(
            "release-e2e-retained-candidate-root-mismatch",
            "detached E2E requires a typed retained candidate identity",
        )
    package = retained_candidate.package_evidence
    if not isinstance(package, RetainedNativePackageEvidence):
        raise ReleaseContractError(
            "release-e2e-retained-candidate-root-mismatch",
            "detached E2E requires typed retained package evidence",
        )
    view = package.view
    run_id = getattr(view, "candidate_run_id", None)
    package_sha256 = getattr(view, "actual_package_manifest_sha256", None)
    sidecar_sha256 = package.receipt_sha256
    if (
        not isinstance(run_id, str) or not run_id or Path(run_id).name != run_id or run_id in {".", ".."}
        or not isinstance(package_sha256, str) or _SHA256.fullmatch(package_sha256) is None
        or not isinstance(sidecar_sha256, str) or _SHA256.fullmatch(sidecar_sha256) is None
    ):
        raise ReleaseContractError(
            "release-e2e-retained-candidate-root-mismatch",
            "retained candidate package identity is not safe for the artifact root",
        )
    candidate_root = root / ".caprmedio_tmp" / "release_candidates" / run_id
    expected_descriptor = candidate_root / "candidate-snapshot.json"
    expected_sidecar = candidate_root / "package_evidence" / f"{sidecar_sha256}.json"
    expected_package = candidate_root / "package" / package_sha256
    raw_paths = (
        retained_candidate.descriptor_path,
        package.receipt_path,
        view.package_root,
    )
    if any(
        not isinstance(path, Path) or not path.is_absolute() or any(part == ".." for part in path.parts)
        for path in raw_paths
    ):
        raise ReleaseContractError(
            "release-e2e-retained-candidate-root-mismatch",
            "retained candidate has an unsafe path before detached reopening",
        )
    if (
        retained_candidate.descriptor_path != expected_descriptor
        or package.receipt_path != expected_sidecar
        or view.package_root != expected_package
    ):
        raise ReleaseContractError(
            "release-e2e-retained-candidate-root-mismatch",
            "retained candidate descriptor or package is outside the explicit artifact root",
        )
    retained = reopen_retained_candidate_identity(retained_candidate)
    if retained != retained_candidate:
        raise ReleaseContractError(
            "release-e2e-retained-candidate-root-mismatch",
            "reopened retained candidate differs from its transport identity",
        )
    return retained


def _validate_detached_native_predecessors(root: Path, retained: RetainedCandidateIdentity,
                                           suite: object, image_build: object,
                                           verification: object,
                                           evidence: object) -> None:
    """Bind native E2E predecessors to the reopened retained package sidecar."""

    from release_image import PortableImageBuildEvidence, PortableImageVerificationEvidence

    if not isinstance(suite, PortableSuiteGateEvidence):
        raise ReleaseContractError("release-e2e-native-predecessor-untrusted", "detached E2E requires typed portable Unit evidence")
    if not isinstance(image_build, PortableImageBuildEvidence):
        raise ReleaseContractError("release-e2e-native-predecessor-untrusted", "detached E2E requires typed portable image-build evidence")
    if not isinstance(verification, PortableImageVerificationEvidence):
        raise ReleaseContractError("release-e2e-native-predecessor-untrusted", "detached E2E requires typed portable image verification evidence")
    if not isinstance(evidence, PortableCandidateE2EGateEvidence):
        raise ReleaseContractError("release-e2e-native-predecessor-untrusted", "detached E2E requires typed portable E2E evidence")
    if not suite.passed or not isinstance(suite.receipt_sha256, str) or _SHA256.fullmatch(suite.receipt_sha256) is None:
        raise ReleaseContractError("release-e2e-native-predecessor-untrusted", "detached E2E requires passed portable Unit evidence")
    try:
        sidecar_relpath = retained.package_evidence.receipt_path.relative_to(root).as_posix()
    except ValueError as error:  # guarded above; keep the public refusal stable
        raise ReleaseContractError("release-e2e-retained-candidate-root-mismatch", "retained package sidecar is outside the artifact root") from error
    view = retained.package_evidence.view
    shared = {
        "candidate_snapshot_manifest_sha256": retained.candidate_snapshot_manifest_sha256,
        "source_catalog_sha256": view.source_catalog_sha256,
        "candidate_run_id": view.candidate_run_id,
        "input_manifest_sha256": view.input_manifest_sha256,
        "framework_version": retained.framework_version,
        "version_toml_sha256": retained.version_toml_sha256,
    }
    expected = (
        ("portable Unit", suite, {**shared, "input_schema": "portable-1", "phase_map_sha256": view.phase_map.sha256}),
        ("portable image build", image_build, {
            **shared,
            "package_schema": "portable-1",
            "package_manifest_sha256": view.actual_package_manifest_sha256,
            "package_evidence_sha256": retained.package_evidence.receipt_sha256,
            "package_evidence_relpath": sidecar_relpath,
        }),
        ("portable image verification", verification, {
            **shared,
            "package_schema": "portable-1",
            "package_manifest_sha256": view.actual_package_manifest_sha256,
            "package_evidence_sha256": retained.package_evidence.receipt_sha256,
            "package_evidence_relpath": sidecar_relpath,
        }),
        ("portable candidate E2E", evidence, {
            **shared,
            "package_schema": "portable-1",
            "package_manifest_sha256": view.actual_package_manifest_sha256,
            "package_evidence_sha256": retained.package_evidence.receipt_sha256,
            "package_evidence_relpath": sidecar_relpath,
        }),
    )
    for label, receipt, fields in expected:
        if any(getattr(receipt, field, None) != value for field, value in fields.items()):
            raise ReleaseContractError(
                "release-e2e-native-predecessor-mismatch",
                f"{label} does not bind the reopened retained package",
            )
    if (
        verification.build_receipt_sha256 != image_build.receipt_sha256
        or verification.candidate_image_digest != image_build.candidate_image_digest
        or evidence.candidate_image_digest != verification.candidate_image_digest
    ):
        raise ReleaseContractError("release-e2e-native-predecessor-mismatch", "native predecessors do not share one immutable image")


def read_detached_candidate_e2e_execution_artifacts(
    artifact_root: Path,
    retained_candidate: RetainedCandidateIdentity,
    suite: PortableSuiteGateEvidence,
    verification: PortableImageVerificationEvidence,
    e2e: PortableCandidateE2EGateEvidence,
    *,
    image_build: PortableImageBuildEvidence,
) -> Path:
    """Reopen one retained native E2E packet without a live candidate or checkout.

    ``artifact_root`` is deliberately authoritative for every reopened packet
    reference.  A retained descriptor is only an immutable identity carrier;
    it is never expanded into a live candidate, compilation, admission, or
    second gate execution.
    """

    root = _detached_artifact_root(artifact_root)
    retained = _reopen_detached_candidate_at_root(root, retained_candidate)
    _validate_detached_native_predecessors(root, retained, suite, image_build, verification, e2e)

    # The Image reader owns the Docker proof.  It consumes the same retained
    # descriptor/package and performs no current source or selector rebind.
    from release_image import read_detached_image_execution_artifacts

    image_attempt = read_detached_image_execution_artifacts(
        root, retained, suite, image_build, verification,
    )
    if image_attempt != _safe_path(root, verification.evidence_root):
        raise ReleaseContractError("release-e2e-predecessor-root-mismatch", "image artifacts reopened outside the retained artifact root")

    grammar, _grammar_bytes = _reopen_retained_grammar(root, e2e)
    phase_map = retained.package_evidence.view.phase_map
    grammar_paths = tuple(sorted(row["source_path"] for row in grammar["harnesses"]))
    if grammar_paths != phase_map.candidate_e2e_paths:
        raise ReleaseContractError("release-e2e-phase-map-mismatch", "retained E2E grammar differs from the retained package phase map")
    _validate_e2e_evidence_envelope(
        retained.candidate_snapshot_manifest_sha256, verification, e2e,
        package=retained.package_evidence.view,
    )
    captured_context = _reopen_relocated_e2e_context(
        root, e2e, retained.candidate_snapshot_manifest_sha256, verification,
        e2e.grammar_sha256, phase_map.sha256, grammar,
    )
    capability = _read_e2e_artifact_packet(
        root, retained.candidate_snapshot_manifest_sha256, verification, e2e,
        package=retained.package_evidence.view, grammar=grammar,
        grammar_sha256=e2e.grammar_sha256, phase_map=phase_map, retained=True,
        captured_context=captured_context,
    )
    _verify_retained_host_capability_for_release(
        root, retained.descriptor.executing_release, suite, capability,
        captured_source_root=captured_context.source_root,
    )
    return root


def _read_candidate_e2e_artifacts(root: Path, candidate: ValidatedCandidate,
                                  compilation: SealedCandidateCompilation | SealedPortableCandidateCompilation,
                                  image: ImageVerificationEvidence,
                                  evidence: CandidateE2EGateEvidence,
                                  *, package: PackageEvidenceView | None = None,
                                  retained: bool = False) -> FrozenHostE2ECapability:
    """Validate E2E proof as fresh admission or as retained original evidence."""

    _validate_e2e_evidence_envelope(candidate.manifest.sha256, image, evidence, package=package)
    if retained:
        grammar, grammar_bytes = _reopen_retained_grammar(root, evidence)
        grammar_sha256 = evidence.grammar_sha256
    else:
        grammar, grammar_bytes, grammar_sha256, _ignored = _load_grammar(root)
    phase_map = _bound_phase_map(candidate, grammar, package)
    capability = _read_e2e_artifact_packet(
        root, candidate.manifest.sha256, image, evidence, package=package,
        grammar=grammar, grammar_sha256=grammar_sha256, phase_map=phase_map,
        retained=retained, candidate=candidate,
    )
    if not retained:
        _source_control_fingerprint(root, candidate, compilation, grammar_bytes)
    return capability


def _validate_e2e_evidence_envelope(candidate_snapshot_manifest_sha256: str,
                                    image: ImageVerificationEvidence,
                                    evidence: CandidateE2EGateEvidence,
                                    *, package: PackageEvidenceView | None) -> None:
    """Validate the typed receipt envelope before reopening its packet bytes."""

    if not isinstance(evidence, CandidateE2EGateEvidence) or not evidence.passed:
        raise ReleaseContractError("release-e2e-evidence-untrusted", "later admission requires passed actual host E2E evidence")
    if (evidence.candidate_snapshot_manifest_sha256 != candidate_snapshot_manifest_sha256
            or evidence.candidate_image_digest != image.candidate_image_digest
            or evidence.execution_kind != "host-subprocess"
            or not isinstance(evidence.receipt_sha256, str) or _SHA256.fullmatch(evidence.receipt_sha256) is None):
        raise ReleaseContractError("release-e2e-evidence-mismatch", "candidate E2E evidence belongs to another candidate or image")
    if package is None:
        if type(evidence) is not CandidateE2EGateEvidence:
            raise ReleaseContractError("release-e2e-evidence-mismatch", "schema-2 candidate E2E evidence has an unsupported receipt schema")
    else:
        if not isinstance(evidence, PortableCandidateE2EGateEvidence):
            raise ReleaseContractError("release-e2e-evidence-mismatch", "portable candidate E2E evidence lacks its package bindings")
        portable_values = {
            "package_schema": package.package_schema,
            "package_manifest_sha256": package.actual_package_manifest_sha256,
            "package_evidence_sha256": getattr(image, "package_evidence_sha256", None),
            "package_evidence_relpath": getattr(image, "package_evidence_relpath", None),
            "source_catalog_sha256": package.source_catalog_sha256,
            "candidate_run_id": package.candidate_run_id,
            "input_manifest_sha256": package.input_manifest_sha256,
            "framework_version": package.framework_version,
            "version_toml_sha256": package.version_toml_sha256,
        }
        if any(getattr(evidence, field, None) != value for field, value in portable_values.items()):
            raise ReleaseContractError("release-e2e-evidence-mismatch", "portable candidate E2E receipt binds another package")


def _read_e2e_artifact_packet(root: Path, candidate_snapshot_manifest_sha256: str,
                              image: ImageVerificationEvidence,
                              evidence: CandidateE2EGateEvidence,
                              *, package: PackageEvidenceView | None,
                              grammar: dict[str, Any], grammar_sha256: str,
                              phase_map, retained: bool,
                              candidate: ValidatedCandidate | None = None,
                              captured_context: _CapturedE2EContext | None = None) -> FrozenHostE2ECapability:
    """Reopen an already typed E2E packet from sealed receipt identities only."""

    phase_map_sha256 = phase_map.sha256
    prefix = f"{EVIDENCE_ROOT}/{candidate_snapshot_manifest_sha256}/"
    if (evidence.grammar_sha256 != grammar_sha256 or evidence.phase_map_sha256 != phase_map_sha256
            or not evidence.evidence_root.startswith(prefix)
            or not evidence.evidence_root.removeprefix(prefix).startswith("attempt-")
            or "/" in evidence.evidence_root.removeprefix(prefix)):
        raise ReleaseContractError("release-e2e-evidence-mismatch", "candidate E2E evidence is outside its exact bound attempt")
    attempt = _safe_path(root, evidence.evidence_root)
    receipt = _regular(root, f"{evidence.evidence_root}/receipt.json", label="candidate E2E receipt").read_bytes()
    if (_digest(receipt) != evidence.receipt_sha256
            or receipt != canonical_json(asdict(replace(evidence, receipt_sha256=None)))):
        raise ReleaseContractError("release-e2e-evidence-untrusted", "candidate E2E receipt changed or is caller-forged")
    if retained:
        limits = _reopen_retained_release_e2e_settings(root, evidence)
    else:
        if candidate is None:  # pragma: no cover - live wrapper always supplies its typed candidate
            raise ReleaseContractError("release-e2e-handoff-untrusted", "live E2E settings require a typed candidate")
        limits = _reopen_release_e2e_settings(root, candidate, evidence)
    capability = _reopen_host_capability(root, evidence)
    if captured_context is None:
        context_path = f"{evidence.evidence_root}/scratch/context.json"
        context = _read_bounded_artifact(root, context_path, limit=_MAX_CONTEXT_BYTES, label="candidate E2E context")
        expected_context, _harnesses = _context_bytes_for_binding(
            root, attempt / "scratch", attempt / "scratch/reports",
            candidate_snapshot_manifest_sha256, image.candidate_image_digest,
            grammar_sha256, phase_map_sha256, grammar,
        )
        if context != expected_context:
            raise ReleaseContractError("release-e2e-evidence-untrusted", "candidate E2E context differs from its exact bound attempt")
        recorded_reports = attempt / "scratch" / "reports"
    else:
        recorded_reports = captured_context.reports_root
    expected_sources = tuple(row["source_path"] for row in grammar["harnesses"])
    source_sha256s = {
        source_path: source_sha256
        for source_path, source_sha256, phase in phase_map.rows
        if phase == "candidate_e2e"
    }
    if len(evidence.harness_receipts) != 3 or tuple(item.source_path for item in evidence.harness_receipts) != expected_sources:
        raise ReleaseContractError("release-e2e-evidence-untrusted", "candidate E2E receipt lacks the exact three harnesses")
    inspect = _read_bounded_artifact(
        root, f"{evidence.evidence_root}/inspect.stdout.bin", limit=limits.max_stdout_bytes,
        label="candidate E2E inspect stdout",
    )
    _read_bounded_artifact(
        root, f"{evidence.evidence_root}/inspect.stderr.bin", limit=limits.max_stderr_bytes,
        label="candidate E2E inspect stderr",
    )
    if inspect.decode("utf-8", "replace").strip() != image.candidate_image_digest:
        raise ReleaseContractError("release-e2e-evidence-untrusted", "candidate E2E inspection does not prove the immutable image")
    for index, (receipt_row, grammar_row) in enumerate(zip(evidence.harness_receipts, grammar["harnesses"], strict=True)):
        pattern = Path(grammar_row["source_path"]).name
        expected_stdout_path = f"{evidence.evidence_root}/harness-{index}.stdout.bin"
        expected_stderr_path = f"{evidence.evidence_root}/harness-{index}.stderr.bin"
        expected_junit_path = f"{evidence.evidence_root}/harness-{index}.junit.xml"
        expected_argv = (
            capability.python.path, capability.n_host_controller.path,
            *grammar_row["argv"][2:7],
            str(recorded_reports / f"{pattern}.xml"),
        )
        if (receipt_row.source_sha256 != source_sha256s.get(receipt_row.source_path)
                or receipt_row.argv != expected_argv
                or receipt_row.stdout_path != expected_stdout_path or receipt_row.stderr_path != expected_stderr_path
                or receipt_row.junit_path != expected_junit_path):
            raise ReleaseContractError("release-e2e-evidence-untrusted", "candidate E2E harness receipt has unbound phase carriers")
        started_at = _parse_utc_timestamp(receipt_row.started_at)
        finished_at = _parse_utc_timestamp(receipt_row.finished_at)
        stdout = _read_bounded_artifact(
            root, receipt_row.stdout_path, limit=limits.max_stdout_bytes,
            label="candidate E2E stdout",
        )
        stderr = _read_bounded_artifact(
            root, receipt_row.stderr_path, limit=limits.max_stderr_bytes,
            label="candidate E2E stderr",
        )
        tests, junit_sha, junit_reason, _junit_payload = _observe_junit(
            _regular(root, receipt_row.junit_path, label="candidate E2E JUnit"),
            limits.max_junit_bytes,
        )
        if (started_at > finished_at
                or type(receipt_row.elapsed_seconds) not in {int, float}
                or not math.isfinite(float(receipt_row.elapsed_seconds)) or receipt_row.elapsed_seconds < 0
                or type(receipt_row.exit_code) is not int or receipt_row.exit_code != 0
                or receipt_row.timed_out is not False
                or receipt_row.stdout_sha256 != _digest(stdout) or receipt_row.stderr_sha256 != _digest(stderr)
                or receipt_row.junit_sha256 != junit_sha or type(receipt_row.executed_tests) is not int
                or receipt_row.executed_tests != tests or junit_reason
                or not isinstance(receipt_row.reason, str) or receipt_row.reason):
            raise ReleaseContractError("release-e2e-evidence-untrusted", "candidate E2E harness receipt is missing or changed")
    return capability


def run_candidate_e2e_gate(
    candidate: ValidatedCandidate,
    compilation: SealedCandidateCompilation | SealedPortableCandidateCompilation,
    unit_suite: SuiteGateEvidence,
    image: ImageVerificationEvidence,
    *,
    image_build: ImageBuildEvidence,
    executor,
    prepared_package: PreparedPortableReleasePackage | None = None,
) -> CandidateE2EGateEvidence:
    """Execute the immutable image inspection plus all three exact host harnesses once."""

    root, package = _reopen_predecessors(
        candidate, compilation, unit_suite, image_build, image, prepared_package=prepared_package,
    )
    execution_kind = _executor_kind(executor)
    grammar, grammar_bytes, grammar_sha256, _ignored_phase_map = _load_grammar(root)
    phase_map = _bound_phase_map(candidate, grammar, package)
    phase_map_sha256 = phase_map.sha256
    source_sha256s = {
        source_path: source_sha256
        for source_path, source_sha256, phase in phase_map.rows
        if phase == "candidate_e2e"
    }
    before = _source_control_fingerprint(root, candidate, compilation, grammar_bytes)
    frozen_limits = _release_e2e_settings(root, candidate)
    limits = frozen_limits.limits
    host_capability = HostE2EExecutor.freeze_capability(root, candidate) if execution_kind == "host-subprocess" else None
    if host_capability is not None:
        executor._bind_frozen_limits(limits)
    parent = _safe_path(root, f"{EVIDENCE_ROOT}/{candidate.manifest.sha256}", create=True)
    attempt = Path(tempfile.mkdtemp(prefix="attempt-", dir=parent))
    evidence_root = attempt.relative_to(root).as_posix()
    scratch = attempt / "scratch"
    reports = scratch / "reports"
    scratch.mkdir()
    reports.mkdir()
    receipts: list[HarnessReceipt] = []
    settings_snapshot_path = (attempt / _SETTINGS_SNAPSHOT_FILENAME).relative_to(root).as_posix()
    settings_snapshot_sha256 = frozen_limits.sha256
    host_capability_path: str | None = None
    host_capability_sha256: str | None = None
    outcome: Literal["passed", "failed", "timed_out", "incomplete", "stale", "recording_uncertain"] = "incomplete"
    reason = "candidate E2E evidence is incomplete"
    try:
        _write_new(attempt / _SETTINGS_SNAPSHOT_FILENAME, frozen_limits.snapshot)
        _write_new(attempt / _RETAINED_GRAMMAR_FILENAME, grammar_bytes)
        _write_new(attempt / _RETAINED_DEFAULT_SETTINGS_FILENAME, frozen_limits.default_settings)
        _write_new(attempt / _RETAINED_INSTANCE_SETTINGS_FILENAME, frozen_limits.instance_settings)
        context_bytes, harnesses = _context_bytes(root, scratch, reports, candidate, image, grammar_sha256, phase_map_sha256, grammar)
        context_path = scratch / "context.json"
        _write_new(context_path, context_bytes)
        trusted_path = host_capability.closed_path if host_capability is not None else os.defpath
        environment = {
            "PATH": trusted_path,
            "TMPDIR": str(scratch),
            CONTEXT_ENVIRONMENT_VARIABLE: str(context_path),
            CANDIDATE_IMAGE_ENVIRONMENT_VARIABLE: image.candidate_image_digest,
        }
        if host_capability is not None:
            capability_bytes = _host_identities_bytes(host_capability)
            capability_file = attempt / "host-identities.json"
            _write_new(capability_file, capability_bytes)
            host_capability_path = capability_file.relative_to(root).as_posix()
            host_capability_sha256 = _digest(capability_bytes)
        inspect_argv = ("docker", "image", "inspect",
                        "--format", "{{.Id}}", image.candidate_image_digest)
        inspect = _cap_test_double_result(_execution_result(executor.run(
            inspect_argv, cwd=root, environment=environment,
            timeout_seconds=limits.inspect_timeout_seconds,
        )), limits)
        _write_new(attempt / "inspect.stdout.bin", inspect.stdout)
        _write_new(attempt / "inspect.stderr.bin", inspect.stderr)
        if inspect.cleanup_uncertain:
            outcome, reason = "incomplete", "immutable candidate-image inspection process cleanup is uncertain"
        elif inspect.timed_out:
            outcome, reason = "timed_out", "immutable candidate-image inspection timed out"
        elif inspect.output_limited:
            outcome, reason = "incomplete", "immutable candidate-image inspection exceeded a frozen output limit"
        elif inspect.exit_code != 0:
            outcome, reason = "failed", "immutable candidate-image inspection failed"
        elif inspect.stdout.decode("utf-8", "replace").strip() != image.candidate_image_digest:
            outcome, reason = "failed", "immutable candidate-image inspection returned a different image ID"
        else:
            outcome, reason = "passed", "all fixed host E2E harnesses passed"
            for row, harness in zip(grammar["harnesses"], harnesses, strict=True):
                argv = tuple(
                    (host_capability.python.path if host_capability is not None else sys.executable) if token == "{trusted_python}"
                    else (host_capability.n_host_controller.path if host_capability is not None else DRIVER_RELATIVE) if token == DRIVER_RELATIVE
                    else harness["junit_path"] if token == "{e2e_junit_path}" else token
                    for token in row["argv"]
                )
                started_at = _utc_timestamp()
                phase_started = time.monotonic()
                result = _cap_test_double_result(_execution_result(executor.run(
                    argv, cwd=root, environment=environment,
                    timeout_seconds=limits.harness_timeout_seconds,
                )), limits)
                elapsed = time.monotonic() - phase_started
                finished_at = _utc_timestamp()
                stdout, stderr = result.stdout, result.stderr
                ordinal = len(receipts)
                stdout_path = f"{evidence_root}/harness-{ordinal}.stdout.bin"
                stderr_path = f"{evidence_root}/harness-{ordinal}.stderr.bin"
                junit_path = f"{evidence_root}/harness-{ordinal}.junit.xml"
                _write_new(attempt / f"harness-{ordinal}.stdout.bin", stdout)
                _write_new(attempt / f"harness-{ordinal}.stderr.bin", stderr)
                tests, junit_sha, junit_reason, junit_payload = _observe_junit(
                    Path(harness["junit_path"]), limits.max_junit_bytes,
                )
                if junit_sha is not None and junit_payload is not None:
                    _write_new(attempt / f"harness-{ordinal}.junit.xml", junit_payload)
                phase_reason = ""
                if result.cleanup_uncertain:
                    outcome, reason, phase_reason = "incomplete", f"E2E harness cleanup is uncertain: {harness['pattern']}", "process cleanup is uncertain"
                elif result.timed_out:
                    outcome, reason, phase_reason = "timed_out", f"E2E harness timed out: {harness['pattern']}", "harness timed out"
                elif result.output_limited:
                    outcome, reason, phase_reason = "incomplete", f"E2E harness exceeded a frozen output limit: {harness['pattern']}", "harness output exceeded a frozen limit"
                elif result.exit_code != 0:
                    outcome, reason, phase_reason = "failed", f"E2E harness failed: {harness['pattern']}", "harness exited nonzero"
                elif junit_reason:
                    outcome, reason, phase_reason = "incomplete", f"E2E harness JUnit is incomplete: {harness['pattern']}", junit_reason
                receipts.append(HarnessReceipt(
                    harness["source_path"], source_sha256s[harness["source_path"]], argv,
                    started_at, finished_at, result.exit_code, result.timed_out,
                    stdout_path, _digest(stdout), stderr_path, _digest(stderr), junit_path,
                    junit_sha, tests, elapsed, phase_reason,
                ))
                if outcome != "passed":
                    break
        _reopen_predecessors(
            candidate, compilation, unit_suite, image_build, image, prepared_package=prepared_package,
        )
        if _source_control_fingerprint(root, candidate, compilation, grammar_bytes) != before:
            raise ReleaseContractError("release-currentness-stale", "candidate source control changed during host E2E execution")
        if _release_e2e_settings(root, candidate) != frozen_limits:
            raise ReleaseContractError("release-currentness-stale", "frozen release E2E Framework settings changed during execution")
        if host_capability is not None:
            HostE2EExecutor.revalidate_capability(root, candidate, host_capability)
        if outcome == "passed" and (execution_kind != "host-subprocess" or image.execution_kind != "docker-subprocess"):
            outcome, reason = "incomplete", "test-double execution cannot prove actual promotion evidence"
    except ReleaseContractError as error:
        if error.code in {"release-currentness-stale", "release-e2e-binding-mismatch"}:
            outcome, reason = "stale", f"stale: {error}"
        else:
            outcome, reason = "incomplete", str(error)
    except (OSError, TypeError, ValueError) as error:
        outcome, reason = "recording_uncertain", f"candidate E2E evidence could not be recorded: {type(error).__name__}"
    evidence_kwargs = {
        "candidate_snapshot_manifest_sha256": candidate.manifest.sha256,
        "candidate_image_digest": image.candidate_image_digest,
        "phase_map_sha256": phase_map_sha256,
        "grammar_sha256": grammar_sha256,
        "outcome": outcome,
        "reason": reason,
        "harness_receipts": tuple(receipts),
        "evidence_root": evidence_root,
        "receipt_sha256": None,
        "settings_snapshot_path": settings_snapshot_path,
        "settings_snapshot_sha256": settings_snapshot_sha256,
        "host_capability_path": host_capability_path,
        "host_capability_sha256": host_capability_sha256,
        "execution_kind": execution_kind,
    }
    if package is None:
        evidence: CandidateE2EGateEvidence = CandidateE2EGateEvidence(**evidence_kwargs)
    else:
        package_evidence_sha256, package_evidence_relpath = _portable_sidecar_binding(image_build, image)
        evidence = PortableCandidateE2EGateEvidence(
            **evidence_kwargs,
            package_schema="portable-1",
            package_manifest_sha256=package.actual_package_manifest_sha256,
            package_evidence_sha256=package_evidence_sha256,
            package_evidence_relpath=package_evidence_relpath,
            source_catalog_sha256=package.source_catalog_sha256,
            candidate_run_id=package.candidate_run_id,
            input_manifest_sha256=package.input_manifest_sha256,
            framework_version=package.framework_version,
            version_toml_sha256=package.version_toml_sha256,
        )
    try:
        receipt = canonical_json(asdict(evidence))
        _write_new(_receipt_path(root, evidence_root), receipt)
        directory_fd = os.open(attempt, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
        return replace(evidence, receipt_sha256=_digest(receipt))
    except OSError:
        return replace(evidence, outcome="recording_uncertain", reason="candidate E2E receipt could not be durably recorded")


__all__ = [
    "CandidateE2EGateEvidence",
    "DEFAULT_RELEASE_E2E_LIMITS",
    "E2EExecutionResult",
    "ExecutableIdentity",
    "FrozenHostE2ECapability",
    "HarnessReceipt",
    "HostE2EExecutor",
    "PortableCandidateE2EGateEvidence",
    "ReleaseE2ELimits",
    "read_candidate_e2e_execution_artifacts",
    "read_detached_candidate_e2e_execution_artifacts",
    "run_candidate_e2e_gate",
    "verify_bound_candidate_e2e_evidence",
]
