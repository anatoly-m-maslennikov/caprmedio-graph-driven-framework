"""Status authority keeps its exact Role across legacy and approved separators."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
from typing import Any
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import authoritative_status_models as models  # noqa: E402
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS  # noqa: E402


class StatusModelSubjectNotationTests(unittest.TestCase):
    def setUp(self) -> None:
        scratch = TOOLS.parents[2] / ".caprmedio_tmp/tests/status-subject-notation"
        scratch.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[project]\nname = "status-subject-notation"\n[paths]\ncontrol_root = ".caprmedio_caprmedio"\n',
            encoding="utf-8",
        )
        rows = write_scope_unit_declarations(
            self.root, ({"scope_unit_name": "METHODOLOGY_SOURCES", "parent": "PROJECT"},),
            control_root=control,
        )
        self.source_path = rows["METHODOLOGY_SOURCES"]["authority_path"] / "status.md"
        self.source_path.parent.mkdir(parents=True)

    def source(self, governed: str, role: str = "Requirement") -> None:
        self.source_path.write_text(
            "---\natom_id: CA-R-999001\ncontent_role: Requirement\n"
            "status: Active\nversion: 1\nsubjects:\n"
            f"  governs: {json.dumps(governed)}\n---\n# Summary\n\nStatus fixture\n"
            "\n## Claim\n\n"
            f"the Core allowed values of {role} Status **must** be exactly "
            "(Draft, Active, Archived).\n",
            encoding="utf-8",
        )

    def resolve(self, role: str, *, indexed: bool, atom_type: str | None = None) -> dict[str, Any]:
        atom = {"content_role": role}
        if atom_type is not None:
            atom["type"] = atom_type
        reader = ReadContext(roots=[str(self.root)], limits=dict(CEILINGS))
        index = models.capture_status_models(self.root, reader) if indexed else None
        result = models.resolve_status_model(self.root, atom, "Active", _index=index)
        if index is not None:
            models.revalidate_status_models(index, reader)
        return result

    def test_legacy_and_dot_dependent_status_preserve_each_exact_role(self) -> None:
        for role in (
            "Concern",
            "Analysis",
            "Plan",
            "Requirement",
            "Method",
            "Evaluation",
            "Delivery",
            "Operations",
        ):
            for separator in ("/", "."):
                with self.subTest(role=role, separator=separator):
                    self.source(f"Atom/Content Role: {role}{separator}Status", role)
                    direct = self.resolve(role, indexed=False)
                    self.assertEqual(direct, self.resolve(role, indexed=True))
                    self.assertEqual(role, direct["content_role"])
                    self.assertEqual(["Draft", "Active", "Archived"], direct["statuses"])

    def test_legacy_and_dot_dependent_type_models_retain_exact_type(self) -> None:
        for tail in ("", "/Status", ".Status"):
            with self.subTest(tail=tail):
                self.source(f"Atom/Content Role: Operations/Type: Action{tail}", "Operations")
                direct = self.resolve("Operations", indexed=False, atom_type="Action")
                self.assertEqual(
                    direct, self.resolve("Operations", indexed=True, atom_type="Action")
                )
                self.assertEqual("Action", direct["type"])

    def test_governed_role_prefix_and_unknown_role_cannot_match_declared_requirement(self) -> None:
        for governed_role in ("Requirements", "RequirementExtra", "Unknown"):
            for separator in ("/", "."):
                self.source(f"Atom/Content Role: {governed_role}{separator}Status")
                for indexed in (False, True):
                    with self.subTest(role=governed_role, separator=separator, indexed=indexed):
                        with self.assertRaises(models.StatusModelError) as raised:
                            self.resolve("Requirement", indexed=indexed)
                        self.assertEqual("source-invalid", raised.exception.code)

    def test_target_role_prefix_and_unknown_role_do_not_widen_model_selection(self) -> None:
        self.source("Atom/Content Role: Requirement.Status")
        for role in ("Requirements", "RequirementExtra", "Unknown"):
            for indexed in (False, True):
                with self.subTest(role=role, indexed=indexed):
                    with self.assertRaises(models.StatusModelError) as raised:
                        self.resolve(role, indexed=indexed)
                    self.assertEqual("model-missing", raised.exception.code)

    def test_nested_authority_and_target_preserve_exact_role_and_form(self) -> None:
        for role, form in (("Requirement", "Rule"), ("Operations", "Action"), ("Analysis & Advisory", "Analysis Report")):
            governed = (
                f'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := "{role}")'
                f'/(.Header.Context.Form := "{form}").Header.State.Status'
            )
            self.source(governed, role)
            body = self.source_path.read_text().split("---\n", 2)[2]
            raw = (
                "---\nidentity:\n  atom_id: CA-R-999001\n"
                "context:\n  role: Requirement\n  form: Rule\n  topics:\n"
                f"    main_subject: {json.dumps(governed)}\n"
                "state:\n  status: Active\n  version: 1\n---\n" + body
            ).encode()
            self.source_path.write_bytes(raw)
            target_front = f"context:\n  role: {json.dumps(role)}\n  form: {json.dumps(form)}\n"
            for indexed in (False, True):
                with self.subTest(role=role, form=form, indexed=indexed):
                    reader = ReadContext(roots=[str(self.root)], limits=dict(CEILINGS))
                    index = models.capture_status_models(self.root, reader) if indexed else None
                    result = models.resolve_status_model(self.root, {"frontmatter": target_front}, "Active", _index=index)
                    self.assertEqual((role, form), (result["content_role"], result["type"]))
                    self.assertEqual(["Draft", "Active", "Archived"], result["statuses"])
                    if index is not None:
                        models.revalidate_status_models(index, reader)
                    self.assertEqual(raw, self.source_path.read_bytes())

    def test_nested_selector_wrong_role_and_undeclared_property_paths_refuse(self) -> None:
        for selector in (
            'Atom/(.Header.Context.Role := Requirements).Header.State.Status',
            'Atom/(.Header.State.Role := Requirement).Header.State.Status',
            'Atom/(.Header.Context.Role := Requirement).Header.Context.Status',
        ):
            self.source(selector)
            with self.subTest(selector=selector), self.assertRaises(models.StatusModelError) as raised:
                self.resolve("Requirement", indexed=True)
            self.assertEqual("source-invalid", raised.exception.code)

    def test_conflicting_nested_target_role_is_a_target_refusal(self) -> None:
        self.source("Atom/Content Role: Requirement.Status")
        for atom in (
            {"role": "Requirement", "context": {"role": "Operations"}},
            {"frontmatter": "role: Requirement\ncontext:\n  role: Operations\n"},
        ):
            with self.subTest(atom=atom), self.assertRaises(models.StatusModelError) as raised:
                models.resolve_status_model(self.root, atom, "Active")
            self.assertEqual("target-invalid", raised.exception.code)


if __name__ == "__main__":
    unittest.main()
