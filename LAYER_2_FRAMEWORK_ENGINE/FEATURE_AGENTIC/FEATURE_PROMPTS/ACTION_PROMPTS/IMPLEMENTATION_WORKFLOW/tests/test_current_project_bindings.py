"""Compatibility checks for the reviewed production source frontier."""
import hashlib
import json
import re
import shutil
import tempfile
import unittest
from pathlib import Path


from frozen_inputs import FROZEN_BINDINGS, FROZEN_PROJECT_ROOT, load_actions as load_frozen_actions


def load_actions():
    return load_frozen_actions()


class CurrentProjectBindings(unittest.TestCase):
    def test_reviewed_workflow_binding_matches_frozen_project(self):
        manifest = json.loads(FROZEN_BINDINGS.read_text(encoding="utf-8"))["sources"]
        expected = next(row for row in manifest if row["atom_id"] == "CA-O-016")
        sources = load_actions().current_source_bindings()
        workflow = next(row for row in sources if row["atom_id"] == "CA-O-016")
        raw = (FROZEN_PROJECT_ROOT / expected["path"]).read_bytes()
        version = re.search(rb"^version: ?[\"']?(\d+)", raw, re.M)
        self.assertIsNotNone(version)
        self.assertEqual(workflow, expected)
        self.assertEqual(workflow["version"], int(version[1]))
        self.assertEqual(workflow["sha256"], hashlib.sha256(raw).hexdigest())
        self.assertNotIn("/archive/", workflow["path"])

    def test_changed_current_source_is_remeasured_without_frozen_pin_comparison(self):
        actions = load_actions()
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory) / "selected-project"
            for row in actions._reviewed_binding_rows():
                source = FROZEN_PROJECT_ROOT / row["path"]
                target = project / row["path"]
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
            workflow_path = next(row["path"] for row in actions._reviewed_binding_rows()
                                 if row["atom_id"] == "CA-O-016")
            workflow = project / workflow_path
            workflow.write_text(workflow.read_text(encoding="utf-8") + "\n", encoding="utf-8")
            observed = next(row for row in actions.current_source_bindings(project)
                            if row["atom_id"] == "CA-O-016")
            self.assertEqual(workflow_path, observed["path"])
            self.assertEqual(hashlib.sha256(workflow.read_bytes()).hexdigest(), observed["sha256"])


if __name__ == "__main__":
    unittest.main()
