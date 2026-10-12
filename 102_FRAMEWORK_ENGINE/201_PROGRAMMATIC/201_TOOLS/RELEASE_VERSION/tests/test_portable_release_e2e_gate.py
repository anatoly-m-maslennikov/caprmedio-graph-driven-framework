"""Portable E2E package-binding tests using physical synthetic candidates only.

These tests deliberately stop before any Docker or host-process invocation.
They prove that E2E refuses missing or mismatched native receipts before its
fixed-three-harness execution boundary is entered.
"""
from __future__ import annotations

from dataclasses import asdict, replace
import hashlib
import json
from types import SimpleNamespace
import sys
import tempfile
import unittest
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for _path in (RELEASE_ROOT, TEST_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

import release_e2e_gate as gate  # noqa: E402
import release_image as image_module  # noqa: E402
from portable_package_fixture import PortablePackageFixture  # noqa: E402
from release_contract import ReleaseContractError, canonical_json  # noqa: E402
from release_handoff import PackageRow  # noqa: E402
from release_image import PortableImageBuildEvidence, PortableImageVerificationEvidence  # noqa: E402
from release_packaging import RUNTIME_ROOT, _render_manifest  # noqa: E402
from release_portable_package import prepare_portable_release_package  # noqa: E402
from release_retained_package import retain_native_package_evidence  # noqa: E402
from release_test_phases import CANDIDATE_E2E_MODULES  # noqa: E402


_UNIT_MODULE = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_portable_e2e_unit.py"


def _test_module(name: str) -> bytes:
    return f"def test_{name.replace('/', '_').replace('.', '_')}():\n    assert True\n".encode("utf-8")


class _NoEffectExecutor:
    """A sentinel: native binding failures must precede all executor calls."""

    execution_kind = "test-double"

    def __init__(self) -> None:
        self.calls = 0

    def run(self, *_args, **_kwargs):
        self.calls += 1
        raise AssertionError("portable E2E binding failure must not invoke an executor")


def _native_predecessors(view, *, mutate: dict[str, object] | None = None):
    evidence_sha256 = "d" * 64
    evidence_relpath = (
        f".caprmedio_tmp/release_candidates/{view.candidate_run_id}/"
        f"package_evidence/{evidence_sha256}.json"
    )
    common = {
        "source_catalog_sha256": view.source_catalog_sha256,
        "candidate_run_id": view.candidate_run_id,
        "input_manifest_sha256": view.input_manifest_sha256,
        "framework_version": view.framework_version,
        "version_toml_sha256": view.version_toml_sha256,
        "phase_map_sha256": view.phase_map.sha256,
    }
    unit = SimpleNamespace(**common, input_schema="portable-1")
    build = SimpleNamespace(
        **common,
        package_schema="portable-1",
        package_manifest_sha256=view.actual_package_manifest_sha256,
        package_evidence_sha256=evidence_sha256,
        package_evidence_relpath=evidence_relpath,
    )
    image = SimpleNamespace(
        **common,
        package_schema="portable-1",
        package_manifest_sha256=view.actual_package_manifest_sha256,
        package_evidence_sha256=evidence_sha256,
        package_evidence_relpath=evidence_relpath,
        candidate_image_digest="sha256:" + "c" * 64,
        evidence_root="synthetic-image-receipt",
    )
    for target in (unit, build, image):
        for field, value in (mutate or {}).items():
            setattr(target, field, value)
    return unit, build, image


def _retained_image_receipts(fixture, prepared):
    """Make native receipt-shaped inputs around a real immutable sidecar."""

    retained = retain_native_package_evidence(fixture.candidate, fixture.sealed, prepared)
    sidecar_relpath = retained.receipt_path.relative_to(fixture.root).as_posix()
    common = {
        "package_schema": "portable-1",
        "package_manifest_sha256": retained.view.actual_package_manifest_sha256,
        "source_catalog_sha256": retained.view.source_catalog_sha256,
        "candidate_run_id": retained.view.candidate_run_id,
        "input_manifest_sha256": retained.view.input_manifest_sha256,
        "framework_version": retained.view.framework_version,
        "version_toml_sha256": retained.view.version_toml_sha256,
        "package_evidence_sha256": retained.receipt_sha256,
        "package_evidence_relpath": sidecar_relpath,
    }
    build = PortableImageBuildEvidence(
        candidate_snapshot_manifest_sha256=fixture.candidate.manifest.sha256,
        outcome="built",
        reason="synthetic retained receipt",
        candidate_image_digest="sha256:" + "c" * 64,
        context_root="synthetic-image-context",
        context_sha256="a" * 64,
        suite_receipt_sha256="b" * 64,
        evidence_root="synthetic-image-build",
        commands_sha256="c" * 64,
        execution_kind="docker-subprocess",
        receipt_sha256="d" * 64,
        **common,
    )
    image = PortableImageVerificationEvidence(
        candidate_snapshot_manifest_sha256=fixture.candidate.manifest.sha256,
        outcome="verified",
        reason="synthetic retained receipt",
        candidate_image_digest=build.candidate_image_digest,
        build_receipt_sha256=build.receipt_sha256,
        evidence_root="synthetic-image-verification",
        commands_sha256="e" * 64,
        execution_kind="docker-subprocess",
        receipt_sha256="f" * 64,
        **common,
    )
    return retained, build, image


def _write(path: Path, payload: bytes, mode: int = 0o644) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    path.chmod(mode)


def _native_image_receipts(fixture, prepared, suite):
    """Record complete native Image artifacts without invoking Docker."""

    retained = retain_native_package_evidence(fixture.candidate, fixture.sealed, prepared)
    view = retained.view
    image_id = "sha256:" + "a" * 64
    build_parent = fixture.root / ".caprmedio_runtime" / "release_image" / fixture.candidate.manifest.sha256 / "build"
    build_parent.mkdir(parents=True)
    build_attempt = Path(tempfile.mkdtemp(prefix="attempt-", dir=build_parent))
    context, package_sha = image_module._portable_context(fixture.root, fixture.candidate, view, build_attempt)
    context_sha = image_module._tree(context)
    build_argv = [
        "docker", "build", "--iidfile", str(build_attempt / "image.id"),
        "--label", f"{image_module.CANDIDATE_LABEL}={fixture.candidate.manifest.sha256}",
        "--label", f"{image_module.CONTEXT_LABEL}={context_sha}",
        "--file", str(context / "Dockerfile"), str(context),
    ]
    inspect_payload = canonical_json([{
        "Config": {"Labels": {
            image_module.CANDIDATE_LABEL: fixture.candidate.manifest.sha256,
            image_module.CONTEXT_LABEL: context_sha,
        }},
    }])
    build_records = [
        {"argv": build_argv, "exit_code": 0, "timed_out": False, "stdout_sha256": hashlib.sha256(b"").hexdigest(), "stderr_sha256": hashlib.sha256(b"").hexdigest()},
        {"argv": ["docker", "image", "inspect", image_id], "exit_code": 0, "timed_out": False,
         "stdout_sha256": hashlib.sha256(inspect_payload).hexdigest(), "stderr_sha256": hashlib.sha256(b"").hexdigest()},
    ]
    build_commands = canonical_json(build_records)
    _write(build_attempt / "commands.json", build_commands)
    _write(build_attempt / "command-0.stdout", b"")
    _write(build_attempt / "command-0.stderr", b"")
    _write(build_attempt / "command-1.stdout", inspect_payload)
    _write(build_attempt / "command-1.stderr", b"")
    common = {
        "package_schema": "portable-1",
        "package_manifest_sha256": package_sha,
        "source_catalog_sha256": view.source_catalog_sha256,
        "candidate_run_id": view.candidate_run_id,
        "input_manifest_sha256": view.input_manifest_sha256,
        "framework_version": view.framework_version,
        "version_toml_sha256": view.version_toml_sha256,
        "package_evidence_sha256": retained.receipt_sha256,
        "package_evidence_relpath": retained.receipt_path.relative_to(fixture.root).as_posix(),
    }
    build = PortableImageBuildEvidence(
        candidate_snapshot_manifest_sha256=fixture.candidate.manifest.sha256,
        outcome="built", reason="synthetic physical receipt", candidate_image_digest=image_id,
        context_root=context.relative_to(fixture.root).as_posix(), context_sha256=context_sha,
        suite_receipt_sha256=suite.receipt_sha256, evidence_root=build_attempt.relative_to(fixture.root).as_posix(),
        commands_sha256=hashlib.sha256(build_commands).hexdigest(), execution_kind="docker-subprocess",
        **common,
    )
    build = image_module._record(build_attempt, build)

    verify_parent = fixture.root / ".caprmedio_runtime" / "release_image" / fixture.candidate.manifest.sha256 / "verify"
    verify_parent.mkdir(parents=True)
    verify_attempt = Path(tempfile.mkdtemp(prefix="attempt-", dir=verify_parent))
    report = canonical_json({
        "schema": "caprmedio.release_version.portable_image_canary.v1",
        "candidate_snapshot_manifest_sha256": fixture.candidate.manifest.sha256,
        "package_schema": view.package_schema,
        "package_manifest_sha256": view.actual_package_manifest_sha256,
        "source_catalog_sha256": view.source_catalog_sha256,
        "candidate_run_id": view.candidate_run_id,
        "input_manifest_sha256": view.input_manifest_sha256,
        "framework_version": view.framework_version,
        "version_toml_sha256": view.version_toml_sha256,
        "verified_files": len(view.member_inventory),
        "mcp_tools": ["get_mcp_reload_status"],
    })
    expected_run = [
        "docker", "run", "--rm", "--network=none", "--read-only", "--cap-drop=ALL",
        "--security-opt=no-new-privileges", "--pids-limit=128", "--tmpfs", "/tmp:rw,nosuid,nodev,size=128m",
        "--entrypoint", "python", image_id, "/opt/caprmedio-release-canary.py",
    ]
    verify_records = [
        {"argv": ["docker", "image", "inspect", image_id], "exit_code": 0, "timed_out": False,
         "stdout_sha256": hashlib.sha256(inspect_payload).hexdigest(), "stderr_sha256": hashlib.sha256(b"").hexdigest()},
        {"argv": expected_run, "exit_code": 0, "timed_out": False,
         "stdout_sha256": hashlib.sha256(report).hexdigest(), "stderr_sha256": hashlib.sha256(b"").hexdigest()},
    ]
    verify_commands = canonical_json(verify_records)
    _write(verify_attempt / "commands.json", verify_commands)
    _write(verify_attempt / "command-0.stdout", inspect_payload)
    _write(verify_attempt / "command-0.stderr", b"")
    _write(verify_attempt / "command-1.stdout", report)
    _write(verify_attempt / "command-1.stderr", b"")
    image = PortableImageVerificationEvidence(
        candidate_snapshot_manifest_sha256=fixture.candidate.manifest.sha256,
        outcome="verified", reason="synthetic physical receipt", candidate_image_digest=image_id,
        build_receipt_sha256=build.receipt_sha256, evidence_root=verify_attempt.relative_to(fixture.root).as_posix(),
        commands_sha256=hashlib.sha256(verify_commands).hexdigest(), execution_kind="docker-subprocess",
        **common,
    )
    return retained, build, image_module._record(verify_attempt, image)


def _write_retained_n(fixture):
    """Create a real minimal schema-2 N package for host-receipt reopening."""

    release = fixture.candidate.authority.executing_release
    package = fixture.root / RUNTIME_ROOT / "releases" / release
    rows_spec = (
        ("FRAMEWORK_ENGINE", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/run_release_e2e.py", "FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/run_release_e2e.py", b"#!/bin/sh\nexit 0\n", 0o755),
        ("FRAMEWORK_ENGINE", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py", "FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py", b"app = 'N'\n", 0o644),
        ("FRAMEWORK_ENGINE", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py", "FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py", b"server = 'N'\n", 0o644),
        ("FRAMEWORK_ENGINE", "102_FRAMEWORK_ENGINE/202_AGENTIC/prompt.md", "FRAMEWORK_ENGINE/202_AGENTIC/prompt.md", b"# N\n", 0o644),
        ("METHODOLOGY", "METHODOLOGY/sources/source.md", "METHODOLOGY/sources/source.md", b"source\n", 0o644),
        ("METHODOLOGY", "METHODOLOGY/compiled/compiled.md", "METHODOLOGY/compiled/compiled.md", b"compiled\n", 0o644),
        ("SKILL", "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md", "SKILLS/ca/SKILL.md", b"# ca\n", 0o644),
        ("SKILL", "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/agents/openai.yaml", "SKILLS/ca/agents/openai.yaml", b"name: ca\n", 0o644),
    )
    rows = []
    for resource, source_path, destination, payload, mode in rows_spec:
        _write(package / destination, payload, mode)
        rows.append(PackageRow.model_validate({
            "resource": resource, "source_path": source_path, "destination_path": destination,
            "sha256": hashlib.sha256(payload).hexdigest(), "mode": mode,
        }))
    version = b'[framework]\nversion = "N"\n'
    _write(package / "version.toml", version)
    rows.append(PackageRow.model_validate({
        "resource": "PACKAGE_CONTROL", "source_path": "version.toml", "destination_path": "version.toml",
        "sha256": hashlib.sha256(version).hexdigest(), "mode": 0o644,
    }))
    manifest = _render_manifest(release, rows, framework_version="N", version_toml_sha256=hashlib.sha256(version).hexdigest())
    _write(package / "manifest.toml", manifest.encode())
    for _resource, _source_path, destination, payload, mode in rows_spec:
        if destination.startswith("SKILLS/ca/"):
            _write(fixture.root / ".agents" / "skills" / "ca" / destination.removeprefix("SKILLS/ca/"), payload, mode)
    return package


def _native_e2e_evidence(fixture, prepared, suite):
    """Assemble a complete physical native E2E packet without effects."""

    retained, build, image = _native_image_receipts(fixture, prepared, suite)
    _write_retained_n(fixture)
    grammar_raw = (RELEASE_ROOT / "release_e2e_bindings.json").read_bytes()
    fixture.write(gate.GRAMMAR_RELATIVE, grammar_raw)
    grammar = gate._parse_grammar(grammar_raw)
    phase_map = retained.view.phase_map
    phase_sha256 = phase_map.sha256
    parent = fixture.root / gate.EVIDENCE_ROOT / fixture.candidate.manifest.sha256
    parent.mkdir(parents=True)
    attempt = Path(tempfile.mkdtemp(prefix="attempt-", dir=parent))
    evidence_root = attempt.relative_to(fixture.root).as_posix()
    scratch, reports = attempt / "scratch", attempt / "scratch" / "reports"
    reports.mkdir(parents=True)
    default_settings = b"""[release_e2e]
inspect_timeout_seconds = 1.0
harness_timeout_seconds = 1.0
cleanup_timeout_seconds = 1.0
max_stdout_bytes = 1024
max_stderr_bytes = 1024
max_junit_bytes = 1024
"""
    instance_settings = b"[release_e2e]\n"
    frozen = gate._freeze_release_e2e_settings(default_settings, instance_settings,
        default_settings_relative=f"{fixture.candidate.manifest.canonical_source_snapshot_ref}/{gate.DEFAULT_FRAMEWORK_SETTINGS_SUFFIX}",
        instance_settings_relative=gate.FRAMEWORK_SETTINGS_RELATIVE)
    _write(attempt / "release-e2e-limits.json", frozen.snapshot)
    _write(attempt / "release-e2e-grammar.json", grammar_raw)
    _write(attempt / "release-e2e-default-settings.toml", default_settings)
    _write(attempt / "release-e2e-instance-settings.toml", instance_settings)
    active = gate._active_n_state(fixture.root, fixture.candidate)
    (
        suite.executing_selector_sha256,
        suite.executing_release_package_sha256,
        suite.executing_skill_sha256,
    ) = active
    controller = fixture.root / RUNTIME_ROOT / "releases" / fixture.candidate.authority.executing_release / gate._N_DRIVER_RELATIVE
    executable = Path(sys.executable).resolve()
    controller_digest = hashlib.sha256(controller.read_bytes()).hexdigest()
    executable_digest = hashlib.sha256(executable.read_bytes()).hexdigest()
    capability = gate.FrozenHostE2ECapability(
        *active,
        gate.ExecutableIdentity("n_host_controller", str(controller), controller_digest),
        gate.ExecutableIdentity("python", str(executable), executable_digest),
        gate.ExecutableIdentity("driver", str(controller), controller_digest),
        gate.ExecutableIdentity("docker", str(executable), executable_digest),
        str(executable.parent),
    )
    capability_payload = gate._host_identities_bytes(capability)
    _write(attempt / "host-identities.json", capability_payload)
    context, _ = gate._context_bytes(
        fixture.root, scratch, reports, fixture.candidate, image, hashlib.sha256(grammar_raw).hexdigest(), phase_sha256, grammar,
    )
    _write(scratch / "context.json", context)
    _write(attempt / "inspect.stdout.bin", (image.candidate_image_digest + "\n").encode())
    _write(attempt / "inspect.stderr.bin", b"")
    junit = b"<testsuite tests='1' failures='0' errors='0' skipped='0'><testcase name='ok'/></testsuite>"
    source_sha256s = {path: digest for path, digest, phase in phase_map.rows if phase == "candidate_e2e"}
    harnesses = []
    for index, row in enumerate(grammar["harnesses"]):
        pattern = Path(row["source_path"]).name
        stdout_path = f"{evidence_root}/harness-{index}.stdout.bin"
        stderr_path = f"{evidence_root}/harness-{index}.stderr.bin"
        junit_path = f"{evidence_root}/harness-{index}.junit.xml"
        stdout = f"harness {index}\n".encode()
        _write(attempt / f"harness-{index}.stdout.bin", stdout)
        _write(attempt / f"harness-{index}.stderr.bin", b"")
        _write(attempt / f"harness-{index}.junit.xml", junit)
        harnesses.append(gate.HarnessReceipt(
            row["source_path"], source_sha256s[row["source_path"]],
            (str(executable), str(controller), *row["argv"][2:7], str((reports / f"{pattern}.xml").resolve())),
            "2026-10-09T00:00:00.000000Z", "2026-10-09T00:00:01.000000Z", 0, False,
            stdout_path, hashlib.sha256(stdout).hexdigest(), stderr_path, hashlib.sha256(b"").hexdigest(),
            junit_path, hashlib.sha256(junit).hexdigest(), 1, 1.0, "",
        ))
    evidence = gate.PortableCandidateE2EGateEvidence(
        candidate_snapshot_manifest_sha256=fixture.candidate.manifest.sha256,
        candidate_image_digest=image.candidate_image_digest,
        phase_map_sha256=phase_sha256, grammar_sha256=hashlib.sha256(grammar_raw).hexdigest(),
        outcome="passed", reason="synthetic physical receipt", harness_receipts=tuple(harnesses), evidence_root=evidence_root,
        receipt_sha256=None, settings_snapshot_path=f"{evidence_root}/release-e2e-limits.json",
        settings_snapshot_sha256=frozen.sha256, host_capability_path=f"{evidence_root}/host-identities.json",
        host_capability_sha256=hashlib.sha256(capability_payload).hexdigest(), execution_kind="host-subprocess",
        package_schema="portable-1", package_manifest_sha256=retained.view.actual_package_manifest_sha256,
        package_evidence_sha256=retained.receipt_sha256,
        package_evidence_relpath=retained.receipt_path.relative_to(fixture.root).as_posix(),
        source_catalog_sha256=retained.view.source_catalog_sha256, candidate_run_id=retained.view.candidate_run_id,
        input_manifest_sha256=retained.view.input_manifest_sha256, framework_version=retained.view.framework_version,
        version_toml_sha256=retained.view.version_toml_sha256,
    )
    receipt = canonical_json(asdict(evidence))
    _write(attempt / "receipt.json", receipt)
    return suite, build, image, replace(evidence, receipt_sha256=hashlib.sha256(receipt).hexdigest())


class PortableReleaseE2EBindingTests(unittest.TestCase):
    def setUp(self) -> None:
        members = {path: _test_module(path) for path in (*CANDIDATE_E2E_MODULES, _UNIT_MODULE)}
        self.fixture = PortablePackageFixture(extra_engine_members=members)
        self.addCleanup(self.fixture.cleanup)
        self.prepared = prepare_portable_release_package(self.fixture.root, self.fixture.sealed)

    def test_reopens_the_exact_prepared_portable_package_before_e2e(self) -> None:
        view = gate._portable_package_view(
            self.fixture.candidate,
            self.fixture.sealed,
            *_native_predecessors(
                gate.bind_package_evidence(
                    self.fixture.candidate, self.fixture.sealed, prepared_package=self.prepared,
                ),
            ),
            prepared_package=self.prepared,
        )

        self.assertIsNotNone(view)
        assert view is not None
        self.assertEqual("portable-1", view.package_schema)
        self.assertEqual(self.prepared.package_manifest_sha256, view.actual_package_manifest_sha256)
        self.assertEqual(self.fixture.sealed.source_catalog_sha256, view.source_catalog_sha256)
        self.assertEqual(self.fixture.run_id, view.candidate_run_id)
        self.assertEqual(self.fixture.sealed.input_manifest_sha256, view.input_manifest_sha256)
        self.assertEqual(self.fixture.candidate.manifest.version_toml_sha256, view.version_toml_sha256)
        self.assertTrue(view.member_inventory)

    def test_missing_prepared_receipt_refuses_before_any_executor_call(self) -> None:
        executor = _NoEffectExecutor()
        with self.assertRaises(ReleaseContractError) as raised:
            gate.run_candidate_e2e_gate(
                self.fixture.candidate,
                self.fixture.sealed,
                object(),  # type: ignore[arg-type]
                object(),  # type: ignore[arg-type]
                image_build=object(),  # type: ignore[arg-type]
                executor=executor,
            )
        self.assertEqual("release-e2e-portable-package-required", raised.exception.code)
        self.assertEqual(0, executor.calls)

    def test_mismatched_native_predecessor_refuses_before_any_executor_call(self) -> None:
        view = gate.bind_package_evidence(
            self.fixture.candidate, self.fixture.sealed, prepared_package=self.prepared,
        )
        unit, build, image = _native_predecessors(view, mutate={"source_catalog_sha256": "0" * 64})
        executor = _NoEffectExecutor()

        with self.assertRaises(ReleaseContractError) as raised:
            gate.run_candidate_e2e_gate(
                self.fixture.candidate,
                self.fixture.sealed,
                unit,  # type: ignore[arg-type]
                image,  # type: ignore[arg-type]
                image_build=build,  # type: ignore[arg-type]
                executor=executor,
                prepared_package=self.prepared,
            )
        self.assertEqual("release-e2e-portable-predecessor-mismatch", raised.exception.code)
        self.assertEqual(0, executor.calls)

    def test_disagreeing_retained_package_sidecars_refuse_before_any_executor_call(self) -> None:
        view = gate.bind_package_evidence(
            self.fixture.candidate, self.fixture.sealed, prepared_package=self.prepared,
        )
        unit, build, image = _native_predecessors(view)
        image.package_evidence_sha256 = "e" * 64
        executor = _NoEffectExecutor()

        with self.assertRaises(ReleaseContractError) as raised:
            gate.run_candidate_e2e_gate(
                self.fixture.candidate,
                self.fixture.sealed,
                unit,  # type: ignore[arg-type]
                image,  # type: ignore[arg-type]
                image_build=build,  # type: ignore[arg-type]
                executor=executor,
                prepared_package=self.prepared,
            )
        self.assertEqual("release-e2e-portable-predecessor-mismatch", raised.exception.code)
        self.assertEqual(0, executor.calls)

    def test_retained_reader_reopens_image_context_without_live_package_rebind(self) -> None:
        retained, build, image = _retained_image_receipts(self.fixture, self.prepared)
        source = self.fixture.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"
        source.write_bytes(source.read_bytes() + b"checkout changed after image evidence\n")

        reopened = gate._read_retained_portable_image_package(self.fixture.root, build, image)

        self.assertEqual(retained.view.actual_package_manifest_sha256, reopened.actual_package_manifest_sha256)
        self.assertEqual(retained.view.member_inventory, reopened.member_inventory)
        self.assertEqual(retained.view.phase_map, reopened.phase_map)
        self.assertEqual(retained.view.package_root, reopened.package_root)

    def test_public_retained_reader_accepts_source_drift_from_its_original_packet(self) -> None:
        suite = SimpleNamespace(receipt_sha256="9" * 64)
        suite, build, image, evidence = _native_e2e_evidence(self.fixture, self.prepared, suite)
        source = self.fixture.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"
        source.write_bytes(source.read_bytes() + b"mutated only after all proof packets were retained\n")
        (self.fixture.root / gate.GRAMMAR_RELATIVE).write_bytes(b"{}\n")
        (self.fixture.root / self.fixture.candidate.manifest.canonical_source_snapshot_ref / gate.DEFAULT_FRAMEWORK_SETTINGS_SUFFIX).write_bytes(b"[release_e2e]\nchanged = true\n")
        (self.fixture.root / gate.FRAMEWORK_SETTINGS_RELATIVE).write_bytes(b"[release_e2e]\nchanged = true\n")

        reopened = gate.read_candidate_e2e_execution_artifacts(
            self.fixture.candidate,
            self.fixture.sealed,
            suite,  # type: ignore[arg-type]
            image,
            evidence,
            image_build=build,
        )

        self.assertEqual(self.fixture.root, reopened)
        with self.assertRaises(ReleaseContractError) as fresh:
            gate._source_control_fingerprint(
                self.fixture.root,
                self.fixture.candidate,
                self.fixture.sealed,
                (RELEASE_ROOT / "release_e2e_bindings.json").read_bytes(),
            )
        self.assertEqual("release-currentness-stale", fresh.exception.code)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
