"""Schema-1 Full Gate binding-boundary tests.

The fixtures are physical synthetic candidates and never execute Docker, a
host E2E process, promotion, or a real release gate.  In particular, these
tests are refusal coverage, not Full Gate proof.
"""

from __future__ import annotations

from contextlib import contextmanager
from dataclasses import replace
import hashlib
import json
import shutil
import sys
from types import SimpleNamespace
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from portable_package_fixture import PortablePackageFixture  # noqa: E402
from full_suite_golden.control_fixture import copy_control_closure  # noqa: E402
from release_compilation import build_preflight_validated_candidate  # noqa: E402
from release_contract import ReleaseContractError, canonical_json  # noqa: E402
from release_e2e_gate import (  # noqa: E402
    DEFAULT_RELEASE_E2E_LIMITS,
    DRIVER_RELATIVE as E2E_DRIVER_RELATIVE,
    E2EExecutionResult,
    ExecutableIdentity,
    FrozenHostE2ECapability,
    GRAMMAR_RELATIVE as E2E_GRAMMAR_RELATIVE,
    HostE2EExecutor,
    run_candidate_e2e_gate,
)
import release_full_gate as full_gate  # noqa: E402
from release_full_gate import (  # noqa: E402
    NativeFullGateEvidence,
    aggregate_bound_release_gates,
    verify_bound_full_gate_evidence,
)
from release_handoff import CANONICAL_SOURCE_RELATIVE, PackageRow  # noqa: E402
from release_image import (  # noqa: E402
    DockerCommandResult,
    DockerSubprocessExecutor,
    build_candidate_image,
    verify_candidate_image,
)
from release_packaging import RUNTIME_ROOT, _render_manifest  # noqa: E402
from release_portable_package import prepare_portable_release_package  # noqa: E402
from release_retained_package import retain_native_package_evidence  # noqa: E402
from release_retained_candidate import retain_retained_candidate_identity  # noqa: E402
from release_suite import (  # noqa: E402
    COMPILED_PROBE_TEST_MODULE,
    MODULE_RULES_RELATIVE,
    SOURCE_BINDINGS_RELATIVE,
    SOURCE_BINDINGS_SHA256_ENVIRONMENT_VARIABLE,
    SUITE_DRIVER_COMMAND,
    SUITE_DRIVER_RELATIVE,
    SuiteExecutionResult,
    _active_n_state,
    execute_bound_release_suite,
)
from release_test_phases import CANDIDATE_E2E_MODULES, derive_test_phase_map_from_rows  # noqa: E402
from release_source_admission import derive_release_execution_source_snapshot  # noqa: E402


_UNIT_MODULE = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_portable_full_gate_unit.py"
_MCP_PACKAGE_MEMBERS = (
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/http_server.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/implementation_server.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/entrypoint.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/project_mcp_backend.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/project_mcp_launcher.py",
    "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/project-mcp.compose.yaml",
)
PROJECT_ROOT = RELEASE_ROOT.parents[3]


def _test_member(path: str) -> bytes:
    return f"def test_{path.replace('/', '_').replace('.', '_')}():\n    assert True\n".encode()


@contextmanager
def _fixture_authority(pin: dict[str, object]):
    """Require the fixture's captured current authority without patching readers."""

    current_pin = derive_release_execution_source_snapshot(PROJECT_ROOT)[2]
    if pin != current_pin:
        raise AssertionError("portable fixture authority differs from current source")
    yield


def _fixture() -> PortablePackageFixture:
    return PortablePackageFixture(
        extra_engine_members={
            path: _test_member(path)
            for path in (*CANDIDATE_E2E_MODULES, _UNIT_MODULE)
        },
    )


