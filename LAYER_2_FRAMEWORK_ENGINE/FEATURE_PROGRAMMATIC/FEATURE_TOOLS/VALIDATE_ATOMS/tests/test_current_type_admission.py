"""Current carrier Type admission follows exact declared coordinates and observed IDs."""

import copy
from dataclasses import replace
import hashlib
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

import yaml

sys.path[:0] = [str(Path(__file__).resolve().parents[2]), str(Path(__file__).resolve().parents[1])]
from validate_atoms_workers.authority import resolve_context  # noqa: E402
from validate_atoms_workers.check_schema_extended import declared_type_coordinate  # noqa: E402
from test_current_frontmatter_encoding import current_source  # noqa: E402
from test_schema_extended import run  # noqa: E402
import test_proposed_carrier_admission_regressions as fixture_projects  # noqa: E402
from golden_authority import frozen_entry  # noqa: E402
from current_atom_locator import CurrentAtomLocator  # noqa: E402
from project_selection import bind_selection  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers import proposed_carrier as admission  # noqa: E402


BASE = "Entity/Object/Continuant/Governing Objects/Atom"


def source_row(text, path="/fixture/current-type.md"):
    metadata = yaml.safe_load(text.split("---", 2)[1])
    return {"text": text, "metadata": metadata,
            "binding": {"atom_id": metadata["atom_id"], "version": metadata["version"],
                        "path": path, "sha256": hashlib.sha256(text.encode()).hexdigest()}}


def captured_sources():
    rows = json.loads((Path(__file__).parent / "fixtures/current_type_authorities.json").read_text())
    return [source_row(row["text"], row["source_path"]) for row in rows]


def fresh_owner(identifier="CA-R-55555", role="Method", kind="Term Definition"):
    metadata = {"atom_id": identifier, "content_role": "Requirement", "type": "Entity Definition",
                "version": 1, "status": "Active", "subjects": {
                    "governs": BASE + f"/(.Content Role:{role})/(.Type:{kind})"}}
    return source_row("---\n" + yaml.safe_dump(metadata) + "---\n## Summary\n\nDefine Type\n\n## Claim\n\nA Type definition.\n")


def declared_authority(selection, scope_unit):
    return selection.root / next(
        Path(row["authority_path"])
        for row in selection.structure["scope_units"]
        if row["scope_unit_name"] == scope_unit
    )


def current_path(selection, identifier):
    hint = frozen_entry(identifier)["source_path"]
    return selection.root / CurrentAtomLocator(selection.root).locate(identifier, hint)


