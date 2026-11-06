"""Query fields are semantic views; full reads retain nested source bytes."""

import sys
import unittest
from pathlib import Path

import yaml

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS / "tests"))

import test_connector_atom_read as fixtures  # noqa: E402
from connector_atom_read import query_atoms, read_atom  # noqa: E402


class NestedHeaderAtomReadTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.AtomConnectorTests(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        for path in (self.fixture.first, self.fixture.second):
            _, header, body = path.read_text().split("---", 2)
            metadata = yaml.safe_load(header)
            subjects = metadata.pop("subjects")
            context = {"role": metadata.pop("content_role"), "form": metadata.pop("type"),
                       "topics": {"main_subject": subjects["governs"],
                                  "dependencies": subjects["depends_on"]}}
            nested = {"identity": {"atom_id": metadata.pop("atom_id")}, "context": context,
                      "state": {key: metadata.pop(key) for key in ("status", "version", "updated_at")},
                      **metadata}
            path.write_text("---\n" + yaml.safe_dump(nested, sort_keys=False) + "---" + body)

    def test_query_returns_nested_topics_as_requested_subjects(self):
        result = query_atoms(self.fixture.filters(), self.fixture.view)

        self.assertEqual([], result["errors"])
        self.assertEqual(2, len(result["data"]["matches"]))
        for row in result["data"]["matches"]:
            self.assertIsInstance(row["subjects"], dict)
            self.assertIn("governs", row["subjects"])

    def test_full_read_preserves_actual_nested_yaml_and_exact_token(self):
        raw = self.fixture.first.read_bytes()

        result = read_atom("CA-R-1", self.fixture.view)

        self.assertEqual(raw.decode(), result["data"]["source"])
        self.assertNotIn("subjects:", result["data"]["frontmatter"])
        self.assertIn("topics:", result["data"]["frontmatter"])
        self.assertEqual(raw, self.fixture.first.read_bytes())


if __name__ == "__main__":
    unittest.main()
