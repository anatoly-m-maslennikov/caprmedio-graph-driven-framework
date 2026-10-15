"""Current rule revisions replace historical manifest pins, never observed input pins."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest
from unittest.mock import patch
from typing import Any

TOOL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL.parent))

from VALIDATE_ATOMS.validate_atoms_workers import authority, context, proposed_carrier as proposed  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers import check_graph_extended as graph  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers import check_schema_extended as schema  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers import check_structure_extended as structure  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers import support_authority as support  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.check_support import Check  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS  # noqa: E402


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


class CurrentRuleSourcesTests(unittest.TestCase):
    def setUp(self) -> None:
        scratch = TOOL.parents[3] / ".caprmedio_tmp/tests/current-rule-sources"
        scratch.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()

    def source(self, identifier: str, *, graph_rule: bool = False) -> Path:
        entry = proposed._entry(identifier, graph=graph_rule)
        matches = [
            path
            for path in (TOOL / "tests/fixtures").glob(f"*/{identifier}.md")
            if sha(path.read_bytes()) == entry["sha256"]
        ]
        self.assertTrue(matches)
        path: Path = self.root / entry["source_path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(matches[0].read_bytes())
        return path

    def revise(self, path: Path) -> int:
        raw = path.read_bytes()
        version = parse_carrier(raw, path).metadata["version"] + 1
        raw = re.sub(rb"(?m)^version: [0-9]+$", f"version: {version}".encode(), raw, count=1)
        raw = re.sub(rb"(?m)^  governs:.*$", b'  governs: "Current Rule.Scope"', raw, count=1)
        path.write_bytes(raw)
        return int(version)

    def load(
        self, identifier: str, *, graph_rule: bool = False
    ) -> tuple[dict[str, Any], ReadContext]:
        reader = ReadContext(roots=[str(self.root)], limits=dict(CEILINGS))
        report: dict[str, Any] = {"bindings": {}, "coverage": {"gaps": []}}
        row = proposed._source(self.root, identifier, reader, report, graph=graph_rule)
        return row, reader

    @staticmethod
    def check(rows: list[dict[str, Any]]) -> Check:
        return Check(
            authority.Obligation("test", [], True, "test"),
            authority.resolve_context([]),
            {"sources": rows},
        )

    def test_fresh_requests_observe_current_version_subjects_and_measured_hash_without_manifest_refresh(
        self,
    ) -> None:
        path = self.source("CA-D-276")
        historical = copy.deepcopy(proposed._entry("CA-D-276"))
        first, _ = self.load("CA-D-276")
        version = self.revise(path)
        current, reader = self.load("CA-D-276")
        self.assertEqual(version, current["binding"]["version"])
        self.assertEqual(sha(path.read_bytes()), current["binding"]["sha256"])
        self.assertEqual("Current Rule.Scope", current["metadata"]["subjects"]["governs"])
        self.assertNotEqual(first["binding"], current["binding"])
        self.assertEqual(historical, proposed._entry("CA-D-276"))
        proposed._current(reader)
        resolved = authority.resolve_context([current])
        obligation = next(
            row for row in resolved.obligations if row.code == "frontmatter.common_encoding"
        )
        self.assertTrue(obligation.supported)
        self.assertEqual([current["binding"]], obligation.authority)

    def test_schema_structure_graph_and_support_gates_use_observed_revision(self) -> None:
        for identifier, graph_rule in (
            ("CA-D-276", False),
            ("CA-D-268", True),
            ("CA-D-378", False),
        ):
            self.revise(self.source(identifier, graph_rule=graph_rule))
            row, _ = self.load(identifier, graph_rule=graph_rule)
            with self.subTest(identifier=identifier):
                self.assertTrue(authority._verified(row, proposed._entry(identifier)))
                if identifier == "CA-D-276":
                    self.assertIs(row, schema._source(self.check([row]), identifier, "test"))
                    self.assertTrue(structure._authority(self.check([row]), identifier))
                elif graph_rule:
                    self.assertTrue(graph._pins(self.check([row]), identifier))
                else:
                    self.assertIs(row, support.exact_source({"sources": [row]}, identifier))

    def test_observed_rule_drift_and_explicit_supplied_bindings_still_refuse(self) -> None:
        path = self.source("CA-D-276")
        original, reader = self.load("CA-D-276")
        self.revise(path)
        with self.assertRaises(proposed.ProposedCarrierError):
            proposed._current(reader)
        report: dict[str, Any] = {"bindings": {}, "coverage": {"gaps": []}}
        fresh = ReadContext(roots=[str(self.root)], limits=dict(CEILINGS))
        self.assertIsNone(context.load_source(path, original["binding"], fresh, report))
        self.assertTrue(report["coverage"]["gaps"])
        self.assertTrue(authority._verified(self.load("CA-D-276")[0], proposed._entry("CA-D-276")))

    def test_missing_malformed_wrong_identity_inactive_and_projected_rules_refuse(self) -> None:
        path = self.source("CA-D-276")
        raw = path.read_bytes()
        cases = (
            b"not a carrier",
            raw.replace(b"CA-D-276", b"CA-D-999999"),
            raw.replace(b'content_role: "Delivery"', b'content_role: "Method"'),
            re.sub(rb"(?m)^content_role:.*\n", b"", raw),
            raw.replace(b'status: "Active"', b'status: "Archived"'),
            re.sub(rb"(?m)^atom_id:.*\n", b"", raw),
            raw.replace(b"subjects:\n", b"projection: true\nsubjects:\n"),
            re.sub(rb"(?m)^version:.*$", b"version: true", raw),
        )
        for malformed in cases:
            with self.subTest(raw=malformed[:40]):
                path.write_bytes(malformed)
                with self.assertRaises(proposed.ProposedCarrierError):
                    self.load("CA-D-276")
        path.unlink()
        with self.assertRaises(proposed.ProposedCarrierError):
            self.load("CA-D-276")

    def test_duplicate_or_inconsistent_rule_records_cannot_supply_authority(self) -> None:
        self.source("CA-D-276")
        row, _ = self.load("CA-D-276")
        for rows in ([], [row, row]):
            self.assertIsNone(schema._source(self.check(rows), "CA-D-276", "test"))
            self.assertFalse(structure._authority(self.check(rows), "CA-D-276"))
        for field, value in (
            ("version", True),
            ("atom_id", "CA-D-999999"),
            ("status", "Draft"),
            ("content_role", "Method"),
            ("content_role", None),
        ):
            malformed = copy.deepcopy(row)
            malformed["metadata"][field] = value
            self.assertFalse(authority._verified(malformed, proposed._entry("CA-D-276")))
        malformed = copy.deepcopy(row)
        malformed["text"] += "\nchanged after capture\n"
        self.assertFalse(authority._verified(malformed, proposed._entry("CA-D-276")))

    def test_historical_manifest_revisions_do_not_override_or_conflict_with_same_locator(
        self,
    ) -> None:
        for other_path in ("rule.md", "different.md"):
            entries = [
                {"version": 1, "sha256": "old", "source_path": "rule.md"},
                {"version": 2, "sha256": "new", "source_path": other_path},
            ]
            documents = [json.dumps({"sources": {"CA-D-276": entry}}) for entry in entries]
            with (
                patch.object(support, "MANIFESTS", ("first.json", "second.json")),
                patch.object(Path, "is_file", return_value=True),
                patch.object(Path, "read_text", side_effect=documents),
            ):
                read = getattr(support.support_sources, "__wrapped__")
                if other_path == "rule.md":
                    self.assertEqual(entries[1], read()["CA-D-276"])
                else:
                    with self.assertRaises(ValueError):
                        read()


if __name__ == "__main__":
    unittest.main()