class _MockNativeSuiteExecutor:
    """Fixture-only report producer; it never launches a process or container."""

    source_context_sha256 = "e" * 64

    def run(self, command, *, workspace, output_root, working_directory, environment, timeout_seconds):
        if tuple(command) != SUITE_DRIVER_COMMAND:
            raise AssertionError(f"unexpected mock Unit argv: {command}")
        bindings_bytes = (workspace / SOURCE_BINDINGS_RELATIVE).read_bytes()
        if hashlib.sha256(bindings_bytes).hexdigest() != environment[SOURCE_BINDINGS_SHA256_ENVIRONMENT_VARIABLE]:
            raise AssertionError("mock Unit received an unbound source envelope")
        bindings = json.loads(bindings_bytes)
        rows = {row["source_path"]: row for row in bindings["package_rows"]}
        phase_map = derive_test_phase_map_from_rows(rows.values())
        rules = json.loads((workspace / MODULE_RULES_RELATIVE).read_bytes())
        compiled_root = environment["CAPRMEDIO_RELEASE_COMPILED_CANDIDATE_ROOT"]
        compiled_probe = next(
            path for path, row in sorted(rows.items())
            if row["resource"] == "METHODOLOGY" and path.startswith(compiled_root + "/")
        )
        report = ET.Element(
            "testsuite",
            tests=str(len(phase_map.unit_paths)),
            failures="0",
            errors="0",
            skipped="0",
            **{
                "caprmedio.phase": "unit",
                "caprmedio.phase_map_sha256": phase_map.sha256,
                "caprmedio.control_context_digest": bindings["control_context_digest"],
            },
        )
        probe_rules = {item["test_module_source_path"]: item for item in rules["module_probes"]}
        for module in phase_map.unit_paths:
            rule = probe_rules[module]
            sources = [module, *rule["source_paths"]]
            if rule.get("compiled_candidate_probe"):
                sources.append(compiled_probe)
            name = f"MOCK DATA ONLY Unit {module}"
            case = ET.SubElement(report, "testcase", classname=module, name=name)
            properties = ET.SubElement(case, "properties")
            ET.SubElement(properties, "property", name="caprmedio.test_id", value=name)
            ET.SubElement(
                properties,
                "property",
                name="caprmedio.source_bindings_sha256",
                value=environment[SOURCE_BINDINGS_SHA256_ENVIRONMENT_VARIABLE],
            )
            for source in sources:
                ET.SubElement(
                    properties,
                    "property",
                    name="caprmedio.source_probe",
                    value=canonical_json({"source_path": source, "sha256": rows[source]["sha256"]}).decode("utf-8"),
                )
        ET.ElementTree(report).write(output_root / "coverage.xml", encoding="utf-8")
        return SuiteExecutionResult(0, b"MOCK DATA ONLY Unit receipt\n", b"")


