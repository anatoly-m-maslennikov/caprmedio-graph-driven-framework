"""A batch can update its grammar Subject before the next native mutation."""

import hashlib
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parent.parent / "201_TOOLS"
for location in (APP, TOOLS, TOOLS / "tests"):
    sys.path.insert(0, str(location))

import atom_operations as operations  # noqa: E402
from lifecycle_intents import carrier_descriptor  # noqa: E402
from subject_batch_authorization import (  # noqa: E402
    capture_batch_review,
    persist_subject_batch_confirmation,
)
from subject_batch_fixture import SubjectBatchProject  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers import proposed_carrier as admission  # noqa: E402


class SubjectBatchSelfRuleTests(unittest.TestCase):
    def test_grammar_subject_update_then_next_atom_uses_current_grammar(self):
        project = SubjectBatchProject(self, count=1)
        operators = project.root / ".caprmedio_caprmedio/operators_registry.toml"
        operators.write_text(
            operators.read_text()
            + ('\n[[operators]]\nname="Anatoly Maslennikov"\nrole="project owner"\n')
        )
        structure = project.root / ".caprmedio_caprmedio/project_structure.toml"
        structure.write_text(
            structure.read_text()
            + (
                '\n[[scope_units]]\nscope_unit_name="CORE_META_MODEL"\nparent="PROJECT"\n'
                'scope_unit_type="Unordered"\nscope_unit_label="FEATURE"\nstructural_level=1\n'
                'navigational_order_number=2\nauthority_path=".caprmedio_caprmedio/'
                '101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL"\n'
                'delivery_path="delivery/CORE_META_MODEL"\n'
            )
        )
        context = admission.source_context_from_project(project.root)
        binding = next(
            row["binding"]
            for row in context.inputs["sources"]
            if row["binding"]["atom_id"] == "CA-D-276"
        )
        rule = Path(binding["path"])
        before = rule.read_bytes()
        target = carrier_descriptor(project.root, rule.relative_to(project.root).as_posix())
        old = operations.parse_carrier(before, rule).metadata["subjects"]["governs"]
        project.packet["atoms"].insert(
            0,
            {
                "target": target,
                "subject_patches": [
                    {
                        "field": "governs",
                        "old": old,
                        "new": "Markdown Atom Carrier.YAML Frontmatter",
                    }
                ],
            },
        )
        project.git(
            "add",
            ".caprmedio_caprmedio/project_structure.toml",
            ".caprmedio_caprmedio/operators_registry.toml",
        )
        project.git(
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "--quiet",
            "-m",
            "Fixture grammar scope",
        )
        project.packet["git_checkpoint"] = project.git("rev-parse", "HEAD").strip()
        project.save_packet()
        runner, frozen = project.execution("subject-batch-self-rule")
        review = capture_batch_review(runner, frozen)
        persist_subject_batch_confirmation(runner, frozen, review, operator_name="golden-operator")
        captures, original = [], admission.source_context_from_project

        def observe(root):
            current = original(root)
            captures.append(
                next(
                    row["binding"]
                    for row in current.inputs["sources"]
                    if row["binding"]["atom_id"] == "CA-D-276"
                )
            )
            return current

        with patch.object(admission, "source_context_from_project", side_effect=observe):
            result = runner.dispatch(frozen)
        self.assertEqual("terminal", result["disposition"])
        after = operations.parse_carrier(rule.read_bytes(), rule)
        self.assertEqual(target["version"] + 1, after.metadata["version"], repr(result))
        self.assertNotEqual(project.before[project.paths[0]], project.paths[0].read_bytes())
        after_digest = hashlib.sha256(rule.read_bytes()).hexdigest()
        self.assertTrue(
            any(
                row["version"] == after.metadata["version"] and row["sha256"] == after_digest
                for row in captures
            )
        )
        archive = rule.parent / "archive" / f"{rule.stem}@{target['version']}.md"
        self.assertEqual(before, archive.read_bytes())


if __name__ == "__main__":
    unittest.main()
