"""Updating O030 itself retains original Run bindings and continues the batch."""

import hashlib
import json
from pathlib import Path
import sys
import unittest

APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parent.parent / "201_TOOLS"
for location in (APP, TOOLS, TOOLS / "tests"):
    sys.path.insert(0, str(location))

import atom_operations as operations  # noqa: E402
from lifecycle_intents import carrier_descriptor  # noqa: E402
from subject_batch_authorization import (  # noqa: E402
    capture_batch_review,
    persist_subject_batch_confirmation,
)
from subject_batch_fixture import SubjectBatchProject  # noqa: E402
from test_subject_apply_portfolio import PUBLICATION_PINS  # noqa: E402
from work_journal import read_records  # noqa: E402


def action_target(project):
    operators = project.root / ".caprmedio_caprmedio/operators_registry.toml"
    operators.write_text(
        operators.read_text()
        + ('\n[[operators]]\nname="Anatoly Maslennikov"\nrole="project owner"\n')
    )
    structure = project.root / ".caprmedio_caprmedio/project_structure.toml"
    scope = Path(PUBLICATION_PINS["CA-O-030"]).parent.parent.as_posix()
    structure.write_text(
        structure.read_text()
        + (
            '\n[[scope_units]]\nscope_unit_name="TOOL_WORKFLOWS"\nparent="PROJECT"\n'
            'scope_unit_type="Unordered"\nscope_unit_label="FEATURE"\nstructural_level=1\n'
            f'navigational_order_number=2\nauthority_path="{scope}"\n'
            'delivery_path="delivery/TOOL_WORKFLOWS"\n'
        )
    )
    path = project.root / PUBLICATION_PINS["CA-O-030"]
    before = path.read_bytes()
    target = carrier_descriptor(project.root, path.relative_to(project.root).as_posix())
    subjects = operations.parse_carrier(before, path).metadata["subjects"]
    patches = [{"field": "governs", "old": subjects["governs"], "new": "Atom.Subjects"}]
    patches.extend(
        {"field": "depends_on", "old": value, "new": value.replace("/", ".")}
        for value in subjects["depends_on"]
        if "/" in value
    )
    project.packet["atoms"].insert(0, {"target": target, "subject_patches": patches})
    project.git(
        "add",
        ".caprmedio_caprmedio/project_structure.toml",
        ".caprmedio_caprmedio/operators_registry.toml",
    )
    project.git(
        "-c",
        "user.name=Fixture",
        "-c",
        "user.email=fixture@example.invalid",
        "commit",
        "--quiet",
        "-m",
        "Fixture self-action scope",
    )
    project.packet["git_checkpoint"] = project.git("rev-parse", "HEAD").strip()
    project.save_packet()
    return path, before, target


class SubjectBatchSelfActionTests(unittest.TestCase):
    def test_updating_own_action_then_next_atom_keeps_original_run_definition(self):
        project = SubjectBatchProject(self, count=1)
        action, before, target = action_target(project)
        archives = project.archives()
        runner, frozen = project.execution("subject-batch-self-action")
        review = capture_batch_review(runner, frozen)
        persist_subject_batch_confirmation(runner, frozen, review, operator_name="golden-operator")
        result = runner.dispatch(frozen)
        progress = json.loads(
            (
                runner.run_directory(frozen["request"]["run_id"]) / "subject_batch_progress.json"
            ).read_bytes()
        )
        self.assertEqual("terminal", result["disposition"], progress)
        self.assertEqual("completed", progress["state"], progress)
        self.assertEqual(2, progress["completed"])
        self.assertTrue(
            all(row["lifecycle_recording"]["state"] == "admitted" for row in progress["atoms"])
        )
        after = operations.parse_carrier(action.read_bytes(), action)
        self.assertEqual(target["version"] + 1, after.metadata["version"])
        self.assertEqual(before, archives[0].read_bytes())
        self.assertEqual(project.before[project.paths[0]], archives[1].read_bytes())
        self.assertNotEqual(project.before[project.paths[0]], project.paths[0].read_bytes())
        events = [
            row
            for row in read_records(project.root)
            if row.get("event") in {"started", "completed"}
            and row.get("run", {}).get("definition", {}).get("atom_id") == "CA-O-030"
        ]
        self.assertEqual(4, len(events))
        self.assertTrue(
            all(
                row["run"]["definition"]["version"] == target["version"]
                and row["run"]["definition"]["digest"] == hashlib.sha256(before).hexdigest()
                for row in events
            )
        )


if __name__ == "__main__":
    unittest.main()