class _NativeHappyPathFixture(PortablePackageFixture):
    """Physical portable inputs for mock-data artifacts and retained readers."""

    def _seed_project(self, extra_engine_members: dict[str, bytes]) -> None:
        required_members = {
            COMPILED_PROBE_TEST_MODULE: _test_member(COMPILED_PROBE_TEST_MODULE),
            **{path: _test_member(path) for path in CANDIDATE_E2E_MODULES},
        }
        required_members.update(extra_engine_members)
        required_members.update({
            path: (PROJECT_ROOT / path).read_bytes() for path in _MCP_PACKAGE_MEMBERS
        })
        super()._seed_project(required_members)
        self._copy_pinned_control_closure()
        default_settings = (
            "[release_suite]\nunit_timeout_seconds = 3600\n\n[release_e2e]\n"
            + "".join(f"{name} = {value}\n" for name, value in DEFAULT_RELEASE_E2E_LIMITS.__dict__.items())
        ).encode("utf-8")
        self.write(
            f"{CANONICAL_SOURCE_RELATIVE}/001_CORE_META_MODEL/caprmedio_framework_default_settings.toml",
            default_settings,
        )
        for relative in (SUITE_DRIVER_RELATIVE, E2E_DRIVER_RELATIVE, E2E_GRAMMAR_RELATIVE):
            source = PROJECT_ROOT / relative
            self.write(relative, source.read_bytes(), source.stat().st_mode & 0o777)
        sources = sorted((
            f"{CANONICAL_SOURCE_RELATIVE}/001_CORE_META_MODEL/04_requirement/CA-R-001--one.md",
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py",
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py",
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py",
            "102_FRAMEWORK_ENGINE/202_AGENTIC/201_PROMPTS/prompt.md",
            "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md",
            "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/agents/openai.yaml",
        ))
        self.write(
            MODULE_RULES_RELATIVE,
            canonical_json({
                "schema_version": 1,
                "module_probes": [{
                    "test_module_source_path": COMPILED_PROBE_TEST_MODULE,
                    "source_paths": sources,
                    "compiled_candidate_probe": True,
                }],
            }),
        )

    def _candidate(self):
        return build_preflight_validated_candidate(
            self.root,
            candidate_release="N+1",
            full_suite_environment={
                "runner": "local-subprocess",
                "command": list(SUITE_DRIVER_COMMAND),
                "working_directory": ".",
            },
            candidate_image_reference="mock-only:N+1",
        )[1]

    def _copy_pinned_control_closure(self) -> None:
        """Seed only the current release-only control snapshot inputs."""

        copy_control_closure(PROJECT_ROOT, self.root)
        self._fixture_authority_pin = derive_release_execution_source_snapshot(self.root)[2]


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _install_active_n(fixture: _NativeHappyPathFixture) -> None:
    """Build a disposable prior-N package; this is fixture setup only."""

    root = fixture.root
    engine_root = root / "102_FRAMEWORK_ENGINE"
    skill_root = engine_root / "202_AGENTIC/205_SKILLS/ca"
    rows: list[PackageRow] = []

    def add(resource: str, source: Path, destination: Path) -> None:
        rows.append(PackageRow(
            resource=resource,
            source_path=source.relative_to(root).as_posix(),
            destination_path=destination.as_posix(),
            sha256=_sha256(source),
            mode=source.stat().st_mode & 0o777,
        ))

    for source in sorted(engine_root.rglob("*")):
        if not source.is_file() or source.is_symlink() or source.name == "Dockerfile" or source.is_relative_to(skill_root):
            continue
        add("FRAMEWORK_ENGINE", source, Path("FRAMEWORK_ENGINE") / source.relative_to(engine_root))
    source_root = root / CANONICAL_SOURCE_RELATIVE
    for source in sorted(source_root.rglob("*")):
        if source.is_file() and not source.is_symlink():
            add("METHODOLOGY", source, Path("METHODOLOGY/sources") / source.relative_to(source_root))
    compiled_root = root / fixture.sealed.private_compilation.compiled_root
    for source in sorted(compiled_root.rglob("*")):
        if source.is_file() and not source.is_symlink():
            add("METHODOLOGY", source, Path("METHODOLOGY/compiled") / source.relative_to(compiled_root))
    for source in sorted(skill_root.rglob("*")):
        if source.is_file() and not source.is_symlink():
            add("SKILL", source, Path("SKILLS/ca") / source.relative_to(skill_root))
    rows.sort(key=lambda row: (row.destination_path, row.source_path, row.sha256))
    package = root / RUNTIME_ROOT / "releases" / "N"
    package.mkdir(parents=True)
    for row in rows:
        target = package / row.destination_path
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(root / row.source_path, target)
        target.chmod(row.mode)
    (package / "manifest.toml").write_text(_render_manifest("N", rows), encoding="utf-8")
    active_skill = root / ".agents/skills/ca"
    if active_skill.exists():
        raise AssertionError("fresh fixture unexpectedly has an active Skill")
    shutil.copytree(package / "SKILLS/ca", active_skill)


def _frozen_host_capability(fixture: _NativeHappyPathFixture) -> FrozenHostE2ECapability:
    selector_sha, package_sha, skill_sha = _active_n_state(fixture.root, fixture.candidate)
    driver = fixture.root / RUNTIME_ROOT / "releases/N" / "FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RELEASE_VERSION/run_release_e2e.py"
    python = Path(sys.executable).resolve(strict=True)
    docker = fixture.root / ".caprmedio_tmp/mock-docker"
    docker.parent.mkdir(parents=True, exist_ok=True)
    docker.write_bytes(b"#!/bin/false\n# MOCK DATA ONLY\n")
    docker.chmod(0o755)
    controller = ExecutableIdentity("n_host_controller", str(driver), _sha256(driver))
    return FrozenHostE2ECapability(
        selector_sha,
        package_sha,
        skill_sha,
        controller,
        ExecutableIdentity("python", str(python), _sha256(python)),
        ExecutableIdentity("driver", str(driver), _sha256(driver)),
        ExecutableIdentity("docker", str(docker), _sha256(docker)),
        str(docker.parent),
    )


