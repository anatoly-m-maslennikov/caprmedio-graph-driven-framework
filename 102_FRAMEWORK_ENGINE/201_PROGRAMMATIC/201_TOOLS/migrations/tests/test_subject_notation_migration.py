"""Focused tests for the sealed, dry-run Subject-notation planner."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "subject_notation_migration.py"
SPEC = importlib.util.spec_from_file_location("subject_notation_migration_under_test", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
MIGRATION = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MIGRATION)


class SubjectNotationMigrationTests(unittest.TestCase):
    def _carrier(self, root: Path, *, atom_id: str = "CA-R-001", subjects: str | None = None,
                 eol: str = "\n") -> tuple[str, bytes, dict]:
        if subjects is None:
            subjects = (
                '  governs: "Atom/Property"\n'
                '  depends_on: ["Atom/Scope", "Entity/Type"]\n'
            )
        text = (
            "---\n"
            f"atom_id: {atom_id}\n"
            "content_role: Requirement\n"
            "type: Requirement\n"
            "subjects:\n"
            f"{subjects}"
            "version: 2\n"
            'updated_at: "2026-10-09 10:00:00 +0400"\n'
            "---\n"
            "# Summary\n"
            "\n"
            "The source body remains byte-for-byte unchanged by a dry run.\n"
        )
        if eol == "\r\n":
            text = text.replace("\n", "\r\n")
        raw = text.encode("utf-8")
        relative = f".caprmedio_caprmedio/fixtures/{atom_id}.md"
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        return relative, raw, {
            "atom_id": atom_id,
            "atom_revision": 2,
            "carrier_path": relative,
            "carrier_sha256": hashlib.sha256(raw).hexdigest(),
            "content_role": "Requirement",
            "type": "Requirement",
            "status": "active",
        }

    def _inventory(self, root: Path, *, carriers: list[tuple[str, bytes, dict]],
                   case_specs: list[tuple[str, str, str, int]],
                   sort_pins: bool = True, sort_cases: bool = True) -> dict:
        pins = [copy.deepcopy(carrier[2]) for carrier in carriers]
        if sort_pins:
            pins.sort(key=lambda item: item["carrier_path"])
        case_rows = []
        for case_id, parent, child, carrier_index in case_specs:
            relative, raw, pin = carriers[carrier_index]
            tokens, _ = MIGRATION._subject_tokens(raw, relative)
            token = next(item for item in tokens if item["value"] == child)
            contribution = {
                "kind": "canonical_atom_property",
                "property_path": token["property_path"],
                "start_line": token["line"],
                "end_line": token["line"],
                "text_sha256": MIGRATION._line_span_digest(raw, token["line"], token["line"]),
            }
            source_ref = {key: pin[key] for key in ("atom_id", "atom_revision", "carrier_path", "carrier_sha256")}
            source_ref["contribution"] = contribution
            case_rows.append({
                "case_id": case_id,
                "old_parent": parent,
                "old_child": child,
                "child_term": child.rsplit("/", 1)[-1],
                "root_term": parent.split("/", 1)[0],
                "bucket": 1,
                "occurrences": [{"role": "GOVERNS" if token["property_path"].endswith("governs") else "DEPENDS_ON",
                                  "source_ref": source_ref, "subject_path": child}],
                "content_source_candidates": [pin["atom_id"]],
            })
        if sort_cases:
            case_rows.sort(key=lambda item: item["case_id"])
        frontier_pins = [copy.deepcopy(carrier[2]) for carrier in carriers]
        frontier_pins.sort(key=lambda item: item["carrier_path"])
        frontier_digest_pins = [
            {key: pin[key] for key in ("atom_id", "atom_revision", "carrier_path", "carrier_sha256")}
            for pin in frontier_pins
        ]
        data = {
            "kind": "subject_notation_migration_analysis_inventory",
            "selection": {"atom_ids": sorted(pin["atom_id"] for pin in pins), "scope_unit_names": []},
            "source_frontier": {
                "selected_folder": ".caprmedio_caprmedio/fixtures",
                "carriers": frontier_pins,
                "source_frontier_sha256": MIGRATION.canonical_digest(frontier_digest_pins),
            },
            "collection_sha256": "0" * 64,
            "source_pins": pins,
            "grammar_pins": [],
            "cases": case_rows,
            "native_fact_admission": "not_performed",
            "source_mutation": False,
        }
        data["inventory_sha256"] = MIGRATION.canonical_digest(data)
        return data

    def _case_id(self, parent: str, child: str) -> str:
        return "slash:" + MIGRATION.canonical_digest({"parent": parent, "child": child})

    def _decision(self, case: dict, *, separator: str = ".", confidence_percent: int = 95,
                  source_refs: list[dict] | None = None, disposition: str = "accepted") -> dict:
        return {
            "case_id": case["case_id"],
            "new_separator": separator,
            "confidence_percent": confidence_percent,
            "source_refs": copy.deepcopy(source_refs if source_refs is not None else [case["occurrences"][0]["source_ref"]]),
            "disposition": disposition,
        }

    @contextmanager
    def _fixture(self, *, two_carriers: bool = False, eol: str = "\n", collision: bool = False):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            carriers = [self._carrier(root, eol=eol)]
            if two_carriers:
                carriers[0] = self._carrier(root, subjects='  governs: "Atom/Property"\n', eol=eol)
                carriers.append(self._carrier(root, atom_id="CA-R-002", subjects='  governs: "Entity/Type"\n', eol=eol))
            specs = [
                (self._case_id("Atom", "Atom/Property"), "Atom", "Atom/Property", 0),
                (self._case_id("Atom", "Atom/Scope"), "Atom", "Atom/Scope", 0),
                (self._case_id("Entity", "Entity/Type"), "Entity", "Entity/Type", 0),
            ]
            if two_carriers:
                specs = [specs[0], (self._case_id("Entity", "Entity/Type"), "Entity", "Entity/Type", 1)]
            if collision:
                relative, raw, pin = carriers[0]
                raw = (raw.replace(b'"Atom/Property"', b'"Other"', 1)
                       .replace(b'"Atom/Scope"', b'"Atom/Property"')
                       .replace(b'"Entity/Type"', b'"Atom.Property"'))
                # The pinned carrier must describe the collision source itself.
                (root / relative).write_bytes(raw)
                pin["carrier_sha256"] = hashlib.sha256(raw).hexdigest()
                carriers[0] = (relative, raw, pin)
                specs = [specs[0]]
            inventory = self._inventory(root, carriers=carriers, case_specs=specs)
            decisions = [self._decision(case) for case in inventory["cases"]]
            yield root, carriers, inventory, decisions

    def test_valid_small_fixture_emits_only_subject_patches_and_preserves_metadata(self) -> None:
        with self._fixture(eol="\r\n") as (root, carriers, inventory, decisions):
            result = MIGRATION.build_changeset(root, inventory, decisions,
                                               inventory_file_sha256="a" * 64)
            self.assertEqual("ready_for_governed_apply", result["global_status"])
            self.assertFalse(result["apply_supported"])
            self.assertEqual(1, len(result["candidate_changes"]))
            change = result["candidate_changes"][0]
            self.assertEqual(["subjects"], change["changed_fields"])
            self.assertEqual(
                {key: inventory["source_pins"][0][key] for key in change["source_pin"]},
                change["source_pin"],
            )
            self.assertIn("updated_at", change)
            self.assertNotIn("candidate_bytes", change)
            self.assertTrue(all(patch["property_path"].startswith("subjects.") for patch in change["patches"]))
            self.assertEqual(0, len(result["diagnostics"]))
            raw = carriers[0][1]
            candidate = raw
            for patch in reversed(change["patches"]):
                start, end = patch["start"], patch["end"]
                candidate = candidate[:start] + patch["new"].encode() + candidate[end:]
            self.assertIn(b"\r\n", candidate)
            self.assertIn(b'governs: "Atom.Property"', candidate)
            self.assertIn(b'depends_on: ["Atom.Scope", "Entity.Type"]', candidate)
            self.assertEqual(raw[change["patches"][0]["start"] - 1:change["patches"][0]["start"]], b'"')
            self.assertEqual(raw[raw.index(b"# Summary"):], candidate[candidate.index(b"# Summary"):])
            self.assertEqual(change["candidate_sha256"], hashlib.sha256(candidate).hexdigest())

    def test_missing_case_blocks_global_apply_but_keeps_unaffected_partial_candidate(self) -> None:
        with self._fixture(two_carriers=True) as (root, carriers, inventory, decisions):
            result = MIGRATION.build_changeset(root, inventory, decisions[:1])
            self.assertEqual("blocked", result["global_status"])
            self.assertIn("missing-cases", result["blocked_reasons"])
            self.assertIn(inventory["cases"][1]["case_id"], result["missing_case_ids"])
            self.assertEqual(1, len(result["candidate_changes"]))
            self.assertNotIn(carriers[0][0], result["affected_paths"])
            self.assertIn(carriers[1][0], result["affected_paths"])

    def test_decision_boundary_rejects_duplicate_unknown_and_non_integer_confidence(self) -> None:
        with self._fixture() as (root, carriers, inventory, decisions):
            duplicate = decisions + [copy.deepcopy(decisions[0])]
            with self.assertRaises(MIGRATION.SubjectNotationMigrationError) as raised:
                MIGRATION.build_changeset(root, inventory, duplicate)
            self.assertEqual("decision-duplicate-case", raised.exception.code)
            unknown = copy.deepcopy(decisions[0])
            unknown["case_id"] = "slash:unknown"
            with self.assertRaises(MIGRATION.SubjectNotationMigrationError) as raised:
                MIGRATION.build_changeset(root, inventory, [unknown])
            self.assertEqual("decision-unknown-case", raised.exception.code)
            fractional = copy.deepcopy(decisions[0])
            fractional["confidence_percent"] = 0.95
            with self.assertRaises(MIGRATION.SubjectNotationMigrationError) as raised:
                MIGRATION.build_changeset(root, inventory, [fractional])
            self.assertEqual("decision-confidence-invalid", raised.exception.code)
            old_shape = copy.deepcopy(decisions[0])
            del old_shape["confidence_percent"]
            old_shape["confidence"] = 0.95
            with self.assertRaises(MIGRATION.SubjectNotationMigrationError) as raised:
                MIGRATION.build_changeset(root, inventory, [old_shape])
            self.assertEqual("decision-shape-invalid", raised.exception.code)

    def test_low_confidence_and_zero_op_are_truthfully_blocked(self) -> None:
        with self._fixture() as (root, carriers, inventory, decisions):
            low = copy.deepcopy(decisions)
            low[0]["confidence_percent"] = 89
            with self.assertRaises(MIGRATION.SubjectNotationMigrationError) as raised:
                MIGRATION.build_changeset(root, inventory, low)
            self.assertEqual("decision-confidence-below-threshold", raised.exception.code)
            no_op = [self._decision(case, separator="/") for case in inventory["cases"]]
            result = MIGRATION.build_changeset(root, inventory, no_op)
            self.assertEqual("blocked", result["global_status"])
            self.assertIn("zero-ops", result["blocked_reasons"])
            self.assertEqual([], result["candidate_changes"])

    def test_changed_source_and_forged_reference_never_produce_candidate(self) -> None:
        with self._fixture() as (root, carriers, inventory, decisions):
            path = root / carriers[0][0]
            path.write_bytes(path.read_bytes().replace(b"source body", b"changed body"))
            result = MIGRATION.build_changeset(root, inventory, decisions)
            self.assertEqual("blocked", result["global_status"])
            self.assertIn("source-frontier-changed", result["blocked_reasons"])
            self.assertEqual([], result["candidate_changes"])
        with self._fixture() as (root, carriers, inventory, decisions):
            forged = copy.deepcopy(decisions)
            forged[0]["source_refs"][0]["carrier_sha256"] = "f" * 64
            result = MIGRATION.build_changeset(root, inventory, forged)
            self.assertEqual("blocked", result["global_status"])
            self.assertIn(inventory["cases"][0]["case_id"], result["blocked_case_ids"])
            self.assertEqual([], result["candidate_changes"])

    def test_collision_is_a_blocked_subject_target_collision(self) -> None:
        with self._fixture(collision=True) as (root, carriers, inventory, decisions):
            result = MIGRATION.build_changeset(root, inventory, decisions)
            self.assertEqual("blocked", result["global_status"])
            self.assertTrue(any(item["code"] == "subject-target-collision" for item in result["diagnostics"]))
            self.assertEqual([], result["candidate_changes"])

    def test_inventory_order_and_source_digest_are_sealed(self) -> None:
        with self._fixture(two_carriers=True) as (root, carriers, inventory, decisions):
            wrong_order = copy.deepcopy(inventory)
            wrong_order["source_pins"] = list(reversed(wrong_order["source_pins"]))
            wrong_order["inventory_sha256"] = MIGRATION.canonical_digest({k: v for k, v in wrong_order.items() if k != "inventory_sha256"})
            with self.assertRaises(MIGRATION.SubjectNotationMigrationError) as raised:
                MIGRATION.build_changeset(root, wrong_order, decisions)
            self.assertEqual("inventory-pins-unsorted", raised.exception.code)
            forged = copy.deepcopy(inventory)
            forged["inventory_sha256"] = "0" * 64
            with self.assertRaises(MIGRATION.SubjectNotationMigrationError) as raised:
                MIGRATION.build_changeset(root, forged, decisions)
            self.assertEqual("inventory-digest-mismatch", raised.exception.code)


if __name__ == "__main__":
    unittest.main()
