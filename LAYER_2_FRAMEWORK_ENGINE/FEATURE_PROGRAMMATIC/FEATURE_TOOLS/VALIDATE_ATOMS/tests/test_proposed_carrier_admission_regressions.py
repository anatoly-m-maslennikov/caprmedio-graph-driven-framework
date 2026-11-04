"""Independent literal controls for finite reference and Project admission."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parents[1]
REPOSITORY = TOOLS.parents[2]
sys.path.insert(0, str(TOOLS))

from project_selection import bind_selection, resolve_project
from scope_declaration_test_support import write_scope_unit_declarations
from authoritative_status_models import capture_status_models  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.authority import Obligation
from VALIDATE_ATOMS.validate_atoms_workers.check_structure_extended import ADAPTERS
from VALIDATE_ATOMS.validate_atoms_workers.check_support import Check
from VALIDATE_ATOMS.validate_atoms_workers import proposed_carrier as admission
from VALIDATE_ATOMS.validate_atoms_workers.proposed_carrier import (
    ProposedCarrierError, _FRONTIER_IDS, _FRONTIER_STATUS_IDS, _GRAPH_IDS, _LEGACY_REGISTRY_IDS,
    _REGISTRY_IDS, _SUPPORT_IDS,
    source_context_from_project, validate_proposed_carrier,
)
from VALIDATE_ATOMS.validate_atoms_workers.proposed_references import (
    ProposedReferenceError, inventory_proposed_references,
)
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier
from VALIDATE_ATOMS.tests.golden_authority import (
    frozen_authority_fixture_bytes,
    frozen_entry,
)


PLAN_BODY = "# Summary\n\nIndependent Plan\n\n## Objective\n\nCheck admission.\n\n## Details\n\n### Definition of Done\n\nExact controls pass.\n"
TARGET = b"---\natom_id: CA-O-701\ncontent_role: Operations\ncurrent_scope_unit: TEST\nstatus: Active\nversion: 7\n---\n# Summary\n\nRequested target\n"
CURRENT_GRAPH_R1947 = Path(__file__).with_name("fixtures") / "current_graph_authority/CA-R-1947.md"
CURRENT_GRAPH_R1539 = Path(__file__).with_name("fixtures") / "current_graph_authority/CA-R-1539.md"
CURRENT_ENCODING = Path(__file__).with_name("fixtures") / "current_encoding_authority.json"
CURRENT_CONTAINMENT = Path(__file__).with_name("fixtures") / "current_containment_authority"
CURRENT_CONTAINMENT_IDS = ("CA-R-2508", "CA-R-2523", "CA-R-2511")


def snapshot(root):
    return {p.relative_to(root).as_posix(): (p.read_bytes(), p.stat().st_mode, p.stat().st_mtime_ns)
            for p in root.rglob("*") if p.is_file() and not p.is_symlink()}


def authority_fixture_bytes(identifier, entry=None, *, graph=False):
    del entry
    return frozen_authority_fixture_bytes(identifier, graph=graph)


def current_containment_bytes(identifier: str) -> bytes:
    raw = (CURRENT_CONTAINMENT / f"{identifier}.md").read_bytes()
    entry = json.loads(Path(admission.__file__).with_name("registry.json").read_text(encoding="utf-8"))["sources"][identifier]
    if hashlib.sha256(raw).hexdigest() != entry["sha256"]:
        raise AssertionError("current containment fixture digest changed: " + identifier)
    return raw


class ProposedCarrierAdmissionRegressions(unittest.TestCase):
    def setUp(self):
        scratch = REPOSITORY / ".caprmedio_tmp/tests/proposed-carrier-admission"
        scratch.mkdir(parents=True, exist_ok=True)
        self.directory = tempfile.TemporaryDirectory(dir=scratch, ignore_cleanup_errors=True)
        self.addCleanup(self.directory.cleanup)
        self.entry_patch = patch.object(admission, "_entry", frozen_entry)
        self.entry_patch.start()
        self.addCleanup(lambda: self.entry_patch.stop())
        self.root = Path(self.directory.name)

    def selected_entry(self, identifier, *, graph=False):
        if identifier == "CA-D-657" or identifier in CURRENT_CONTAINMENT_IDS:
            entry = dict(json.loads(
                Path(admission.__file__).with_name("registry.json").read_text(encoding="utf-8")
            )["sources"][identifier])
            raw = (
                json.loads(CURRENT_ENCODING.read_text(encoding="utf-8"))["text"].encode("utf-8")
                if identifier == "CA-D-657"
                else current_containment_bytes(identifier)
            )
        else:
            entry = dict(frozen_entry(identifier, graph=graph))
            raw = frozen_authority_fixture_bytes(identifier, graph=graph)
        metadata = parse_carrier(raw, Path(identifier + ".md")).metadata
        role = metadata.get("role", metadata.get("content_role"))
        if not isinstance(role, str):
            raise AssertionError("fixture authority has no role: " + identifier)
        entry["source_path"] = (
            ".caprmedio_caprmedio/" + self._core_relative + "/"
            + self._role_folders[role] + "/" + identifier + ".md"
        )
        return entry

    def put(self, relative, raw):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        return path

    def inventory(self):
        return inventory_proposed_references(
            self.root, {"scope_units": [{"scope_unit_name": "TEST", "authority_path": "authority"}]}, ["CA-O-701"],
            admitted_role_folders={"Operations": "09_operations"},
            admitted_status_folders={"Operations": {"Active": "", "Archived": "archived"}},
        )

    def test_unrelated_partial_and_identityless_legacy_do_not_block_exact_target(self):
        source = self.put("authority/09_operations/requested.md", TARGET)
        self.put("authority/09_operations/unrelated.md", b"---\natom_id: CA-M-999\nversion: 1\n---\n# Legacy\n")
        self.put("authority/09_operations/archive/old.md", b"---\nversion: 2\n---\n# Historical legacy\n")
        before = snapshot(self.root)
        result = self.inventory()
        self.assertEqual(len(result.direct_targets), 1)
        actual = result.direct_targets[0]
        self.assertEqual((actual.atom_id, actual.status, actual.version, actual.path),
                         ("CA-O-701", "Active", 7, "authority/09_operations/requested.md"))
        self.assertEqual(actual.sha256, hashlib.sha256(TARGET).hexdigest())
        self.assertEqual(source.read_bytes(), TARGET)
        self.assertEqual(snapshot(self.root), before)

    def test_requested_missing_status_or_bad_version_still_refuses(self):
        for raw in (TARGET.replace(b"status: Active\n", b""),
                    TARGET.replace(b"version: 7", b"version: 0"),
                    TARGET.replace(b"version: 7", b"version: true")):
            with self.subTest(raw=raw):
                self.put("authority/09_operations/requested.md", raw)
                before = snapshot(self.root)
                with self.assertRaises(ProposedReferenceError):
                    self.inventory()
                self.assertEqual(snapshot(self.root), before)

    def test_requested_duplicate_yaml_and_unrelated_malformed_yaml_refuse(self):
        for requested, unrelated in (
            (TARGET.replace(b"status: Active", b"status: Active\nstatus: Done"), None),
            (TARGET, b"---\natom_id: [unterminated\n---\n# Malformed\n"),
        ):
            with self.subTest(requested=requested, unrelated=unrelated):
                self.put("authority/09_operations/requested.md", requested)
                if unrelated is not None:
                    self.put("authority/09_operations/unrelated.md", unrelated)
                with self.assertRaises(ProposedReferenceError):
                    self.inventory()

    def test_duplicate_current_missing_and_archived_status_targets_refuse(self):
        first = self.put("authority/09_operations/one.md", TARGET)
        second = self.put("authority/09_operations/two.md", TARGET)
        with self.assertRaisesRegex(ProposedReferenceError, "ambiguous"):
            self.inventory()
        first.unlink()
        second.unlink()
        with self.assertRaisesRegex(ProposedReferenceError, "missing"):
            self.inventory()
        self.put("authority/09_operations/archived/old.md", TARGET.replace(b"status: Active", b"status: Archived"))
        with self.assertRaisesRegex(ProposedReferenceError, "inactive or archived"):
            self.inventory()

    def test_filename_does_not_supply_missing_requested_identity(self):
        self.put("authority/09_operations/CA-O-701--not-an-identity-proof.md", b"---\nversion: 7\nstatus: Active\n---\n# Legacy\n")
        with self.assertRaises(ProposedReferenceError):
            self.inventory()

    def project(
        self, name="amber", control_name=".caprmedio_selected", *, root=None, source_ids=(),
        encoding_profile="current",
    ):
        root = self.root if root is None else root
        control = root / control_name
        control.mkdir(parents=True, exist_ok=True)
        (control / "caprmedio_project_settings.toml").write_text(
            f'[project]\nname = "{name}"\nkey = "{name}"\nrepository_slug = "{name}-repo"\n'
            f'[paths]\ncontrol_root = "{control_name}"\n'
            '[artifacts.identity]\nproject_prefix = "CA"\n', encoding="utf-8",
        )
        declarations = write_scope_unit_declarations(
            root,
            (
                {"scope_unit_name": "FRAMEWORK_METHODOLOGY", "scope_unit_label": "Layer"},
                {"scope_unit_name": "METHODOLOGY_SOURCES", "parent": "FRAMEWORK_METHODOLOGY", "scope_unit_label": "Layer"},
                {"scope_unit_name": "CORE_META_MODEL", "parent": "METHODOLOGY_SOURCES", "scope_unit_label": "Layer"},
            ),
            control_root=control,
        )
        (control / "operators_registry.toml").write_text(
            '[[operators]]\nname = "Fixture Operator"\nrole = "project owner"\n', encoding="utf-8",
        )
        core = Path(declarations["CORE_META_MODEL"]["authority_path"])
        self._core_relative = core.relative_to(control).as_posix()
        self._role_folders = {
            "Requirement": "04_requirement", "Method": "05_method", "Evaluation": "06_evaluation",
            "Delivery": "07_delivery", "Operations": "09_operations", "Plan": "03_plan",
            "Concern": "01_concern", "Analysis": "02_analysis",
        }
        if encoding_profile == "current":
            if {"CA-D-276", *_LEGACY_REGISTRY_IDS} & set(source_ids):
                raise ValueError("current fixture cannot materialize historical encoding authority")
            encoding_ids = (
                "CA-D-657", *(identifier for identifier in _REGISTRY_IDS if identifier != "CA-D-276"),
                *CURRENT_CONTAINMENT_IDS,
            )
        elif encoding_profile == "legacy":
            if "CA-D-657" in source_ids:
                raise ValueError("legacy fixture cannot materialize Current encoding authority")
            encoding_ids = (*_REGISTRY_IDS, *_LEGACY_REGISTRY_IDS)
        else:
            raise ValueError("unknown fixture encoding profile: " + encoding_profile)
        identifiers = tuple(dict.fromkeys((
            *encoding_ids, *_SUPPORT_IDS, *_FRONTIER_STATUS_IDS.values(), "CA-R-1947", *source_ids,
        )))
        self.materialize_authority(core, identifiers)
        self.entry_patch.stop()
        self.entry_patch = patch.object(admission, "_entry", self.selected_entry)
        self.entry_patch.start()
        return resolve_project(root, control_name)

    def legacy_project(self, *args, **kwargs):
        """Materialize the explicit D276 fixture profile for historical carriers."""
        return self.project(*args, encoding_profile="legacy", **kwargs)

    def materialize_authority(self, core: Path, identifiers: tuple[str, ...]) -> None:
        role_folders = {
            "Requirement": "04_requirement", "Method": "05_method", "Evaluation": "06_evaluation",
            "Delivery": "07_delivery", "Operations": "09_operations", "Plan": "03_plan",
            "Concern": "01_concern", "Analysis": "02_analysis",
        }
        for identifier in identifiers:
            raw = (
                CURRENT_GRAPH_R1947.read_bytes() if identifier == "CA-R-1947"
                else CURRENT_GRAPH_R1539.read_bytes() if identifier == "CA-R-1539"
                else json.loads(CURRENT_ENCODING.read_text(encoding="utf-8"))["text"].encode("utf-8")
                if identifier == "CA-D-657"
                else current_containment_bytes(identifier)
                if identifier in CURRENT_CONTAINMENT_IDS
                else frozen_authority_fixture_bytes(identifier)
            )
            metadata = parse_carrier(raw, Path(identifier + ".md")).metadata
            role = metadata.get("role", metadata.get("content_role"))
            if not isinstance(role, str):
                raise AssertionError("fixture authority has no role: " + identifier)
            self.put(core / role_folders[role] / (identifier + ".md"), raw)

    @staticmethod
    def metadata(name="amber", **changes):
        value = {"atom_id": "CA-P-701", "content_role": "Plan", "type": "Plan", "label": "Task",
                 "current_scope_unit": name, "claim_target_scope_unit": name,
                 "local_tier": "Standard", "global_tier": 2, "status": "Active",
                 "author": "Fixture Operator", "version": 1, "updated_at": "2026-10-13 15:00:00 +0400",
                 "subjects": {"governs": "Tool", "depends_on": ["Plan"]}, "relations": {}}
        value.update(changes)
        return value

    def validate_plan(self, selection, metadata=None, relative=Path("03_plan/CA-P-701--independent-plan.md")):
        with bind_selection(selection):
            context = source_context_from_project(selection.root)
            status_index = capture_status_models(selection.root, context._reader)
            return validate_proposed_carrier(self.metadata(selection.settings["project"]["name"]) if metadata is None else metadata,
                                             PLAN_BODY, context, relative, allow_existing_relations=True,
                                             _status_index=status_index)

    def test_root_and_foreign_project_names_use_real_selected_settings_not_folder_name(self):
        for name, control in (("amber", ".caprmedio_selected"), ("violet", ".caprmedio_other")):
            with self.subTest(name=name, control=control):
                root = self.root / name
                root.mkdir()
                selection = self.legacy_project(name, control, root=root)
                before = snapshot(root)
                result = self.validate_plan(selection)
                self.assertFalse(result["findings"] + result["gaps"])
                self.assertEqual(snapshot(root), before)

    def test_context_supplies_the_verified_scope_unit_declaration_aggregate(self):
        selection = self.legacy_project()
        with bind_selection(selection):
            context = source_context_from_project(self.root)
        declarations = context.inputs["scope_unit_declarations"]
        self.assertEqual(declarations.digest, selection.declaration_digest)
        self.assertEqual(declarations.as_structure()["scope_units"],
                         [dict(row) for row in context.inputs["structure"]["scope_units"]])
        self.assertEqual(declarations.root.name, "amber")

    def test_explicit_legacy_profile_keeps_deep_plan_decomposition_guard(self):
        selection = self.legacy_project()
        with self.assertRaisesRegex(ProposedCarrierError, "deep Plan placement requires an admitted decomposition parent"):
            self.validate_plan(selection, relative=Path("03_plan/parent/CA-P-701--independent-plan.md"))

    def test_current_and_legacy_encoding_profiles_are_disjoint(self):
        current = self.project()
        with bind_selection(current):
            context = source_context_from_project(self.root)
        identifiers = {row["binding"]["atom_id"] for row in context.inputs["sources"]}
        self.assertIn("CA-D-657", identifiers)
        self.assertNotIn("CA-D-276", identifiers)

        core = current.root / Path(next(
            row["authority_path"] for row in current.structure["scope_units"]
            if row["scope_unit_name"] == "CORE_META_MODEL"
        ))
        self.materialize_authority(core, ("CA-D-276",))
        with bind_selection(current), self.assertRaisesRegex(
            ProposedCarrierError, "required Project context is unreadable",
        ) as caught:
            source_context_from_project(self.root)
        self.assertIn("frontmatter encoding authority is ambiguous", str(caught.exception.__cause__))

        legacy_root = self.root / "legacy"
        legacy_root.mkdir()
        legacy = self.project(root=legacy_root, encoding_profile="legacy")
        with bind_selection(legacy):
            legacy_context = source_context_from_project(legacy.root)
        legacy_identifiers = {row["binding"]["atom_id"] for row in legacy_context.inputs["sources"]}
        self.assertIn("CA-D-276", legacy_identifiers)
        self.assertNotIn("CA-D-657", legacy_identifiers)

    def test_project_owner_adapter_accepts_only_actual_bound_identity(self):
        selection = self.legacy_project()
        with bind_selection(selection):
            context = source_context_from_project(self.root)
            for owner, accepted in (("amber", True), ("other-project", False), ("PROJECT", False)):
                with self.subTest(owner=owner):
                    check = Check(Obligation("owner.resolution", [], True, "independent test"), context.authority,
                                  dict(context.inputs))
                    ADAPTERS["owner.resolution"](self.metadata(current_scope_unit=owner), PLAN_BODY, check)
                    self.assertEqual(not check.findings and not check.gaps, accepted)

    def test_unknown_target_wrong_project_owner_and_outside_project_path_refuse(self):
        selection = self.legacy_project()
        for metadata, relative in (
            (self.metadata(claim_target_scope_unit="unknown"), Path("03_plan/CA-P-701--independent-plan.md")),
            (self.metadata(current_scope_unit="other-project"), Path("03_plan/CA-P-701--independent-plan.md")),
            (self.metadata(), Path("../03_plan/CA-P-701--outside.md")),
        ):
            with self.subTest(metadata=metadata, relative=relative):
                with self.assertRaises(ProposedCarrierError):
                    self.validate_plan(selection, metadata, relative)

    def test_selected_settings_changed_or_missing_after_resolution_refuse(self):
        selection = self.legacy_project()
        original = selection.settings_path.read_bytes()
        for raw in (original.replace(b'name = "amber"', b'name = "other"'), None):
            with self.subTest(raw=raw):
                if raw is None:
                    selection.settings_path.unlink()
                else:
                    selection.settings_path.write_bytes(raw)
                with self.assertRaises((ProposedCarrierError, ValueError)):
                    self.validate_plan(selection)
                selection.settings_path.write_bytes(original)

    def test_bound_selection_from_foreign_root_cannot_supply_project_identity(self):
        selection = self.legacy_project()
        foreign = self.root / "foreign"
        foreign.mkdir()
        with bind_selection(selection), self.assertRaises((ProposedCarrierError, ValueError)):
            source_context_from_project(foreign)

    def test_project_and_declared_scope_unit_name_collision_refuses(self):
        selection = self.legacy_project()
        control = self.root / selection.control_relative
        root_declaration = next(
            path for path in selection.declaration_paths if path.parent == selection.control_root
        )
        root_declaration.rename(root_declaration.with_name(root_declaration.stem + "-duplicate.md"))
        write_scope_unit_declarations(self.root, control_root=control)
        before = snapshot(self.root)
        with self.assertRaises(ValueError):
            resolve_project(self.root, selection.control_relative)
        self.assertEqual(snapshot(self.root), before)

    def test_captured_context_rechecks_settings_and_structure_before_validation(self):
        selection = self.legacy_project()
        with bind_selection(selection):
            context = source_context_from_project(self.root)
            status_index = capture_status_models(self.root, context._reader)
        for path in (selection.settings_path, *selection.declaration_paths):
            with self.subTest(path=path.name):
                original = path.read_bytes()
                path.write_bytes(original + b"\n# independently introduced stale bytes\n")
                with self.assertRaises((ProposedCarrierError, ValueError)):
                    validate_proposed_carrier(self.metadata(), PLAN_BODY, context,
                                             Path("03_plan/CA-P-701--independent-plan.md"),
                                             _status_index=status_index)
                path.write_bytes(original)

    def test_captured_context_does_not_borrow_an_ambient_foreign_selection(self):
        selection = self.legacy_project()
        with bind_selection(selection):
            context = source_context_from_project(self.root)
            status_index = capture_status_models(self.root, context._reader)
        foreign = self.root / "sibling"
        foreign.mkdir()
        other = self.legacy_project("violet", ".caprmedio_foreign", root=foreign)
        before = snapshot(self.root)
        result = validate_proposed_carrier(self.metadata(), PLAN_BODY, context,
                                          Path("03_plan/CA-P-701--independent-plan.md"),
                                          _status_index=status_index)
        self.assertFalse(result["findings"] + result["gaps"])
        with bind_selection(other):
            result = validate_proposed_carrier(self.metadata(), PLAN_BODY, context,
                                              Path("03_plan/CA-P-701--independent-plan.md"),
                                              _status_index=status_index)
        self.assertFalse(result["findings"] + result["gaps"])
        self.assertEqual(snapshot(self.root), before)

    def test_explicit_project_plan_subtree_resolves_exact_parent_chain(self):
        selection = self.legacy_project()
        base = selection.control_relative / "03_plan"
        parent = base / "CA-P-702--parent.md"
        self.put(parent, b"---\natom_id: CA-P-702\ncontent_role: Plan\ntype: Plan\ncurrent_scope_unit: amber\nstatus: Active\nversion: 1\n---\n# Summary\n\nParent\n")
        self.put(base / "unrelated-legacy.md", b"---\nversion: 1\n---\n# Legacy\n")
        before = snapshot(self.root)
        result = inventory_proposed_references(
            self.root, {"scope_units": [{"scope_unit_name": "TEST", "authority_path": "authority"}]}, ["CA-P-702"],
            candidate_metadata=self.metadata(relations={"is_decomposition_of": ["CA-P-702"]}),
            candidate_path=parent.with_suffix("") / "CA-P-701--child.md",
            project_authority_paths=(selection.control_relative,), project_name="amber",
            admitted_role_folders={"Plan": "03_plan"},
            admitted_status_folders={"Plan": {"Active": "", "Done": "done"}},
        )
        self.assertEqual([row.atom_id for row in result.direct_targets], ["CA-P-702"])
        self.assertEqual([row.path for row in result.plan_parent_closure], [parent.as_posix()])
        self.assertEqual(snapshot(self.root), before)

    def test_relation_bearing_caller_uses_verified_whitelist_and_graph_authority(self):
        selection = self.legacy_project()
        control = selection.control_relative
        target_root = Path(next(
            row["authority_path"] for row in selection.structure["scope_units"]
            if row["scope_unit_name"] == "CORE_META_MODEL"
        ))
        self.materialize_authority(target_root, tuple(dict.fromkeys((*_FRONTIER_IDS, *_GRAPH_IDS))))
        target = self.put(target_root / "09_operations/action.md", TARGET.replace(
            b"current_scope_unit: TEST", b"current_scope_unit: CORE_META_MODEL"
        ).replace(b"version: 7", b"type: Action\nversion: 7"))
        self.put(target_root / "evidence/09_operations/broken.md", b"---\natom_id: [unterminated\n---\n")
        self.put(target_root / "09_operations/evidence/broken.md", b"---\natom_id: [unterminated\n---\n")
        metadata = self.metadata(atom_id="CA-E-701", content_role="Evaluation", type="QA Case", relations={"evaluation_for": ["CA-O-701"]})
        body = "# Summary\n\nEvaluate action.\n\n## Scope\n\nSelected action.\n\n## Claim\n\nVerify the action.\n\n## Details\n\nIndependent check.\n"
        before = snapshot(self.root)

        with bind_selection(selection):
            context = source_context_from_project(self.root)
            status_index = capture_status_models(self.root, context._reader)
            result = validate_proposed_carrier(
                metadata, body, context, Path("06_evaluation/CA-E-701--related.md"),
                _status_index=status_index,
            )

        self.assertFalse(result["findings"] + result["gaps"])
        self.assertEqual(snapshot(self.root), before)
        target.unlink()
        with self.assertRaises(ProposedCarrierError):
            validate_proposed_carrier(
                metadata, body, context, Path("06_evaluation/CA-E-701--related.md"),
                _status_index=status_index,
            )


if __name__ == "__main__":
    unittest.main()
