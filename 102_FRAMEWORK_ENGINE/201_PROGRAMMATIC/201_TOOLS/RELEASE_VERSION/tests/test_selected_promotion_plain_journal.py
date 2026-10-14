"""Selected publication retains real authority, not Journal-record proofs."""

from __future__ import annotations

import json
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import test_selected_installation_command as fixture
from release_contract import ReleaseContractError, canonical_json
from release_promotion import admit_selected_native_promotion_start
from selected_installation_command import (
    SelectedInstallationCommandError,
    read_selected_installation_command_receipt,
    reopen_selected_installation_command_start,
)


class SelectedPromotionPlainJournalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = fixture.SelectedInstallationCommandTests("run")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)

    def test_current_registry_observation_is_required_without_journal_proof(self) -> None:
        with patch.object(
            self.fixture.tracker,
            "source_observer",
            return_value={"selected": True, "current": False},
        ):
            with self.assertRaises(ReleaseContractError):
                admit_selected_native_promotion_start(self.fixture.run, self.fixture.context)

    def test_actual_definition_cannot_differ_from_admitted_source(self) -> None:
        self.fixture.session.actual["action"]["definition"] = {**self.fixture.source, "version": 99}
        with self.assertRaises(ReleaseContractError):
            admit_selected_native_promotion_start(self.fixture.run, self.fixture.context)

    def test_changed_actual_source_bytes_still_refuse(self) -> None:
        (self.fixture.root / self.fixture.source["path"]).write_bytes(b"changed source")
        with self.assertRaises(ReleaseContractError):
            admit_selected_native_promotion_start(self.fixture.run, self.fixture.context)

    def test_actual_parent_lineage_and_no_replay_state_still_refuse(self) -> None:
        for mutate in (
            lambda: self.fixture.session.actual["action"].update(parent_run_id="another-step"),
            lambda: self.fixture.session.terminal.update(action={"outcome": "completed"}),
        ):
            with self.subTest(mutate=mutate):
                original = self.fixture.session.actual["action"]["parent_run_id"]
                mutate()
                with self.assertRaises(ReleaseContractError):
                    admit_selected_native_promotion_start(self.fixture.run, self.fixture.context)
                self.fixture.session.actual["action"]["parent_run_id"] = original

    def test_historical_command_keeps_old_bytes_without_receipt_interpretation(self) -> None:
        receipt = self.fixture.command()
        document = json.loads(receipt.payload)
        document["selected_start_receipt"] = {"old": "uninterpreted Journal metadata"}
        payload = canonical_json(document)
        historical = read_selected_installation_command_receipt(payload)
        path = (
            self.fixture.root
            / ".caprmedio_runtime/installation/commands"
            / f"{historical.sha256}.json"
        )
        path.write_bytes(payload)
        self.assertEqual(payload, historical.payload)
        self.assertIsNone(reopen_selected_installation_command_start(self.fixture.root, historical))
        self.assertNotIn("selected_start_receipt", json.loads(receipt.payload))

    def test_historical_source_need_not_be_current_but_exact_command_bytes_do(self) -> None:
        receipt = self.fixture.command()
        (self.fixture.root / self.fixture.source["path"]).unlink()
        self.assertIsNone(reopen_selected_installation_command_start(self.fixture.root, receipt))
        path = (
            self.fixture.root
            / ".caprmedio_runtime/installation/commands"
            / f"{receipt.sha256}.json"
        )
        path.write_bytes(receipt.payload + b"\n")
        with self.assertRaises(SelectedInstallationCommandError):
            reopen_selected_installation_command_start(self.fixture.root, receipt)

    def test_direct_discovery_consumes_run_locator_not_event_or_journal_proof(self) -> None:
        sys.path.insert(0, str(fixture.RELEASE_ROOT.parents[1] / "203_APPS/WORKFLOW_ORCHESTRATOR"))
        from framework_installation_command import FrameworkInstallationCommandReceipt
        from installed_mcp_binding import _RUNTIME_SELECTOR_KEYS
        from native_selected_installation import _PROOF_KEYS
        from release_promotion import bind_selected_native_n_from_checkpoint

        root = self.fixture.root
        selector_path = root / ".caprmedio_runtime/installation/current.toml"
        selector_path.parent.mkdir(parents=True, exist_ok=True)
        selector_path.touch()
        selector = dict.fromkeys(_RUNTIME_SELECTOR_KEYS, "a" * 64)
        selector.update(schema_version=1, state_generation=1)
        proof = dict.fromkeys(_PROOF_KEYS, "a" * 64)
        proof.update(schema_version=2)

        def encode(value):
            return "\n".join(f"{key}={json.dumps(item)}" for key, item in value.items()).encode()

        command = FrameworkInstallationCommandReceipt(
            "command",
            "operator",
            "account",
            "a" * 64,
            {},
            "a" * 64,
            "a" * 64,
            "a" * 64,
            None,
            "a" * 64,
            b"command",
        )
        binding = SimpleNamespace(
            selected=SimpleNamespace(state_generation=1, full_gate_receipt_sha256="a" * 64)
        )
        carrier_bytes = [
            encode(selector),
            encode(proof),
            b'{"operation":"install_framework_runtime"}',
            b"actual-result",
        ]
        with (
            patch("native_selected_installation._read", autospec=True, side_effect=carrier_bytes),
            patch(
                "framework_installation_command.read_framework_installation_command_receipt",
                autospec=True,
                return_value=command,
            ),
            patch(
                "framework_installation_command.reopen_framework_installation_command_start",
                autospec=True,
                return_value="direct-action:actual",
            ) as start,
            patch(
                "framework_package.verify_framework_package", autospec=True, return_value=object()
            ),
            patch(
                "installed_mcp_binding._context",
                autospec=True,
                return_value=SimpleNamespace(control_child_relpath=".caprmedio_caprmedio"),
            ),
            patch("release_checkpoint.read_direct_native_result_effects", autospec=True) as effects,
            patch("release_checkpoint.read_direct_native_result_packet", autospec=True) as packet,
            patch("release_handoff.bind_native_installed_n", autospec=True, return_value=binding),
            patch("work_journal.read_records", side_effect=AssertionError("not a Journal proof")),
            patch(
                "work_journal.append_sealed_events",
                side_effect=AssertionError("read-only discovery"),
            ),
        ):
            self.assertIs(binding, bind_selected_native_n_from_checkpoint(root))
        start.assert_called_once()
        self.assertEqual("direct-action:actual", effects.call_args.kwargs["action_run_id"])
        self.assertEqual("direct-action:actual", packet.call_args.kwargs["action_run_id"])


if __name__ == "__main__":
    unittest.main()
