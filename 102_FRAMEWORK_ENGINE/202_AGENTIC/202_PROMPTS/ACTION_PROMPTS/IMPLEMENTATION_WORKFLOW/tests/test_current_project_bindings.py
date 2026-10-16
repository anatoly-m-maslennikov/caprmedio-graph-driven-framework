"""Compatibility checks for the reviewed production source frontier."""
import hashlib
import importlib.util
import json
import re
import shutil
import tempfile
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[6]


def load_actions():
    spec = importlib.util.spec_from_file_location("implementation_actions", HERE / "implementation_actions.py")
    actions = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(actions)
    return actions


class CurrentProjectBindings(unittest.TestCase):
    def test_reviewed_workflow_binding_matches_current_project(self):
        manifest = json.loads((HERE / "source_bindings.json").read_text(encoding="utf-8"))["sources"]
        expected = next(row for row in manifest if row["atom_id"] == "CA-O-016")
        sources = load_actions().current_source_bindings()
        workflow = next(row for row in sources if row["atom_id"] == "CA-O-016")
        raw = (ROOT / expected["path"]).read_bytes()
        version = re.search(rb"^version: ?[\"']?(\d+)", raw, re.M)
        self.assertIsNotNone(version)
        self.assertEqual(workflow, expected)
        self.assertEqual(workflow["version"], int(version[1]))
        self.assertEqual(workflow["sha256"], hashlib.sha256(raw).hexdigest())
        self.assertNotIn("/archive/", workflow["path"])

    def test_stale_selected_project_source_is_rejected_without_archive_fallback(self):
        actions = load_actions()
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory) / "selected-project"
            for row in actions._reviewed_binding_rows():
                source = ROOT / row["path"]
                target = project / row["path"]
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)
            workflow_path = next(row["path"] for row in actions._reviewed_binding_rows()
                                 if row["atom_id"] == "CA-O-016")
            workflow = project / workflow_path
            workflow.write_text(workflow.read_text(encoding="utf-8") + "\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "stale reviewed source binding: CA-O-016"):
                actions.current_source_bindings(project)


if __name__ == "__main__":
    unittest.main()
