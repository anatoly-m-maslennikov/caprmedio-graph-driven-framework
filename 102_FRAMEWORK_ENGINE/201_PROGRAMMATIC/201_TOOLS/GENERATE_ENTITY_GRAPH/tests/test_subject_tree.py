"""Tree rendering preserves literal identities and value-link direction."""

import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import subject_tree


def fixture():
    return {"entities_graph": {
        "nodes": [{"identity": name} for name in ("Atom", "Atom/Revision", "Atom/Revision/Version", "Atom/Status", "Atom/Status: Active", "Workflow", "Workflow/Status", "Workflow/Status: Active", "Isolated")],
        "edges": [
            {"source_separator": "/", "source_identity": "Atom", "target_identity": "Atom/Revision"},
            {"source_separator": "/", "source_identity": "Atom/Revision", "target_identity": "Atom/Revision/Version"},
            {"source_separator": "/", "source_identity": "Atom", "target_identity": "Atom/Status"},
            {"source_separator": ":", "source_identity": "Atom/Status: Active", "target_identity": "Atom/Status"},
            {"source_separator": "/", "source_identity": "Workflow", "target_identity": "Workflow/Status"},
            {"source_separator": ":", "source_identity": "Workflow/Status: Active", "target_identity": "Workflow/Status"},
        ]}}


class SubjectTreeTests(unittest.TestCase):
    def test_full_forest_preserves_context_and_isolated_nodes(self):
        data = fixture()
        original = copy.deepcopy(data)
        self.assertEqual("Atom\n├── /Revision\n│   └── /Version\n└── /Status\n    └── : Active\n\nIsolated\n\nWorkflow\n└── /Status\n    └── : Active\n", subject_tree.entity_tree(data))
        self.assertEqual(original, data)

    def test_one_branch_and_missing_root(self):
        self.assertEqual("Atom/Revision\n└── /Version\n", subject_tree.entity_tree(fixture(), "Atom/Revision"))
        with self.assertRaisesRegex(ValueError, "tree-root-unavailable"):
            subject_tree.entity_tree(fixture(), "Missing")

    def test_order_does_not_change_output(self):
        data = fixture()
        expected = subject_tree.entity_tree(data)
        data["entities_graph"]["nodes"].reverse()
        data["entities_graph"]["edges"].reverse()
        self.assertEqual(expected, subject_tree.entity_tree(data))

    def test_missing_endpoint_and_non_prefix_edge_fail(self):
        for parent, child in (("Missing", "Atom/Status"), ("Atom/Revision", "Atom")):
            data = fixture()
            data["entities_graph"]["edges"][0].update(source_identity=parent, target_identity=child)
            with self.assertRaisesRegex(ValueError, "tree-prefix-edge-invalid"):
                subject_tree.entity_tree(data)


if __name__ == "__main__":
    unittest.main()