class CurrentTypeAdmissionTests(unittest.TestCase):
    def test_shared_validation_scope_resolves_each_role_type_and_retains_source_freshness(self):
        fixture = fixture_projects.ProposedCarrierAdmissionRegressions("test_root_and_foreign_project_names_use_real_selected_settings_not_folder_name")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        selection = fixture.project(source_ids=("CA-R-1309", "CA-R-1397"))
        fixture.entry_patch.stop()
        live_entry = admission._entry
        with patch.object(admission, "_entry", side_effect=lambda identifier, **kw:
                          live_entry(identifier, **kw) if identifier == "CA-D-657"
                          else fixture.selected_entry(identifier, **kw)):
            current_path(selection, "CA-D-276").unlink()
            encoding = current_source()
            encoding_path = declared_authority(selection, "CORE_META_MODEL") / "07_delivery" / Path(encoding["binding"]["path"]).name
            encoding_path.parent.mkdir(parents=True, exist_ok=True)
            encoding_path.write_text(encoding["text"])
            authority = declared_authority(selection, "CORE_META_MODEL") / "04_requirement"
            authority.mkdir(parents=True, exist_ok=True)
            for source in (captured_sources()[1], fresh_owner()):
                (authority / (source["binding"]["atom_id"] + "--type.md")).write_text(source["text"])
            body = "# Summary\n\nA scoped candidate\n\n## Scope\n\nOne candidate.\n\n## Claim\n\nA readable Claim.\n\n## Details\n"
            scope = admission.CarrierValidationScope(selection.root)
            before = fixture_projects.snapshot(selection.root)
            with bind_selection(selection):
                for role, kind, identity, directory, owner in (
                    ("Requirement", "Rule", "CA-R-701", "04_requirement", "CA-R-2000"),
                    ("Method", "Term Definition", "CA-M-701", "05_method", "CA-R-55555"),
                ):
                    metadata = fixture.metadata(content_role=role, type=kind, atom_id=identity, tier=1)
                    metadata.pop("local_tier")
                    metadata.pop("global_tier")
                    result = scope.validate(selection.root, metadata, body, Path(directory) / (identity + "--candidate.md"),
                                            allow_existing_relations=True)
                    self.assertEqual(result["findings"] + result["gaps"], [])
                    domain = next(row for row in result["outcomes"] if row["code"] == "model.domains")
                    self.assertIn(owner, [row["atom_id"] for row in domain["authority"]])
                scope.revalidate()
                self.assertEqual(fixture_projects.snapshot(selection.root), before)
                self.assertNotIn("CA-R-2000", [row["binding"]["atom_id"] for row in scope._context.inputs["sources"]])
                owner_path = authority / "CA-R-55555--type.md"
                owner_path.write_text(owner_path.read_text() + "\nChanged source.\n")
                with self.assertRaisesRegex(admission.ProposedCarrierError, "changed|unavailable"):
                    scope.revalidate()

    def test_nondefining_rule_on_the_same_coordinate_does_not_own_or_ambiguate_type(self):
        owner = fresh_owner()
        constraint_metadata = {**owner["metadata"], "atom_id": "CA-R-55556", "type": "Rule"}
        constraint = source_row("---\n" + yaml.safe_dump(constraint_metadata)
                                + "---\n## Summary\n\nConstrain Type\n\n## Claim\n\nA Type constraint.\n")
        rows = [current_source(), captured_sources()[0], constraint]
        metadata = {"content_role": "Method", "type": "Term Definition"}
        self.assertTrue(run("model.domains", metadata, source_rows=rows).gaps)
        result = run("model.domains", metadata, source_rows=[*rows, owner])
        self.assertEqual(result.findings + result.gaps, [])
        self.assertEqual([row["atom_id"] for row in result.obligation.authority], ["CA-R-55555"])

    def test_current_domain_uses_source_coordinate_and_carries_definition_provenance(self):
        rows = [current_source(), *captured_sources()]
        result = run("model.domains", {"content_role": "Requirement", "type": "Rule"}, source_rows=rows)
        self.assertEqual(result.findings + result.gaps, [])
        self.assertIn("CA-R-2000", [row["atom_id"] for row in result.obligation.authority])
        unknown = run("model.domains", {"content_role": "Method", "type": "Term Definition"}, source_rows=rows)
        self.assertTrue(unknown.gaps)  # R2229 still declares the Requirement coordinate.
        rows.append(fresh_owner())
        result = run("model.domains", {"content_role": "Method", "type": "Term Definition"}, source_rows=rows)
        self.assertEqual(result.findings + result.gaps, [])
        self.assertIn("CA-R-55555", [row["atom_id"] for row in result.obligation.authority])

    def test_missing_duplicate_inactive_forged_and_reference_only_sources_do_not_admit_type(self):
        base = [current_source(), captured_sources()[0]]
        owner = fresh_owner()
        wrong_role = fresh_owner(role="Requirement")
        reference = copy.deepcopy(owner)
        reference["metadata"]["subjects"] = {"depends_on": [owner["metadata"]["subjects"]["governs"]]}
        forged = copy.deepcopy(owner)
        forged["metadata"]["subjects"]["governs"] = BASE + "/(.Content Role:Method)/(.Type:Forged)"
        inactive = copy.deepcopy(owner)
        inactive["metadata"]["status"] = "Archived"
        stale = copy.deepcopy(owner)
        stale["text"] += "\nChanged bytes.\n"
        for additions in ([], [wrong_role], [reference], [owner, fresh_owner("CA-R-55556")], [inactive], [stale]):
            with self.subTest(additions=additions):
                result = run("model.domains", {"content_role": "Method", "type": "Term Definition"},
                             source_rows=base + additions)
                self.assertTrue(result.gaps)
        result = run("model.domains", {"content_role": "Method", "type": "Forged"}, source_rows=base + [forged])
        self.assertTrue(result.gaps)

    def test_whole_qualified_coordinate_is_required(self):
        for target in (BASE + "/Content Role: Method/Type: Term Definition",
                       BASE + "/(.Content Role:Method)/(.Type:Term Definition)"):
            self.assertEqual(declared_type_coordinate({"subjects": {"governs": target}}),
                             ("Method", "Term Definition"))
        for target in ("Atom/Content Role:Method/Type:Term Definition",
                       "@(" + BASE + "/(.Content Role:Method)/(.Type:Term Definition))",
                       BASE + "/(.Content Role:Method)/(.Type:Term Definition).Claim",
                       BASE + "/(.Content Role:Method)/(.Type:Term Definition)[String]"):
            self.assertIsNone(declared_type_coordinate({"subjects": {"governs": target}}))

    def test_current_encoding_obligations_replace_the_historical_selector_without_id_alias(self):
        context = resolve_context([current_source()])
        selected = [item for item in context.obligations if item.code in {
            "frontmatter.common_encoding", "model.domains", "property.admission"}]
        self.assertEqual(len(selected), 3)
        self.assertTrue(all(item.supported for item in selected))
        self.assertTrue(all(item.authority[0]["atom_id"] == "CA-D-657" for item in selected))
        result = run("property.admission", {"content_role": "Requirement", "type": "Rule", "tier": 1,
                                             "label": "Explicit"}, source_rows=[current_source()])
        self.assertEqual(result.findings + result.gaps, [])

    def test_registered_inventory_resolves_fresh_definition_id_and_rejects_duplicate_owners(self):
        fixture = fixture_projects.ProposedCarrierAdmissionRegressions("test_root_and_foreign_project_names_use_real_selected_settings_not_folder_name")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        selection = fixture.project()
        # The helper patches only historical fixture locators. D657 is an
        # independently captured Current source, not part of that frozen set.
        fixture.entry_patch.stop()
        live_entry = admission._entry
        with patch.object(admission, "_entry", side_effect=lambda identifier, **kw:
                          live_entry(identifier, **kw) if identifier == "CA-D-657"
                          else fixture.selected_entry(identifier, **kw)):
            current_path(selection, "CA-D-276").unlink()
            source = current_source()
            current_source_path = declared_authority(selection, "CORE_META_MODEL") / "07_delivery" / Path(source["binding"]["path"]).name
            current_source_path.parent.mkdir(parents=True, exist_ok=True)
            current_source_path.write_text(source["text"])
            owner_path = declared_authority(selection, "CORE_META_MODEL") / "04_requirement/CA-R-55555--type.md"
            owner_path.parent.mkdir(parents=True, exist_ok=True)
            owner_path.write_text(fresh_owner()["text"])
            with bind_selection(selection):
                context = admission.source_context_from_project(selection.root)
                ids = [row["binding"]["atom_id"] for row in context.inputs["sources"]]
                self.assertNotIn("CA-D-276", ids)
                self.assertNotIn("CA-D-288", ids)
                self.assertNotIn("CA-R-793", ids)
                inputs = admission._type_inputs(context, {"content_role": "Method", "type": "Term Definition"})
                self.assertIn("CA-R-55555", [row["binding"]["atom_id"] for row in inputs["sources"]])
                owner_path.with_name("CA-R-55556--type.md").write_text(fresh_owner("CA-R-55556")["text"])
                # A new scope observes the newly added owner; the original scope
                # would correctly fail freshness before validating another carrier.
                fresh_context = replace(context, _reader=admission.ReadContext(roots=[str(selection.root)], limits=dict(admission.CEILINGS)))
                with self.assertRaisesRegex(admission.ProposedCarrierError, "exactly one"):
                    admission._type_inputs(fresh_context, {"content_role": "Method", "type": "Term Definition"})


if __name__ == "__main__":
    unittest.main()
