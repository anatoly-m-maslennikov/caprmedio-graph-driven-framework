"""Scratch-only tests for CA-P-2046's one-off review-ledger preparation."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
SPEC = importlib.util.spec_from_file_location(
    "integrate_current_subject_reviews", HERE / "integrate_current_subject_reviews.py"
)
assert SPEC and SPEC.loader
integrator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(integrator)
from verify_current_inventory import VerificationError


class CurrentSubjectLedgerTests(unittest.TestCase):
    def setUp(self) -> None:
        scratch = integrator.ROOT / ".caprmedio_tmp"
        scratch.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=scratch, prefix="current-subject-ledger-", ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name)
        self._create_fixture()
        self.counts = mock.patch.multiple(
            integrator,
            EXPECTED_SOURCES=1,
            EXPECTED_OCCURRENCES=1,
            EXPECTED_QUARANTINED_SOURCES=1,
            EXPECTED_REVIEW_TASKS=1,
            EXPECTED_SOURCE_CONTRACT_SHA=self._sha((self.root / self.source_contract).read_bytes()),
            EXPECTED_REVIEW_CONTRACT_SHA=self._sha((self.root / self.review_contract).read_bytes()),
        )
        self.counts.start()

    def tearDown(self) -> None:
        self.counts.stop()
        self.temporary.cleanup()

    @staticmethod
    def _sha(raw: bytes) -> str:
        return hashlib.sha256(raw).hexdigest()

    def _write(self, relative: str, value: dict | str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        raw = json.dumps(value, indent=2, sort_keys=True).encode() + b"\n" if isinstance(value, dict) else value.encode()
        path.write_bytes(raw)
        return path

    def _load(self, relative: str) -> dict:
        return json.loads((self.root / relative).read_text())

    def _save(self, relative: str, value: dict) -> None:
        self._write(relative, value)

    def _fake_inventory(self, _root: Path) -> dict:
        return {"outcome": "PASS", "selected_sources": 1, "occurrences": 1, "batches": 1}

    @staticmethod
    def _fake_review(_root: Path, _number: int, report: dict) -> dict:
        return {"outcome": "PASS", "sources": len(report["source_reviews"]), "occurrences": len(report["occurrences"])}

    def _build(self) -> dict:
        return integrator.build_ledger(self.root, inventory_verifier=self._fake_inventory, review_verifier=self._fake_review)

    def _create_fixture(self) -> None:
        stage = ".caprmedio_caprmedio/_projection/core-entity-review/stage2"
        self.inventory_relative = stage + "/current-subjects.inventory.json"
        self.manifest_relative = stage + "/current-subjects.batches.json"
        self.ownership_relative = stage + "/current-subjects.review.ownership.json"
        self.source_contract = stage + "/current-subjects.contract.md"
        self.review_contract = stage + "/current-subjects.review.contract.md"
        self._write(self.source_contract, "source contract\n")
        self._write(self.review_contract, "review contract\n")
        source = {"relative_path": ".caprmedio_caprmedio/current/CA-R-1.md", "full_file_sha256": "source", "atom_id": "CA-R-1", "version": 1, "quarantined": True, "findings": ["invalid_metadata"]}
        occurrence = {"occurrence_id": source["relative_path"] + "#subjects.governs", "source_path": source["relative_path"], "source_atom_id": "CA-R-1", "source_version": 1, "source_sha256": "source", "field": "governs", "index": None, "old_value": "Atom", "quarantined": True}
        inventory = {"schema_version": 1, "non_authoritative": True, "selected_sources": [source], "occurrences": [occurrence]}
        inventory_path = self._write(self.inventory_relative, inventory)
        inventory_sha = self._sha(inventory_path.read_bytes())
        self.batch_relative = stage + "/inputs/current-subjects.batch-001.json"
        batch = {"schema_version": 1, "batch_id": "current-subjects.batch-001", "input_inventory_sha256": inventory_sha, "selected_sources": [source], "occurrences": [occurrence]}
        batch_path = self._write(self.batch_relative, batch)
        batch_sha = self._sha(batch_path.read_bytes())
        manifest = {"schema_version": 1, "inventory_path": self.inventory_relative, "batches": [{"path": self.batch_relative, "sha256": batch_sha, "source_count": 1, "occurrence_count": 1}]}
        manifest_path = self._write(self.manifest_relative, manifest)
        report_relative = stage + "/reviews/current-subjects.batch-001.review.json"
        review_source = {**source, "main_content_read": True, "finding_dispositions": [{"finding": "invalid_metadata", "reason": "Retained."}], "questions": []}
        review_occurrence = {**occurrence, "decision": "unresolved", "proposed_value": None, "confidence": 0.0, "reason": "Meaning remains unresolved.", "candidate_basis": [], "preserved_distinctions": ["Source meaning retained."], "question": "What is the canonical identity?", "evidence": [{"path": source["relative_path"], "sha256": "source", "start_line": 1, "end_line": 1, "span_sha256": "span", "reason": "Fixture evidence."}], "executable": False}
        report = {"task_id": "CA-P-1992", "batch_id": batch["batch_id"], "input_batch_path": self.batch_relative, "input_batch_sha256": batch_sha, "input_inventory_sha256": inventory_sha, "source_reviews": [review_source], "occurrences": [review_occurrence]}
        report_path = self._write(report_relative, report)
        report_sha = self._sha(report_path.read_bytes())
        self.plan_relative = ".caprmedio_caprmedio/03_plan/done/02-CA-P-1992-TASK--review.md"
        self._write(self.plan_relative, "---\natom_id: CA-P-1992\ncontent_role: Plan\ntype: Plan\nstatus: Done\nrelations:\n  is_decomposition_of: [CA-P-1966]\n---\n# Done\n")
        task = {"task_id": "CA-P-1992", "plan_path": ".caprmedio_caprmedio/03_plan/02-CA-P-1992-TASK--review.md", "input_batch_path": self.batch_relative, "input_batch_sha256": batch_sha, "source_count": 1, "occurrence_count": 1, "output_path": report_relative}
        ownership = {"inventory_sha256": inventory_sha, "batches_manifest_sha256": self._sha(manifest_path.read_bytes()), "review_contract_sha256": self._sha((self.root / self.review_contract).read_bytes()), "counts": {"sources": 1, "occurrences": 1, "review_tasks": 1, "integration_tasks": 1}, "review_tasks": [task]}
        self._write(self.ownership_relative, ownership)
        self.receipt_relative = stage + "/task-1992.receipt.json"
        receipt = {"task": "CA-P-1992", "result": "PASS", "output": {"path": report_relative, "sha256": report_sha}, "input_batch": {"path": self.batch_relative, "sha256": batch_sha}, "checks": {"independent_structural_verifier": "PASS", "sources": 1, "occurrences": 1, "proposed": 0, "unchanged": 0, "unresolved": 1, "all_executable_false": True}}
        self._write(self.receipt_relative, receipt)
        for number in (1972, 1988, 1989, 1990):
            self._write(stage + f"/task-{number}.receipt.json", {"task": f"CA-P-{number}", "result": "PASS: fixture"})

    def test_preview_aggregates_exact_rows_and_origins(self) -> None:
        ledger = self._build()
        self.assertEqual(ledger["counts"]["sources"], 1)
        self.assertEqual(ledger["counts"]["occurrences"], 1)
        self.assertEqual(ledger["counts"]["unresolved"], 1)
        self.assertEqual(ledger["occurrences"][0]["originating_review_path"], self._load(self.receipt_relative)["output"]["path"])
        self.assertEqual(ledger["unresolved_occurrence_refs"][0]["occurrence_id"], ledger["occurrences"][0]["occurrence_id"])

    def test_unfinished_plan_is_rejected(self) -> None:
        plan = self.root / self.plan_relative
        plan.write_text(plan.read_text().replace("status: Done", "status: Active"))
        with self.assertRaises(VerificationError):
            self._build()

    def test_stale_receipt_is_rejected(self) -> None:
        receipt = self._load(self.receipt_relative)
        receipt["output"]["sha256"] = "stale"
        self._save(self.receipt_relative, receipt)
        with self.assertRaises(VerificationError):
            self._build()

    def test_receipt_decision_count_is_rejected(self) -> None:
        receipt = self._load(self.receipt_relative)
        receipt["checks"]["unresolved"] = 0
        self._save(self.receipt_relative, receipt)
        with self.assertRaises(VerificationError):
            self._build()

    def test_missing_occurrence_is_rejected(self) -> None:
        report = self._load(self._load(self.ownership_relative)["review_tasks"][0]["output_path"])
        report["occurrences"] = []
        self._save(self._load(self.ownership_relative)["review_tasks"][0]["output_path"], report)
        self._refresh_receipt()
        with self.assertRaises(VerificationError):
            self._build()

    def test_duplicate_occurrence_is_rejected(self) -> None:
        report_relative = self._load(self.ownership_relative)["review_tasks"][0]["output_path"]
        report = self._load(report_relative)
        report["occurrences"].append(copy.deepcopy(report["occurrences"][0]))
        self._save(report_relative, report)
        self._refresh_receipt()
        with self.assertRaises(VerificationError):
            self._build()

    def test_persist_refuses_overwrite(self) -> None:
        target = self.root / integrator.LEDGER_REL
        target.write_text("already exists\n")
        with self.assertRaises(VerificationError):
            integrator.persist_ledger(self.root, inventory_verifier=self._fake_inventory, review_verifier=self._fake_review)

    def test_persist_refuses_symlink_target(self) -> None:
        target = self.root / integrator.LEDGER_REL
        target.symlink_to(self.root / self.source_contract)
        with self.assertRaises(VerificationError):
            integrator.persist_ledger(self.root, inventory_verifier=self._fake_inventory, review_verifier=self._fake_review)

    def test_persist_creates_only_the_derived_ledger(self) -> None:
        ledger = integrator.persist_ledger(self.root, inventory_verifier=self._fake_inventory, review_verifier=self._fake_review)
        target = self.root / integrator.LEDGER_REL
        self.assertTrue(target.is_file())
        self.assertEqual(json.loads(target.read_text())["counts"], ledger["counts"])

    def _refresh_receipt(self) -> None:
        receipt = self._load(self.receipt_relative)
        report_relative = receipt["output"]["path"]
        receipt["output"]["sha256"] = self._sha((self.root / report_relative).read_bytes())
        self._save(self.receipt_relative, receipt)


if __name__ == "__main__":
    unittest.main()