class PortableReleaseFullGateBoundaryTests(unittest.TestCase):
    def test_missing_prepared_package_refuses_before_any_predecessor_reader(self) -> None:
        fixture = _fixture()

        with self.assertRaises(ReleaseContractError) as raised:
            aggregate_bound_release_gates(
                fixture.candidate,
                fixture.sealed,
                object(),  # type: ignore[arg-type]
                object(),  # type: ignore[arg-type]
                object(),  # type: ignore[arg-type]
                object(),  # type: ignore[arg-type]
            )

        self.assertEqual("release-full-gate-portable-package-required", raised.exception.code)

    def test_alternate_valid_package_receipt_cannot_cross_candidate_boundary(self) -> None:
        fixture = _fixture()
        other = _fixture()
        alternate = prepare_portable_release_package(other.root, other.sealed)

        with self.assertRaises(ReleaseContractError):
            aggregate_bound_release_gates(
                fixture.candidate,
                fixture.sealed,
                object(),  # type: ignore[arg-type]
                object(),  # type: ignore[arg-type]
                object(),  # type: ignore[arg-type]
                object(),  # type: ignore[arg-type]
                prepared_package=alternate,
            )

    def test_raw_predecessors_cannot_bypass_the_retained_package_sidecar(self) -> None:
        fixture = _fixture()
        prepared = prepare_portable_release_package(fixture.root, fixture.sealed)

        with self.assertRaises(ReleaseContractError) as raised:
            aggregate_bound_release_gates(
                fixture.candidate,
                fixture.sealed,
                object(),  # type: ignore[arg-type]
                object(),  # type: ignore[arg-type]
                object(),  # type: ignore[arg-type]
                object(),  # type: ignore[arg-type]
                prepared_package=prepared,
            )

        self.assertEqual("release-full-gate-native-predecessor-untrusted", raised.exception.code)
        sidecars = tuple((fixture.root / ".caprmedio_tmp/release_candidates" / fixture.run_id / "package_evidence").glob("*.json"))
        self.assertEqual(1, len(sidecars))

    def test_retained_verifier_reopens_sidecar_before_trusting_typed_receipt(self) -> None:
        fixture = _fixture()
        prepared = prepare_portable_release_package(fixture.root, fixture.sealed)
        retained = retain_native_package_evidence(fixture.candidate, fixture.sealed, prepared)
        view = retained.view
        evidence = NativeFullGateEvidence(
            candidate_snapshot_manifest_sha256=view.candidate_snapshot_manifest_sha256,
            candidate_image_digest="sha256:" + "0" * 64,
            phase_map_sha256=view.phase_map.sha256,
            suite_receipt_sha256="0" * 64,
            build_receipt_sha256="0" * 64,
            image_receipt_sha256="0" * 64,
            e2e_receipt_sha256="0" * 64,
            outcome="passed",
            reason="synthetic receipt-shape only; not a Full Gate proof",
            evidence_root=f".caprmedio_runtime/release_full_gate/{view.candidate_snapshot_manifest_sha256}/attempt-synthetic",
            receipt_sha256="0" * 64,
            executed_tests=0,
            package_schema="portable-1",
            package_manifest_sha256=view.actual_package_manifest_sha256,
            package_evidence_sha256=retained.receipt_sha256,
            package_evidence_relpath=retained.receipt_path.relative_to(fixture.root).as_posix(),
            source_catalog_sha256=view.source_catalog_sha256,
            candidate_run_id=view.candidate_run_id,
            input_manifest_sha256=view.input_manifest_sha256,
            framework_version=view.framework_version,
            version_toml_sha256=view.version_toml_sha256,
        )

        for forged in (
            replace(retained, receipt_sha256="0" * 64),
            replace(retained, view=replace(view, member_inventory=())),
        ):
            with self.subTest(forged=forged), self.assertRaises(ReleaseContractError) as raised:
                verify_bound_full_gate_evidence(
                    fixture.candidate,
                    fixture.sealed,
                    object(),  # type: ignore[arg-type]
                    object(),  # type: ignore[arg-type]
                    object(),  # type: ignore[arg-type]
                    object(),  # type: ignore[arg-type]
                    evidence,
                    retained_package=forged,
                )

            self.assertEqual("release-full-gate-retained-package-mismatch", raised.exception.code)

    def test_portable_partial_e2e_partition_is_refused(self) -> None:
        fixture = _fixture()
        prepared = prepare_portable_release_package(fixture.root, fixture.sealed)
        retained = retain_native_package_evidence(fixture.candidate, fixture.sealed, prepared)
        phase_map = retained.view.phase_map
        evidence_root = ".caprmedio_runtime/release_suite/synthetic-partial"
        report = fixture.root / evidence_root / "coverage.xml"
        report.parent.mkdir(parents=True)
        report.write_text(
            "<testsuite tests=\"1\" failures=\"0\" errors=\"0\" skipped=\"0\" "
            f"caprmedio.phase=\"unit\" caprmedio.phase_map_sha256=\"{phase_map.sha256}\">"
            f"<testcase classname=\"{phase_map.unit_paths[0]}\" name=\"synthetic_unit\"/>"
            "</testsuite>",
            encoding="utf-8",
        )
        suite = SimpleNamespace(
            phase_map_sha256=phase_map.sha256,
            evidence_root=evidence_root,
            executed_tests=1,
        )
        e2e = SimpleNamespace(harness_receipts=())

        with self.assertRaises(ReleaseContractError) as raised:
            full_gate._observe_partition(fixture.root, suite, e2e, phase_map)

        self.assertEqual("release-full-gate-partition-invalid", raised.exception.code)

    def test_mock_native_aggregate_reopens_public_retained_artifacts_after_source_and_selector_drift(self) -> None:
        """Mock-data-only happy path through real public retained readers.

        No command is executed.  The typed production executor classes are
        patched only at their command/capability seams to write bounded,
        physical fixture artifacts.  The post-drift assertion patches no
        constituent reader or Full Gate verifier and is not real Full Gate
        proof, Docker proof, host-process proof, or release evidence.
        """

        fixture = _NativeHappyPathFixture()
        with _fixture_authority(fixture._fixture_authority_pin):
            self._run_mock_native_retained_happy_path(fixture)

    def _run_mock_native_retained_happy_path(self, fixture: _NativeHappyPathFixture):
        _install_active_n(fixture)
        suite = execute_bound_release_suite(
            fixture.candidate,
            fixture.sealed,
            executor=_MockNativeSuiteExecutor(),
        )
        self.assertTrue(suite.passed, suite.reason)
        prepared = prepare_portable_release_package(fixture.root, fixture.sealed)
        retained = retain_native_package_evidence(fixture.candidate, fixture.sealed, prepared)
        retained_candidate = retain_retained_candidate_identity(fixture.candidate, fixture.sealed, prepared)
        image_id = "sha256:" + "a" * 64
        image_labels: dict[str, str] = {}
        canary_spec: dict[str, object] = {}

        def docker_run(argv, *, cwd, timeout_seconds):
            argv = tuple(argv)
            if argv[:2] == ("docker", "build"):
                iid_path = Path(argv[argv.index("--iidfile") + 1])
                for index, value in enumerate(argv):
                    if value == "--label":
                        key, label_value = argv[index + 1].split("=", 1)
                        image_labels[key] = label_value
                canary_spec.update(json.loads((Path(argv[-1]) / "canary.json").read_bytes()))
                iid_path.write_text(image_id, encoding="utf-8")
                return DockerCommandResult(0, b"MOCK DATA ONLY Docker build\n", b"")
            if argv[:3] == ("docker", "image", "inspect"):
                return DockerCommandResult(
                    0,
                    canonical_json([{"Id": image_id, "Config": {"Labels": image_labels}}]),
                    b"",
                )
            if argv[:2] == ("docker", "run"):
                report = {
                    "schema": "caprmedio.release_version.portable_image_canary.v1",
                    "candidate_snapshot_manifest_sha256": canary_spec["candidate_snapshot_manifest_sha256"],
                    "package_schema": canary_spec["package_schema"],
                    "package_manifest_sha256": canary_spec["package_manifest_sha256"],
                    "source_catalog_sha256": canary_spec["source_catalog_sha256"],
                    "candidate_run_id": canary_spec["candidate_run_id"],
                    "input_manifest_sha256": canary_spec["input_manifest_sha256"],
                    "framework_version": canary_spec["framework_version"],
                    "version_toml_sha256": canary_spec["version_toml_sha256"],
                    "verified_files": len(canary_spec["package_rows"]),
                    "mcp_tools": ["get_mcp_reload_status"],
                }
                return DockerCommandResult(0, canonical_json(report), b"")
            raise AssertionError(f"unexpected mock Docker argv: {argv}")

        docker = DockerSubprocessExecutor()
        with patch.object(docker, "run", side_effect=docker_run):
            build = build_candidate_image(
                fixture.candidate,
                fixture.sealed,
                suite,
                executor=docker,
                prepared_package=prepared,
            )
            verification = verify_candidate_image(
                fixture.candidate,
                fixture.sealed,
                suite,
                build,
                executor=docker,
                prepared_package=prepared,
            )
        self.assertEqual("built", build.outcome, build.reason)
        self.assertEqual("verified", verification.outcome, verification.reason)

        capability = _frozen_host_capability(fixture)

        def host_run(argv, *, cwd, environment, timeout_seconds):
            argv = tuple(argv)
            if argv[:3] == ("docker", "image", "inspect"):
                return E2EExecutionResult(0, (image_id + "\n").encode("utf-8"), b"")
            junit = Path(argv[argv.index("--junit") + 1])
            module = Path(argv[argv.index("--pattern") + 1]).stem
            junit.write_bytes(
                f"<testsuite tests='1' failures='0' errors='0' skipped='0'>"
                f"<testcase classname='{module}.Mock' name='MOCK DATA ONLY'/></testsuite>".encode("utf-8")
            )
            return E2EExecutionResult(0, b"MOCK DATA ONLY E2E receipt\n", b"")

        host = HostE2EExecutor()
        with (
            patch.object(HostE2EExecutor, "freeze_capability", return_value=capability),
            patch.object(HostE2EExecutor, "revalidate_capability", return_value=None),
            patch.object(host, "run", side_effect=host_run),
        ):
            e2e = run_candidate_e2e_gate(
                fixture.candidate,
                fixture.sealed,
                suite,
                verification,
                image_build=build,
                executor=host,
                prepared_package=prepared,
            )
            full = aggregate_bound_release_gates(
                fixture.candidate,
                fixture.sealed,
                suite,
                build,
                verification,
                e2e,
                prepared_package=prepared,
            )
        self.assertTrue(e2e.passed, e2e.reason)
        self.assertIsInstance(full, NativeFullGateEvidence)
        self.assertTrue(full.passed, full.reason)
        self.assertEqual(retained.receipt_sha256, full.package_evidence_sha256)

        # These mutate the live currentness sources *after* every original
        # artifact exists.  Retained verification must use only its native
        # sidecar/package and recorded public image/E2E reader artifacts.
        tool = fixture.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"
        tool.write_bytes(tool.read_bytes() + b"# source drift after selection\n")
        (fixture.root / ".caprmedio_runtime/framework/current.toml").write_text('release = "other"\n', encoding="utf-8")

        self.assertEqual(
            fixture.root,
            verify_bound_full_gate_evidence(
                fixture.candidate,
                fixture.sealed,
                suite,
                build,
                verification,
                e2e,
                full,
                retained_package=retained,
            ),
        )
        return suite, build, verification, e2e, full, retained_candidate


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
