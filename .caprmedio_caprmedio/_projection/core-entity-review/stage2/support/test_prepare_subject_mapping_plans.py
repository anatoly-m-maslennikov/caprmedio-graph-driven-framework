"""Focused tests for the one-off current-Subject review Plan printer."""

from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[4]
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import verify_current_inventory as verifier


SPEC = importlib.util.spec_from_file_location("prepare_subject_mapping_plans", HERE / "prepare_subject_mapping_plans.py")
assert SPEC and SPEC.loader
planner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(planner)


class PrepareSubjectMappingPlansTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(
            dir=REPO_ROOT / ".caprmedio_tmp", prefix="prepare-subject-plans-"
        )
        self.root = Path(self.temporary.name)
        self._create_fixture()
        self.original_root = planner.ROOT
        planner.ROOT = self.root

    def tearDown(self) -> None:
        planner.ROOT = self.original_root
        self.temporary.cleanup()

    def _write(self, relative: str, content: str | bytes) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content.encode("utf-8") if isinstance(content, str) else content)
        return path

    def _sha(self, path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def _pin(self, relative: str) -> dict[str, str]:
        return {"path": relative, "sha256": self._sha(self.root / relative)}

    def _create_fixture(self) -> None:
        self._write(
            ".caprmedio_caprmedio/project_structure.toml",
            """schema_version = 1

[[scope_units]]
scope_unit_name = "CORE_META_MODEL"
authority_path = ".caprmedio_caprmedio/current-core"
""",
        )
        for relative, content in {
            ".caprmedio_caprmedio/_projection/core-entity-review/presentation/operator.entity-graph.candidate.json": "{}\n",
            ".caprmedio_caprmedio/_projection/core-entity-review/consolidated/nodes.review.json": "{}\n",
            ".caprmedio_caprmedio/_projection/core-entity-review/consolidated/contract.md": "review\n",
            ".caprmedio_caprmedio/_projection/core-entity-review/baseline.inventory.json": "{}\n",
            ".caprmedio_caprmedio/_projection/core-entity-review/stage2/current-subjects.contract.md": "preparation\n",
            ".caprmedio_caprmedio/_projection/core-entity-review/stage2/current-subjects.review.contract.md": "review output\n",
        }.items():
            self._write(relative, content)

        depends_on = ", ".join(f"Dependency{index}" for index in range(1, 120))
        for number in range(1, 52):
            self._write(
                f".caprmedio_caprmedio/current-core/04_requirement/CA-R-{number}.md",
                f"""---
atom_id: CA-R-{number}
content_role: Requirement
current_scope_unit: CORE_META_MODEL
status: Active
author: Tester
version: 1
updated_at: "2026-10-11 00:00:00 +0400"
subjects:
  governs: Entity{number}
  depends_on: [{depends_on}]
---
# Claim
""",
            )

        expected = verifier.enumerate_current_sources(self.root)
        inventory = {
            "schema_version": 1,
            "non_authoritative": True,
            "source_migration": "not_performed",
            "native_admission": "not_performed",
            "input_pins": verifier.expected_input_pins(self.root, expected["structure"]),
            "selected_sources": expected["selected_sources"],
            "excluded_sources": expected["excluded_sources"],
            "diagnostics": expected["diagnostics"],
            "occurrences": expected["occurrences"],
        }
        stage = self.root / planner.STAGE
        inventory_path = stage / "current-subjects.inventory.json"
        inventory_bytes = json.dumps(inventory, indent=2, sort_keys=True).encode("utf-8") + b"\n"
        inventory_path.parent.mkdir(parents=True, exist_ok=True)
        inventory_path.write_bytes(inventory_bytes)
        inventory_sha = hashlib.sha256(inventory_bytes).hexdigest()

        descriptors: list[dict[str, object]] = []
        groups = verifier._batch_groups(expected["selected_sources"], expected["occurrences"])
        self.assertEqual(len(groups), 51)
        for number, group in enumerate(groups, start=1):
            name = f"current-subjects.batch-{number:03d}.json"
            group_paths = {source["relative_path"] for source in group}
            batch = {
                "schema_version": 1,
                "batch_id": Path(name).stem,
                "input_inventory_sha256": inventory_sha,
                "selected_sources": group,
                "occurrences": [
                    occurrence
                    for occurrence in expected["occurrences"]
                    if occurrence["source_path"] in group_paths
                ],
            }
            raw = json.dumps(batch, indent=2, sort_keys=True).encode("utf-8") + b"\n"
            relative = f".caprmedio_caprmedio/_projection/core-entity-review/stage2/inputs/{name}"
            self._write(relative, raw)
            descriptors.append(
                {
                    "path": relative,
                    "sha256": hashlib.sha256(raw).hexdigest(),
                    "source_count": len(group),
                    "occurrence_count": len(batch["occurrences"]),
                }
            )
        manifest = {
            "schema_version": 1,
            "inventory_path": ".caprmedio_caprmedio/_projection/core-entity-review/stage2/current-subjects.inventory.json",
            "batches": descriptors,
            "source_count": len(expected["selected_sources"]),
            "occurrence_count": len(expected["occurrences"]),
        }
        manifest_relative = ".caprmedio_caprmedio/_projection/core-entity-review/stage2/current-subjects.batches.json"
        self._write(manifest_relative, json.dumps(manifest, indent=2, sort_keys=True) + "\n")

        for relative in (
            ".caprmedio_caprmedio/_projection/core-entity-review/stage2/support/inventory_current_subjects.py",
            ".caprmedio_caprmedio/_projection/core-entity-review/stage2/support/compare_current_snapshot.py",
            ".caprmedio_caprmedio/_projection/core-entity-review/stage2/current-snapshot.delta.json",
            ".caprmedio_caprmedio/_projection/core-entity-review/stage2/support/verify_current_inventory.py",
            ".caprmedio_caprmedio/_projection/core-entity-review/stage2/support/test_current_inventory.py",
        ):
            self._write(relative, "fixture\n")
        inventory_relative = ".caprmedio_caprmedio/_projection/core-entity-review/stage2/current-subjects.inventory.json"
        receipt_outputs = {
            "CA-P-1988": [
                ".caprmedio_caprmedio/_projection/core-entity-review/stage2/support/inventory_current_subjects.py",
                inventory_relative,
                manifest_relative,
            ],
            "CA-P-1989": [
                ".caprmedio_caprmedio/_projection/core-entity-review/stage2/support/compare_current_snapshot.py",
                ".caprmedio_caprmedio/_projection/core-entity-review/stage2/current-snapshot.delta.json",
            ],
            "CA-P-1990": [
                ".caprmedio_caprmedio/_projection/core-entity-review/stage2/support/verify_current_inventory.py",
                ".caprmedio_caprmedio/_projection/core-entity-review/stage2/support/test_current_inventory.py",
            ],
        }
        for task, outputs in receipt_outputs.items():
            receipt: dict[str, object] = {
                "task": task,
                "result": "PASS: fixture",
                "outputs": [self._pin(relative) for relative in outputs],
            }
            if task == "CA-P-1989":
                receipt["checks"] = {"current_inventory_sha256": inventory_sha}
            if task == "CA-P-1990":
                receipt["input_pins"] = {
                    "inventory": inventory_sha,
                    "batches_manifest": self._sha(self.root / manifest_relative),
                }
            self._write(
                f".caprmedio_caprmedio/_projection/core-entity-review/stage2/task-{task.removeprefix('CA-P-')}.receipt.json",
                json.dumps(receipt, indent=2, sort_keys=True) + "\n",
            )

    def _run(self, *arguments: str) -> str:
        output = io.StringIO()
        with patch.object(sys, "argv", ["prepare_subject_mapping_plans.py", *arguments]), contextlib.redirect_stdout(output):
            planner.main()
        return output.getvalue()

    def _valid_arguments(self) -> tuple[str, ...]:
        return ("--first-id", "1992", "--timestamp", "2026-10-11 00:00:00 +0400", "--start", "0", "--stop", "1")

    def test_happy_path_prints_pinned_review_plan_with_relations(self) -> None:
        patch_text = self._run(*self._valid_arguments())
        self.assertIn("atom_id: CA-P-1992", patch_text)
        self.assertIn('depends_on: ["CA-P-1972", "CA-P-1988", "CA-P-1989", "CA-P-1990"]', patch_text)
        self.assertIn("current-subjects.review.contract.md", patch_text)
        self.assertIn("CA-P-2043", patch_text)
        integration = self._run(
            "--first-id", "1992", "--timestamp", "2026-10-11 00:00:00 +0400", "--start", "51", "--stop", "52"
        )
        self.assertIn("atom_id: CA-P-2043", integration)
        self.assertIn("CA-P-1992", integration)
        self.assertIn("CA-P-2042", integration)

    def test_wrong_first_id_is_refused(self) -> None:
        with self.assertRaisesRegex(SystemExit, "expected --first-id 1992"):
            self._run("--first-id", "1991", "--timestamp", "2026-10-11 00:00:00 +0400")

    def test_stale_batch_is_refused_before_printing(self) -> None:
        path = self.root / ".caprmedio_caprmedio/_projection/core-entity-review/stage2/inputs/current-subjects.batch-001.json"
        path.write_bytes(b"{}\n")
        with self.assertRaisesRegex(SystemExit, "inventory verification failed"):
            self._run(*self._valid_arguments())

    def test_frontmatter_collision_in_renamed_carrier_is_refused(self) -> None:
        self._write(
            ".caprmedio_caprmedio/renamed-carrier.md",
            """---
atom_id: CA-P-1992
content_role: Plan
---
# Renamed
""",
        )
        with self.assertRaisesRegex(SystemExit, "Plan ID already exists in carrier frontmatter: CA-P-1992"):
            self._run(*self._valid_arguments())

    def test_equivalent_yaml_atom_ids_in_renamed_carrier_are_refused(self) -> None:
        for declaration in (
            '"atom_id": CA-P-1992',
            "atom_id : CA-P-1992",
            "atom_id: !!str CA-P-1992",
            "atom_id: &plan CA-P-1992",
        ):
            with self.subTest(declaration=declaration):
                self._write(
                    ".caprmedio_caprmedio/renamed-carrier.md",
                    "---\n" + declaration + "\ncontent_role: Plan\n---\n# Renamed\n",
                )
                with self.assertRaisesRegex(SystemExit, "Plan ID already exists in carrier frontmatter: CA-P-1992"):
                    self._run(*self._valid_arguments())

    def test_malformed_carrier_cannot_silently_reserve_a_plan_id(self) -> None:
        self._write(
            ".caprmedio_caprmedio/malformed-renamed-carrier.md",
            """---
atom_id: CA-P-1992
atom_id: CA-P-1992
---
# Malformed
""",
        )
        with self.assertRaisesRegex(SystemExit, "malformed carrier could reserve generated Plan ID"):
            self._run(*self._valid_arguments())


if __name__ == "__main__":
    unittest.main()
