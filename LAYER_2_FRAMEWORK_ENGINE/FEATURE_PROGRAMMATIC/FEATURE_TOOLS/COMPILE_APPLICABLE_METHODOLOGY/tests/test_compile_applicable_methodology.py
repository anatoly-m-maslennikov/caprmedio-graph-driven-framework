from __future__ import annotations

import importlib.util
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


TOOL = Path(__file__).resolve().parents[1] / "compile_applicable_methodology.py"
SPEC = importlib.util.spec_from_file_location("compile_applicable_methodology", TOOL)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def carrier(atom_id: str, version: int = 1, extra: str = "", body: str = "claim", relations: str = "{}") -> bytes:
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "cce_version: cce_1\n"
        "cce_form: obligation\n"
        "status: Active\n"
        f"{extra}"
        f"version: {version}\n"
        "updated_at: 2026-08-27 00:00:00 +0400\n"
        f"relations: {relations}\n"
        "---\n"
        f"# {atom_id}\n\n{body}\n"
    ).encode()


def definition_carrier(atom_id: str, term: str, subject_path: str | None = None) -> bytes:
    governed = subject_path or term
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "cce_version: cce_1\n"
        "cce_form: definition\n"
        "subjects:\n"
        "  governs:\n"
        "    continuant:\n"
        f"      - {json.dumps(governed)}\n"
        "  depends_on:\n"
        "    continuant: []\n"
        "status: Active\n"
        "version: 1\n"
        "updated_at: 2026-08-29 00:00:00 +0400\n"
        "relations: {}\n"
        "---\n"
        f"# Define {term}\n\n"
        f"{term} definition.\n"
    ).encode()


