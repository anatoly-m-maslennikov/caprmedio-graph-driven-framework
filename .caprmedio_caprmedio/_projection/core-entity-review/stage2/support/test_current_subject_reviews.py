"""Isolated structural-evidence tests for CA-P-2044's review checker.

These fixtures exercise only the independent checker.  They do not import a
review producer or recreate subject-mapping decisions.
"""
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
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
SPEC = importlib.util.spec_from_file_location(
    "verify_current_subject_reviews", HERE / "verify_current_subject_reviews.py"
)
assert SPEC and SPEC.loader
verifier = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verifier)
from verify_current_inventory import VerificationError


class CurrentSubjectReviewVerifierTests(unittest.TestCase):
    def setUp(self) -> None:
        scratch = verifier.ROOT / ".caprmedio_tmp"
        scratch.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(
            dir=scratch,
            prefix="current-subject-reviews-",
            ignore_cleanup_errors=True,
        )
        self.root = Path(self.temporary.name)
        self._create_fixture()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    @staticmethod
    def _json_bytes(value: dict) -> bytes:
        return json.dumps(value, indent=2, sort_keys=True).encode() + b"\n"

    @staticmethod
    def _sha(raw: bytes) -> str:
        return hashlib.sha256(raw).hexdigest()

    def _write(self, relative: str, content: str | bytes) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content.encode() if isinstance(content, str) else content)
        return path

    def _load(self, path: Path) -> dict:
        return json.loads(path.read_text())

    def _save(self, path: Path, value: dict) -> None:
        path.write_bytes(self._json_bytes(value))

    def _span(self, path: Path, start_line: int, end_line: int) -> str:
        return self._sha(b"".join(path.read_bytes().splitlines(keepends=True)[start_line - 1:end_line]))

    def _review(self) -> dict:
        return self._load(self.review_path)

    def _save_review(self, review: dict) -> None:
        self._save(self.review_path, review)

    def _assert_rejected(self) -> None:
        with self.assertRaises(VerificationError):
            verifier.verify_review(self.root, 1, self._review())

    def _create_fixture(self) -> None:
        base = ".caprmedio_caprmedio/_projection/core-entity-review"
        stage = base + "/stage2"
        self.source_relative = ".caprmedio_caprmedio/current-core/CA-R-1.md"
        source_path = self._write(
            self.source_relative,
            """---
atom_id: CA-R-1
version: 1
subjects:
  governs: Atom
  depends_on: [Relation]
---
# Claim

An Atom is evidence-bearing in this current source.
""",
        )
        self.other_relative = ".caprmedio_caprmedio/current-core/unrelated.md"
        other_path = self._write(
            self.other_relative,
            """---
atom_id: CA-R-2
---
# Claim

Unrelated current content.
""",
        )
        candidate_relative = base + "/presentation/operator.entity-graph.candidate.json"
        consolidated_relative = base + "/consolidated/nodes.review.json"
        source_contract_relative = stage + "/current-subjects.contract.md"
        review_contract_relative = stage + "/current-subjects.review.contract.md"
        candidate_path = self._write(candidate_relative, self._json_bytes({"rules": [{"name": "Artifact/Atom"}]}))
        consolidated_path = self._write(consolidated_relative, self._json_bytes({"kind": "frozen review"}))
        self._write(source_contract_relative, "source-review contract\n")
        self._write(review_contract_relative, "review-output contract\n")

        source_raw = source_path.read_bytes()
        source_sha = self._sha(source_raw)
        source = {
            "relative_path": self.source_relative,
            "full_file_sha256": source_sha,
            "atom_id": "CA-R-1",
            "version": 1,
            "quarantined": True,
            "findings": ["example_metadata_finding"],
        }
        occurrences = [
            {
                "occurrence_id": self.source_relative + "#subjects.governs",
                "source_path": self.source_relative,
                "source_atom_id": "CA-R-1",
                "source_version": 1,
                "source_sha256": source_sha,
                "field": "governs",
                "index": None,
                "old_value": "Atom",
                "quarantined": True,
            },
            {
                "occurrence_id": self.source_relative + "#subjects.depends_on[0]",
                "source_path": self.source_relative,
                "source_atom_id": "CA-R-1",
                "source_version": 1,
                "source_sha256": source_sha,
                "field": "depends_on",
                "index": 0,
                "old_value": "Relation",
                "quarantined": True,
            },
        ]
        inventory = {"selected_sources": [source], "occurrences": occurrences, "input_pins": {candidate_relative: {"path": candidate_relative, "sha256": self._sha(candidate_path.read_bytes())}}}
        inventory_relative = stage + "/current-subjects.inventory.json"
        inventory_path = self._write(inventory_relative, self._json_bytes(inventory))
        inventory_sha = self._sha(inventory_path.read_bytes())
        self.batch_relative = stage + "/inputs/current-subjects.batch-001.json"
        batch = {
            "schema_version": 1,
            "batch_id": "current-subjects.batch-001",
            "input_inventory_sha256": inventory_sha,
            "selected_sources": [source],
            "occurrences": occurrences,
        }
        batch_path = self._write(self.batch_relative, self._json_bytes(batch))
        batch_sha = self._sha(batch_path.read_bytes())
        batches = {
            "schema_version": 1,
            "inventory_path": inventory_relative,
            "batches": [
                {
                    "path": self.batch_relative,
                    "sha256": batch_sha,
                    "source_count": 1,
                    "occurrence_count": 2,
                }
            ],
        }
        self._write(stage + "/current-subjects.batches.json", self._json_bytes(batches))

        lines = source_raw.splitlines(keepends=True)
        self.body_start = next(index + 1 for index, line in enumerate(lines[1:], 1) if line.strip() == b"---") + 1
        self.body_end = len(lines)
        body_span = {
            "path": self.source_relative,
            "sha256": source_sha,
            "start_line": self.body_start,
            "end_line": self.body_end,
            "span_sha256": self._span(source_path, self.body_start, self.body_end),
            "reason": "Current Main Content establishes the reviewed source meaning.",
        }
        self.other_span = {
            "path": self.other_relative,
            "sha256": self._sha(other_path.read_bytes()),
            "start_line": 5,
            "end_line": 5,
            "span_sha256": self._span(other_path, 5, 5),
            "reason": "Unrelated current content.",
        }
        evidence_pins = {
            "frozen_candidate": {"path": candidate_relative, "sha256": self._sha(candidate_path.read_bytes())},
            "consolidated_review": {
                "path": consolidated_relative,
                "sha256": self._sha(consolidated_path.read_bytes()),
                "captured_core_commit": "a971d0e00c33c779f485fc8cad63194894d440fb",
            },
            "source_contract": {
                "path": source_contract_relative,
                "sha256": self._sha((self.root / source_contract_relative).read_bytes()),
            },
            "review_contract": {
                "path": review_contract_relative,
                "sha256": self._sha((self.root / review_contract_relative).read_bytes()),
            },
        }
        rows = []
        for index, occurrence in enumerate(occurrences):
            row = copy.deepcopy(occurrence)
            if index == 0:
                row.update(
                    {
                        "decision": "proposed",
                        "proposed_value": "Artifact/Atom",
                        "confidence": 0.95,
                        "reason": "Current meaning supports the candidate's exact Artifact/Atom identity.",
                        "candidate_basis": [{"pointer": "/rules/0/name", "reason": "Exact confirmed candidate value."}],
                    }
                )
            else:
                row.update(
                    {
                        "decision": "unresolved",
                        "proposed_value": None,
                        "confidence": 0.50,
                        "reason": "Current meaning does not settle a canonical replacement.",
                        "candidate_basis": [],
                    }
                )
            row.update(
                {
                    "evidence": [copy.deepcopy(body_span)],
                    "preserved_distinctions": ["The current role distinction is preserved."],
                    "question": None,
                    "executable": False,
                }
            )
            rows.append(row)
        review = {
            "schema_version": 1,
            "non_authoritative": True,
            "source_migration": "not_performed",
            "native_admission": "not_performed",
            "task_id": "CA-P-1992",
            "batch_id": batch["batch_id"],
            "input_batch_path": self.batch_relative,
            "input_batch_sha256": batch_sha,
            "input_inventory_sha256": inventory_sha,
            "evidence_pins": evidence_pins,
            "source_reviews": [
                {
                    **source,
                    "main_content_read": True,
                    "finding_dispositions": [
                        {"finding": "example_metadata_finding", "reason": "Retained as a quarantined metadata finding."}
                    ],
                    "questions": [],
                }
            ],
            "occurrences": rows,
        }
        self.review_path = self._write(stage + "/reviews/current-subjects.batch-001.review.json", self._json_bytes(review))

    def test_named_evidence_pin_fixture_passes(self) -> None:
        result = verifier.verify_review(self.root, 1, self._review())
        self.assertEqual(result["outcome"], "PASS")
        self.assertEqual(result["sources"], 1)
        self.assertEqual(result["occurrences"], 2)

    def test_list_evidence_pins_are_accepted_too(self) -> None:
        review = self._review()
        review["evidence_pins"] = list(review["evidence_pins"].values())
        self._save_review(review)
        self.assertEqual(verifier.verify_review(self.root, 1, self._review())["outcome"], "PASS")

    def test_structured_main_content_read_record_is_accepted(self) -> None:
        review = self._review()
        review["source_reviews"][0]["main_content_read"] = {
            "path": self.source_relative,
            "sha256": self._sha((self.root / self.source_relative).read_bytes()),
            "start_line": self.body_start,
            "end_line": self.body_end,
            "span_sha256": self._span(self.root / self.source_relative, self.body_start, self.body_end),
        }
        self._save_review(review)
        self.assertEqual(verifier.verify_review(self.root, 1, self._review())["outcome"], "PASS")

    def test_wrong_occurrence_is_rejected(self) -> None:
        review = self._review()
        review["occurrences"][0]["old_value"] = "Forged"
        self._save_review(review)
        self._assert_rejected()

    def test_missing_occurrence_is_rejected(self) -> None:
        review = self._review()
        review["occurrences"].pop()
        self._save_review(review)
        self._assert_rejected()

    def test_source_pin_change_is_rejected(self) -> None:
        source = self.root / self.source_relative
        source.write_bytes(source.read_bytes() + b"\nCurrent bytes changed.\n")
        self._assert_rejected()

    def test_evidence_pin_change_is_rejected(self) -> None:
        review = self._review()
        review["evidence_pins"]["frozen_candidate"]["sha256"] = self._sha(b"stale")
        self._save_review(review)
        self._assert_rejected()

    def test_unrelated_source_span_is_rejected(self) -> None:
        review = self._review()
        review["occurrences"][0]["evidence"] = [copy.deepcopy(self.other_span)]
        self._save_review(review)
        self._assert_rejected()

    def test_metadata_only_span_is_rejected(self) -> None:
        review = self._review()
        metadata_span = review["occurrences"][0]["evidence"][0]
        metadata_span["start_line"] = 1
        metadata_span["end_line"] = 1
        metadata_span["span_sha256"] = self._span(self.root / self.source_relative, 1, 1)
        self._save_review(review)
        self._assert_rejected()

    def test_wrong_span_digest_is_rejected(self) -> None:
        review = self._review()
        review["occurrences"][0]["evidence"][0]["span_sha256"] = self._sha(b"wrong span")
        self._save_review(review)
        self._assert_rejected()

    def test_candidate_pointer_absent_is_rejected(self) -> None:
        review = self._review()
        review["occurrences"][0]["candidate_basis"][0]["pointer"] = "/rules/99/name"
        self._save_review(review)
        self._assert_rejected()

    def test_low_confidence_decided_value_is_rejected(self) -> None:
        review = self._review()
        review["occurrences"][0]["confidence"] = 0.89
        self._save_review(review)
        self._assert_rejected()

    def test_executable_true_is_rejected(self) -> None:
        review = self._review()
        review["occurrences"][0]["executable"] = True
        self._save_review(review)
        self._assert_rejected()

    def test_missing_finding_disposition_is_rejected(self) -> None:
        review = self._review()
        review["source_reviews"][0]["finding_dispositions"] = []
        self._save_review(review)
        self._assert_rejected()


if __name__ == "__main__":
    unittest.main()
