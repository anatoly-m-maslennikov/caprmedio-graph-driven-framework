"""Bounded retained-response cases for the Integrated continuation frontier."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

import selected_integrated_frontier as frontier  # noqa: E402
from selected_integrated_frontier import (  # noqa: E402
    IntegratedFrontierError,
    IntegratedFrontierStore,
    admit_submission,
    complete_receipt,
    load_pending,
    save_pending,
)
from selected_integrated_frontier_records import MAX_RECORD_BYTES, canonical, digest  # noqa: E402
from selected_integrated_frontier_state import write_state  # noqa: E402
import test_selected_integrated_frontier as fixtures  # noqa: E402


class IntegratedResponseCarrierTests(unittest.TestCase):
    def _fixture(self) -> fixtures.SelectedIntegratedFrontierTests:
        fixture = fixtures.SelectedIntegratedFrontierTests()
        fixture.setUp()
        self.addCleanup(fixture.tearDown)
        return fixture

    @staticmethod
    def _response(continuation_id: str) -> dict[str, object]:
        rows = [
            {
                "packet": f"packet-{index}-" + "p" * 2_900,
                "trusted_definition": f"definition-{index}-" + "d" * 2_900,
            }
            for index in range(40)
        ]
        return {"continuation_id": continuation_id, "frozen_rows": rows}

    @staticmethod
    def _state_path(fixture: fixtures.SelectedIntegratedFrontierTests) -> Path:
        return (
            fixture.project
            / ".caprmedio_install/workflow_orchestrator/runs"
            / fixture.run_id
            / "integrated_frontier.json"
        )

    def _completed(
        self, continuation_id: str = "first"
    ) -> tuple[fixtures.SelectedIntegratedFrontierTests, dict[str, object]]:
        fixture = self._fixture()
        save_pending(fixture.project, fixture.run_id, fixture._frontier(continuation_id))
        admit_submission(fixture.project, fixture.run_id, fixture._submission(continuation_id))
        response = self._response(continuation_id)
        complete_receipt(fixture.project, fixture.run_id, continuation_id, response)
        return fixture, response

    def test_three_large_responses_stay_out_of_the_bounded_state(self) -> None:
        fixture = self._fixture()
        responses = []
        for index in range(3):
            continuation_id = f"continuation-{index}"
            save_pending(
                fixture.project,
                fixture.run_id,
                fixture._frontier(continuation_id, candidate=f"candidate-{index}"),
            )
            admit_submission(fixture.project, fixture.run_id, fixture._submission(continuation_id))
            response = self._response(continuation_id)
            self.assertLess(len(canonical(response)), MAX_RECORD_BYTES)
            complete_receipt(fixture.project, fixture.run_id, continuation_id, response)
            responses.append(response)

        state_path = self._state_path(fixture)
        state = json.loads(state_path.read_text(encoding="utf-8"))
        self.assertEqual(2, state["schema_version"])
        self.assertLess(len(canonical(state)), MAX_RECORD_BYTES)
        self.assertTrue(all("response_ref" in record for record in state["records"].values()))
        restored = load_pending(fixture.project, fixture.run_id)
        self.assertEqual(responses, [item["response"] for item in restored["receipts"].values()])

    def test_repeat_restart_and_record_keep_the_original_response_shape(self) -> None:
        fixture, response = self._completed()
        first = complete_receipt(fixture.project, fixture.run_id, "first", response)
        self.assertEqual(response, first["response"])
        with self.assertRaises(IntegratedFrontierError):
            complete_receipt(fixture.project, fixture.run_id, "first", {"different": True})
        with IntegratedFrontierStore(fixture.project, fixture.run_id) as store:
            record = store.record("first")
            self.assertEqual(response, record["response"])
            record["response"]["frozen_rows"][0]["packet"] = "tampered"
            self.assertEqual(response, store.record("first")["response"])
        self.assertEqual(
            response, load_pending(fixture.project, fixture.run_id)["receipts"]["first"]["response"]
        )

    def test_response_carrier_rejects_missing_tampered_and_symlinked_files(self) -> None:
        for fault in ("missing", "tampered", "symlink"):
            with self.subTest(fault=fault):
                fixture, _response = self._completed(fault)
                state_path = self._state_path(fixture)
                state = json.loads(state_path.read_text(encoding="utf-8"))
                carrier = state_path.with_name(state["records"][fault]["response_ref"])
                if fault == "missing":
                    carrier.unlink()
                elif fault == "tampered":
                    carrier.write_text('{"tampered":true}', encoding="utf-8")
                else:
                    external = fixture.project.parent / "external-response.json"
                    external.write_text(carrier.read_text(encoding="utf-8"), encoding="utf-8")
                    carrier.unlink()
                    carrier.symlink_to(external)
                with self.assertRaises(IntegratedFrontierError):
                    load_pending(fixture.project, fixture.run_id)

    def test_legacy_inline_v1_receipt_remains_readable_and_upgrades_on_new_completion(self) -> None:
        fixture = self._fixture()
        save_pending(fixture.project, fixture.run_id, fixture._frontier("legacy"))
        admit_submission(fixture.project, fixture.run_id, fixture._submission("legacy"))
        legacy_response = {"legacy": "response"}
        with IntegratedFrontierStore(fixture.project, fixture.run_id) as store:
            state = store._state_value()
            record = state["records"]["legacy"]
            record.update(
                response=legacy_response, response_digest=digest(legacy_response), state="completed"
            )
            state["schema_version"] = 1
            write_state(store._path(), store.root, store.run_id, state)
        self.assertEqual(
            legacy_response,
            load_pending(fixture.project, fixture.run_id)["receipts"]["legacy"]["response"],
        )
        save_pending(fixture.project, fixture.run_id, fixture._frontier("next", candidate="next"))
        admit_submission(fixture.project, fixture.run_id, fixture._submission("next"))
        complete_receipt(fixture.project, fixture.run_id, "next", {"next": True})
        state = json.loads(self._state_path(fixture).read_text(encoding="utf-8"))
        self.assertEqual(2, state["schema_version"])
        self.assertIn("response_ref", state["records"]["legacy"])

    def test_completion_does_not_reopen_state_while_holding_the_run_lock(self) -> None:
        fixture = self._fixture()
        save_pending(fixture.project, fixture.run_id, fixture._frontier("once"))
        admit_submission(fixture.project, fixture.run_id, fixture._submission("once"))
        with patch.object(frontier, "read_state", wraps=frontier.read_state) as reader:
            complete_receipt(fixture.project, fixture.run_id, "once", self._response("once"))
        self.assertEqual(1, reader.call_count)


if __name__ == "__main__":
    unittest.main()
