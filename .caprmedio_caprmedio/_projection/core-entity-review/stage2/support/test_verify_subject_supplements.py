"""Isolated scratch tests for CA-P-2060's supplement verifier."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("verify_subject_supplements", HERE / "verify_subject_supplements.py")
assert SPEC and SPEC.loader
checker = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = checker
SPEC.loader.exec_module(checker)


class SubjectSupplementTests(unittest.TestCase):
    def setUp(self) -> None:
        scratch = checker.ROOT / ".caprmedio_tmp"
        scratch.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=scratch, prefix="subject-supplements-", ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name)
        self.spec = checker.ReportSpec("history", "CA-P-2050", "research", "history")
        self._create_fixture()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    @staticmethod
    def _sha(raw: bytes) -> str:
        return hashlib.sha256(raw).hexdigest()

    def _write(self, relative: str, value: dict | str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        raw = json.dumps(value, sort_keys=True, indent=2).encode() + b"\n" if isinstance(value, dict) else value.encode()
        path.write_bytes(raw)
        return path

    def _load(self, relative: str) -> dict:
        return json.loads((self.root / relative).read_text())

    def _save(self, relative: str, value: dict) -> None:
        self._write(relative, value)

    def _pin(self, relative: str) -> dict[str, str]:
        return {"path": relative, "sha256": self._sha((self.root / relative).read_bytes())}

    def _create_fixture(self) -> None:
        stage = checker.STAGE
        self.source_rel = ".caprmedio_caprmedio/current/CA-R-1.md"
        source = "---\natom_id: CA-R-1\n---\nCurrent Main Content.\n"
        source_path = self._write(self.source_rel, source)
        source_sha = self._sha(source_path.read_bytes())
        span_sha = self._sha(b"Current Main Content.\n")
        self._write(checker.CANDIDATE_REL, {"rules": {"legacy": "Modern"}})
        self._write(checker.SUPPLEMENT_CONTRACT_REL, "supplement contract\n")
        self._write(checker.DECISION_REL, {"decisions": {"substance": {}}})
        occurrence = {
            "occurrence_id": self.source_rel + "#subjects.depends_on[0]",
            "source_path": self.source_rel,
            "source_atom_id": "CA-R-1",
            "source_version": 1,
            "source_sha256": source_sha,
            "field": "depends_on",
            "index": 0,
            "old_value": "Legacy",
            "quarantined": False,
            "batch_id": "current-subjects.batch-001",
            "task_id": "CA-P-1992",
            "originating_review_path": f"{stage}/reviews/current-subjects.batch-001.review.json",
            "originating_review_sha256": "origin-sha",
            "decision": "unresolved",
            "proposed_value": None,
        }
        ledger = {"occurrences": [occurrence]}
        ledger_path = self._write(checker.LEDGER_REL, ledger)
        self.assertEqual(self._sha(ledger_path.read_bytes()), self._sha(ledger_path.read_bytes()))
        # The production constant is intentionally frozen; patch it only for
        # this fully isolated fixture through the test helper below.
        self.ledger_sha = self._sha(ledger_path.read_bytes())
        ownership = {
            "base_ledger": {"path": checker.LEDGER_REL, "sha256": self.ledger_sha},
            "research_tasks": [{"group": "history", "task_id": "CA-P-2050", "old_values": ["Legacy"], "occurrences": 1, "sources": 1, "occurrence_ids_sha256": checker.id_digest([occurrence["occurrence_id"]])}],
        }
        self._write(checker.OWNERSHIP_REL, ownership)
        report = {
            "schema_version": 1,
            "task_id": "CA-P-2050",
            "non_authoritative": True,
            "source_migration": "not_performed",
            "native_admission": "not_performed",
            "base_ledger": {"path": checker.LEDGER_REL, "sha256": self.ledger_sha},
            "evidence_pins": [self._pin(checker.CANDIDATE_REL), self._pin(checker.SUPPLEMENT_CONTRACT_REL)],
            "occurrences": [{
                **{key: occurrence[key] for key in ("occurrence_id", "source_path", "source_atom_id", "source_version", "source_sha256", "field", "index", "old_value", "quarantined", "batch_id", "task_id", "originating_review_path", "originating_review_sha256")},
                "baseline_decision": "unresolved",
                "baseline_proposed_value": None,
                "decision": "proposed",
                "proposed_value": "Modern",
                "confidence": 0.95,
                "reason": "Fixture source explicitly supports the bounded proposal.",
                "candidate_basis": [{"pointer": "/rules/legacy", "reason": "Fixture candidate rule."}],
                "preserved_distinctions": ["Fixture distinction retained."],
                "question": None,
                "executable": False,
                "evidence": [{"path": self.source_rel, "sha256": source_sha, "start_line": 4, "end_line": 4, "span_sha256": span_sha, "reason": "Current body evidence."}],
            }],
        }
        self.report_rel = self.spec.path
        self._write(self.report_rel, report)

    def _verify(self) -> dict:
        original = checker.BASE_LEDGER_SHA
        checker.BASE_LEDGER_SHA = self.ledger_sha
        try:
            return checker.verify_supplements(self.root, (self.spec,))
        finally:
            checker.BASE_LEDGER_SHA = original

    def test_happy_fixture_passes(self) -> None:
        result = self._verify()
        self.assertEqual(result["outcome"], "PASS")
        self.assertEqual(result["occurrences"], 1)

    def test_missing_occurrence_is_rejected(self) -> None:
        report = self._load(self.report_rel)
        report["occurrences"] = []
        self._save(self.report_rel, report)
        with self.assertRaises(checker.VerificationError):
            self._verify()

    def test_duplicate_occurrence_is_rejected(self) -> None:
        report = self._load(self.report_rel)
        report["occurrences"].append(copy.deepcopy(report["occurrences"][0]))
        self._save(self.report_rel, report)
        with self.assertRaises(checker.VerificationError):
            self._verify()

    def test_stale_source_pin_is_rejected(self) -> None:
        (self.root / self.source_rel).write_text("---\natom_id: CA-R-1\n---\nChanged.\n")
        with self.assertRaises(checker.VerificationError):
            self._verify()

    def test_stale_evidence_pin_is_rejected(self) -> None:
        report = self._load(self.report_rel)
        report["evidence_pins"][0]["sha256"] = "0" * 64
        self._save(self.report_rel, report)
        with self.assertRaises(checker.VerificationError):
            self._verify()

    def test_false_proposed_row_is_rejected(self) -> None:
        report = self._load(self.report_rel)
        report["occurrences"][0]["confidence"] = 0.5
        self._save(self.report_rel, report)
        with self.assertRaises(checker.VerificationError):
            self._verify()

    def test_missing_candidate_pointer_is_rejected(self) -> None:
        report = self._load(self.report_rel)
        report["occurrences"][0]["candidate_basis"][0]["pointer"] = "/rules/missing"
        self._save(self.report_rel, report)
        with self.assertRaises(checker.VerificationError):
            self._verify()

    def test_executable_row_is_rejected(self) -> None:
        report = self._load(self.report_rel)
        report["occurrences"][0]["executable"] = True
        self._save(self.report_rel, report)
        with self.assertRaises(checker.VerificationError):
            self._verify()


if __name__ == "__main__":
    unittest.main()
