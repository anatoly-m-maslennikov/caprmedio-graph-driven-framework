"""A batch can update its grammar Subject before the next native mutation."""

from pathlib import Path
import sys
import unittest
from unittest.mock import patch

APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parent.parent / "201_TOOLS"
for location in (APP, TOOLS, TOOLS / "tests"):
    sys.path.insert(0, str(location))

import atom_operations as operations  # noqa: E402
import subject_batch_execution as batch  # noqa: E402
from lifecycle_intents import carrier_descriptor  # noqa: E402
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
        rule = Path(
            next(
                row["binding"]["path"]
                for row in context.inputs["sources"]
                if row["binding"]["atom_id"] == "CA-D-276"
            )
        )
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
        observations, original = [], batch.subject_update_action

        def observe(root, parameters, **kwargs):
            if parameters["target"] == project.targets[0]:
                observations.append(rule.read_bytes())
            return original(root, parameters, **kwargs)

        with patch.object(batch, "subject_update_action", side_effect=observe):
            result = runner.dispatch(frozen)
        self.assertEqual("terminal", result["disposition"])
        after = operations.parse_carrier(rule.read_bytes(), rule)
        self.assertEqual(target["version"] + 1, after.metadata["version"], repr(result))
        self.assertEqual([rule.read_bytes()], observations)
        next_atom = operations.parse_carrier(project.paths[0].read_bytes(), project.paths[0])
        self.assertEqual(project.targets[0]["version"] + 1, next_atom.metadata["version"])
        archive = rule.parent / "archive" / f"{rule.stem}@{target['version']}.md"
        self.assertEqual(before, archive.read_bytes())


if __name__ == "__main__":
    unittest.main()
