"""Current Atom folder selection and Subject syntax, without migration profiles."""

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOL = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOL.parent), str(TOOL)]
import current_entity_sources  # noqa: E402
from current_entity_sources import build_current_graph, read_current_carriers, read_current_model_carriers  # noqa: E402
from current_subject_graph import compose_current_graph  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.parsing import CarrierError  # noqa: E402

TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp/tests/test_current_entity_sources"


class CurrentEntitySourcesTests(unittest.TestCase):
    def setUp(self):
        TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.repository = Path(self.temporary.name)
        self.selected = self.repository / "sources"
        self.selected.mkdir()

    def write(self, atom_id, subject, *, version=1, status="Active", folder="", dependencies=()):
        path = self.selected / folder / f"{atom_id}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            f"---\natom_id: {atom_id}\nversion: {version}\nstatus: {status}\n"
            "content_role: Requirement\nsubjects:\n"
            f"  governs: {json.dumps(subject)}\n  depends_on: {json.dumps(dependencies)}\n"
            "---\n# Source\n\nSource content does not classify edges.\n",
            encoding="utf-8",
        )
        return path

    def build(self, selected=None):
        return build_current_graph(self.selected if selected is None else selected, self.repository)

    def test_folder_selection_excludes_draft_archived_paths_but_not_status(self):
        self.write("CA-R-9001", "Done Entity", status="Done", folder="020_done")
        self.write("CA-R-9002", "Backlog Entity", status="Backlog", folder="001_backlog")
        excluded = ("draft", "drafts", "archive", "archived", "000_draft", "099_archived")
        for index, folder in enumerate(excluded, 3):
            self.write(f"CA-R-900{index}", "Excluded", folder=f"nested/{folder}/deep")
        graph, provenance = self.build()
        self.assertEqual(
            {"Done Entity", "Backlog Entity"}, {row["identity"] for row in graph["nodes"]}
        )
        self.assertEqual(
            {"CA-R-9001", "CA-R-9002"}, {row["source"]["atom_id"] for row in provenance["owners"]}
        )
        for folder in excluded:
            with self.subTest(selected=folder):
                selected = self.selected / "nested" / folder / "deep"
                self.assertEqual([], self.build(selected)[0]["nodes"])

    def test_reader_returns_exact_source_bytes_metadata_and_body(self):
        path = self.write("CA-R-9001", "Current Entity")
        raw = path.read_bytes()

        carriers = read_current_carriers(self.selected, self.repository)

        self.assertEqual(1, len(carriers))
        carrier = carriers[0]
        self.assertEqual(
            {
                "atom_id": "CA-R-9001",
                "version": 1,
                "path": "sources/CA-R-9001.md",
                "sha256": hashlib.sha256(raw).hexdigest(),
            },
            carrier["source"],
        )
        self.assertEqual("Current Entity", carrier["subjects"]["governs"])
        self.assertEqual("Requirement", carrier["metadata"]["content_role"])
        self.assertIn("# Source", carrier["body"])
        self.assertEqual(raw, carrier["raw"])

    def test_reader_preserves_exact_body_line_endings_separately_from_parsed_body(self):
        path = self.selected / "CA-R-9001.md"
        body = "# Rule\r\n\r\n```yaml\nrule: keep\r\n```\n"
        raw = (
            "---\r\natom_id: CA-R-9001\nversion: 1\r\nstatus: Active\n"
            "content_role: Requirement\r\nsubjects:\n  governs: Current\r\n"
            "---\r\n" + body
        ).encode("utf-8")
        path.write_bytes(raw)

        carrier = read_current_carriers(self.selected, self.repository)[0]

        self.assertEqual(body, carrier["raw_body"])
        self.assertNotEqual(body, carrier["body"])
        self.assertEqual(raw, carrier["raw"])

    def test_enriched_reader_keeps_existing_graph_and_provenance_unchanged(self):
        self.write("CA-R-9001", "Shared")
        self.write("CA-R-9002", "Shared", version=2)
        carriers = read_current_carriers(self.selected, self.repository)
        expected = compose_current_graph(
            [{"source": row["source"], "subjects": row["subjects"]} for row in carriers]
        )

        self.assertEqual(expected, self.build())

    def test_explicit_draft_and_archived_statuses_are_not_current(self):
        draft = self.write("CA-R-9001", "Draft", status="Active")
        archived = self.write("CA-R-9002", "Archived", status="Active")
        self.write("CA-R-9003", "Current")
        draft.write_text(draft.read_text(encoding="utf-8").replace("status: Active", "status: Draft"), encoding="utf-8")
        archived.write_text(archived.read_text(encoding="utf-8").replace("status: Active", "status: Archived"), encoding="utf-8")

        carriers = read_current_carriers(self.selected, self.repository)

        self.assertEqual(["CA-R-9003"], [row["source"]["atom_id"] for row in carriers])
        self.assertEqual(["Current"], [row["identity"] for row in self.build()[0]["nodes"]])

    def test_malformed_atom_is_rejected_instead_of_silently_omitted(self):
        self.write("CA-R-9001", "Valid")
        malformed = self.selected / "CA-R-9002.md"
        malformed.write_text("---\natom_id: [broken\n---\n# Broken\n", encoding="utf-8")

        with self.assertRaises(CarrierError):
            read_current_carriers(self.selected, self.repository)

    def test_model_reads_requirements_without_parsing_known_other_roles(self):
        declaration = self.write("CA-R-9001", "Declared Entity")
        declaration.write_text(declaration.read_text().replace("content_role: Requirement\n",
                                                               "content_role: Requirement\nform: Declaration\n"))
        (self.selected / "CA-D-9002.md").write_text(
            "---\natom_id: CA-D-9002\nrole: Delivery\nsubjects:\n  active: Old\n"
            "topics:\n  main_subject: New\n---\n## Summary\n\nDelivery\n"
        )
        carriers = read_current_model_carriers(self.selected, self.repository)
        self.assertEqual(["CA-R-9001"], [row["source"]["atom_id"] for row in carriers])
        with self.assertRaises(CarrierError):
            read_current_carriers(self.selected, self.repository)
        (self.selected / "CA-R-9003.md").write_text("---\natom_id: [broken\n---\n")
        with self.assertRaises(CarrierError):
            read_current_model_carriers(self.selected, self.repository)

    def test_preview_replaces_a_pinned_current_declaration_with_two_draft_sources(self):
        current = self.write("CA-R-9001", "Original")
        other = self.write("CA-R-9002", "Unchanged")
        current.write_text(current.read_text().replace("status: Active\n", "status: Active\nform: Declaration\n"))
        draft_paths = [
            self.write(f"CA-R-900{number}", f"Replacement {number}", version=2, status="Draft", folder="000_draft")
            for number in (3, 4)
        ]
        entries = []
        for draft in draft_paths:
            reference = f"{draft.stem}@2-draft"
            draft.write_text(draft.read_text().replace("status: Draft\n",
                                                      f"status: Draft\nform: Declaration\nref_id: {reference}\n"))
            entries.append({
                "source": current.relative_to(self.repository).as_posix(),
                "source_sha256": hashlib.sha256(current.read_bytes()).hexdigest(),
                "draft": draft.relative_to(self.repository).as_posix(),
                "draft_ref": reference,
            })
        manifest = self.repository / "preview.json"
        manifest.write_text(json.dumps(entries))

        baseline = read_current_carriers(self.selected, self.repository)
        preview = read_current_carriers(self.selected, self.repository, model_draft_manifest=manifest)

        self.assertEqual([current.stem, other.stem], [row["source"]["atom_id"] for row in baseline])
        self.assertEqual([other.stem, *(draft.stem for draft in draft_paths)],
                         [row["source"]["atom_id"] for row in preview])
        self.assertEqual([draft.read_bytes() for draft in draft_paths], [row["raw"] for row in preview[1:]])
        self.assertEqual(["Draft", "Draft"], [row["read_view"]["status"] for row in preview[1:]])
        entries[0]["source_sha256"] = "stale"
        manifest.write_text(json.dumps(entries))
        with self.assertRaisesRegex(ValueError, "predecessor is absent or has changed"):
            read_current_carriers(self.selected, self.repository, model_draft_manifest=manifest)

    def test_reader_checks_existing_file_size_ceiling_before_parsing(self):
        self.write("CA-R-9001", "Too Large")

        with patch.dict(current_entity_sources.CEILINGS, {"max_file_bytes": 8}):
            with self.assertRaisesRegex(ValueError, "max_file_bytes ceiling"):
                read_current_carriers(self.selected, self.repository)

    def test_live_edit_added_and_deleted_sources_are_reflected_without_snapshot(self):
        first = self.write("CA-R-9001", "Before", version=2)
        stale = self.repository / ".caprmedio_caprmedio/_projection/graph.json"
        stale.parent.mkdir(parents=True)
        stale.write_text("invalid stale snapshot", encoding="utf-8")
        self.assertEqual({"Before"}, {row["identity"] for row in self.build()[0]["nodes"]})
        self.write("CA-R-9001", "After", version=3)
        self.write("CA-R-9002", "New Entity", version=4)
        graph, provenance = self.build()
        self.assertEqual({"After", "New Entity"}, {row["identity"] for row in graph["nodes"]})
        self.assertEqual(
            {("CA-R-9001", 3), ("CA-R-9002", 4)},
            {(row["source"]["atom_id"], row["source"]["version"]) for row in provenance["owners"]},
        )
        first.unlink()
        graph, provenance = self.build()
        self.assertEqual(["New Entity"], [row["identity"] for row in graph["nodes"]])
        self.assertEqual(["CA-R-9002"], [row["source"]["atom_id"] for row in provenance["owners"]])
        self.assertEqual("invalid stale snapshot", stale.read_text(encoding="utf-8"))

    def test_identical_subject_identity_merges_and_keeps_all_current_provenance(self):
        paths = [self.write("CA-R-9001", "Shared"), self.write("CA-R-9002", "Shared", version=5)]
        before = {path: path.read_bytes() for path in paths}
        graph, provenance = self.build()
        self.assertEqual(["Shared"], [row["identity"] for row in graph["nodes"]])
        self.assertNotIn("profile", graph["nodes"][0])
        self.assertEqual(2, len(graph["nodes"][0]["occurrence_ids"]))
        for owner in provenance["owners"]:
            source = owner["source"]
            path = self.repository / source["path"]
            self.assertEqual(hashlib.sha256(before[path]).hexdigest(), source["sha256"])
        self.assertEqual(before, {path: path.read_bytes() for path in paths})

    def test_current_atom_discovery_accepts_revision_names_and_declared_project_ids(self):
        canonical = self.write("CA-R-9001", "Revision Named", version=2)
        canonical.rename(self.selected / "CA-R-9001@2-current.md")
        self.write("OTHER-R-9002", "Other Project")
        (self.selected / "README.md").write_text("# Ordinary documentation\n", encoding="utf-8")
        (self.selected / "notes.md").write_text(
            "---\ntitle: Ordinary note\n---\n# Not an Atom\n", encoding="utf-8"
        )
        graph, provenance = self.build()
        self.assertEqual(
            {"Revision Named", "Other Project"}, {node["identity"] for node in graph["nodes"]}
        )
        self.assertEqual(
            {("CA-R-9001", 2), ("OTHER-R-9002", 1)},
            {
                (owner["source"]["atom_id"], owner["source"]["version"])
                for owner in provenance["owners"]
            },
        )

    def test_source_selection_does_not_follow_symlink_into_outside_folder(self):
        self.write("CA-R-9001", "Selected")
        outside = self.write("CA-R-9002", "Outside", folder="../outside")
        (self.selected / "linked").symlink_to(outside.parent, target_is_directory=True)
        graph, provenance = self.build()
        self.assertEqual(["Selected"], [node["identity"] for node in graph["nodes"]])
        self.assertEqual(["CA-R-9001"], [row["source"]["atom_id"] for row in provenance["owners"]])

    def test_subject_syntax_has_qualified_relation_endpoints_and_no_incidence_edges(self):
        self.write("CA-R-9001", "Artifact/Atom.Status: Active", dependencies=["Workflow.State"])
        self.write("CA-R-9002", "Atom/Content Role: Plan")
        graph, _ = self.build()
        names = {node["id"]: node["identity"] for node in graph["nodes"]}
        actual = {
            (edge["kind"], names[edge["relation_source"]], names[edge["relation_target"]])
            for edge in graph["edges"]
        }
        self.assertEqual(
            {
                ("NARROWER_THAN", "Artifact/Atom", "Artifact"),
                ("IS_PROPERTY_OF", "Artifact/Atom.Status", "Artifact/Atom"),
                ("IS_ALLOWED_VALUE_OF", "Artifact/Atom.Status:Active", "Artifact/Atom.Status"),
                ("IS_PROPERTY_OF", "Workflow.State", "Workflow"),
                ("NARROWER_THAN", "Atom/Content Role", "Atom"),
                ("IS_ALLOWED_VALUE_OF", "Atom/Content Role:Plan", "Atom/Content Role"),
            },
            actual,
        )
        self.assertIn("Atom/Content Role", names.values())

    def test_malformed_subject_fails_without_guessed_nodes(self):
        self.write("CA-R-9001", "Atom///Broken")
        with self.assertRaisesRegex(ValueError, "Subject projection failed"):
            self.build()


if __name__ == "__main__":
    unittest.main()
