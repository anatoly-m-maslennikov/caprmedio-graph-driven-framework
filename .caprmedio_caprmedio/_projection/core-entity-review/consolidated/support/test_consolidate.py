"""Standard-library acceptance checks for the deterministic consolidator."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any


SCRIPT = Path(__file__).resolve().with_name("consolidate.py")
TEST_TMP_ROOT = SCRIPT.parents[5] / ".caprmedio_tmp/consolidation-tests"
TEST_TMP_ROOT.mkdir(parents=True, exist_ok=True)
SPEC = importlib.util.spec_from_file_location("consolidate_under_test", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules["consolidate_under_test"] = MODULE
SPEC.loader.exec_module(MODULE)


def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


class FakeSnapshot:
    COMMIT = MODULE.CAPTURED_CORE_COMMIT

    def __init__(self) -> None:
        self.raw = b"---\ntitle: Captured\n---\n# Source\n## Claim\nA captured meaning.\n"
        self.pins = {
            "SRC-1": {
                "atom_id": "SRC-1",
                "atom_revision": 1,
                "carrier_path": "fake/SRC-1.md",
                "carrier_sha256": digest(self.raw),
            },
            "SRC-2": {
                "atom_id": "SRC-2",
                "atom_revision": 1,
                "carrier_path": "fake/SRC-2.md",
                "carrier_sha256": digest(self.raw),
            },
        }

    def source_pins(self) -> dict[str, dict[str, Any]]:
        return self.pins

    def read_source(self, atom_id: str) -> bytes:
        if atom_id not in self.pins:
            raise KeyError(atom_id)
        return self.raw


def make_fixture(root: Path, *, evidence: bool = False) -> tuple[Any, FakeSnapshot]:
    base = root / "core-entity-review"
    (base / "presentation").mkdir(parents=True)
    (base / "nodes/inputs").mkdir(parents=True)
    (base / "nodes/support").mkdir(parents=True)
    (base / "consolidated/reviews").mkdir(parents=True)
    (base / "consolidated").mkdir(exist_ok=True)
    (base / "consolidated/contract.md").write_text("consolidated contract")
    fake_snapshot = FakeSnapshot()

    candidate = {"kind": "Entity Graph Candidate", "status": "Candidate", "root_entities": [{"name": name, "meaning": name} for name in MODULE.ROOT_ENTITIES]}
    candidate_raw = json.dumps(candidate, sort_keys=True).encode()
    (base / "presentation/operator.entity-graph.candidate.json").write_bytes(candidate_raw)

    baseline = {"schema_version": 1, "nodes": [{"identity": "One"}, {"identity": "Two"}]}
    baseline["inventory_sha256"] = digest(canonical({k: v for k, v in baseline.items() if k != "inventory_sha256"}))
    baseline_raw = json.dumps(baseline, sort_keys=True).encode()
    (base / "baseline.inventory.json").write_bytes(baseline_raw)

    evidence_ref = "CA-P-1928/batch-0/E-SRC-1-6"
    evidence_ref_batch_1 = "CA-P-1929/batch-1/E-SRC-1-6"
    evidence_item = {
        "atom_id": "SRC-1",
        "atom_revision": 1,
        "carrier_path": "fake/SRC-1.md",
        "carrier_sha256": digest(fake_snapshot.raw),
        "start_line": 5,
        "end_line": 6,
        "quote": "## Claim\nA captured meaning.",
        "text_sha256": digest("## Claim\nA captured meaning.".encode()),
    }
    prior_marks = []
    prior_marks.append({
        "identity": "One",
        "review_row": {"identity": "One", "disposition": "question"},
        "source_review": {"checked_source_atom_ids": ["SRC-2"]},
    })
    prior_marks.append({"identity": "Two", "review_row": {"identity": "Two", "disposition": "question"}})
    catalogue = {evidence_ref: evidence_item, evidence_ref_batch_1: evidence_item} if evidence else {}
    prior = {"schema_version": 1, "node_disposition_marks": prior_marks, "evidence_catalogue": catalogue}
    prior_raw = json.dumps(prior, sort_keys=True).encode()
    (base / "nodes/nodes.dispositions.json").write_bytes(prior_raw)

    for rel, content in (
        ("nodes/snapshot.context.md", "captured snapshot"),
        ("nodes/contract.md", "contract"),
        ("nodes/scope.omission.decision.md", "operator direction"),
        ("nodes/support/snapshot_sources.py", "# fake reader"),
    ):
        (base / rel).write_text(content)
    legacy = {
        "schema_version": 1,
        "kind": "Legacy question consolidation",
        "non_authoritative": True,
        "native_admission": "not_performed",
        "source_migration": "not_performed",
        "candidate": {"sha256": digest(candidate_raw)},
        "legacy_case_count": 47,
        "operator_questions_from_legacy_wording": 0,
        "cases": [{} for _ in range(47)],
    }
    (base / "consolidated/legacy-questions.review.json").write_text(json.dumps(legacy, sort_keys=True))

    for batch, identities in ((0, ("One",)), (1, ("Two",))):
        inp = {
            "batch": batch,
            "source_task": f"CA-P-{1928 + batch}",
            "baseline": {"sha256": digest(baseline_raw), "inventory_sha256": baseline["inventory_sha256"]},
            "nodes": [{"identity": identity, "source_atom_ids": ["SRC-1"], "governing_source_atom_ids": []} for identity in identities],
        }
        inp["partition_sha256"] = digest(canonical({k: v for k, v in inp.items() if k != "partition_sha256"}))
        (base / f"nodes/inputs/nodes.batch-{batch}.input.json").write_text(json.dumps(inp, sort_keys=True))

        rows = []
        for identity in identities:
            row = {
                "identity": identity,
                "prior_disposition": "question",
                "action": "review_required",
                "candidate_root": None,
                "candidate_path": None,
                "content_view": "unclassified",
                "confidence_percent": 80,
                "reason": "The captured meaning needs a bounded follow-up for this identity.",
                "operator_rules": ["root_entities"],
                "evidence_refs": [evidence_ref if batch == 0 else evidence_ref_batch_1] if evidence else [],
                "checked_source_atom_ids": ["SRC-1"],
                "preserved_distinctions": ["Original identity remains unchanged."],
                "question": {"kind": "source_gap", "text": "Which captured meaning supports the candidate mapping?"},
            }
            rows.append(row)
        review = {
            "schema_version": 1,
            "batch": batch,
            "kind": "Captured nodes against Operator candidate",
            "non_authoritative": True,
            "native_admission": "not_performed",
            "source_migration": "not_performed",
            "captured_core_commit": MODULE.CAPTURED_CORE_COMMIT,
            "candidate_sha256": digest(candidate_raw),
            "input_sha256": "placeholder",
            "baseline_sha256": digest(baseline_raw),
            "prior_review_sha256": digest(prior_raw),
            "review_method": "Reused old reviewed meanings, checked captured Main Content and latest Operator directions; no fresh audit is claimed.",
            "nodes": rows,
        }
        inp_raw = (base / f"nodes/inputs/nodes.batch-{batch}.input.json").read_bytes()
        review["input_sha256"] = digest(inp_raw)
        (base / f"consolidated/reviews/batch-{batch}.review.json").write_text(json.dumps(review, sort_keys=True))

    config = MODULE.ConsolidationConfig(
        base_dir=base,
        batches=(0, 1),
        expected_identity_count=2,
        expected_candidate_sha256=None,
        expected_baseline_sha256=None,
        expected_prior_review_sha256=None,
    )
    return config, fake_snapshot


class ConsolidateTests(unittest.TestCase):
    def run_fixture(self, *, evidence: bool = False) -> tuple[tempfile.TemporaryDirectory[str], Any, FakeSnapshot]:
        temp = tempfile.TemporaryDirectory(prefix="consolidation-", dir=TEST_TMP_ROOT)
        config, snapshot = make_fixture(Path(temp.name), evidence=evidence)
        original_loader = MODULE._load_snapshot_reader
        MODULE._load_snapshot_reader = lambda _config: snapshot
        self.addCleanup(lambda: setattr(MODULE, "_load_snapshot_reader", original_loader))
        return temp, config, snapshot

    def test_duplicate_and_missing_identity_is_rejected(self) -> None:
        temp, config, _ = self.run_fixture()
        self.addCleanup(temp.cleanup)
        path = config.base_dir / "nodes/inputs/nodes.batch-1.input.json"
        value = json.loads(path.read_text())
        value["nodes"] = [{"identity": "One"}]
        value["partition_sha256"] = digest(canonical({k: v for k, v in value.items() if k != "partition_sha256"}))
        path.write_text(json.dumps(value, sort_keys=True))
        with self.assertRaisesRegex(MODULE.ConsolidationError, "outside baseline|do not cover|duplicate|not disjoint"):
            MODULE.consolidate(config)

    def test_evidence_quote_hash_and_span_are_rejected(self) -> None:
        temp, config, _ = self.run_fixture(evidence=True)
        self.addCleanup(temp.cleanup)
        path = config.base_dir / "nodes/nodes.dispositions.json"
        prior = json.loads(path.read_text())
        prior["evidence_catalogue"]["CA-P-1928/batch-0/E-SRC-1-6"]["text_sha256"] = "0" * 64
        path.write_text(json.dumps(prior, sort_keys=True))
        for batch in (0, 1):
            review_path = config.base_dir / f"consolidated/reviews/batch-{batch}.review.json"
            review = json.loads(review_path.read_text())
            review["prior_review_sha256"] = digest(path.read_bytes())
            review_path.write_text(json.dumps(review, sort_keys=True))
        with self.assertRaisesRegex(MODULE.ConsolidationError, "quote hash mismatch"):
            MODULE.consolidate(config)
        prior["evidence_catalogue"]["CA-P-1928/batch-0/E-SRC-1-6"]["text_sha256"] = digest(
            "## Claim\nA captured meaning.".encode()
        )
        prior["evidence_catalogue"]["CA-P-1928/batch-0/E-SRC-1-6"]["end_line"] = 5
        path.write_text(json.dumps(prior, sort_keys=True))
        for batch in (0, 1):
            review_path = config.base_dir / f"consolidated/reviews/batch-{batch}.review.json"
            review = json.loads(review_path.read_text())
            review["prior_review_sha256"] = digest(path.read_bytes())
            review_path.write_text(json.dumps(review, sort_keys=True))
        with self.assertRaisesRegex(MODULE.ConsolidationError, "does not exactly match captured line span"):
            MODULE.consolidate(config)

    def test_low_confidence_cannot_commit_mapping(self) -> None:
        temp, config, _ = self.run_fixture()
        self.addCleanup(temp.cleanup)
        path = config.base_dir / "consolidated/reviews/batch-0.review.json"
        review = json.loads(path.read_text())
        row = review["nodes"][0]
        row["candidate_root"] = "Artifact"
        row["candidate_path"] = "Artifact/Atom"
        path.write_text(json.dumps(review, sort_keys=True))
        with self.assertRaisesRegex(MODULE.ConsolidationError, "low confidence has a candidate mapping"):
            MODULE.consolidate(config)

    def test_known_captured_but_unrelated_source_is_rejected(self) -> None:
        temp, config, _ = self.run_fixture()
        self.addCleanup(temp.cleanup)
        path = config.base_dir / "consolidated/reviews/batch-1.review.json"
        review = json.loads(path.read_text())
        review["nodes"][0]["checked_source_atom_ids"] = ["SRC-1", "SRC-2"]
        path.write_text(json.dumps(review, sort_keys=True))
        with self.assertRaisesRegex(MODULE.ConsolidationError, "not allowed for this identity"):
            MODULE.consolidate(config)

    def test_same_identity_accepted_crossprofile_source_is_allowed(self) -> None:
        temp, config, _ = self.run_fixture()
        self.addCleanup(temp.cleanup)
        path = config.base_dir / "consolidated/reviews/batch-0.review.json"
        review = json.loads(path.read_text())
        review["nodes"][0]["checked_source_atom_ids"] = ["SRC-1", "SRC-2"]
        path.write_text(json.dumps(review, sort_keys=True))
        MODULE.consolidate(config)

    def test_low_confidence_without_question_remains_review_backlog(self) -> None:
        temp, config, _ = self.run_fixture()
        self.addCleanup(temp.cleanup)
        path = config.base_dir / "consolidated/reviews/batch-0.review.json"
        review = json.loads(path.read_text())
        review["nodes"][0]["question"] = None
        path.write_text(json.dumps(review, sort_keys=True))
        MODULE.consolidate(config)

    def test_unknown_action_root_and_view_are_rejected(self) -> None:
        for field, value, expected in (
            ("action", "not_an_action", "action is unknown"),
            ("candidate_root", "Not a root", "candidate_root is unknown"),
            ("content_view", "X", "content_view is unknown"),
        ):
            temp, config, _ = self.run_fixture()
            self.addCleanup(temp.cleanup)
            path = config.base_dir / "consolidated/reviews/batch-0.review.json"
            review = json.loads(path.read_text())
            review["nodes"][0][field] = value
            path.write_text(json.dumps(review, sort_keys=True))
            with self.subTest(field=field), self.assertRaisesRegex(MODULE.ConsolidationError, expected):
                MODULE.consolidate(config)

    def test_operator_core_boundary_and_negated_audit_disclaimer(self) -> None:
        temp, config, _ = self.run_fixture()
        self.addCleanup(temp.cleanup)
        path = config.base_dir / "consolidated/reviews/batch-0.review.json"
        review = json.loads(path.read_text())
        review["review_method"] = "Reused captured Operator directions; this is a fresh exhaustive audit of all 951 sources."
        path.write_text(json.dumps(review, sort_keys=True))
        with self.assertRaisesRegex(MODULE.ConsolidationError, "overclaims source audit"):
            MODULE.consolidate(config)
        review["review_method"] = "Reused captured Operator directions and treated current Core as replacement evidence."
        path.write_text(json.dumps(review, sort_keys=True))
        with self.assertRaisesRegex(MODULE.ConsolidationError, "overclaims current Core"):
            MODULE.consolidate(config)
        review["review_method"] = "Reused old meanings from the captured snapshot and Operator directions; not a fresh exhaustive audit of all 951 source pins."
        path.write_text(json.dumps(review, sort_keys=True))
        MODULE.consolidate(config)

    def test_create_only_mismatch_has_no_partial_writes(self) -> None:
        temp, config, _ = self.run_fixture()
        self.addCleanup(temp.cleanup)
        MODULE.consolidate(config, persist=True)
        mismatch = config.base_dir / "consolidated/entity-graph.indented.txt"
        mismatch.write_text("tampered\n")
        missing = config.base_dir / "consolidated/review.summary.txt"
        missing.unlink()
        with self.assertRaisesRegex(MODULE.ConsolidationError, "existing output mismatch"):
            MODULE.consolidate(config, persist=True)
        self.assertFalse(missing.exists(), "preflight failure must not create another output")

    def test_byte_reproduction_and_verify_output(self) -> None:
        temp, config, _ = self.run_fixture()
        self.addCleanup(temp.cleanup)
        MODULE.consolidate(config, persist=True)
        before = {name: (config.base_dir / "consolidated" / name).read_bytes() for name in ("nodes.review.json", "entity-graph.indented.txt", "review.summary.txt", "manifest.json")}
        result = MODULE.consolidate(config, verify_output=True)
        self.assertEqual(result["status"], "verified")
        after = {name: (config.base_dir / "consolidated" / name).read_bytes() for name in before}
        self.assertEqual(before, after)
        self.assertNotIn(b"unspecified", after["entity-graph.indented.txt"])
        graph = after["entity-graph.indented.txt"].decode()
        self.assertIn("/ Atom:", graph)
        self.assertIn(".Summary:", graph)
        self.assertIn("one governed lifecycle; dependent Entities do not have independent lifecycles", graph)
        manifest = json.loads(after["manifest.json"])
        manifest_kinds = {item["kind"] for item in manifest["inputs"]}
        self.assertIn("legacy_question_review", manifest_kinds)
        self.assertIn("consolidated_review_contract", manifest_kinds)
        self.assertIn("consolidator_compiler_recipe", manifest_kinds)
        self.assertIn(b"Legacy question review: 47 preserved cases", after["review.summary.txt"])


if __name__ == "__main__":
    unittest.main()
