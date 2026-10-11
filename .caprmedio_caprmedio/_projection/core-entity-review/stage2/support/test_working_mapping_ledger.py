"""Focused adversarial checks for the independent working-ledger verifier."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import tempfile
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("verify_working_mapping_ledger", HERE / "verify_working_mapping_ledger.py")
assert SPEC and SPEC.loader
verifier = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verifier)


class WorkingMappingLedgerVerifierTests(unittest.TestCase):
    def setUp(self) -> None:
        scratch = verifier.ROOT / ".caprmedio_tmp"
        scratch.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=scratch, prefix="working-ledger-verifier-", ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name)
        self.source_path = ".caprmedio_caprmedio/current-core/04_requirement/CA-R-1.md"
        path = self.root / self.source_path
        path.parent.mkdir(parents=True, exist_ok=True)
        self.raw = b"---\natom_id: CA-R-1\n---\n# Claim\nAtom has a status.\n"
        path.write_bytes(self.raw)
        self.source_sha = hashlib.sha256(self.raw).hexdigest()
        self.expected = {
            "occurrence_id": f"{self.source_path}#subjects.depends_on[0]",
            "source_path": self.source_path,
            "source_atom_id": "CA-R-1",
            "source_version": 1,
            "source_sha256": self.source_sha,
            "field": "depends_on",
            "index": 0,
            "old_value": "Atom",
            "quarantined": False,
        }

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _row(self, *, decision: str = "proposed", target: str | None = "Atom.Status", historical_sha: str | None = None) -> dict:
        historic_sha = historical_sha or self.source_sha
        row = {
            **copy.deepcopy(self.expected),
            "historical_origin": {
                **copy.deepcopy(self.expected),
                "source_sha256": historic_sha,
                "decision": decision,
                "proposed_value": target,
                "confidence": .95 if decision == "proposed" else .0,
            },
            "decision": decision,
            "proposed_value": target,
            "confidence": .95 if decision == "proposed" else .0,
            "reason": "Fixture keeps the occurrence accountable.",
            "evidence": [{
                "path": self.source_path,
                "sha256": self.source_sha,
                "start_line": 4,
                "end_line": 5,
                "span_sha256": hashlib.sha256(b"# Claim\nAtom has a status.\n").hexdigest(),
            }],
            "applied_layers": [{
                "layer": "baseline",
                "accepted": False,
                "decision": decision,
                "proposed_value": target,
            }],
            "executable": False,
        }
        if historic_sha != self.source_sha:
            row["replacement_lineage"] = {
                "historic_occurrence_id": self.expected["occurrence_id"],
                "current_occurrence_id": self.expected["occurrence_id"],
                "historic_source_sha256": historic_sha,
                "current_source_sha256": self.source_sha,
                "field": "depends_on",
                "index": 0,
                "old_value": "Atom",
            }
        return row

    def _baseline(self, row: dict) -> dict:
        return copy.deepcopy(row["historical_origin"])

    def _verify(self, rows: list[dict], layers: dict | None = None, actors: dict | None = None, grammar: dict | None = None, baseline: dict | None = None) -> dict:
        return verifier._verify_rows(
            self.root,
            rows,
            [self.expected],
            baseline if baseline is not None else {self.expected["occurrence_id"]: self._baseline(rows[0])} if rows else {},
            layers or {},
            actors or {},
            grammar or {},
        )

    def _rejects(self, rows: list[dict]) -> None:
        with self.assertRaises(verifier.VerificationError):
            self._verify(rows)

    def test_independent_row_accepts_literal_current_origin_and_span(self) -> None:
        self.assertEqual(self._verify([self._row()]), {"proposed": 1, "unchanged": 0, "unresolved": 0})

    def test_dropped_or_duplicated_occurrence_is_rejected(self) -> None:
        self._rejects([])
        self._rejects([self._row(), self._row()])

    def test_wrong_priority_or_target_is_rejected(self) -> None:
        wrong_priority = self._row()
        wrong_priority["applied_layers"] = [{
            "layer": "CA-P-2072", "priority": 99,
            "decision": "proposed", "proposed_value": "Atom.Status",
        }]
        with self.assertRaises(verifier.VerificationError):
            self._verify([wrong_priority], {"CA-P-2072": {self.expected["occurrence_id"]: ("proposed", "Atom.Status", .95)}})
        selector = self._row(target="Atom[@kind=Status]")
        selector["applied_layers"][0]["proposed_value"] = selector["proposed_value"]
        self._rejects([selector])

    def test_stale_current_pin_and_span_are_rejected(self) -> None:
        stale = self._row()
        stale["source_sha256"] = "b" * 64
        self._rejects([stale])
        stale_span = self._row()
        stale_span["evidence"][0]["span_sha256"] = "c" * 64
        self._rejects([stale_span])

    def test_changed_historic_pin_requires_lossless_replacement_lineage(self) -> None:
        changed = self._row(historical_sha="d" * 64)
        del changed["replacement_lineage"]
        self._rejects([changed])
        changed = self._row(historical_sha="d" * 64)
        changed["replacement_lineage"]["old_value"] = "Claim"
        self._rejects([changed])

    def test_unresolved_stays_explicit_and_non_executable(self) -> None:
        unresolved = self._row(decision="unresolved", target=None)
        unresolved["applied_layers"][0]["decision"] = "unresolved"
        unresolved["applied_layers"][0]["proposed_value"] = None
        unresolved["evidence"] = []
        self.assertEqual(self._verify([unresolved])["unresolved"], 1)
        unresolved["executable"] = True
        self._rejects([unresolved])

    def test_omitted_later_layer_is_rejected(self) -> None:
        row = self._row()
        with self.assertRaises(verifier.VerificationError):
            self._verify([row], {"CA-P-2072": {self.expected["occurrence_id"]: ("proposed", "Atom.Type", .95)}})

    def test_true_wrong_target_and_wrong_baseline_are_rejected(self) -> None:
        wrong_target = self._row()
        wrong_target["applied_layers"].append({
            "layer": "CA-P-2072", "priority": 2,
            "decision": "proposed", "proposed_value": "Atom.Type",
        })
        wrong_target["decision"] = "proposed"
        wrong_target["proposed_value"] = "Atom.Type"
        with self.assertRaises(verifier.VerificationError):
            self._verify([wrong_target], {"CA-P-2072": {self.expected["occurrence_id"]: ("proposed", "Atom.Status", .95)}})
        wrong_baseline = self._row()
        wrong_baseline["applied_layers"][0]["proposed_value"] = "Atom.Type"
        wrong_baseline["proposed_value"] = "Atom.Type"
        with self.assertRaises(verifier.VerificationError):
            self._verify([wrong_baseline])

    def test_actor_target_and_unaccepted_grammar_reset_are_required(self) -> None:
        actor = self._row()
        with self.assertRaises(verifier.VerificationError):
            self._verify([actor], actors={self.expected["occurrence_id"]: "Actor.Type: Operator"})
        grammar = self._row()
        with self.assertRaises(verifier.VerificationError):
            self._verify([grammar], grammar={"CA-R-1": {}})

    def test_missing_or_wrong_historical_counterpart_is_rejected(self) -> None:
        missing = self._row()
        baseline = {self.expected["occurrence_id"]: self._baseline(missing)}
        del missing["historical_origin"]
        with self.assertRaises(verifier.VerificationError):
            self._verify([missing], baseline=baseline)
        wrong = self._row()
        alternate = self._baseline(wrong)
        alternate["occurrence_id"] = alternate["occurrence_id"].replace("[0]", "[9]")
        alternate["index"] = 9
        alternate["old_value"] = "Different"
        wrong["historical_origin"] = copy.deepcopy(alternate)
        with self.assertRaises(verifier.VerificationError):
            self._verify([wrong], baseline={alternate["occurrence_id"]: alternate})


if __name__ == "__main__":
    unittest.main()
