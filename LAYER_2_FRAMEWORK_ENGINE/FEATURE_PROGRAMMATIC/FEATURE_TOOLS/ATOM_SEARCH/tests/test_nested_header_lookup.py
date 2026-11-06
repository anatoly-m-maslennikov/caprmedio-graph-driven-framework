"""Nested Headers cross the public lookup boundary without mutating sources."""

from __future__ import annotations

import io
import json
import sys
import unittest
from pathlib import Path

import yaml

TOOLS = Path(__file__).resolve().parents[2]
for directory in (TOOLS, TOOLS / "ATOM_SEARCH", TOOLS / "ATOM_SEARCH/tests"):
    sys.path.insert(0, str(directory))

import atom_search as provider  # noqa: E402
import test_subject_lookup_provider as fixtures  # noqa: E402


class NestedHeaderLookupTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = fixtures.SubjectLookupProviderTests(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.diagnostics = io.StringIO()
        self.fixture.adapter = provider.create_adapter(self.fixture.root, diagnostic_stream=self.diagnostics)

    def _nest(self, path: Path, *, topics: bool = False) -> None:
        parsed = provider.parse_carrier(path.read_bytes(), path)
        source = dict(parsed.metadata)
        identity = {key: source.pop(key) for key in ("atom_id", "ref_id") if key in source}
        context = {"role": source.pop("content_role")}
        if "type" in source:
            context["form"] = source.pop("type")
        if topics:
            subjects = source.pop("subjects")
            context["topics"] = {"main_subject": subjects["governs"]}
            if "depends_on" in subjects:
                context["topics"]["dependencies"] = subjects["depends_on"]
        state = {key: source.pop(key) for key in ("status", "version", "updated_at")}
        metadata = {"identity": identity, "context": context, "state": state, **source}
        path.write_text("---\n" + yaml.safe_dump(metadata, sort_keys=False) + "---\n" + parsed.body)

    def test_nested_targets_and_contract_return_complete_matches(self) -> None:
        for path in self.fixture.fixture.role.glob("CA-R-*.md"):
            self._nest(path)
        self._nest(self.fixture.root / provider.SOURCE_PINS[0]["path"])

        result = self.fixture.invoke()

        self.assertEqual([], result["errors"])
        self.assertTrue(result["data"]["complete"])
        self.assertEqual(["CA-R-1", "CA-R-1"],
                         [row["atom_id"] for row in result["data"]["matches"]])
        self.assertEqual(1, result["current_state"][0]["version"])

    def test_nested_topics_are_searchable_without_authored_subject_aliases(self) -> None:
        for path in self.fixture.fixture.role.glob("CA-R-*.md"):
            self._nest(path, topics=True)

        result = self.fixture.invoke()

        self.assertEqual([], result["errors"])
        self.assertTrue(result["data"]["complete"])
        self.assertEqual(["CA-R-1", "CA-R-1"],
                         [row["atom_id"] for row in result["data"]["matches"]])

    def test_conflicting_nested_identity_is_warning_with_valid_partial_results(self) -> None:
        path = next(self.fixture.fixture.role.glob("CA-R-2-*.md"))
        self._nest(path)
        path.write_text(path.read_text().replace("---\n", "---\natom_id: CA-R-999\n", 1))

        result = self.fixture.invoke()

        self.assertEqual(["schema_invalid"], [error["code"] for error in result["errors"]])
        self.assertFalse(result["data"]["complete"])
        self.assertEqual(["CA-R-1", "CA-R-1"],
                         [row["atom_id"] for row in result["data"]["matches"]])
        self.assertEqual(path.relative_to(self.fixture.root).as_posix(),
                         result["data"]["warnings"][0]["path"])
        record = json.loads(self.diagnostics.getvalue())
        self.assertEqual(("WARNING", "schema_invalid", "CA"),
                         (record["severity"], record["code"], record["project_prefix"]))


if __name__ == "__main__":
    unittest.main()
