"""Isolated regression tests for the CA-P-1972 current inventory verifier."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("verify_current_inventory", HERE / "verify_current_inventory.py")
assert SPEC and SPEC.loader
verifier = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verifier)


class CurrentInventoryVerifierTests(unittest.TestCase):
    def setUp(self) -> None:
        scratch = verifier.ROOT / ".caprmedio_tmp"
        scratch.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(
            dir=scratch,
            prefix="current-inventory-",
            ignore_cleanup_errors=True,
        )
        self.root = Path(self.temporary.name)
        self._create_fixture()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _write(self, relative: str, content: str | bytes) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content.encode() if isinstance(content, str) else content)
        return path

    @staticmethod
    def _json_bytes(value: dict) -> bytes:
        return json.dumps(value, indent=2, sort_keys=True).encode() + b"\n"

    @staticmethod
    def _sha(raw: bytes) -> str:
        return hashlib.sha256(raw).hexdigest()

    def _create_fixture(self) -> None:
        structure = """schema_version = 1

[[scope_units]]
scope_unit_name = "CORE_META_MODEL"
authority_path = ".caprmedio_caprmedio/current-core"
"""
        self._write(".caprmedio_caprmedio/project_structure.toml", structure)
        self._write(".caprmedio_caprmedio/_projection/core-entity-review/presentation/operator.entity-graph.candidate.json", "{}\n")
        self._write(".caprmedio_caprmedio/_projection/core-entity-review/consolidated/nodes.review.json", "{}\n")
        self._write(".caprmedio_caprmedio/_projection/core-entity-review/consolidated/contract.md", "review\n")
        self._write(".caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json", "{}\n")
        self._write(
            ".caprmedio_caprmedio/current-core/04_requirement/CA-R-1.md",
            """---
atom_id: CA-R-1
content_role: Requirement
current_scope_unit: CORE_META_MODEL
status: Active
author: Tester
version: 1
updated_at: "2026-10-11 00:00:00 +0400"
subjects:
  governs: Entity
  depends_on: [Atom, Subject]
---
# Claim

Example.
""",
        )
        self._write(
            ".caprmedio_caprmedio/current-core/05_method/CA-M-2.md",
            """---
atom_id: CA-M-2
content_role: Method
current_scope_unit: CORE_META_MODEL
status: Active
author: Tester
version: 2
updated_at: 2026-10-11
subjects:
  governs: Method
---
# Procedure

Example.
""",
        )
        self._write(
            ".caprmedio_caprmedio/current-core/06_evaluation/CA-E-3.md",
            """---
atom_id: CA-E-3
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
status: Active
author: Tester
version: 3
updated_at: "2026-10-11 00:00:00 +0400"
subjects: malformed
---
# Case

Malformed Subjects shape is preserved for review.
""",
        )
        self._write(
            ".caprmedio_caprmedio/current-core/06_evaluation/excluded.md",
            """---
atom_id: CA-E-X
content_role: Evaluation
current_scope_unit: PROJECT_CONFIGURATION
status: Active
version: 1
updated_at: "2026-10-11"
subjects:
  governs: Entity
---
# Condition

