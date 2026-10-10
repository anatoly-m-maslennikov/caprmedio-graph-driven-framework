"""Focused D604/O200 command binding tests with disposable physical carriers."""

from __future__ import annotations

import hashlib
import json
from dataclasses import replace
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = RELEASE_ROOT.parent
TOOLS_TEST_ROOT = TOOLS_ROOT / "tests"
for _path in (RELEASE_ROOT, TOOLS_ROOT, TOOLS_TEST_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from direct_action_session import INSTALLATION_ATOM_RELATIVE  # noqa: E402
from framework_installation_command import (  # noqa: E402
    COMMAND_DIRECTORY,
    DirectFullGateEffectClosure,
    FrameworkInstallationCommandError,
    FrameworkInstallationCommandRequest,
    build_framework_installation_command_receipt,
    prepare_direct_full_gate_effect_closure,
    read_framework_installation_command_receipt,
    record_direct_installation_result,
    run_framework_installation_command,
)
import framework_installation_command as command_module  # noqa: E402
from framework_package import _path_digest, assemble_framework_package  # noqa: E402
from installation_context import TargetProjectRequest, bind_target_project_context  # noqa: E402
from source_admission_fixture import write_source_admission_receipt  # noqa: E402
import test_detached_native_full_gate as detached_gate_fixture  # noqa: E402
import test_native_installation_proof as proof_fixture  # noqa: E402
import test_native_selected_installation as selected_fixture  # noqa: E402


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


def _repository_root() -> Path:
    for candidate in RELEASE_ROOT.parents:
        source = (
            candidate
            / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"
            / "000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations"
            / INSTALLATION_ATOM_RELATIVE.name
        )
        if source.is_file():
            return candidate
    raise RuntimeError("repository O200 source is unavailable")


REPOSITORY_ROOT = _repository_root()
DEFAULT_SETTINGS_SOURCE = (
    REPOSITORY_ROOT
    / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"
    / "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/caprmedio_framework_default_settings.toml"
)


class FrameworkInstallationCommandTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.package = self._package()
        self.root, self.control = self._project("alpha")

    def _write(self, root: Path, relative: str, payload: bytes, *, mode: int = 0o644) -> Path:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
        path.chmod(mode)
        return path

    def _package(self):
        source = self.base / "package-source"
        releases = self.base / "package-releases"
        action_source = (
            REPOSITORY_ROOT
            / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"
            / "000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations"
            / INSTALLATION_ATOM_RELATIVE.name
        )
        action_relative = INSTALLATION_ATOM_RELATIVE.as_posix()
        self._write(source, "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py", b"tool = 'fixture'\n", mode=0o755)
        self._write(
            source,
            "methodology/active/001_CORE_META_MODEL/04_requirement/CA-R-001--fixture.md",
            b"# core Methodology\n",
        )
        self._write(source, action_relative, action_source.read_bytes())
        self._write(source, "methodology/support/CA-D-001--fixture.md", b"# support\n")
        self._write(source, "SKILLS/ca/SKILL.md", b"# ca\n")
        self._write(source, "defaults/framework.toml", b"[defaults]\nname = 'fixture'\n")
        self._write(source, "pyproject.toml", b"[project]\nname = 'fixture'\nversion = '0.1.0'\n")
        self._write(source, "uv.lock", b"version = 1\n")
        self._write(source, "version.toml", b"[framework]\nversion = '0.1.0'\n")
        rows = (
            ("core", "core", "102_FRAMEWORK_ENGINE"),
            ("methodology", "methodology", "methodology/active/001_CORE_META_MODEL"),
            ("project-configuration", "configuration", "methodology/active/003_PROJECT_CONFIGURATION"),
            ("support", "support", "methodology/support"),
        )
        descriptors = tuple(
            {
                "identity": identity,
                "kind": kind,
                "revision": _path_digest(source, Path(relative), code="fixture-catalog"),
                "sha256": _path_digest(source, Path(relative), code="fixture-catalog"),
                "visibility": "public",
                "selection_default": False,
                "path": relative,
            }
            for identity, kind, relative in rows
        )
        receipt = write_source_admission_receipt(source, descriptors)
        lines = ["schema_version = 1", ""]
        for descriptor in descriptors:
            lines.extend(
                [
                    f"[source.{descriptor['identity']}]",
                    f'kind = "{descriptor["kind"]}"',
                    f'revision = "{descriptor["revision"]}"',
                    f'sha256 = "{descriptor["sha256"]}"',
                    f'admission_receipt_sha256 = "{receipt.sha256}"',
                    f'visibility = "{descriptor["visibility"]}"',
                    "selection_default = false",
                    f'path = "{descriptor["path"]}"',
                    "",
                ]
            )
        self._write(source, "catalog.toml", ("\n".join(lines) + "\n").encode())
        return assemble_framework_package(source, releases)

    def _project(self, name: str) -> tuple[Path, Path]:
        root = self.base / name
        control = root / f".caprmedio_{name}"
        control.mkdir(parents=True)
        (control / "caprmedio_project_settings.toml").write_text(
            "[project]\n"
            f'name = "{name}"\n\n'
            "[paths]\n"
            f'control_root = ".caprmedio_{name}"\n'
            f'journal_root = ".caprmedio_{name}/_journal"\n'
            'runtime_root = ".caprmedio_runtime"\n',
            encoding="utf-8",
        )
        (control / "project_structure.toml").write_text("schema_version = 1\nscope_units = []\n", encoding="utf-8")
        (control / "operators_registry.toml").write_text(
            '[[operators]]\nname = "Fixture Operator"\nrole = "project owner"\njournal_author = "fixture-operator"\n',
            encoding="utf-8",
        )
        framework = control / "000_CAPRMEDIO_framework"
        framework.mkdir()
        (framework / "caprmedio_framework_settings.toml").write_text(
            "# no optional Extension or Configuration selected\n",
            encoding="utf-8",
        )
        defaults = framework / "00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL"
        defaults.mkdir(parents=True)
        (defaults / "caprmedio_framework_default_settings.toml").write_bytes(DEFAULT_SETTINGS_SOURCE.read_bytes())
        return root, control

    def _request(self, *, mode: str = "bootstrap") -> FrameworkInstallationCommandRequest:
        target = TargetProjectRequest(
            target_root=self.root,
            control_child=self.control.name,
            mode=mode,
            target_project_identity="alpha",
            settings_path=self.control / "caprmedio_project_settings.toml",
            project_structure_path=self.control / "project_structure.toml",
            operators_registry_path=self.control / "operators_registry.toml",
            repository_identity=False,
            root_locator="fixtures/target",
            package_root=self.package.root,
            package_evidence=__import__("framework_package").provide_installation_package_evidence(self.package.root),
        )
        return FrameworkInstallationCommandRequest(
            target=target,
            target_context=bind_target_project_context(target),
            package=self.package,
            full_gate_receipt_sha256="a" * 64,
            command_id="fixture-install-command",
            operator="Fixture Operator",
        )

    def _events(self) -> list[dict[str, object]]:
        journal = self.control / "_journal"
        return [json.loads(line) for path in sorted(journal.glob("*.ndjson")) for line in path.read_text(encoding="utf-8").splitlines()]

    def test_retains_exact_d604_receipt_and_actual_o200_start(self) -> None:
        result = run_framework_installation_command(self._request())
        self.addCleanup(result.action_session.close)

        self.assertEqual(self.root / COMMAND_DIRECTORY / f"{result.command_receipt.sha256}.json", result.command_receipt_path)
        self.assertEqual(result.package.manifest_digest, result.command_receipt.package_manifest_sha256)
        self.assertEqual(result.target_context.sha256, result.command_receipt.target_project_context_sha256)
        self.assertIsNone(result.command_receipt.prior_runtime_selector_sha256)
        self.assertEqual("fixture-operator", result.action_provenance.author)
        self.assertEqual(result.action_start["run_id"], result.action_provenance.action_run_id)
        self.assertEqual(["started"], [event["event"] for event in self._events()])
        self.assertEqual("CA-O-200", self._events()[0]["action_id"])
        self.assertFalse((self.root / ".caprmedio_runtime/installation/current.toml").exists())
        self.assertFalse((self.root / ".caprmedio_install/current.toml").exists())

    def test_literal_registered_account_needs_no_alias_mapping(self) -> None:
        (self.control / "operators_registry.toml").write_text(
            '[[operators]]\nname = "fixture-operator"\nrole = "project owner"\n',
            encoding="utf-8",
        )
        request = replace(self._request(), operator="fixture-operator")

        result = run_framework_installation_command(request)
        self.addCleanup(result.action_session.close)

        self.assertEqual("fixture-operator", result.command_receipt.operator)
        self.assertEqual("fixture-operator", result.command_receipt.journal_author)
        self.assertEqual("fixture-operator", result.action_provenance.author)
        self.assertEqual(["started"], [event["event"] for event in self._events()])

    def test_human_display_name_without_account_mapping_refuses_before_start(self) -> None:
        (self.control / "operators_registry.toml").write_text(
            '[[operators]]\nname = "Fixture Operator"\nrole = "project owner"\n',
            encoding="utf-8",
        )

        with self.assertRaises(FrameworkInstallationCommandError) as refused:
            run_framework_installation_command(self._request())

        self.assertEqual("installation-command-operator-invalid", refused.exception.code)
        self.assertFalse((self.root / COMMAND_DIRECTORY).exists())
        self.assertEqual([], self._events())

    def test_adopt_binds_the_exact_observed_legacy_runtime_selector(self) -> None:
        tool_selector = self.root / ".caprmedio_install/current.toml"
        framework_selector = self.root / ".caprmedio_runtime/framework/current.toml"
        tool_selector.parent.mkdir(parents=True)
        framework_selector.parent.mkdir(parents=True)
        tool_selector.write_bytes(b"tool_release = 'legacy-tool'\n")
        framework_selector.write_bytes(b"framework_release = 'legacy-framework'\n")

        result = run_framework_installation_command(self._request(mode="adopt"))
        self.addCleanup(result.action_session.close)

        self.assertEqual(
            hashlib.sha256(framework_selector.read_bytes()).hexdigest(),
            result.command_receipt.prior_runtime_selector_sha256,
        )
        self.assertNotEqual(
            hashlib.sha256(tool_selector.read_bytes()).hexdigest(),
            result.command_receipt.prior_runtime_selector_sha256,
        )

    def test_tool_selector_alone_is_not_aliased_as_legacy_framework_execution(self) -> None:
        tool_selector = self.root / ".caprmedio_install/current.toml"
        tool_selector.parent.mkdir(parents=True)
        tool_selector.write_bytes(b"tool_release = 'legacy-tool-only'\n")

        result = run_framework_installation_command(self._request(mode="adopt"))
        self.addCleanup(result.action_session.close)

        self.assertIsNone(result.command_receipt.prior_runtime_selector_sha256)

    def test_native_execution_selector_precedes_distinct_legacy_framework_and_tool_selectors(self) -> None:
        native_selector = self.root / ".caprmedio_runtime/installation/current.toml"
        framework_selector = self.root / ".caprmedio_runtime/framework/current.toml"
        tool_selector = self.root / ".caprmedio_install/current.toml"
        for selector, payload in (
            (native_selector, b"native_execution = 'current'\n"),
            (framework_selector, b"framework_release = 'legacy-framework'\n"),
            (tool_selector, b"tool_release = 'legacy-tool'\n"),
        ):
            selector.parent.mkdir(parents=True, exist_ok=True)
            selector.write_bytes(payload)

        result = run_framework_installation_command(self._request(mode="adopt"))
        self.addCleanup(result.action_session.close)

        self.assertEqual(
            hashlib.sha256(native_selector.read_bytes()).hexdigest(),
            result.command_receipt.prior_runtime_selector_sha256,
        )

    def test_refuses_package_drift_before_command_or_journal_effect(self) -> None:
        request = self._request()
        source = self.package.root / INSTALLATION_ATOM_RELATIVE
        source.write_bytes(source.read_bytes() + b"changed\n")

        with self.assertRaises(FrameworkInstallationCommandError) as refused:
            run_framework_installation_command(request)

        self.assertEqual("installation-command-context-stale", refused.exception.code)
        self.assertFalse((self.root / COMMAND_DIRECTORY).exists())
        self.assertEqual([], self._events())

    def test_registry_drift_after_start_leaves_only_recoverable_start(self) -> None:
        request = self._request()
        registry = self.control / "operators_registry.toml"
        original_begin = command_module.DirectActionSession.begin_action

        def mutate_after_start(session, **kwargs):
            started = original_begin(session, **kwargs)
            registry.write_text(
                '[[operators]]\nname = "Fixture Operator"\nrole = "project owner"\njournal_author = "changed-author"\n',
                encoding="utf-8",
            )
            return started

        with patch.object(command_module.DirectActionSession, "begin_action", new=mutate_after_start):
            with self.assertRaises(FrameworkInstallationCommandError) as refused:
                run_framework_installation_command(request)

        self.assertEqual("installation-command-context-stale", refused.exception.code)
        self.assertTrue(list((self.root / COMMAND_DIRECTORY).glob("*.json")))
        self.assertEqual(["started"], [event["event"] for event in self._events()])

    def test_closed_receipt_reader_refuses_extra_fields_and_digest_mismatch(self) -> None:
        payload = build_framework_installation_command_receipt(
            command_id="receipt-test",
            operator="Fixture Operator",
            journal_author="fixture-operator",
            operators_registry_sha256="a" * 64,
            action_source={
                "atom_id": "CA-O-200",
                "version": 1,
                "path": INSTALLATION_ATOM_RELATIVE.as_posix(),
                "sha256": "ffae75bedb643a4de5a5b081c65333a6bde6ea1055a4b29a6d6481139d0d71ce",
            },
            target_project_context_sha256="b" * 64,
            package_manifest_sha256="c" * 64,
            full_gate_receipt_sha256="d" * 64,
            prior_runtime_selector_sha256=None,
        )
        receipt = read_framework_installation_command_receipt(payload)
        with self.assertRaises(FrameworkInstallationCommandError) as mismatch:
            read_framework_installation_command_receipt(payload, expected_sha256="0" * 64)
        self.assertEqual("installation-command-receipt-digest-mismatch", mismatch.exception.code)
        forged = json.loads(payload)
        forged["permission"] = True
        with self.assertRaises(FrameworkInstallationCommandError) as invalid:
            read_framework_installation_command_receipt(json.dumps(forged, sort_keys=True, separators=(",", ":")).encode())
        self.assertEqual("installation-command-receipt-invalid", invalid.exception.code)
        self.assertEqual(hashlib.sha256(payload).hexdigest(), receipt.sha256)


class DirectInstallationResultEffectsTests(unittest.TestCase):
    """D604v7 retains an actual packet closure before any direct cut-over."""

    @classmethod
    def setUpClass(cls) -> None:
        fixture = selected_fixture._O200NativeHappyPathFixture()
        (
            proof_fixture.CandidateNativeInstallationProofTests._source_archive,
            proof_fixture.CandidateNativeInstallationProofTests._source_identity,
            proof_fixture.CandidateNativeInstallationProofTests._suite,
            proof_fixture.CandidateNativeInstallationProofTests._build,
            proof_fixture.CandidateNativeInstallationProofTests._verification,
            proof_fixture.CandidateNativeInstallationProofTests._e2e,
            proof_fixture.CandidateNativeInstallationProofTests._full,
        ) = detached_gate_fixture.DetachedNativeFullGateTests()._packet(fixture)

    def setUp(self) -> None:
        self.fixture = proof_fixture.CandidateNativeInstallationProofTests("runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        defaults = (
            self.fixture.control
            / "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"
            / "000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL"
        )
        defaults.mkdir(parents=True, exist_ok=True)
        (defaults / "caprmedio_framework_default_settings.toml").write_bytes(DEFAULT_SETTINGS_SOURCE.read_bytes())
        self.packet = self.fixture._packet()
        self.command = run_framework_installation_command(
            FrameworkInstallationCommandRequest(
                target=self.fixture.target_request,
                target_context=self.fixture.context,
                package=self.fixture.package,
                full_gate_receipt_sha256=self.packet.evidence.receipt_sha256,
                command_id="direct-result-fixture",
                operator="Anatoly Maslennikov",
            )
        )
        self.addCleanup(self.command.action_session.close)

    def test_retains_the_seven_physical_original_gate_carriers_before_terminal_recording(self) -> None:
        closure = prepare_direct_full_gate_effect_closure(self.command, full_gate_packet=self.packet)

        self.assertIsInstance(closure, DirectFullGateEffectClosure)
        self.assertEqual(
            (
                "full_gate_receipt",
                "retained_candidate_descriptor",
                "retained_package_sidecar",
                "unit_gate_receipt",
                "build_receipt",
                "verification_receipt",
                "e2e_gate_receipt",
            ),
            tuple(effect.kind for effect in closure.effects),
        )
        for effect in closure.effects:
            carrier = self.fixture.target / effect.reference
            self.assertTrue(carrier.is_file())
            self.assertEqual(hashlib.sha256(carrier.read_bytes()).hexdigest(), effect.sha256)

        with patch.object(self.command.action_session, "finish_action", side_effect=RuntimeError("terminal unavailable")):
            pending = record_direct_installation_result(
                self.command,
                full_gate_effects=closure,
                state_generation=1,
                effect_outcome="blocked_before_delete",
                reason="fixture-blocked",
            )

        self.assertEqual("recording_pending", pending["state"])
        retained = self.fixture.target / pending["result_ref"]
        self.assertEqual(0o600, retained.stat().st_mode & 0o777)
        self.assertEqual(
            tuple(effect.kind for effect in closure.effects),
            tuple(row["kind"] for row in pending["result"]["effects"]),
        )

    def test_refuses_a_handcrafted_exact_closure_before_result_or_terminal(self) -> None:
        """Matching rows are evidence only when the private observation exists."""

        observed = prepare_direct_full_gate_effect_closure(self.command, full_gate_packet=self.packet)
        handcrafted = DirectFullGateEffectClosure(
            action_run_id=observed.action_run_id,
            installation_command_sha256=observed.installation_command_sha256,
            package_manifest_sha256=observed.package_manifest_sha256,
            target_project_context_sha256=observed.target_project_context_sha256,
            full_gate_receipt_sha256=observed.full_gate_receipt_sha256,
            effects=observed.effects,
        )
        action_run = self.command.action_start["run_id"]
        result_path = self.fixture.target / ".caprmedio_tmp/installation/results" / action_run / "result.json"

        with (
            patch.object(self.command.action_session, "record_effects") as record_effects,
            patch.object(self.command.action_session, "finish_action") as finish_action,
        ):
            with self.assertRaises(FrameworkInstallationCommandError) as refused:
                record_direct_installation_result(
                    self.command,
                    full_gate_effects=handcrafted,
                    state_generation=1,
                    effect_outcome="blocked_before_delete",
                    reason="handcrafted-closure",
                )

        self.assertEqual("installation-command-result-invalid", refused.exception.code)
        self.assertFalse(result_path.exists())
        record_effects.assert_not_called()
        finish_action.assert_not_called()

    def test_completed_result_retains_exact_eleven_observed_effect_rows(self) -> None:
        closure = prepare_direct_full_gate_effect_closure(self.command, full_gate_packet=self.packet)
        generation = 1
        current_rows = (
            ("package_selector", Path(".caprmedio_install/current.toml"), b"package-current\n"),
            ("runtime_selector", Path(".caprmedio_runtime/installation/current.toml"), b"runtime-current\n"),
            (
                "release_proof",
                Path(".caprmedio_runtime/installation/generations") / str(generation) / "release-proof.toml",
                b"release-proof\n",
            ),
            (
                "package_manifest",
                Path(".caprmedio_install/releases") / self.command.package.manifest_digest / "manifest.toml",
                b"package-manifest\n",
            ),
        )
        for _kind, relative, payload in current_rows:
            carrier = self.fixture.target / relative
            carrier.parent.mkdir(parents=True, exist_ok=True)
            carrier.write_bytes(payload)

        recorded = record_direct_installation_result(
            self.command,
            full_gate_effects=closure,
            state_generation=generation,
            effect_outcome="completed",
            reason=None,
        )

        expected = [
            (kind, relative.as_posix(), hashlib.sha256(payload).hexdigest())
            for kind, relative, payload in current_rows
        ] + [(effect.kind, effect.reference, effect.sha256) for effect in closure.effects]
        rows = recorded["result"]["effects"]
        self.assertEqual("recorded", recorded["state"])
        self.assertEqual(11, len(rows))
        self.assertEqual(
            tuple(kind for kind, _reference, _sha256 in expected),
            tuple(row["kind"] for row in rows),
        )
        self.assertEqual(
            tuple(reference for _kind, reference, _sha256 in expected),
            tuple(row["reference"] for row in rows),
        )
        self.assertEqual(
            tuple(digest for _kind, _reference, digest in expected),
            tuple(row["sha256"] for row in rows),
        )

    def test_refuses_a_changed_original_gate_carrier_before_any_result_or_terminal(self) -> None:
        receipt = self.packet.artifact_root / self.packet.evidence.evidence_root / "receipt.json"
        receipt.write_bytes(receipt.read_bytes() + b"changed")

        with self.assertRaises(FrameworkInstallationCommandError) as refused:
            prepare_direct_full_gate_effect_closure(self.command, full_gate_packet=self.packet)

        self.assertEqual("installation-command-full-gate-invalid", refused.exception.code)
        action_run = self.command.action_start["run_id"]
        self.assertFalse((self.fixture.target / ".caprmedio_tmp/installation/results" / action_run / "result.json").exists())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