class CompilerTest(unittest.TestCase):
    def test_definition_subject_accepts_scalar_governs_shorthand(self) -> None:
        frontmatter = (
            "atom_id: CA-R-001\n"
            "cce_form: definition\n"
            "subjects:\n"
            '  governs: "Evaluation For Relation"\n'
            "version: 1\n"
        )

        term, subject_path = module.definition_subject(frontmatter, "CA-R-001.md")

        self.assertEqual("Evaluation For Relation", term)
        self.assertEqual("Evaluation For Relation", subject_path)

    def test_identity_is_independent_of_mutable_filename_tokens(self) -> None:
        for name in (
            "CA-M-120-GOVERN-CORE-METHOD--old.md",
            "CA-M-120-CORE_META_MODEL-CORE-METHOD--new.md",
            "03-CA-M-120-CORE_META_MODEL-METHOD--new.md",
        ):
            self.assertEqual("CA-M-120", module.derive_atom_id(Path(name), "version: 1"))
        self.assertEqual(
            "CAPRMEDIO-E-169-EVAL_APPROACH",
            module.derive_atom_id(Path("CAPRMEDIO-E-169-CORE-EVAL_APPROACH--new.md"),
                                 'atom_id: "CAPRMEDIO-E-169-EVAL_APPROACH"'),
        )

    def setUp(self) -> None:
        from scope_declaration_test_support import write_scope_unit_declarations

        temporary = Path.cwd() / ".caprmedio_tmp/compiler-tests"
        temporary.mkdir(parents=True, exist_ok=True)
        self.temp = Path(tempfile.mkdtemp(prefix="case-", dir=temporary))
        settings = self.temp / module.SETTINGS_PATH
        settings.parent.mkdir(parents=True, exist_ok=True)
        settings.write_text(
            '[project]\nname = "caprmedio"\n[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
        )
        self.declarations = write_scope_unit_declarations(
            self.temp,
            (
                {"scope_unit_name": "METHODOLOGY_SOURCES", "parent": "PROJECT", "scope_unit_type": "Unordered"},
                {"scope_unit_name": "CORE_META_MODEL", "parent": "METHODOLOGY_SOURCES", "scope_unit_type": "Unordered"},
                {"scope_unit_name": "INSTALLED_EXTENSIONS", "parent": "METHODOLOGY_SOURCES", "scope_unit_type": "Unordered"},
                {"scope_unit_name": "PROJECT_CONFIGURATION", "parent": "METHODOLOGY_SOURCES", "scope_unit_type": "Unordered"},
            ),
        )
        self.source = Path(self.declarations["METHODOLOGY_SOURCES"]["authority_path"])
        self.output = Path(self.declarations["METHODOLOGY_SOURCES"]["delivery_path"])
        self.layers = {
            name: Path(self.declarations[name]["authority_path"])
            for name, _, _ in module.LAYERS
        }
        self.logical_layers = dict(zip(
            ("001_CORE_META_MODEL", "002_INSTALLED_EXTENSIONS", "003_PROJECT_CONFIGURATION"),
            ("CORE_META_MODEL", "INSTALLED_EXTENSIONS", "PROJECT_CONFIGURATION"),
            strict=True,
        ))
        for path in self.layers.values():
            path.mkdir(parents=True)
        (self.layers["INSTALLED_EXTENSIONS"] / ".gitkeep").write_text("")

    def tearDown(self) -> None:
        shutil.rmtree(self.temp, ignore_errors=True)

    def write(self, layer: str, role: str, name: str, data: bytes) -> Path:
        path = self.layers[self.logical_layers.get(layer, layer)] / role / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def invoke(self, *arguments: str) -> tuple[int, dict[str, object]]:
        self.assertIn(arguments, {(), ("--apply",)})
        report, candidates, snapshot = module.compile_report(self.temp)
        if report["can_apply"] and arguments == ("--apply",):
            module.replace_outputs_atomically(self.temp, module.stage_outputs(self.temp, candidates, snapshot))
        return (0 if report["can_apply"] else 2), report

    def output_digest(self) -> dict[str, bytes]:
        output = self.temp / self.output
        return {
            path.relative_to(output).as_posix(): path.read_bytes()
            for path in sorted(output.rglob("*.md"))
        }

    def test_dry_run_apply_rerun_and_regeneration_are_deterministic(self) -> None:
        source = self.write("001_CORE_META_MODEL", "04_requirement", "CA-R-001-REQUIREMENT--one.md", carrier("CA-R-001"))
        local = self.write("003_PROJECT_CONFIGURATION", "05_method", "CA-M-001-METHOD--two.md", carrier("CA-M-001", body="two"))
        before = {source: source.read_bytes(), local: local.read_bytes()}

        first_code, first = self.invoke()
        second_code, second = self.invoke()
        self.assertEqual((first_code, first), (0, second))
        self.assertEqual(first["conflict_count"], 0)

        apply_code, applied = self.invoke("--apply")
        self.assertEqual(apply_code, 0)
        first_tree = self.output_digest()
        self.assertEqual(before, {source: source.read_bytes(), local: local.read_bytes()})
        projected = self.temp / self.output / "04_requirement" / source.name
        projected_text = projected.read_text()
        self.assertIn(
            f"projection:\n  source_carrier_path: {Path(os.path.relpath(source, start=projected.parent)).as_posix()}",
            projected_text,
        )
        self.assertIn("# CA-R-001\n\nclaim", projected_text)

        rerun_code, rerun = self.invoke("--apply")
        self.assertEqual(rerun_code, 0)
        self.assertEqual(first_tree, self.output_digest())

        for _, role in module.ROLES:
            for path in (self.temp / self.output / role).glob("*"):
                path.unlink()
        regenerate_code, regenerated = self.invoke("--apply")
        self.assertEqual(regenerate_code, 0)
        self.assertEqual(first_tree, self.output_digest())
        self.assertEqual(before, {source: source.read_bytes(), local: local.read_bytes()})

    def test_nested_header_compiles_alongside_flat_source_without_rewriting_either(self) -> None:
        nested = (
            b"---\nidentity:\n  atom_id: CA-R-001\n  ref_id: CA-R-001@2\n"
            b"context:\n  role: Requirement\n  form: Rule\n  topics:\n    main_subject: Header\n    dependencies: []\n"
            b"relations: {}\nstate:\n  status: Active\n  version: 2\n"
            b'  updated_at: "2026-11-06 00:00:00 +0400"\n'
            b"destination:\n  file:\n    name: CA-R-001--nested\n    path: preserved/path\n"
            b"---\n# Claim\n\nExact nested source body.\n"
        )
        source = self.write("001_CORE_META_MODEL", "04_requirement", "CA-R-001--nested.md", nested)
        flat = self.write("003_PROJECT_CONFIGURATION", "05_method", "CA-M-001--flat.md", carrier("CA-M-001"))
        before = {source: nested, flat: flat.read_bytes()}
        candidates, diagnostics, _ = module.discover_candidates(self.temp)
        self.assertFalse(diagnostics)
        self.assertEqual({"CA-R-001": 2, "CA-M-001": 1}, {row.atom_id: row.version for row in candidates})

        code, report = self.invoke("--apply")
        self.assertEqual(0, code, report)
        projected = self.temp / self.output / "04_requirement" / source.name
        candidate = next(row for row in candidates if row.atom_id == "CA-R-001")
        relative = Path(os.path.relpath(source, start=projected.parent)).as_posix()
        module.validate_projection_source_preservation(nested, projected.read_bytes(), relative, candidate)
        self.assertEqual(before, {path: path.read_bytes() for path in before})

    def test_conflicting_flat_and_nested_state_is_a_source_diagnostic(self) -> None:
        raw = carrier("CA-R-001").replace(b"status: Active\n", b"status: Active\nstate:\n  status: Draft\n")
        source = self.write("001_CORE_META_MODEL", "04_requirement", "CA-R-001--conflict.md", raw)
        candidates, diagnostics, _ = module.discover_candidates(self.temp)
        self.assertFalse(candidates)
        self.assertIn("source-frontmatter-invalid", {row["code"] for row in diagnostics})
        self.assertEqual(raw, source.read_bytes())

    def test_ignores_ds_store_in_source_snapshot(self) -> None:
        self.write("001_CORE_META_MODEL", "04_requirement", "CA-R-001--one.md", carrier("CA-R-001"))
        places = module.methodology_paths(self.temp)
        snapshot = module.source_state_snapshot(self.temp, places)

        (self.layers["CORE_META_MODEL"] / ".DS_Store").write_bytes(b"finder metadata")
        (self.layers["PROJECT_CONFIGURATION"] / ".DS_Store").write_bytes(b"finder metadata")

        self.assertEqual(snapshot, module.source_state_snapshot(self.temp, places))
        self.assertEqual(snapshot, module.source_state_snapshot(self.temp, places))

    def test_source_unit_role_directories_do_not_count_as_source_layers(self) -> None:
        (self.source / "04_requirement").mkdir(exist_ok=True)
        (self.source / "04_requirement/CA-R-100--define-source-layer-goal.md").write_bytes(carrier("CA-R-100"))
        self.write("001_CORE_META_MODEL", "04_requirement", "CA-R-001--one.md", carrier("CA-R-001"))

        code, report = self.invoke()

        self.assertEqual(code, 0)
        self.assertTrue(report["can_apply"])
        self.assertEqual(report["selected_candidate_count"], 1)

    def test_declarations_drive_configured_projection_places(self) -> None:
        places = module.methodology_paths(self.temp)

        self.assertEqual(self.source.relative_to(self.temp), places.source)
        self.assertEqual(self.output.relative_to(self.temp), places.output)
        self.assertIn(
            self.declarations["METHODOLOGY_SOURCES"]["declaration_path"].relative_to(self.temp).as_posix(),
            module.declaration_source_pins(self.temp, places),
        )

    def test_changed_declaration_frontier_blocks_staging_at_original_places(self) -> None:
        self.write("001_CORE_META_MODEL", "05_method", "CA-M-001--one.md", carrier("CA-M-001"))
        places = module.methodology_paths(self.temp)
        _, candidates, snapshot = module.compile_report(self.temp, places)
        declaration = Path(self.declarations["METHODOLOGY_SOURCES"]["declaration_path"])
        declaration.write_text(declaration.read_text(encoding="utf-8").replace("2026-11-02", "2026-11-03"), encoding="utf-8")

        with self.assertRaises(module.CompileError) as raised:
            module.stage_outputs(self.temp, candidates, snapshot, places)

        self.assertEqual("source-frontier-changed", raised.exception.code)
        self.assertFalse((self.temp / self.output).exists())

    def test_changed_control_root_blocks_staging_at_original_places(self) -> None:
        self.write("001_CORE_META_MODEL", "05_method", "CA-M-001--one.md", carrier("CA-M-001"))
        places = module.methodology_paths(self.temp)
        _, candidates, snapshot = module.compile_report(self.temp, places)
        (self.temp / module.SETTINGS_PATH).write_text(
            '[project]\nname = "caprmedio"\n[paths]\ncontrol_root = ".caprmedio_other_project"\n'
        )

        with self.assertRaises(module.CompileError) as raised:
            module.stage_outputs(self.temp, candidates, snapshot, places)

        self.assertEqual("source-frontier-changed", raised.exception.code)
        self.assertFalse((self.temp / places.output / "05_method").exists())
        self.assertFalse((self.temp / ".caprmedio_other_project").exists())

    def test_explicit_release_child_places_remain_independent_of_canonical_target(self) -> None:
        original = self.write("001_CORE_META_MODEL", "05_method", "CA-M-001--one.md", carrier("CA-M-001"))
        canonical = module.methodology_paths(self.temp)
        child_output = canonical.output / "_release_materialized/selected-candidate"
        places = module.MethodologyPaths(
            source=canonical.source, output=child_output,
            declaration_digest=canonical.declaration_digest, control_root=canonical.control_root,
        )

        report, selected, snapshot = module.compile_report(self.temp, places)
        staging = module.stage_outputs(self.temp, selected, snapshot, places)
        module.replace_outputs_atomically(self.temp, staging, places)

        projected = self.temp / child_output / "05_method" / original.name
        self.assertTrue(report["can_apply"])
        self.assertEqual(projected.relative_to(self.temp).as_posix(), report["output_plan"][0]["output_path"])
        self.assertIn(b"projection:", projected.read_bytes())
        self.assertEqual(carrier("CA-M-001"), original.read_bytes())
        self.assertFalse((self.temp / canonical.output / "05_method").exists())

    def test_duplicate_identity_blocks_apply_without_exact_approval(self) -> None:
        self.write("001_CORE_META_MODEL", "04_requirement", "CA-R-001-A--one.md", carrier("CA-R-001"))
        self.write("003_PROJECT_CONFIGURATION", "04_requirement", "CA-R-001-B--two.md", carrier("CA-R-001", version=2))
        code, report = self.invoke()
        self.assertEqual(code, 2)
        self.assertGreaterEqual(report["conflict_count"], 1)
        self.assertIn("duplicate_selected_atom_identity", {item["type"] for item in report["conflicts"]})
        apply_code, applied = self.invoke("--apply")
        self.assertEqual(apply_code, 2)
        self.assertFalse(applied["can_apply"])
        for _, role in module.ROLES:
            self.assertFalse((self.temp / self.output / role).exists())

    def test_duplicate_governed_term_definition_blocks_apply(self) -> None:
        self.write(
            "001_CORE_META_MODEL",
            "04_requirement",
            "CA-R-010--define-shared-term.md",
            definition_carrier("CA-R-010", "Shared Term"),
        )
        self.write(
            "003_PROJECT_CONFIGURATION",
            "04_requirement",
            "CA-R-011--redefine-shared-term.md",
            definition_carrier("CA-R-011", "Shared Term", "Artifact/Type: Shared Term"),
        )

        code, report = self.invoke()

        self.assertEqual(2, code)
        conflict = next(
            row for row in report["conflicts"] if row["type"] == "duplicate_governed_term_definition"
        )
        self.assertEqual("Shared Term", conflict["details"]["term"])
        apply_code, applied = self.invoke("--apply")
        self.assertEqual(2, apply_code)
        self.assertFalse(applied["can_apply"])

    def test_output_collision_is_reported(self) -> None:
        self.write("001_CORE_META_MODEL", "04_requirement", "SHARED--claim.md", carrier("CA-R-001"))
        self.write("003_PROJECT_CONFIGURATION", "04_requirement", "SHARED--claim.md", carrier("CA-R-002"))
        code, report = self.invoke()
        self.assertEqual(code, 2)
        self.assertIn("output_path_collision", {item["type"] for item in report["conflicts"]})

    def test_dry_run_reports_all_five_conflict_classes(self) -> None:
        self.write("001_CORE_META_MODEL", "04_requirement", "CA-R-001-A--one.md", carrier("CA-R-001"))
        self.write("003_PROJECT_CONFIGURATION", "04_requirement", "CA-R-001-B--two.md", carrier("CA-R-001", version=2))
        self.write(
            "001_CORE_META_MODEL",
            "04_requirement",
            "CA-R-002--replacer.md",
            carrier("CA-R-002", relations="\n  replacement_of:\n    - CA-R-003"),
        )
        self.write("003_PROJECT_CONFIGURATION", "04_requirement", "CA-R-003--replaced.md", carrier("CA-R-003"))
        self.write(
            "001_CORE_META_MODEL",
            "04_requirement",
            "CA-R-004--incompatible.md",
            carrier("CA-R-004", relations="\n  incompatible_with:\n    - CA-R-005"),
        )
        self.write("003_PROJECT_CONFIGURATION", "04_requirement", "CA-R-005--other.md", carrier("CA-R-005"))
        self.write(
            "001_CORE_META_MODEL",
            "05_method",
            "CA-M-001--priority-a.md",
            carrier("CA-M-001", extra="applicable_methodology_priority_group: group-one\npriority: 10\n"),
        )
        self.write(
            "003_PROJECT_CONFIGURATION",
            "05_method",
            "CA-M-002--priority-b.md",
            carrier("CA-M-002", extra="applicable_methodology_priority_group: group-one\npriority: 20\n"),
        )
        self.write("001_CORE_META_MODEL", "06_evaluation", "SHARED--collision.md", carrier("CA-E-001"))
        self.write("003_PROJECT_CONFIGURATION", "06_evaluation", "SHARED--collision.md", carrier("CA-E-002"))

        code, report = self.invoke()
        self.assertEqual(code, 2)
        self.assertEqual(
            {item["type"] for item in report["conflicts"]},
            {
                "duplicate_selected_atom_identity",
                "unresolved_replacement",
                "incompatible_retained_candidates",
                "unresolved_priority",
                "output_path_collision",
            },
        )

    def test_drafts_archives_cap_and_implementation_are_excluded(self) -> None:
        active = self.write(
            "001_CORE_META_MODEL",
            "09_operations",
            "CA-O-001-OPERATIONS--active.md",
            carrier("CA-O-001"),
        )
        original = active.read_bytes()
        for index, directory in enumerate(("draft", "drafts", "archive", "archived", "Draft", "Archived")):
            historical = active.parent / f"copy-{index}" / directory / active.name
            historical.parent.mkdir(parents=True)
            historical.write_bytes(original)
        (self.layers["CORE_META_MODEL"] / "01_concern").mkdir()
        (self.layers["CORE_META_MODEL"] / "01_concern/CA-C-001.md").write_bytes(carrier("CA-C-001"))
        (self.layers["CORE_META_MODEL"] / "08_implementation").mkdir()
        (self.layers["CORE_META_MODEL"] / "08_implementation/CA-I-001.md").write_bytes(carrier("CA-I-001"))
        code, report = self.invoke()
        self.assertEqual(code, 0)
        self.assertEqual(report["eligible_candidate_count"], 1)
        self.assertEqual(report["conflict_count"], 0)
        self.assertEqual(report["output_plan"][0]["source_carrier_path"], active.relative_to(self.temp).as_posix())
        self.assertEqual(original, active.read_bytes())

    def test_failed_multi_directory_swap_rolls_back(self) -> None:
        self.write("001_CORE_META_MODEL", "04_requirement", "CA-R-001--one.md", carrier("CA-R-001"))
        self.write("001_CORE_META_MODEL", "05_method", "CA-M-001--two.md", carrier("CA-M-001"))
        code, _ = self.invoke("--apply")
        self.assertEqual(code, 0)
        output = self.temp / self.output
        before = {path.relative_to(output): path.read_bytes() for path in output.rglob("*.md")}
        _, selected, snapshot = module.compile_report(self.temp)
        staging = module.stage_outputs(self.temp, selected, snapshot)
        real_replace = module.os.replace
        calls = 0

        def fail_once(source: Path, target: Path) -> None:
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("injected")
            real_replace(source, target)

        with mock.patch.object(module.os, "replace", side_effect=fail_once):
            with self.assertRaises(module.CompileError):
                module.replace_outputs_atomically(self.temp, staging)
        after = {path.relative_to(output): path.read_bytes() for path in output.rglob("*.md")}
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
