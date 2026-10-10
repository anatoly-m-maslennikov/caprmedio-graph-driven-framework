"""Focused same-session phase-driver coverage."""

from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch


PUBLIC_RELEASE = Path(__file__).resolve().parents[1]
if str(PUBLIC_RELEASE) not in sys.path:
    sys.path.insert(0, str(PUBLIC_RELEASE))

import public_release  # noqa: E402


class _Session:
    def __init__(self, root: Path) -> None:
        self.tracker = SimpleNamespace(root=root)
        pairs = (("CA-O-189", "CA-O-190"), ("CA-O-191", "CA-O-192"),
                 ("CA-O-193", "CA-O-194"), ("CA-O-195", "CA-O-196"),
                 ("CA-O-197", "CA-O-198"))
        rows = [{"requested_run_id": "workflow", "kind": "workflow", "parent_requested_run_id": None,
                 "definition": {"atom_id": "CA-O-188"}}]
        for index, (step, action) in enumerate(pairs, 1):
            step_id = f"step-{index}"
            rows.extend((
                {"requested_run_id": step_id, "kind": "step", "parent_requested_run_id": "workflow",
                 "definition": {"atom_id": step}},
                {"requested_run_id": f"action-{index}", "kind": "action", "parent_requested_run_id": step_id,
                 "definition": {"atom_id": action}},
            ))
        self.request = {"requested_runs": rows}
        self.started: list[str] = []

    def start_run(self, requested_run_id: str) -> dict[str, object]:
        self.started.append(requested_run_id)
        row = next(row for row in self.request["requested_runs"] if row["requested_run_id"] == requested_run_id)
        return {"run_id": requested_run_id, "kind": row["kind"], "definition": row["definition"]}


class PublicSessionPhasesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.session = _Session(self.root)
        self.finishes: list[dict[str, object]] = []

    def _driver(self):
        return public_release.SelectedPublicSessionPhases(self.root, self.session)

    def test_typed_callback_completes_the_exact_requested_pair_and_preserves_refs(self) -> None:
        call = public_release.ToolCallEvidence("inputs/one.json", "results/one.json", ("effects/one.json",), ("reports/one.json",))
        with patch.object(public_release, "RunExecutionSession", _Session), \
                patch.object(public_release, "_run_evidence_ref", side_effect=lambda _session, run, *, outcome: f"runs/{run['run_id']}-{outcome}.json"), \
                patch.object(public_release, "_finish", side_effect=lambda _session, run, **kwargs: self.finishes.append({"run": run, **kwargs})):
            result = self._driver().execute("discover_matching_pr", lambda: SimpleNamespace(call=call))

        self.assertEqual(call, result.call)
        self.assertEqual(["step-1", "action-1"], self.session.started)
        self.assertEqual(["action-1", "step-1"], [row["run"]["run_id"] for row in self.finishes])
        self.assertTrue(all(row["outcome"] == "completed" for row in self.finishes))
        self.assertEqual(["effects/one.json"], self.finishes[0]["effect_refs"])
        self.assertEqual("results/one.json", self.finishes[0]["result_ref"])

    def test_failed_callback_closes_the_started_pair_and_stops_the_driver(self) -> None:
        with patch.object(public_release, "RunExecutionSession", _Session), \
                patch.object(public_release, "_run_evidence_ref", side_effect=lambda _session, run, *, outcome: f"runs/{run['run_id']}-{outcome}.json"), \
                patch.object(public_release, "_finish", side_effect=lambda _session, run, **kwargs: self.finishes.append({"run": run, **kwargs})):
            driver = self._driver()
            with self.assertRaisesRegex(public_release.PublicReleaseError, "refused"):
                driver.execute("discover_matching_pr", lambda: (_ for _ in ()).throw(public_release.PublicReleaseError("refused", "refused")))
            with self.assertRaisesRegex(public_release.PublicReleaseError, "not available"):
                driver.execute("prepare_public_materials", lambda: SimpleNamespace(call=None))

        self.assertEqual(["step-1", "action-1"], self.session.started)
        self.assertTrue(all(row["outcome"] == "failed" for row in self.finishes))

    def test_explicit_begin_and_finish_hold_one_phase_for_multiple_native_receipts(self) -> None:
        capture = public_release.ToolCallEvidence(
            "inputs/capture.json", "results/capture.json", ("effects/capture.json",),
            ("reports/capture.json",),
        )
        commit = public_release.ToolCallEvidence(
            "inputs/commit.json", "results/commit.json", ("effects/commit.json",),
            ("reports/commit.json",),
        )
        with patch.object(public_release, "RunExecutionSession", _Session), \
                patch.object(public_release, "_run_evidence_ref", side_effect=lambda _session, run, *, outcome: f"runs/{run['run_id']}-{outcome}.json"), \
                patch.object(public_release, "_finish", side_effect=lambda _session, run, **kwargs: self.finishes.append({"run": run, **kwargs})):
            driver = self._driver()
            driver.execute("discover_matching_pr", lambda: SimpleNamespace(call=capture))
            driver.begin("prepare_public_materials")
            result = driver.finish(SimpleNamespace(call=commit), prior_results=(SimpleNamespace(call=capture),))

        self.assertEqual(commit, result.call)
        self.assertEqual(["step-1", "action-1", "step-2", "action-2"], self.session.started)
        self.assertEqual(
            ["effects/capture.json", "effects/commit.json"],
            self.finishes[-2]["effect_refs"],
        )


if __name__ == "__main__":
    unittest.main()
