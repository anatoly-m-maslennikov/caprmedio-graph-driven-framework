"""Independent byte/effect oracles for the isolated current W02 fixture."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parent.parent / "201_TOOLS"
for location in (TOOLS / "ATOM_UPDATE/tests", TOOLS, APP):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import atom_operations as operations  # noqa: E402
import atom_subject_apply as native  # noqa: E402
from test_subject_apply_portfolio import REPOSITORY, SubjectApplyProject  # noqa: E402


EFFECT_TIME = "2026-10-13 19:20:21 +0400"
BEFORE_TIME = "2026-10-06 00:00:00 +0000"
SCRATCH = REPOSITORY / ".caprmedio_tmp/tests/independent-subject-portfolio"
SCRATCH.mkdir(parents=True, exist_ok=True)


def expected_bytes(role, status, newline, *, changed):
    """Literal source contract, independent of the Subject planner/materializer."""
    letter = "P" if role == "Plan" else "R"
    type_line = "type: Plan\n" if role == "Plan" else ""
    sections = (
        "## Objective\n\nFixture objective value.\n\n"
        "## Details\n\nFixture details value.\n\n"
        "### Definition of Done\n\nFixture completion condition.\n"
        if role == "Plan" else
        "## Scope\n\nFixture scope value.\n\n"
        "## Claim\n\nFixture claim value.\n\n"
        "## Details\n\nFixture details value.\n\n"
    )
    before = (
        f"---\natom_id: CA-{letter}-8100\ncontent_role: {role}\n{type_line}"
        "current_scope_unit: PARENT\nclaim_target_scope_unit: PARENT\n"
        "local_tier: Standard\nglobal_tier: 5\nauthor: golden-operator\n"
        f"status: {status}\nsubjects:\n  governs: Atom/Test\n  depends_on: []\n"
        f"version: 3\nupdated_at: '{BEFORE_TIME}'\nrelations: {{}}\n---\n"
        "# Summary\n\nDocker status proof carrier\n\n" + sections
    )
    if changed:
        for old, new in (
            ("  governs: Atom/Test\n", '  governs: "Atom.State"\n'),
            ("version: 3\n", "version: 4\n"),
            (f"updated_at: '{BEFORE_TIME}'\n", f'updated_at: "{EFFECT_TIME}"\n'),
        ):
            assert before.count(old) == 1
            before = before.replace(old, new)
    return before.replace("\n", newline).encode("utf-8")


def authority_snapshot(root):
    control = root / ".caprmedio_caprmedio"
    return {path.relative_to(root).as_posix(): (path.read_bytes(), path.stat().st_mode & 0o777)
            for path in control.rglob("*") if path.is_file()
            and not {"_projection", "_journal"}.intersection(path.relative_to(control).parts)}


def paths(role, status):
    letter, directory = ("P", "03_plan") if role == "Plan" else ("R", "04_requirement")
    role_path = Path(".caprmedio_caprmedio/PARENT") / directory
    placement = "done" if status == "Done" else "001_backlog" if status == "Backlog" else ""
    filename = f"CA-{letter}-8100--docker-status.md"
    history_directory = "archived" if role == "Plan" else "archive"
    return (role_path / placement / filename).as_posix(), (role_path / history_directory / f"CA-{letter}-8100--docker-status@3.md").as_posix()


def descriptor(role, status, path, raw, *, changed=False, archived=False):
    return {"atom_id": "CA-P-8100" if role == "Plan" else "CA-R-8100", "path": path,
            "filename": Path(path).name, "version": 4 if changed else 3,
            "digest": hashlib.sha256(raw).hexdigest(),
            "lifecycle": "archived" if archived else "done" if status == "Done" else "active",
            "status": status, "updated_at": EFFECT_TIME if changed else BEFORE_TIME,
            "content_role": role, "type": "Plan" if role == "Plan" else None}


class IndependentSubjectPortfolioTests(unittest.TestCase):
    def fixture(self, *, role="Requirement", status="Active", newline="\n", noop=False):
        directory = tempfile.TemporaryDirectory(dir=SCRATCH, ignore_cleanup_errors=True)
        self.addCleanup(directory.cleanup)
        return SubjectApplyProject(Path(directory.name), role=role, status=status, newline=newline, noop=noop)

    def assert_ledger(self, expected_files, observed_files, expected_effects, observed_effects,
                      expected_refs, observed_refs):
        self.assertEqual(expected_files, observed_files, "complete authoritative byte/mode frontier")
        self.assertEqual(expected_effects, observed_effects, "exact ordered native effect ledger")
        self.assertEqual(expected_refs, observed_refs, "exact recorded Action effect references")

    def publication(self, *, role="Requirement", status="Active", newline="\n"):
        fixture = self.fixture(role=role, status=status, newline=newline)
        current_path, history_path = paths(role, status)
        before = expected_bytes(role, status, newline, changed=False)
        after = expected_bytes(role, status, newline, changed=True)
        self.assertEqual(before, fixture.path.read_bytes())
        self.assertEqual(current_path, fixture.path.relative_to(fixture.root).as_posix())
        self.assertEqual(descriptor(role, status, current_path, before), fixture.target)
        for raw in (before, after):
            frontmatter, content = operations.split_frontmatter(raw.decode("utf-8"))
            operations._validate_complete_carrier(fixture.root, fixture.path, frontmatter, content, creating=False)
        before_files = authority_snapshot(fixture.root)
        expected_files = {**before_files, current_path: (after, 0o640), history_path: (before, 0o640)}
        expected_effects = [
            {"state": "changed", "carrier": descriptor(role, status, current_path, after, changed=True)},
            {"state": "changed", "carrier": descriptor(role, status, history_path, before, archived=True)},
        ]
        expected_refs = sorted([current_path, history_path])
        run_id = f"independent-{role}-{status}-{len(newline)}"
        runner, frozen = fixture.execution(run_id)
        confirmation = fixture.confirmation(frozen)
        self.assertEqual(before_files, authority_snapshot(fixture.root), "preview/staging changed authority")
        with patch.object(native, "current_timestamp", return_value=EFFECT_TIME) as clock:
            result = runner._dispatch_confirmed_subject(frozen, confirmation)
        clock.assert_called_once_with(fixture.root)
        self.assertEqual("terminal", result["disposition"])
        child = next(row["requested_run_id"] for row in frozen["request"]["execution"]["requested_runs"]
                     if row["definition"]["atom_id"] == "CA-O-030")
        terminal = next(row for row in result["terminal_runs"] if row["run_id"] == child)
        self.assertEqual("completed", terminal["outcome"])
        retained = json.loads((fixture.root / terminal["result_ref"]).read_bytes())
        actual = retained["native_result"]
        self.assertEqual("applied", actual["outcome"])
        self.assertEqual("admitted", retained["lifecycle_recording"]["state"])
        self.assertEqual(expected_effects[0]["carrier"], actual["observed"])
        self.assertEqual(expected_effects[1]["carrier"], actual["history"]["prior_revision"])
        observed_files = authority_snapshot(fixture.root)
        self.assert_ledger(expected_files, observed_files, expected_effects, actual["effects"],
                           expected_refs, terminal["effect_refs"])
        events = [json.loads(line)
                  for path in (fixture.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson")
                  for line in path.read_bytes().splitlines()]
        child_events = [event for event in events if event.get("run", {}).get("run_id") == child]
        self.assertEqual(["started", "completed"], [event["event"] for event in child_events])
        self.assertEqual(expected_refs, child_events[1]["effect_refs"])
        with patch.object(native, "subject_update_action", side_effect=AssertionError("publication replayed")):
            self.assertEqual(result, runner.dispatch(frozen))
        return expected_files, observed_files, expected_effects, actual["effects"], expected_refs, terminal["effect_refs"], current_path, history_path

    def test_active_lf_matches_independent_full_byte_and_effect_ledgers(self):
        self.publication()

    def test_active_crlf_matches_independent_full_byte_and_effect_ledgers(self):
        self.publication(newline="\r\n")

    def test_plan_done_keeps_non_active_status_and_admitted_placement(self):
        self.publication(role="Plan", status="Done")

    def test_plan_backlog_keeps_non_active_status_and_crlf_placement(self):
        self.publication(role="Plan", status="Backlog", newline="\r\n")

    def test_plan_done_noop_has_independent_unchanged_ledger_and_real_receipt(self):
        fixture = self.fixture(role="Plan", status="Done", noop=True)
        current_path, history_path = paths("Plan", "Done")
        self.assertEqual(expected_bytes("Plan", "Done", "\n", changed=False), fixture.path.read_bytes())
        before = authority_snapshot(fixture.root)
        runner, frozen = fixture.execution("independent-done-noop")
        with patch.object(native, "current_timestamp", return_value=EFFECT_TIME) as clock:
            result = runner.dispatch(frozen)
        clock.assert_not_called()
        self.assertEqual(before, authority_snapshot(fixture.root))
        self.assertEqual("terminal", result["disposition"])
        outer = next(row["requested_run_id"] for row in frozen["request"]["execution"]["requested_runs"]
                     if row["definition"]["atom_id"] == "CA-O-128")
        terminal = next(row for row in result["terminal_runs"] if row["run_id"] == outer)
        self.assertEqual("no_op", terminal["outcome"])
        self.assertTrue(all(row["effect_refs"] == [] for row in result["terminal_runs"]))
        self.assertFalse((fixture.root / history_path).exists())
        self.assertEqual(before[current_path], (fixture.path.read_bytes(), fixture.path.stat().st_mode & 0o777))

    def test_wrong_current_history_and_effect_outputs_fail_independent_oracle(self):
        expected_files, observed_files, expected_effects, observed_effects, expected_refs, observed_refs, current, history = self.publication()
        for name, path in (("wrong-current", current), ("wrong-history", history)):
            with self.subTest(control=name):
                wrong = dict(observed_files)
                raw, mode = wrong[path]
                wrong[path] = (raw + b"unrequested byte\n", mode)
                with self.assertRaises(AssertionError):
                    self.assert_ledger(expected_files, wrong, expected_effects, observed_effects, expected_refs, observed_refs)
        for name, wrong in (("missing", observed_effects[:1]), ("extra", observed_effects + observed_effects[:1]),
                            ("reordered", list(reversed(observed_effects)))):
            with self.subTest(control=name), self.assertRaises(AssertionError):
                self.assert_ledger(expected_files, observed_files, expected_effects, wrong, expected_refs, observed_refs)
        wrong = copy.deepcopy(observed_effects)
        wrong[0]["carrier"]["digest"] = "0" * 64
        with self.subTest(control="wrong-effect-digest"), self.assertRaises(AssertionError):
            self.assert_ledger(expected_files, observed_files, expected_effects, wrong, expected_refs, observed_refs)
        with self.subTest(control="wrong-recorded-effects"), self.assertRaises(AssertionError):
            self.assert_ledger(expected_files, observed_files, expected_effects, observed_effects, expected_refs, observed_refs + ["unrequested.md"])


if __name__ == "__main__":
    unittest.main()
