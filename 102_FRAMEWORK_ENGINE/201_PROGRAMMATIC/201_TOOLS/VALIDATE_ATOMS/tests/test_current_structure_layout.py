"""Current D442 parent declarations replace authored structural depth explicitly."""

import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest

sys.path[:0] = [str(Path(__file__).resolve().parents[2]), str(Path(__file__).resolve().parents[1])]
from validate_atoms_workers.authority import AuthorityContext, Obligation  # noqa: E402
from validate_atoms_workers.check_structure_extended import _structure  # noqa: E402
from validate_atoms_workers.check_support import Check  # noqa: E402
from test_current_type_admission import source_row  # noqa: E402
from test_structure_extended import sources as historical_sources, unit  # noqa: E402


def current_sources():
    rows = json.loads((Path(__file__).parent / "fixtures/current_structure_authorities.json").read_text())
    return [source_row(row["text"], row["source_path"]) for row in rows]


def current_unit(name="CORE", parent="PROJECT"):
    return {"scope_unit_name": name, "parent": parent, "scope_unit_type": "Unordered",
            "scope_unit_label": "LAYER", "navigational_order_number": 1,
            "authority_path": ".caprmedio_example/" + name, "delivery_path": "src/" + name}


def checked(document, rows=None):
    rows = current_sources() if rows is None else rows
    context = AuthorityContext([row["binding"] for row in rows], 0, 0, 0, [], (), {}, False)
    check = Check(Obligation("target.resolution", [], True, "structure fixture"), context,
                  {"structure": document, "sources": rows})
    return _structure(check), check


class CurrentStructureLayoutTests(unittest.TestCase):
    def test_current_parentage_needs_no_authored_structural_level(self):
        document = {"schema_version": 1, "scope_units": [current_unit(), current_unit("CHILD", "CORE")]}
        before = copy.deepcopy(document)
        result, check = checked(document)
        self.assertEqual(set(result), {"CORE", "CHILD"})
        self.assertEqual(check.findings + check.gaps, [])
        self.assertEqual(document, before)
        self.assertEqual(checked({"schema_version": 1, "scope_units": []})[0], {})

    def test_current_rejects_retired_unknown_missing_and_misordered_fields(self):
        row = current_unit()
        malformed = [{**row, "structural_level": 1}, {**row, "node_id": "node"},
                     {key: value for key, value in row.items() if key != "parent"},
                     dict(reversed(list(row.items()))), {**row, "navigational_order_number": True},
                     {**row, "local_order": 1}, {**row, "authority_mode": "unknown"}]
        for value in malformed:
            with self.subTest(value=value):
                result, check = checked({"schema_version": 1, "scope_units": [value]})
                self.assertIsNone(result)
                self.assertTrue(check.gaps)

    def test_current_rejects_invalid_parentage_paths_and_document_keys(self):
        malformed = [
            {"schema_version": 1, "scope_units": [current_unit(), current_unit()]},
            {"schema_version": 1, "scope_units": [current_unit(parent="MISSING")]},
            {"schema_version": 1, "scope_units": [current_unit(parent="CORE")]},
            {"schema_version": 1, "scope_units": [current_unit("PROJECT")]},
            {"schema_version": True, "scope_units": []},
            {"schema_version": 1, "scope_units": [], "unknown": 1},
        ]
        for path in ("../escape", "/absolute", "C:/absolute", "folder\\escape"):
            malformed.append({"schema_version": 1, "scope_units": [{**current_unit(), "authority_path": path}]})
        for document in malformed:
            with self.subTest(document=document):
                self.assertIsNone(checked(document)[0])

    def test_historical_fixture_keeps_its_explicit_authored_depth_contract(self):
        old = {"schema_version": 1, "scope_units": [unit()]}
        self.assertIsNotNone(checked(old, historical_sources())[0])
        self.assertIsNone(checked(old)[0])
        self.assertIsNone(checked({"schema_version": 1, "scope_units": [current_unit()]}, historical_sources())[0])

    def test_unknown_or_changed_claim_is_a_gap_and_version_never_selects_layout(self):
        rows = current_sources()
        unknown = copy.deepcopy(rows)
        authority = next(row for row in unknown if row["binding"]["atom_id"] == "CA-D-442")
        authority["text"] += "\nA new mandatory field is required.\n"
        authority["binding"]["sha256"] = hashlib.sha256(authority["text"].encode()).hexdigest()
        self.assertIsNone(checked({"schema_version": 1, "scope_units": []}, unknown)[0])
        stale = copy.deepcopy(rows)
        stale[-1]["text"] += "\nChanged bytes.\n"
        self.assertIsNone(checked({"schema_version": 1, "scope_units": []}, stale)[0])
        revised = copy.deepcopy(rows)
        authority = next(row for row in revised if row["binding"]["atom_id"] == "CA-D-442")
        text = authority["text"].replace("version: 23", "version: 24")
        revised[revised.index(authority)] = source_row(text, authority["binding"]["path"])
        self.assertIsNotNone(checked({"schema_version": 1, "scope_units": []}, revised)[0])


if __name__ == "__main__":
    unittest.main()
