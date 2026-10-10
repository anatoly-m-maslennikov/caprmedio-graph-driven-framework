"""Focused composition coverage for the direct CA-O-200 runtime installer."""

from __future__ import annotations

from dataclasses import replace
from pathlib import Path
import sys
import unittest
from unittest.mock import ANY, patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = RELEASE_ROOT.parent
TOOLS_TEST_ROOT = TOOLS_ROOT / "tests"
RELEASE_TEST_ROOT = RELEASE_ROOT / "tests"
for _path in (RELEASE_ROOT, TOOLS_ROOT, TOOLS_TEST_ROOT, RELEASE_TEST_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from framework_installation import PortableInstallationRequest  # noqa: E402
from installation_transaction import InstallationTransactionError  # noqa: E402
from portable_runtime_publication import DirectPublishedRuntime, PortableRuntimePublicationError  # noqa: E402
import framework_runtime_installation as runtime_installation  # noqa: E402
import test_framework_installation_command as command_fixture  # noqa: E402


class FrameworkRuntimeInstallationTests(unittest.TestCase):
    """Composition tests retain an actual O200 command/start, not a fake grant."""

    def setUp(self) -> None:
        self.command_fixture = command_fixture.FrameworkInstallationCommandTests("runTest")
        self.command_fixture.setUp()
        self.addCleanup(self.command_fixture.doCleanups)
        command_request = self.command_fixture._request()
        self.root = self.command_fixture.root
        self.request = PortableInstallationRequest(
            target=replace(command_request.target, mode="adopt"),
            retained_gate_receipt_path=self.root / "retained" / "receipt.json",
            full_gate_packet=object(),
        )
        self.receipt = "a" * 64
        self.image = "sha256:" + "b" * 64

    def _packet_patch(self):
        return patch.object(
            runtime_installation,
            "_packet_facts",
            return_value=runtime_installation._PacketFacts(self.receipt, self.image),
        )

    def _seed_legacy_pair(self) -> tuple[bytes, bytes]:
        package = b"legacy-tools-package-selector\n"
        execution = b"legacy-framework-execution-selector\n"
        package_path = self.root / ".caprmedio_install" / "current.toml"
        package_path.parent.mkdir(parents=True)
        package_path.write_bytes(package)
        execution_path = self.root / ".caprmedio_runtime" / "framework" / "current.toml"
        execution_path.parent.mkdir(parents=True)
        execution_path.write_bytes(execution)
        return package, execution

    def test_predecessor_accepts_empty_and_complete_pairs_but_refuses_incomplete_state(self) -> None:
        empty = runtime_installation._predecessor(self.root)
        self.assertIsNone(empty.package_selector)
        self.assertIsNone(empty.execution_selector)
        self.assertEqual(1, empty.next_generation)

        package = b"native-package-selector\n"
        execution = b"state_generation = 4\n"
        package_path = self.root / ".caprmedio_install" / "current.toml"
        package_path.parent.mkdir(parents=True)
        package_path.write_bytes(package)
        execution_path = self.root / ".caprmedio_runtime" / "installation" / "current.toml"
        execution_path.parent.mkdir(parents=True)
        execution_path.write_bytes(execution)
        native = runtime_installation._predecessor(self.root)
        self.assertEqual(package, native.package_selector)
        self.assertEqual((Path(".caprmedio_runtime/installation/current.toml"), execution), native.execution_selector)
        self.assertEqual(5, native.next_generation)

        execution_path.unlink()
        with self.assertRaisesRegex(
            runtime_installation.FrameworkRuntimeInstallationError,
            "runtime-installation-predecessor-incomplete",
        ):
            runtime_installation._predecessor(self.root)

    def test_composes_actual_command_with_distinct_legacy_selectors_and_uv_stage(self) -> None:
        package_selector, execution_selector = self._seed_legacy_pair()
        methodology = object()
        prepared = object()
        publication = DirectPublishedRuntime(publication=None, recording={"state": "recorded"})
        captured: dict[str, object] = {}

        def build(*args, **kwargs):
            captured.update(kwargs)
            return prepared

        with (
            self._packet_patch(),
            patch.object(runtime_installation, "verify_prospective_portable_full_gate", return_value=self.receipt),
            patch.object(runtime_installation, "prepare_target_portable_methodology_publication", return_value=methodology),
            patch.object(runtime_installation, "reopen_prepared_target_portable_methodology_publication", return_value=methodology),
            patch.object(runtime_installation, "build_prepared_native_publication", side_effect=build),
            patch.object(runtime_installation, "execute_direct_native_runtime", return_value=publication) as execute,
        ):
            result = runtime_installation.install_framework_runtime(
                self.request,
                command_id="fixture-runtime-composition",
                operator="Fixture Operator",
            )
        self.addCleanup(result.command.action_session.close)

        self.assertIs(prepared, result.prepared)
        self.assertIs(publication, result.publication)
        self.assertEqual(["started"], [event["event"] for event in self.command_fixture._events()])
        self.assertEqual(package_selector, captured["old_package_selector"])
        self.assertEqual(
            (Path(".caprmedio_runtime/framework/current.toml"), execution_selector),
            captured["old_execution_selector"],
        )
        self.assertEqual(1, captured["state_generation"])
        stage = captured["runtime_stage_request"]
        self.assertEqual(
            (
                "--project-root",
                "../../..",
                "--control-root",
                self.request.target.control_child,
            ),
            stage.fixed_arguments,
        )
        self.assertEqual(
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/implementation_server.py",
            stage.entrypoint,
        )
        self.assertEqual(self.request.full_gate_packet, stage.full_gate_packet)
        self.assertTrue(Path(stage.path_directories[0]).is_dir())
        execute.assert_called_once_with(result.command, prepared, lock=ANY)

    def test_full_gate_failure_refuses_before_direct_command_start(self) -> None:
        with (
            self._packet_patch(),
            patch.object(runtime_installation, "verify_prospective_portable_full_gate", side_effect=RuntimeError("stale")),
            patch.object(runtime_installation, "run_framework_installation_command") as run,
        ):
            with self.assertRaisesRegex(
                runtime_installation.FrameworkRuntimeInstallationError,
                "runtime-installation-full-gate-invalid",
            ):
                runtime_installation.install_framework_runtime(
                    self.request,
                    command_id="fixture-runtime-refusal",
                    operator="Fixture Operator",
                )
        run.assert_not_called()
        self.assertEqual([], self.command_fixture._events())

    def test_no_uv_refuses_before_direct_command_start_without_python_fallback(self) -> None:
        with (
            self._packet_patch(),
            patch.object(runtime_installation, "verify_prospective_portable_full_gate", return_value=self.receipt),
            patch.object(runtime_installation, "prepare_target_portable_methodology_publication", return_value=object()),
            patch.object(runtime_installation.shutil, "which", return_value=None),
            patch.object(runtime_installation, "run_framework_installation_command") as run,
        ):
            with self.assertRaisesRegex(
                runtime_installation.FrameworkRuntimeInstallationError,
                "runtime-installation-uv-unavailable",
            ):
                runtime_installation.install_framework_runtime(
                    self.request,
                    command_id="fixture-runtime-no-uv",
                    operator="Fixture Operator",
                )
        run.assert_not_called()
        self.assertEqual([], self.command_fixture._events())

    def test_preparation_failure_records_blocked_result_without_execution_retry(self) -> None:
        self._seed_legacy_pair()
        methodology = object()
        recorded = {"state": "recorded", "result_ref": "retained/result.json"}
        closure = object()
        with (
            self._packet_patch(),
            patch.object(runtime_installation, "verify_prospective_portable_full_gate", return_value=self.receipt),
            patch.object(runtime_installation, "prepare_target_portable_methodology_publication", return_value=methodology),
            patch.object(runtime_installation, "reopen_prepared_target_portable_methodology_publication", return_value=methodology),
            patch.object(runtime_installation, "build_prepared_native_publication", side_effect=RuntimeError("stage unavailable")),
            patch.object(runtime_installation, "prepare_direct_full_gate_effect_closure", return_value=closure),
            patch.object(runtime_installation, "record_direct_installation_result", return_value=recorded) as record,
            patch.object(runtime_installation, "execute_direct_native_runtime") as execute,
        ):
            result = runtime_installation.install_framework_runtime(
                self.request,
                command_id="fixture-runtime-blocked",
                operator="Fixture Operator",
            )
        self.addCleanup(result.command.action_session.close)

        self.assertIsNone(result.prepared)
        self.assertIsNone(result.publication.publication)
        self.assertEqual(recorded, result.publication.recording)
        record.assert_called_once()
        self.assertEqual("blocked_before_delete", record.call_args.kwargs["effect_outcome"])
        self.assertEqual("RuntimeError", record.call_args.kwargs["reason"])
        execute.assert_not_called()
        self.assertEqual(["started"], [event["event"] for event in self.command_fixture._events()])

    def test_preparation_ca_skill_os_failure_retains_vetted_stage_and_errno(self) -> None:
        self._seed_legacy_pair()
        methodology = object()
        recorded = {"state": "recorded", "result_ref": "retained/result.json"}
        failure = PortableRuntimePublicationError(
            "portable-publication-ca-skill-failed",
            "local ca Skill replacement stopped with retained preparation",
            stage="remove_prior_skill",
            os_errno=1,
            relative_path=".agents/skills/ca",
        )
        with (
            self._packet_patch(),
            patch.object(runtime_installation, "verify_prospective_portable_full_gate", return_value=self.receipt),
            patch.object(runtime_installation, "prepare_target_portable_methodology_publication", return_value=methodology),
            patch.object(runtime_installation, "reopen_prepared_target_portable_methodology_publication", return_value=methodology),
            patch.object(runtime_installation, "build_prepared_native_publication", side_effect=failure),
            patch.object(runtime_installation, "prepare_direct_full_gate_effect_closure", return_value=object()),
            patch.object(runtime_installation, "record_direct_installation_result", return_value=recorded) as record,
            patch.object(runtime_installation, "execute_direct_native_runtime") as execute,
        ):
            result = runtime_installation.install_framework_runtime(
                self.request,
                command_id="fixture-runtime-ca-skill-failure",
                operator="Fixture Operator",
            )
        self.addCleanup(result.command.action_session.close)

        self.assertEqual(recorded, result.publication.recording)
        self.assertEqual(
            "portable-publication-ca-skill-failed; stage=remove_prior_skill; errno=1; path=.agents/skills/ca",
            record.call_args.kwargs["reason"],
        )
        self.assertEqual("blocked_before_delete", record.call_args.kwargs["effect_outcome"])
        execute.assert_not_called()

    def test_lock_acquisition_failure_records_started_command_without_execution_retry(self) -> None:
        self._seed_legacy_pair()
        methodology = object()
        recorded = {"state": "recorded", "result_ref": "retained/result.json"}
        closure = object()
        with (
            self._packet_patch(),
            patch.object(runtime_installation, "verify_prospective_portable_full_gate", return_value=self.receipt),
            patch.object(runtime_installation, "prepare_target_portable_methodology_publication", return_value=methodology),
            patch.object(
                runtime_installation.InstallationPublicationLock,
                "acquire",
                side_effect=InstallationTransactionError("installation-lock-busy", "fixture lock is busy"),
            ),
            patch.object(runtime_installation, "prepare_direct_full_gate_effect_closure", return_value=closure),
            patch.object(runtime_installation, "record_direct_installation_result", return_value=recorded) as record,
            patch.object(runtime_installation, "execute_direct_native_runtime") as execute,
        ):
            result = runtime_installation.install_framework_runtime(
                self.request,
                command_id="fixture-runtime-lock-blocked",
                operator="Fixture Operator",
            )
        self.addCleanup(result.command.action_session.close)

        self.assertIsNone(result.prepared)
        self.assertEqual(recorded, result.publication.recording)
        self.assertEqual("blocked_before_delete", record.call_args.kwargs["effect_outcome"])
        execute.assert_not_called()
        self.assertEqual(["started"], [event["event"] for event in self.command_fixture._events()])

    def test_recording_pending_preserves_uncertain_lock_without_retry(self) -> None:
        self._seed_legacy_pair()
        methodology = object()
        pending = {"state": "recording_pending", "result_ref": "retained/result.json"}
        with (
            self._packet_patch(),
            patch.object(runtime_installation, "verify_prospective_portable_full_gate", return_value=self.receipt),
            patch.object(runtime_installation, "prepare_target_portable_methodology_publication", return_value=methodology),
            patch.object(runtime_installation, "reopen_prepared_target_portable_methodology_publication", return_value=methodology),
            patch.object(runtime_installation, "build_prepared_native_publication", side_effect=RuntimeError("stage unavailable")),
            patch.object(runtime_installation, "prepare_direct_full_gate_effect_closure", return_value=object()),
            patch.object(runtime_installation, "record_direct_installation_result", return_value=pending),
            patch.object(runtime_installation, "execute_direct_native_runtime") as execute,
        ):
            result = runtime_installation.install_framework_runtime(
                self.request,
                command_id="fixture-runtime-recording-pending",
                operator="Fixture Operator",
            )
        self.addCleanup(result.command.action_session.close)

        self.assertIsNone(result.prepared)
        self.assertEqual(pending, result.publication.recording)
        self.assertTrue((self.root / ".caprmedio_runtime" / "installation" / "lock.toml").is_file())
        execute.assert_not_called()
        self.assertEqual(["started"], [event["event"] for event in self.command_fixture._events()])

    def test_executor_failure_is_not_reclassified_as_predelete_blocked(self) -> None:
        self._seed_legacy_pair()
        methodology = object()
        prepared = object()
        with (
            self._packet_patch(),
            patch.object(runtime_installation, "verify_prospective_portable_full_gate", return_value=self.receipt),
            patch.object(runtime_installation, "prepare_target_portable_methodology_publication", return_value=methodology),
            patch.object(runtime_installation, "reopen_prepared_target_portable_methodology_publication", return_value=methodology),
            patch.object(runtime_installation, "build_prepared_native_publication", return_value=prepared),
            patch.object(runtime_installation, "record_direct_installation_result") as record,
            patch.object(runtime_installation, "execute_direct_native_runtime", side_effect=RuntimeError("post-effect")),
        ):
            with self.assertRaisesRegex(RuntimeError, "post-effect"):
                runtime_installation.install_framework_runtime(
                    self.request,
                    command_id="fixture-runtime-executor-failure",
                    operator="Fixture Operator",
                )
        record.assert_not_called()
        self.assertTrue((self.root / ".caprmedio_runtime" / "installation" / "lock.toml").is_file())
        self.assertEqual(["started"], [event["event"] for event in self.command_fixture._events()])

    def test_untyped_request_never_reaches_direct_command(self) -> None:
        with patch.object(runtime_installation, "run_framework_installation_command") as run:
            with self.assertRaisesRegex(
                runtime_installation.FrameworkRuntimeInstallationError,
                "runtime-installation-request-invalid",
            ):
                runtime_installation.install_framework_runtime(  # type: ignore[arg-type]
                    object(), command_id="fixture-runtime-untyped", operator="Fixture Operator"
                )
        run.assert_not_called()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