Excluded.
""",
        )
        self._write(
            ".caprmedio_caprmedio/current-core/04_requirement/archive/broken.md",
            b"not a carrier and intentionally not UTF-8: \xff\n",
        )
        self._write(
            ".caprmedio_caprmedio/current-core/05_method/broken.md",
            "not a carrier\n",
        )

        requirement_path = ".caprmedio_caprmedio/current-core/04_requirement/CA-R-1.md"
        method_path = ".caprmedio_caprmedio/current-core/05_method/CA-M-2.md"
        evaluation_path = ".caprmedio_caprmedio/current-core/06_evaluation/CA-E-3.md"
        requirement_raw = (self.root / requirement_path).read_bytes()
        method_raw = (self.root / method_path).read_bytes()
        evaluation_raw = (self.root / evaluation_path).read_bytes()
        expected_sources = [
            {
                "relative_path": requirement_path,
                "full_file_sha256": self._sha(requirement_raw),
                "atom_id": "CA-R-1",
                "version": 1,
                "role": "Requirement",
                "owner": "CORE_META_MODEL",
                "author": "Tester",
                "status": "Active",
                "updated_at": "2026-10-11 00:00:00 +0400",
                "updated_at_type": "str",
                "quarantined": False,
                "findings": [],
            },
            {
                "relative_path": method_path,
                "full_file_sha256": self._sha(method_raw),
                "atom_id": "CA-M-2",
                "version": 2,
                "role": "Method",
                "owner": "CORE_META_MODEL",
                "author": "Tester",
                "status": "Active",
                "updated_at": "2026-10-11",
                "updated_at_type": "date",
                "quarantined": True,
                "findings": ["updated_at_invalid_or_naive"],
            },
            {
                "relative_path": evaluation_path,
                "full_file_sha256": self._sha(evaluation_raw),
                "atom_id": "CA-E-3",
                "version": 3,
                "role": "Evaluation",
                "owner": "CORE_META_MODEL",
                "author": "Tester",
                "status": "Active",
                "updated_at": "2026-10-11 00:00:00 +0400",
                "updated_at_type": "str",
                "quarantined": True,
                "findings": ["subjects_not_mapping", "governs_missing_or_invalid"],
            },
        ]
        expected_occurrences = [
            {
                "occurrence_id": f"{requirement_path}#subjects.depends_on[0]",
                "source_path": requirement_path,
                "source_atom_id": "CA-R-1",
                "source_version": 1,
                "source_sha256": self._sha(requirement_raw),
                "field": "depends_on",
                "index": 0,
                "old_value": "Atom",
                "quarantined": False,
            },
            {
                "occurrence_id": f"{requirement_path}#subjects.depends_on[1]",
                "source_path": requirement_path,
                "source_atom_id": "CA-R-1",
                "source_version": 1,
                "source_sha256": self._sha(requirement_raw),
                "field": "depends_on",
                "index": 1,
                "old_value": "Subject",
                "quarantined": False,
            },
            {
                "occurrence_id": f"{requirement_path}#subjects.governs",
                "source_path": requirement_path,
                "source_atom_id": "CA-R-1",
                "source_version": 1,
                "source_sha256": self._sha(requirement_raw),
                "field": "governs",
                "index": None,
                "old_value": "Entity",
                "quarantined": False,
            },
            {
                "occurrence_id": f"{method_path}#subjects.governs",
                "source_path": method_path,
                "source_atom_id": "CA-M-2",
                "source_version": 2,
                "source_sha256": self._sha(method_raw),
                "field": "governs",
                "index": None,
                "old_value": "Method",
                "quarantined": True,
            },
        ]
        expected_occurrences.sort(key=lambda item: item["occurrence_id"])
        expected_excluded = [
            {
                "relative_path": ".caprmedio_caprmedio/current-core/04_requirement/archive/broken.md",
                "reason": "archived_lifecycle_copy",
            },
            {
                "relative_path": ".caprmedio_caprmedio/current-core/05_method/broken.md",
                "reason": "strict_parse_error",
                "code": "CARRIER_INVALID",
                "detail": "Unreadable UTF-8 or malformed frontmatter.",
            },
            {
                "relative_path": ".caprmedio_caprmedio/current-core/06_evaluation/excluded.md",
                "reason": "owner_mismatch",
                "content_role": "Evaluation",
                "current_scope_unit": "PROJECT_CONFIGURATION",
                "status": "Active",
            },
        ]
        pin_paths = {
            "structure": ".caprmedio_caprmedio/project_structure.toml",
            ".caprmedio_caprmedio/_projection/core-entity-review/presentation/operator.entity-graph.candidate.json": ".caprmedio_caprmedio/_projection/core-entity-review/presentation/operator.entity-graph.candidate.json",
            ".caprmedio_caprmedio/_projection/core-entity-review/consolidated/nodes.review.json": ".caprmedio_caprmedio/_projection/core-entity-review/consolidated/nodes.review.json",
            ".caprmedio_caprmedio/_projection/core-entity-review/consolidated/contract.md": ".caprmedio_caprmedio/_projection/core-entity-review/consolidated/contract.md",
            ".caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json": ".caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json",
        }
        expected_pins = {
            key: {"path": relative, "sha256": self._sha((self.root / relative).read_bytes())}
            for key, relative in pin_paths.items()
        }
        inventory = {
            "schema_version": 1,
            "non_authoritative": True,
            "source_migration": "not_performed",
            "native_admission": "not_performed",
            "input_pins": expected_pins,
            "selected_sources": expected_sources,
            "excluded_sources": expected_excluded,
            "diagnostics": [
                {
                    "relative_path": ".caprmedio_caprmedio/current-core/06_evaluation/excluded.md",
                    "code": "owner_mismatch",
                    "expected": "CORE_META_MODEL",
                    "actual": "PROJECT_CONFIGURATION",
                }
            ],
            "occurrences": expected_occurrences,
        }
        stage2 = self.root / verifier.STAGE2_REL
        inputs = stage2 / "inputs"
        inputs.mkdir(parents=True)
        inventory_path = stage2 / "current-subjects.inventory.json"
        inventory_path.parent.mkdir(parents=True, exist_ok=True)
        inventory_bytes = self._json_bytes(inventory)
        inventory_path.write_bytes(inventory_bytes)
        inventory_sha = self._sha(inventory_bytes)
        name = "current-subjects.batch-001.json"
        batch = {
            "schema_version": 1,
            "batch_id": Path(name).stem,
            "input_inventory_sha256": inventory_sha,
            "selected_sources": expected_sources,
            "occurrences": expected_occurrences,
        }
        raw = self._json_bytes(batch)
        (inputs / name).write_bytes(raw)
        descriptors = [
            {
                "path": (verifier.STAGE2_REL / "inputs" / name).as_posix(),
                "sha256": self._sha(raw),
                "source_count": len(expected_sources),
                "occurrence_count": len(expected_occurrences),
            }
        ]
        batches = {
            "schema_version": 1,
            "inventory_path": (verifier.STAGE2_REL / "current-subjects.inventory.json").as_posix(),
            "batches": descriptors,
            "source_count": len(expected_sources),
            "occurrence_count": len(expected_occurrences),
        }
        (stage2 / "current-subjects.batches.json").write_bytes(self._json_bytes(batches))
        self.inventory_path = inventory_path
        self.batches_path = stage2 / "current-subjects.batches.json"
        self.expected_sources = expected_sources
        self.expected_occurrences = expected_occurrences
        self.expected_excluded = expected_excluded

    def _load(self, path: Path) -> dict:
        return json.loads(path.read_text())

    def _save(self, path: Path, value: dict) -> None:
        path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")

    def _assert_rejected(self) -> None:
        with self.assertRaises(verifier.VerificationError):
            verifier.verify_inventory(self.root)

    def test_valid_fixture_passes_with_live_pins_and_exact_partition(self) -> None:
        result = verifier.verify_inventory(self.root)
        self.assertEqual(result["outcome"], "PASS")
        self.assertEqual(result["selected_sources"], 3)
        self.assertEqual(result["excluded_sources"], 3)
        self.assertEqual(result["occurrences"], 4)
        self.assertEqual(result["batches"], 1)
        self.assertEqual(self.expected_sources[0]["owner"], "CORE_META_MODEL")
        self.assertEqual(self.expected_sources[0]["updated_at_type"], "str")
        self.assertFalse(self.expected_sources[0]["quarantined"])
        self.assertEqual(self.expected_sources[1]["updated_at_type"], "date")
        self.assertTrue(self.expected_sources[1]["quarantined"])
        self.assertEqual(self.expected_sources[2]["findings"], ["subjects_not_mapping", "governs_missing_or_invalid"])
        self.assertEqual(self.expected_excluded[0]["reason"], "archived_lifecycle_copy")
        self.assertEqual(self.expected_excluded[1]["reason"], "strict_parse_error")

    def test_missing_authoritative_structure_is_rejected(self) -> None:
        (self.root / ".caprmedio_caprmedio/project_structure.toml").unlink()
        self._assert_rejected()

    def test_wrong_occurrence_value_is_rejected(self) -> None:
        inventory = self._load(self.inventory_path)
        inventory["occurrences"][0]["old_value"] = "FORGED"
        self._save(self.inventory_path, inventory)
        self._assert_rejected()

    def test_removed_occurrence_is_rejected(self) -> None:
        inventory = self._load(self.inventory_path)
        inventory["occurrences"].pop()
        self._save(self.inventory_path, inventory)
        self._assert_rejected()

    def test_overlapping_occurrence_partition_is_rejected(self) -> None:
        batches = self._load(self.batches_path)
        first = self.root / batches["batches"][0]["path"]
        second = copy.deepcopy(self._load(first))
        second["occurrences"].append(second["occurrences"][0])
        # Keep the mutation's descriptor internally consistent so the failure
        # proves overlap accounting, rather than only a stale byte hash.
        second_path = self.root / batches["batches"][0]["path"]
        second_raw = self._json_bytes(second)
        second_path.write_bytes(second_raw)
        batches["batches"][0]["sha256"] = self._sha(second_raw)
        batches["batches"][0]["occurrence_count"] = len(second["occurrences"])
        self._save(self.batches_path, batches)
        self._assert_rejected()

    def test_stale_input_pin_is_rejected(self) -> None:
        inventory = self._load(self.inventory_path)
        inventory["input_pins"]["structure"]["sha256"] = hashlib.sha256(b"stale").hexdigest()
        self._save(self.inventory_path, inventory)
        self._assert_rejected()

    def test_batch_hash_must_cover_actual_newline_terminated_bytes(self) -> None:
        batches = self._load(self.batches_path)
        batch_path = self.root / batches["batches"][0]["path"]
        raw = batch_path.read_bytes()
        self.assertTrue(raw.endswith(b"\n"))
        batches["batches"][0]["sha256"] = self._sha(raw[:-1])
        self._save(self.batches_path, batches)
        self._assert_rejected()


if __name__ == "__main__":
    unittest.main()
