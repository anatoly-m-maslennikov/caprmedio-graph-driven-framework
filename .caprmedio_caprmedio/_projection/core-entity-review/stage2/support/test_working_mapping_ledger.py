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

    def _verify(self, rows: list[dict], layers: dict | None = None, actors: dict | None = None, grammar: dict | None = None, accepted_grammar: dict | None = None, baseline: dict | None = None, layer_refs: dict | None = None) -> dict:
        layer_refs = layer_refs if layer_refs is not None else {
            task: {
                "report": {"path": f"{task}.report.json", "sha256": "a" * 64},
                "receipt": {"path": f"{task}.receipt.json", "sha256": "a" * 64},
            }
            for task in (layers or {})
        }
        if accepted_grammar is not None:
            layer_refs.setdefault("CA-P-2087", {
                "report": {"path": "grammar.report.json", "sha256": "a" * 64},
                "receipt": {"path": "grammar.receipt.json", "sha256": "a" * 64},
            })
        return verifier._verify_rows(
            self.root,
            rows,
            [self.expected],
            baseline if baseline is not None else {self.expected["occurrence_id"]: self._baseline(rows[0])} if rows else {},
            layers or {},
            actors or {},
            grammar or {},
            accepted_grammar,
            layer_refs,
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
        references = {
            "CA-P-2072": {
                "report": {"path": "task-2072.review.json", "sha256": "a" * 64},
                "receipt": {"path": "task-2072.receipt.json", "sha256": "a" * 64},
            }
        }
        valid_target = self._row()
        valid_target["applied_layers"].append({
            "layer": "CA-P-2072", "priority": 2,
            **references["CA-P-2072"],
            "decision": "proposed", "proposed_value": "Atom.Status",
        })
        layers = {"CA-P-2072": {self.expected["occurrence_id"]: ("proposed", "Atom.Status", .95)}}
        self.assertEqual(self._verify([valid_target], layers, layer_refs=references)["proposed"], 1)
        wrong_target = copy.deepcopy(valid_target)
        wrong_target["applied_layers"][-1]["proposed_value"] = "Atom.Type"
        with self.assertRaises(verifier.VerificationError):
            self._verify([wrong_target], layers, layer_refs=references)
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

    def test_accepted_grammar_layer_is_required_and_exact(self) -> None:
        accepted = {self.expected["occurrence_id"]: ("proposed", "Atom.Status", .95)}
        missing = self._row()
        with self.assertRaises(verifier.VerificationError):
            self._verify([missing], grammar={"CA-R-1": {}}, accepted_grammar=accepted)
        references = {
            "CA-P-2087": {
                "report": {"path": "grammar.report.json", "sha256": "a" * 64},
                "receipt": {"path": "grammar.receipt.json", "sha256": "a" * 64},
            }
        }
        valid = self._row()
        valid["applied_layers"].append({
            "layer": "CA-P-2087", "priority": "current_grammar",
            "status": "independently_accepted_current_grammar",
            **references["CA-P-2087"],
            "decision": "proposed", "proposed_value": "Atom.Status", "confidence": .95,
        })
        self.assertEqual(self._verify([valid], grammar={"CA-R-1": {}}, accepted_grammar=accepted, layer_refs=references)["proposed"], 1)
        wrong = copy.deepcopy(valid)
        wrong["applied_layers"][-1]["proposed_value"] = "Atom.Type"
        with self.assertRaises(verifier.VerificationError):
            self._verify([wrong], grammar={"CA-R-1": {}}, accepted_grammar=accepted, layer_refs=references)

    def test_accepted_grammar_status_and_recorded_confidence_are_required(self) -> None:
        accepted = {self.expected["occurrence_id"]: ("proposed", "Atom.Status", .95)}
        references = {
            "CA-P-2087": {
                "report": {"path": "grammar.report.json", "sha256": "a" * 64},
                "receipt": {"path": "grammar.receipt.json", "sha256": "a" * 64},
            }
        }
        row = self._row()
        row["applied_layers"].append({
            "layer": "CA-P-2087", "priority": "current_grammar",
            "status": "independently_accepted_current_grammar",
            **references["CA-P-2087"],
            "decision": "proposed", "proposed_value": "Atom.Status", "confidence": .94,
        })
        with self.assertRaises(verifier.VerificationError):
            self._verify([row], grammar={"CA-R-1": {}}, accepted_grammar=accepted, layer_refs=references)
        row["applied_layers"][-1]["confidence"] = .95
        row["applied_layers"][-1]["status"] = "accepted"
        with self.assertRaises(verifier.VerificationError):
            self._verify([row], grammar={"CA-R-1": {}}, accepted_grammar=accepted, layer_refs=references)

    def test_stale_per_row_report_descriptor_is_rejected(self) -> None:
        row = self._row()
        report = {"path": "task-2072.review.json", "sha256": "a" * 64}
        receipt = {"path": "task-2072.receipt.json", "sha256": "a" * 64}
        row["applied_layers"].append({
            "layer": "CA-P-2072", "priority": 2,
            "report": {**report, "sha256": "b" * 64},
            "receipt": receipt,
            "decision": "proposed", "proposed_value": "Atom.Status",
        })
        layers = {"CA-P-2072": {self.expected["occurrence_id"]: ("proposed", "Atom.Status", .95)}}
        with self.assertRaises(verifier.VerificationError):
            self._verify([row], layers, layer_refs={"CA-P-2072": {"report": report, "receipt": receipt}})

    def test_present_grammar_receipt_requires_manifest(self) -> None:
        ledger = {"input_pins": {"accepted_layers": [{} for _ in range(len(verifier.LAYER_SPECS) + 1)]}}
        self.assertIsNone(verifier._read_accepted_grammar_rows(self.root, ledger, [], {}))
        receipt = self.root / verifier.GRAMMAR_RECEIPT_REL
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text("{}\n")
        with self.assertRaises(verifier.VerificationError):
            verifier._read_accepted_grammar_rows(self.root, ledger, [], {})

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

    def test_followup_reports_have_exact_live_selection_and_acceptance(self) -> None:
        """The six prospective layers are independently live-checked before replacement."""

        current_ledger = verifier.read_json(verifier.ROOT / verifier.LEDGER_REL, "current working ledger")
        baseline = verifier._read_baseline_rows(verifier.ROOT, current_ledger)
        expected = verifier.enumerate_current_frontier(verifier.ROOT)["occurrences"]
        accepted = [{} for _task, _kind in verifier.LAYER_SPECS]
        for task, _kind, rows, _proposed, _unresolved, report_sha in verifier.FOLLOWUP_LAYER_SPECS:
            report_rel = verifier._layer_path(task)
            receipt_rel = verifier.STAGE2_REL / f"task-{task.removeprefix('CA-P-')}.receipt.json"
            accepted.append({
                "task": task,
                "kind": "research",
                "priority": verifier.ORDINARY_LAYER_PRIORITY[task],
                "rows": rows,
                "report": verifier._descriptor(verifier.ROOT / report_rel, report_rel),
                "receipt": verifier._descriptor(verifier.ROOT / receipt_rel, receipt_rel),
                "independent_review_sha256": report_sha,
            })
        accepted.append({})
        accepted.append({})
        layers, references = verifier._read_followup_layer_rows(
            verifier.ROOT,
            {"input_pins": {"accepted_layers": accepted}},
            expected,
            baseline,
        )
        self.assertEqual(list(layers), [item[0] for item in verifier.FOLLOWUP_LAYER_SPECS])
        self.assertEqual(sum(len(rows) for rows in layers.values()), 180)
        self.assertEqual(sum(decision == "proposed" for rows in layers.values() for decision, _target, _confidence in rows.values()), 80)
        self.assertEqual(sum(decision == "unresolved" for rows in layers.values() for decision, _target, _confidence in rows.values()), 100)
        self.assertTrue(all(reference["independent_review_sha256"] == reference["report"]["sha256"] for reference in references.values()))

    def test_followup_layer_requires_exact_provenance_target_and_current_origin(self) -> None:
        references = {
            "CA-P-2094": {
                "report": {"path": "task-2094.research.json", "sha256": "a" * 64},
                "receipt": {"path": "task-2094.receipt.json", "sha256": "b" * 64},
                "independent_review_sha256": "c" * 64,
            }
        }
        layers = {"CA-P-2094": {self.expected["occurrence_id"]: ("proposed", "Atom.Status", .95)}}
        valid = self._row()
        valid["applied_layers"].append({
            "layer": "CA-P-2094",
            "priority": 14,
            **references["CA-P-2094"],
            "decision": "proposed",
            "proposed_value": "Atom.Status",
            "confidence": .95,
        })
        self.assertEqual(self._verify([valid], layers, layer_refs=references)["proposed"], 1)
        with self.assertRaises(verifier.VerificationError):
            self._verify([self._row()], layers, layer_refs=references)
        wrong_target = copy.deepcopy(valid)
        wrong_target["applied_layers"][-1]["proposed_value"] = "Atom.Type"
        with self.assertRaises(verifier.VerificationError):
            self._verify([wrong_target], layers, layer_refs=references)
        stale_acceptance_pin = copy.deepcopy(valid)
        stale_acceptance_pin["applied_layers"][-1]["report"] = {**references["CA-P-2094"]["report"], "sha256": "d" * 64}
        with self.assertRaises(verifier.VerificationError):
            self._verify([stale_acceptance_pin], layers, layer_refs=references)
        stale_origin = copy.deepcopy(valid)
        stale_origin["source_sha256"] = "e" * 64
        with self.assertRaises(verifier.VerificationError):
            self._verify([stale_origin], layers, layer_refs=references)
        extra_origin = copy.deepcopy(valid)
        extra_origin["occurrence_id"] = f"{self.source_path}#subjects.depends_on[1]"
        with self.assertRaises(verifier.VerificationError):
            self._verify([extra_origin], layers, layer_refs=references)

    def test_followup_manifest_cannot_admit_a_partial_extension(self) -> None:
        partial = {"input_pins": {"accepted_layers": [{} for _ in range(len(verifier.LAYER_SPECS) + 3)]}}
        with self.assertRaises(verifier.VerificationError):
            verifier._layer_layout(partial)
        complete = {"input_pins": {"accepted_layers": [{} for _ in range(len(verifier.LAYER_SPECS) + len(verifier.FOLLOWUP_LAYER_SPECS) + 2)]}}
        specs, actor_position, grammar_position = verifier._layer_layout(complete)
        self.assertEqual([item[0] for item in specs][-6:], [item[0] for item in verifier.FOLLOWUP_LAYER_SPECS])
        self.assertEqual(actor_position, len(verifier.LAYER_SPECS) + len(verifier.FOLLOWUP_LAYER_SPECS))
        self.assertEqual(grammar_position, len(complete["input_pins"]["accepted_layers"]) - 1)
        second_complete = {"input_pins": {"accepted_layers": [{} for _ in range(len(verifier.LAYER_SPECS) + len(verifier.FOLLOWUP_LAYER_SPECS) + len(verifier.SECOND_FOLLOWUP_LAYER_SPECS) + 2)]}}
        specs, actor_position, grammar_position = verifier._layer_layout(second_complete)
        self.assertEqual([item[0] for item in specs][-6:], [item[0] for item in verifier.SECOND_FOLLOWUP_LAYER_SPECS])
        self.assertEqual([item[3] for item in specs][-6:], [20, 21, 22, 23, 24, 25])
        self.assertEqual(actor_position, len(verifier.LAYER_SPECS) + len(verifier.FOLLOWUP_LAYER_SPECS) + len(verifier.SECOND_FOLLOWUP_LAYER_SPECS))
        self.assertEqual(grammar_position, len(second_complete["input_pins"]["accepted_layers"]) - 1)
        third_complete = {"input_pins": {"accepted_layers": [{} for _ in range(len(verifier.LAYER_SPECS) + len(verifier.FOLLOWUP_LAYER_SPECS) + len(verifier.SECOND_FOLLOWUP_LAYER_SPECS) + len(verifier.THIRD_FOLLOWUP_LAYER_SPECS) + 2)]}}
        specs, actor_position, grammar_position = verifier._layer_layout(third_complete)
        self.assertEqual([item[0] for item in specs][-6:], [item[0] for item in verifier.THIRD_FOLLOWUP_LAYER_SPECS])
        self.assertEqual([item[3] for item in specs][-6:], [26, 27, 28, 29, 30, 31])
        self.assertEqual(actor_position, len(verifier.LAYER_SPECS) + len(verifier.FOLLOWUP_LAYER_SPECS) + len(verifier.SECOND_FOLLOWUP_LAYER_SPECS) + len(verifier.THIRD_FOLLOWUP_LAYER_SPECS))
        self.assertEqual(grammar_position, len(third_complete["input_pins"]["accepted_layers"]) - 1)
        fourth_complete = {"input_pins": {"accepted_layers": [{} for _ in range(len(verifier.LAYER_SPECS) + len(verifier.FOLLOWUP_LAYER_SPECS) + len(verifier.SECOND_FOLLOWUP_LAYER_SPECS) + len(verifier.THIRD_FOLLOWUP_LAYER_SPECS) + len(verifier.FOURTH_FOLLOWUP_LAYER_SPECS) + 2)]}}
        specs, actor_position, grammar_position = verifier._layer_layout(fourth_complete)
        self.assertEqual([item[0] for item in specs][-8:], [item[0] for item in verifier.FOURTH_FOLLOWUP_LAYER_SPECS])
        self.assertEqual([item[3] for item in specs][-8:], [32, 33, 34, 35, 36, 37, 38, 39])
        self.assertEqual(actor_position, len(verifier.LAYER_SPECS) + len(verifier.FOLLOWUP_LAYER_SPECS) + len(verifier.SECOND_FOLLOWUP_LAYER_SPECS) + len(verifier.THIRD_FOLLOWUP_LAYER_SPECS) + len(verifier.FOURTH_FOLLOWUP_LAYER_SPECS))
        self.assertEqual(grammar_position, len(fourth_complete["input_pins"]["accepted_layers"]) - 1)
        fifth_complete = {"input_pins": {"accepted_layers": [{} for _ in range(len(verifier.LAYER_SPECS) + len(verifier.FOLLOWUP_LAYER_SPECS) + len(verifier.SECOND_FOLLOWUP_LAYER_SPECS) + len(verifier.THIRD_FOLLOWUP_LAYER_SPECS) + len(verifier.FOURTH_FOLLOWUP_LAYER_SPECS) + len(verifier.FIFTH_FOLLOWUP_LAYER_SPECS) + 2)]}}
        specs, actor_position, grammar_position = verifier._layer_layout(fifth_complete)
        self.assertEqual([item[0] for item in specs][-8:], [item[0] for item in verifier.FIFTH_FOLLOWUP_LAYER_SPECS])
        self.assertEqual([item[3] for item in specs][-8:], [40, 41, 42, 43, 44, 45, 46, 47])
        self.assertEqual(actor_position, len(verifier.LAYER_SPECS) + len(verifier.FOLLOWUP_LAYER_SPECS) + len(verifier.SECOND_FOLLOWUP_LAYER_SPECS) + len(verifier.THIRD_FOLLOWUP_LAYER_SPECS) + len(verifier.FOURTH_FOLLOWUP_LAYER_SPECS) + len(verifier.FIFTH_FOLLOWUP_LAYER_SPECS))
        self.assertEqual(grammar_position, len(fifth_complete["input_pins"]["accepted_layers"]) - 1)

    def test_live_followup_receipt_requires_complete_extension(self) -> None:
        old_layout = {"input_pins": {"accepted_layers": [{} for _ in range(len(verifier.LAYER_SPECS) + 2)]}}
        verifier._require_followup_extension_when_receipts_exist(self.root, old_layout)
        receipt = self.root / verifier.STAGE2_REL / "task-2094.receipt.json"
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text("{}\n")
        with self.assertRaises(verifier.VerificationError):
            verifier._require_followup_extension_when_receipts_exist(self.root, old_layout)

    def test_live_second_followup_receipt_requires_complete_extension(self) -> None:
        first_layout = {"input_pins": {"accepted_layers": [{} for _ in range(len(verifier.LAYER_SPECS) + len(verifier.FOLLOWUP_LAYER_SPECS) + 2)]}}
        verifier._require_followup_extension_when_receipts_exist(self.root, first_layout)
        receipt = self.root / verifier.STAGE2_REL / "task-2103.receipt.json"
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text("{}\n")
        with self.assertRaises(verifier.VerificationError):
            verifier._require_followup_extension_when_receipts_exist(self.root, first_layout)

    def test_live_third_followup_receipt_requires_complete_extension(self) -> None:
        second_layout = {"input_pins": {"accepted_layers": [{} for _ in range(len(verifier.LAYER_SPECS) + len(verifier.FOLLOWUP_LAYER_SPECS) + len(verifier.SECOND_FOLLOWUP_LAYER_SPECS) + 2)]}}
        verifier._require_followup_extension_when_receipts_exist(self.root, second_layout)
        receipt = self.root / verifier.STAGE2_REL / "task-2112.receipt.json"
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text("{}\n")
        with self.assertRaises(verifier.VerificationError):
            verifier._require_followup_extension_when_receipts_exist(self.root, second_layout)

    def test_live_fourth_followup_receipt_requires_complete_extension(self) -> None:
        third_layout = {"input_pins": {"accepted_layers": [{} for _ in range(len(verifier.LAYER_SPECS) + len(verifier.FOLLOWUP_LAYER_SPECS) + len(verifier.SECOND_FOLLOWUP_LAYER_SPECS) + len(verifier.THIRD_FOLLOWUP_LAYER_SPECS) + 2)]}}
        verifier._require_followup_extension_when_receipts_exist(self.root, third_layout)
        receipt = self.root / verifier.STAGE2_REL / "task-2121.receipt.json"
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text("{}\n")
        with self.assertRaises(verifier.VerificationError):
            verifier._require_followup_extension_when_receipts_exist(self.root, third_layout)

    def test_live_fifth_followup_receipt_requires_complete_extension(self) -> None:
        fourth_layout = {"input_pins": {"accepted_layers": [{} for _ in range(len(verifier.LAYER_SPECS) + len(verifier.FOLLOWUP_LAYER_SPECS) + len(verifier.SECOND_FOLLOWUP_LAYER_SPECS) + len(verifier.THIRD_FOLLOWUP_LAYER_SPECS) + len(verifier.FOURTH_FOLLOWUP_LAYER_SPECS) + 2)]}}
        verifier._require_followup_extension_when_receipts_exist(self.root, fourth_layout)
        receipt = self.root / verifier.STAGE2_REL / "task-2132.receipt.json"
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text("{}\n")
        with self.assertRaises(verifier.VerificationError):
            verifier._require_followup_extension_when_receipts_exist(self.root, fourth_layout)

    def test_second_followup_reports_are_exact_and_per_row_provenance_is_fail_closed(self) -> None:
        current_ledger = verifier.read_json(verifier.ROOT / verifier.LEDGER_REL, "current working ledger")
        baseline = verifier._read_baseline_rows(verifier.ROOT, current_ledger)
        expected = verifier.enumerate_current_frontier(verifier.ROOT)["occurrences"]
        accepted = [{} for _task, _kind in verifier.LAYER_SPECS]
        for specs in (verifier.FOLLOWUP_LAYER_SPECS, verifier.SECOND_FOLLOWUP_LAYER_SPECS):
            for task, _kind, rows, _proposed, _unresolved, report_sha in specs:
                report_rel = verifier._layer_path(task)
                receipt_rel = verifier.STAGE2_REL / f"task-{task.removeprefix('CA-P-')}.receipt.json"
                accepted.append({
                    "task": task,
                    "kind": "research",
                    "priority": verifier.ORDINARY_LAYER_PRIORITY[task],
                    "rows": rows,
                    "report": verifier._descriptor(verifier.ROOT / report_rel, report_rel),
                    "receipt": verifier._descriptor(verifier.ROOT / receipt_rel, receipt_rel),
                    "independent_review_sha256": report_sha,
                })
        accepted.extend(({}, {}))
        ledger = {"input_pins": {"accepted_layers": accepted}}
        layers, references = verifier._read_followup_layer_rows(
            verifier.ROOT,
            ledger,
            expected,
            baseline,
            verifier.SECOND_FOLLOWUP_LAYER_SPECS,
            verifier.SECOND_FOLLOWUP_MANIFEST_REL,
            verifier.SECOND_FOLLOWUP_MANIFEST_SHA256,
            len(verifier.LAYER_SPECS) + len(verifier.FOLLOWUP_LAYER_SPECS),
            "second follow-up",
            "50ab0114669787dba6331b58f8054cd8fb33b5abbed33df6fbf5b52df53923fa",
            True,
        )
        self.assertEqual(list(layers), [item[0] for item in verifier.SECOND_FOLLOWUP_LAYER_SPECS])
        self.assertEqual(sum(len(rows) for rows in layers.values()), 183)
        self.assertEqual(sum(decision == "proposed" for rows in layers.values() for decision, _target, _confidence in rows.values()), 100)
        self.assertEqual(sum(decision == "unresolved" for rows in layers.values() for decision, _target, _confidence in rows.values()), 83)
        self.assertTrue(all(reference["independent_review_sha256"] == reference["report"]["sha256"] for reference in references.values()))

        task = "CA-P-2103"
        _occurrence_id, (decision, target, confidence) = next(iter(layers[task].items()))
        row = self._row(decision=decision, target=target)
        row["confidence"] = confidence
        row["applied_layers"].append({
            "layer": task,
            "priority": verifier.ORDINARY_LAYER_PRIORITY[task],
            **references[task],
            "decision": decision,
            "proposed_value": target,
            "confidence": confidence,
        })
        row["candidate_basis"] = []
        row["preserved_distinctions"] = []
        fixture_reference = copy.deepcopy(references[task])
        fixture_reference["proofs"] = {
            self.expected["occurrence_id"]: {
                field: copy.deepcopy(row.get(field))
                for field in verifier.LATER_FOLLOWUP_PROOF_FIELDS
            }
        }
        fixture_layers = {task: {self.expected["occurrence_id"]: (decision, target, confidence)}}
        self.assertEqual(self._verify([row], fixture_layers, layer_refs={task: fixture_reference})[decision], 1)
        wrong_priority = copy.deepcopy(row)
        wrong_priority["applied_layers"][-1]["priority"] = 25
        with self.assertRaises(verifier.VerificationError):
            self._verify([wrong_priority], fixture_layers, layer_refs={task: fixture_reference})
        missing_review_pin = copy.deepcopy(row)
        del missing_review_pin["applied_layers"][-1]["independent_review_sha256"]
        with self.assertRaises(verifier.VerificationError):
            self._verify([missing_review_pin], fixture_layers, layer_refs={task: fixture_reference})
        wrong_target = copy.deepcopy(row)
        wrong_target["applied_layers"][-1]["proposed_value"] = "Atom.Type"
        with self.assertRaises(verifier.VerificationError):
            self._verify([wrong_target], fixture_layers, layer_refs={task: fixture_reference})
        wrong_confidence = copy.deepcopy(row)
        wrong_confidence["applied_layers"][-1]["confidence"] = confidence - .01
        with self.assertRaises(verifier.VerificationError):
            self._verify([wrong_confidence], fixture_layers, layer_refs={task: fixture_reference})
        dropped_proof = copy.deepcopy(row)
        del dropped_proof["candidate_basis"]
        with self.assertRaises(verifier.VerificationError):
            self._verify([dropped_proof], fixture_layers, layer_refs={task: fixture_reference})

    def test_third_followup_reports_are_exact_and_per_row_provenance_is_fail_closed(self) -> None:
        """The fixed 2112--2117 group is live-checked before its replacement exists."""

        current_ledger = verifier.read_json(verifier.ROOT / verifier.LEDGER_REL, "current working ledger")
        baseline = verifier._read_baseline_rows(verifier.ROOT, current_ledger)
        expected = verifier.enumerate_current_frontier(verifier.ROOT)["occurrences"]
        accepted = [{} for _task, _kind in verifier.LAYER_SPECS]
        for specs in (verifier.FOLLOWUP_LAYER_SPECS, verifier.SECOND_FOLLOWUP_LAYER_SPECS, verifier.THIRD_FOLLOWUP_LAYER_SPECS):
            for task, _kind, rows, _proposed, _unresolved, report_sha in specs:
                report_rel = verifier._layer_path(task)
                receipt_rel = verifier.STAGE2_REL / f"task-{task.removeprefix('CA-P-')}.receipt.json"
                accepted.append({
                    "task": task,
                    "kind": "research",
                    "priority": verifier.ORDINARY_LAYER_PRIORITY[task],
                    "rows": rows,
                    "report": verifier._descriptor(verifier.ROOT / report_rel, report_rel),
                    "receipt": verifier._descriptor(verifier.ROOT / receipt_rel, receipt_rel),
                    "independent_review_sha256": report_sha,
                })
        accepted.extend(({}, {}))
        ledger = {"input_pins": {"accepted_layers": accepted}}
        offset = len(verifier.LAYER_SPECS) + len(verifier.FOLLOWUP_LAYER_SPECS) + len(verifier.SECOND_FOLLOWUP_LAYER_SPECS)
        layers, references = verifier._read_followup_layer_rows(
            verifier.ROOT,
            ledger,
            expected,
            baseline,
            verifier.THIRD_FOLLOWUP_LAYER_SPECS,
            verifier.THIRD_FOLLOWUP_MANIFEST_REL,
            verifier.THIRD_FOLLOWUP_MANIFEST_SHA256,
            offset,
            "third follow-up",
            "c52b26478acac8d5cfa9687b0925a1a9165a3647bd510e9877d69b06cbf214d4",
            True,
        )
        self.assertEqual(list(layers), [item[0] for item in verifier.THIRD_FOLLOWUP_LAYER_SPECS])
        self.assertEqual(sum(len(rows) for rows in layers.values()), 137)
        self.assertEqual(sum(decision == "proposed" for rows in layers.values() for decision, _target, _confidence in rows.values()), 87)
        self.assertEqual(sum(decision == "unresolved" for rows in layers.values() for decision, _target, _confidence in rows.values()), 50)
        self.assertTrue(all(reference["independent_review_sha256"] == reference["report"]["sha256"] for reference in references.values()))

        task = "CA-P-2112"
        _occurrence_id, (decision, target, confidence) = next(iter(layers[task].items()))
        row = self._row(decision=decision, target=target)
        row["confidence"] = confidence
        row["applied_layers"].append({
            "layer": task,
            "priority": verifier.ORDINARY_LAYER_PRIORITY[task],
            **references[task],
            "decision": decision,
            "proposed_value": target,
            "confidence": confidence,
        })
        row["candidate_basis"] = []
        row["preserved_distinctions"] = []
        fixture_reference = copy.deepcopy(references[task])
        fixture_reference["proofs"] = {
            self.expected["occurrence_id"]: {
                field: copy.deepcopy(row.get(field))
                for field in verifier.LATER_FOLLOWUP_PROOF_FIELDS
            }
        }
        fixture_layers = {task: {self.expected["occurrence_id"]: (decision, target, confidence)}}
        self.assertEqual(self._verify([row], fixture_layers, layer_refs={task: fixture_reference})[decision], 1)
        with self.assertRaises(verifier.VerificationError):
            self._verify([self._row()], fixture_layers, layer_refs={task: fixture_reference})
        missing_origin = copy.deepcopy(row)
        missing_origin["occurrence_id"] = f"{self.source_path}#subjects.depends_on[1]"
        with self.assertRaises(verifier.VerificationError):
            self._verify([missing_origin], fixture_layers, layer_refs={task: fixture_reference})
        stale_source = copy.deepcopy(row)
        stale_source["source_sha256"] = "0" * 64
        with self.assertRaises(verifier.VerificationError):
            self._verify([stale_source], fixture_layers, layer_refs={task: fixture_reference})
        executable = copy.deepcopy(row)
        executable["executable"] = True
        with self.assertRaises(verifier.VerificationError):
            self._verify([executable], fixture_layers, layer_refs={task: fixture_reference})
        wrong_priority = copy.deepcopy(row)
        wrong_priority["applied_layers"][-1]["priority"] = 31
        with self.assertRaises(verifier.VerificationError):
            self._verify([wrong_priority], fixture_layers, layer_refs={task: fixture_reference})
        missing_review_pin = copy.deepcopy(row)
        del missing_review_pin["applied_layers"][-1]["independent_review_sha256"]
        with self.assertRaises(verifier.VerificationError):
            self._verify([missing_review_pin], fixture_layers, layer_refs={task: fixture_reference})
        wrong_target = copy.deepcopy(row)
        wrong_target["applied_layers"][-1]["proposed_value"] = "Atom.Type"
        with self.assertRaises(verifier.VerificationError):
            self._verify([wrong_target], fixture_layers, layer_refs={task: fixture_reference})
        wrong_confidence = copy.deepcopy(row)
        wrong_confidence["applied_layers"][-1]["confidence"] = confidence - .01
        with self.assertRaises(verifier.VerificationError):
            self._verify([wrong_confidence], fixture_layers, layer_refs={task: fixture_reference})
        dropped_proof = copy.deepcopy(row)
        del dropped_proof["candidate_basis"]
        with self.assertRaises(verifier.VerificationError):
            self._verify([dropped_proof], fixture_layers, layer_refs={task: fixture_reference})
        stale_receipt_ledger = copy.deepcopy(ledger)
        stale_receipt_ledger["input_pins"]["accepted_layers"][offset]["receipt"]["sha256"] = "0" * 64
        with self.assertRaises(verifier.VerificationError):
            verifier._read_followup_layer_rows(
                verifier.ROOT,
                stale_receipt_ledger,
                expected,
                baseline,
                verifier.THIRD_FOLLOWUP_LAYER_SPECS,
                verifier.THIRD_FOLLOWUP_MANIFEST_REL,
                verifier.THIRD_FOLLOWUP_MANIFEST_SHA256,
                offset,
                "third follow-up",
                "c52b26478acac8d5cfa9687b0925a1a9165a3647bd510e9877d69b06cbf214d4",
                True,
            )

    def test_fourth_followup_reports_are_exact_and_per_row_provenance_is_fail_closed(self) -> None:
        """The fixed 2121--2128 group is live-checked before replacement exists."""

        current_ledger = verifier.read_json(verifier.ROOT / verifier.LEDGER_REL, "current working ledger")
        baseline = verifier._read_baseline_rows(verifier.ROOT, current_ledger)
        expected = verifier.enumerate_current_frontier(verifier.ROOT)["occurrences"]
        offset = len(verifier.LAYER_SPECS) + len(verifier.FOLLOWUP_LAYER_SPECS) + len(verifier.SECOND_FOLLOWUP_LAYER_SPECS) + len(verifier.THIRD_FOLLOWUP_LAYER_SPECS)
        accepted = [{} for _ in range(offset)]
        for task, _kind, rows, _proposed, _unresolved, report_sha in verifier.FOURTH_FOLLOWUP_LAYER_SPECS:
            report_rel = verifier._layer_path(task)
            receipt_rel = verifier.STAGE2_REL / f"task-{task.removeprefix('CA-P-')}.receipt.json"
            accepted.append({
                "task": task,
                "kind": "research",
                "priority": verifier.ORDINARY_LAYER_PRIORITY[task],
                "rows": rows,
                "report": verifier._descriptor(verifier.ROOT / report_rel, report_rel),
                "receipt": verifier._descriptor(verifier.ROOT / receipt_rel, receipt_rel),
                "independent_review_sha256": report_sha,
            })
        accepted.extend(({}, {}))
        ledger = {"input_pins": {"accepted_layers": accepted}}
        layers, references = verifier._read_followup_layer_rows(
            verifier.ROOT,
            ledger,
            expected,
            baseline,
            verifier.FOURTH_FOLLOWUP_LAYER_SPECS,
            verifier.FOURTH_FOLLOWUP_MANIFEST_REL,
            verifier.FOURTH_FOLLOWUP_MANIFEST_SHA256,
            offset,
            "fourth follow-up",
            "4f2ec9d285283a76386dd176f6d4a6bf6a101db32219349462a91bc6c666ecf2",
            True,
        )
        self.assertEqual(list(layers), [item[0] for item in verifier.FOURTH_FOLLOWUP_LAYER_SPECS])
        self.assertEqual(sum(len(rows) for rows in layers.values()), 205)
        self.assertEqual(sum(decision == "proposed" for rows in layers.values() for decision, _target, _confidence in rows.values()), 71)
        self.assertEqual(sum(decision == "unresolved" for rows in layers.values() for decision, _target, _confidence in rows.values()), 134)
        self.assertTrue(all(reference["independent_review_sha256"] == reference["report"]["sha256"] for reference in references.values()))

        task = "CA-P-2125"
        _occurrence_id, (decision, target, confidence) = next(iter(layers[task].items()))
        row = self._row(decision=decision, target=target)
        row["confidence"] = confidence
        row["applied_layers"].append({
            "layer": task,
            "priority": verifier.ORDINARY_LAYER_PRIORITY[task],
            **references[task],
            "decision": decision,
            "proposed_value": target,
            "confidence": confidence,
        })
        row["candidate_basis"] = []
        row["preserved_distinctions"] = []
        fixture_reference = copy.deepcopy(references[task])
        fixture_reference["proofs"] = {
            self.expected["occurrence_id"]: {
                field: copy.deepcopy(row.get(field))
                for field in verifier.LATER_FOLLOWUP_PROOF_FIELDS
            }
        }
        fixture_layers = {task: {self.expected["occurrence_id"]: (decision, target, confidence)}}
        self.assertEqual(self._verify([row], fixture_layers, layer_refs={task: fixture_reference})[decision], 1)
        for variant in ("priority", "target", "confidence", "executable", "proof", "review"):
            wrong = copy.deepcopy(row)
            if variant == "priority":
                wrong["applied_layers"][-1]["priority"] = 31
            elif variant == "target":
                wrong["applied_layers"][-1]["proposed_value"] = "Atom.Type"
            elif variant == "confidence":
                wrong["applied_layers"][-1]["confidence"] = confidence - .01
            elif variant == "executable":
                wrong["executable"] = True
            elif variant == "proof":
                del wrong["candidate_basis"]
            else:
                del wrong["applied_layers"][-1]["independent_review_sha256"]
            with self.assertRaises(verifier.VerificationError, msg=variant):
                self._verify([wrong], fixture_layers, layer_refs={task: fixture_reference})
        stale_receipt_ledger = copy.deepcopy(ledger)
        stale_receipt_ledger["input_pins"]["accepted_layers"][offset]["receipt"]["sha256"] = "0" * 64
        with self.assertRaises(verifier.VerificationError):
            verifier._read_followup_layer_rows(
                verifier.ROOT,
                stale_receipt_ledger,
                expected,
                baseline,
                verifier.FOURTH_FOLLOWUP_LAYER_SPECS,
                verifier.FOURTH_FOLLOWUP_MANIFEST_REL,
                verifier.FOURTH_FOLLOWUP_MANIFEST_SHA256,
                offset,
                "fourth follow-up",
                "4f2ec9d285283a76386dd176f6d4a6bf6a101db32219349462a91bc6c666ecf2",
                True,
            )

    def test_fifth_followup_successor_is_core_only_and_exact(self) -> None:
        """The fixed fifth group admits the accepted Core-only successor only."""

        current_ledger = verifier.read_json(verifier.ROOT / verifier.LEDGER_REL, "current working ledger")
        baseline = verifier._read_baseline_rows(verifier.ROOT, current_ledger)
        expected = verifier.enumerate_current_frontier(verifier.ROOT)["occurrences"]
        source_pins = {row["source_path"]: row["source_sha256"] for row in expected}
        successor_rel, successor_receipt_rel = verifier._followup_artifact_paths("CA-P-2133")
        successor = verifier.read_json(verifier.ROOT / successor_rel, "Core-only CA-P-2133 successor")
        successor_receipt = verifier.read_json(verifier.ROOT / successor_receipt_rel, "Core-only CA-P-2133 receipt")
        successor_pin = verifier._descriptor(verifier.ROOT / successor_rel, successor_rel)
        verifier._verify_followup_successor_binding(verifier.ROOT, "CA-P-2133", successor, successor_receipt, successor_pin)
        self.assertEqual(sum(item[2] for item in verifier.FIFTH_FOLLOWUP_LAYER_SPECS), 195)
        self.assertEqual(sum(item[3] for item in verifier.FIFTH_FOLLOWUP_LAYER_SPECS), 63)
        self.assertEqual(sum(item[4] for item in verifier.FIFTH_FOLLOWUP_LAYER_SPECS), 132)
        self.assertTrue(all(
            verifier._later_followup_evidence_is_current(verifier.ROOT, evidence, source_pins, "Core-only CA-P-2133 supporting evidence")
            for row in successor["rows"]
            for evidence in row["evidence"]
        ))
        offset = len(verifier.LAYER_SPECS) + len(verifier.FOLLOWUP_LAYER_SPECS) + len(verifier.SECOND_FOLLOWUP_LAYER_SPECS) + len(verifier.THIRD_FOLLOWUP_LAYER_SPECS) + len(verifier.FOURTH_FOLLOWUP_LAYER_SPECS)
        accepted = [{} for _ in range(offset)]
        for task, _kind, rows, _proposed, _unresolved, report_sha in verifier.FIFTH_FOLLOWUP_LAYER_SPECS:
            report_rel, receipt_rel = verifier._followup_artifact_paths(task)
            expected_sha = verifier._followup_expected_report_sha256(task, report_sha)
            accepted.append({
                "task": task, "kind": "research", "priority": verifier.ORDINARY_LAYER_PRIORITY[task], "rows": rows,
                "report": verifier._descriptor(verifier.ROOT / report_rel, report_rel),
                "receipt": verifier._descriptor(verifier.ROOT / receipt_rel, receipt_rel), "independent_review_sha256": expected_sha,
            })
        accepted.extend(({}, {}))
        layers, _references = verifier._read_followup_layer_rows(
            verifier.ROOT,
            {"input_pins": {"accepted_layers": accepted}},
            expected,
            baseline,
            verifier.FIFTH_FOLLOWUP_LAYER_SPECS,
            verifier.FIFTH_FOLLOWUP_MANIFEST_REL,
            verifier.FIFTH_FOLLOWUP_MANIFEST_SHA256,
            offset,
            "fifth follow-up",
            "19d55f08f9bd809d5a7cf7c937992b597e1a17d4b641e186ebc144b1e26c1186",
            True,
        )
        self.assertEqual(sum(len(rows) for rows in layers.values()), 195)
        self.assertEqual(sum(decision == "proposed" for rows in layers.values() for decision, _target, _confidence in rows.values()), 63)
        self.assertEqual(sum(decision == "unresolved" for rows in layers.values() for decision, _target, _confidence in rows.values()), 132)

    def test_fifth_successor_binding_rejects_withdrawn_foreign_report(self) -> None:
        """CA-P-2133 may use only the separately accepted Core-only successor."""

        report_path = verifier.ROOT / verifier._layer_path("CA-P-2133")
        receipt_relative = verifier.STAGE2_REL / "task-2133.receipt.json"
        receipt_path = verifier.ROOT / receipt_relative
        report = verifier.read_json(report_path, "withdrawn CA-P-2133 report")
        receipt = verifier.read_json(receipt_path, "withdrawn CA-P-2133 receipt")
        successor_report, successor_receipt = verifier._followup_artifact_paths("CA-P-2133")
        self.assertEqual(successor_report.as_posix(), (verifier.STAGE2_REL / "semantic-reviews/task-2133.core-only.research.json").as_posix())
        self.assertEqual(successor_receipt.as_posix(), (verifier.STAGE2_REL / "task-2133.core-only.receipt.json").as_posix())
        with self.assertRaisesRegex(verifier.VerificationError, "successor report path"):
            verifier._verify_followup_successor_binding(
                verifier.ROOT,
                "CA-P-2133",
                report,
                receipt,
                verifier._descriptor(report_path, verifier._layer_path("CA-P-2133")),
            )

    def test_fifth_successor_contract_bytes_are_live_and_pinned(self) -> None:
        """Receipt metadata cannot mask a stale successor-contract file."""

        binding = verifier.FIFTH_SUCCESSOR_BINDINGS["CA-P-2133"]
        predecessor_relative = Path(binding["supersedes"]["path"])
        predecessor = self.root / predecessor_relative
        predecessor.parent.mkdir(parents=True, exist_ok=True)
        predecessor.write_bytes((verifier.ROOT / predecessor_relative).read_bytes())
        predecessor_receipt_relative = Path(binding["predecessor_receipt"]["path"])
        predecessor_receipt = self.root / predecessor_receipt_relative
        predecessor_receipt.parent.mkdir(parents=True, exist_ok=True)
        predecessor_receipt.write_bytes((verifier.ROOT / predecessor_receipt_relative).read_bytes())
        contract_relative = Path(binding["successor_contract"]["path"])
        contract = self.root / contract_relative
        contract.parent.mkdir(parents=True, exist_ok=True)
        contract.write_bytes((verifier.ROOT / contract_relative).read_bytes())
        report_relative, receipt_relative = verifier._followup_artifact_paths("CA-P-2133")
        report_path = verifier.ROOT / report_relative
        report = verifier.read_json(report_path, "Core-only CA-P-2133 successor")
        receipt = verifier.read_json(verifier.ROOT / receipt_relative, "Core-only CA-P-2133 receipt")
        report_pin = verifier._descriptor(report_path, report_relative)
        verifier._verify_followup_successor_binding(self.root, "CA-P-2133", report, receipt, report_pin)
        contract.write_bytes(b"stale successor contract bytes\n")
        with self.assertRaisesRegex(verifier.VerificationError, "successor contract pin"):
            verifier._verify_followup_successor_binding(self.root, "CA-P-2133", report, receipt, report_pin)

    def test_fifth_successor_preserves_live_predecessor_report_and_receipt(self) -> None:
        """Historical predecessor bytes are checked without making them authority."""

        binding = verifier.FIFTH_SUCCESSOR_BINDINGS["CA-P-2133"]
        predecessor_relative = Path(binding["supersedes"]["path"])
        predecessor = self.root / predecessor_relative
        predecessor.parent.mkdir(parents=True, exist_ok=True)
        predecessor.write_bytes((verifier.ROOT / predecessor_relative).read_bytes())
        predecessor_receipt_relative = Path(binding["predecessor_receipt"]["path"])
        predecessor_receipt = self.root / predecessor_receipt_relative
        predecessor_receipt.parent.mkdir(parents=True, exist_ok=True)
        predecessor_receipt.write_bytes((verifier.ROOT / predecessor_receipt_relative).read_bytes())
        contract_relative = Path(binding["successor_contract"]["path"])
        contract = self.root / contract_relative
        contract.parent.mkdir(parents=True, exist_ok=True)
        contract.write_bytes((verifier.ROOT / contract_relative).read_bytes())
        report_relative, receipt_relative = verifier._followup_artifact_paths("CA-P-2133")
        report_path = verifier.ROOT / report_relative
        report = verifier.read_json(report_path, "Core-only CA-P-2133 successor")
        receipt = verifier.read_json(verifier.ROOT / receipt_relative, "Core-only CA-P-2133 receipt")
        report_pin = verifier._descriptor(report_path, report_relative)
        verifier._verify_followup_successor_binding(self.root, "CA-P-2133", report, receipt, report_pin)
        predecessor.write_bytes(b"stale predecessor report bytes\n")
        with self.assertRaisesRegex(verifier.VerificationError, "successor predecessor report pin"):
            verifier._verify_followup_successor_binding(self.root, "CA-P-2133", report, receipt, report_pin)
        missing_root = self.root / "missing-predecessor-receipt"
        missing_predecessor = missing_root / predecessor_relative
        missing_predecessor.parent.mkdir(parents=True, exist_ok=True)
        missing_predecessor.write_bytes((verifier.ROOT / predecessor_relative).read_bytes())
        missing_contract = missing_root / contract_relative
        missing_contract.parent.mkdir(parents=True, exist_ok=True)
        missing_contract.write_bytes((verifier.ROOT / contract_relative).read_bytes())
        with self.assertRaisesRegex(verifier.VerificationError, "successor predecessor receipt exists"):
            verifier._verify_followup_successor_binding(missing_root, "CA-P-2133", report, receipt, report_pin)

    def test_later_followup_supporting_evidence_is_current_or_exact_operator_decision(self) -> None:
        """Later-group supporting spans are live, and stale/non-Core pins fail."""

        current = verifier.enumerate_current_frontier(verifier.ROOT)["occurrences"]
        source_pins = {row["source_path"]: row["source_sha256"] for row in current}
        report = verifier.read_json(verifier.ROOT / verifier._layer_path("CA-P-2103"), "second follow-up report")
        evidence = next(row["evidence"] for row in report["rows"] if len(row["evidence"]) > 1)
        self.assertTrue(all(
            verifier._later_followup_evidence_is_current(verifier.ROOT, item, source_pins, "second follow-up fixture")
            for item in evidence
        ))
        stale = copy.deepcopy(evidence[-1])
        stale["sha256"] = "0" * 64
        self.assertFalse(verifier._later_followup_evidence_is_current(verifier.ROOT, stale, source_pins, "second follow-up stale fixture"))
        wrong_file = copy.deepcopy(evidence[-1])
        wrong_file["path"] = ".caprmedio_caprmedio/03_plan/not-meaning-evidence.md"
        self.assertFalse(verifier._later_followup_evidence_is_current(verifier.ROOT, wrong_file, source_pins, "second follow-up wrong-file fixture"))
        third_report = verifier.read_json(verifier.ROOT / verifier._layer_path("CA-P-2117"), "third follow-up report")
        self.assertTrue(all(
            verifier._later_followup_evidence_is_current(verifier.ROOT, item, source_pins, "third follow-up fixture")
            for row in third_report["rows"]
            for item in row["evidence"]
        ))
        fourth_report = verifier.read_json(verifier.ROOT / verifier._layer_path("CA-P-2125"), "fourth follow-up report")
        self.assertTrue(all(
            verifier._later_followup_evidence_is_current(verifier.ROOT, item, source_pins, "fourth follow-up fixture")
            for row in fourth_report["rows"]
            for item in row["evidence"]
        ))
        fifth_report = verifier.read_json(verifier.ROOT / verifier._layer_path("CA-P-2137"), "fifth follow-up report")
        self.assertTrue(all(
            verifier._later_followup_evidence_is_current(verifier.ROOT, item, source_pins, "fifth follow-up fixture")
            for row in fifth_report["rows"]
            for item in row["evidence"]
        ))


if __name__ == "__main__":
    unittest.main()
