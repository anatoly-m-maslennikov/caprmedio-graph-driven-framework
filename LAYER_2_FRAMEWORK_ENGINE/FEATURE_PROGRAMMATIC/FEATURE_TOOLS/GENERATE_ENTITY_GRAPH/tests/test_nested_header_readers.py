"""Grouped Header readers retain source identity, bytes and contribution offsets."""

import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

TOOL = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOL.parent), str(TOOL)]

import generate_entity_graph as graph  # noqa: E402
import graph_fact_context as facts  # noqa: E402
from cfel_claim_constraints import preview_constraints_from_paths  # noqa: E402
from current_entity_sources import build_current_graph, read_current_carriers  # noqa: E402
from owned_scope_selection import prepare_owned_scope_selection  # noqa: E402
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.parsing import CarrierError  # noqa: E402


HEADER = """identity:
  atom_id: OTHER-R-901
  ref_id: OTHER-R-901
context:
  container:
    scope_unit: TEST-SU-1
  role: Requirement
  form: Rule
  topics:
    main_subject: Entity
    dependencies: []
state:
  status: Active
  version: 3
  updated_at: "2026-11-06 12:00:00 +0400"
destination:
  file:
    name: unchanged.md
    path: selected
"""
BODY = """# Summary
Grouped source.

## Scope
Selected.

## Claim
Entity MEANS one grouped source.

## Details
Exact details.
"""


class NestedHeaderReadersTests(unittest.TestCase):
    def setUp(self):
        temporary_root = Path.cwd() / ".caprmedio_tmp/tests/test_nested_header_readers"
        temporary_root.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temporary_root, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.selected = self.root / "selected"
        self.selected.mkdir()
        self.path = self.selected / "unchanged.md"
        self.write()

    def write(self, header=HEADER, body=BODY):
        raw = ("---\n" + header + "---\n" + body).encode()
        self.path.write_bytes(raw)
        return raw

    def test_discovery_preserves_golden_source_and_nested_identity_state(self):
        raw = self.path.read_bytes()
        carriers, diagnostics = graph.discover_atoms(self.root, self.selected)
        self.assertEqual([], diagnostics)
        self.assertEqual(1, len(carriers))
        carrier = carriers[0]
        self.assertEqual(("OTHER-R-901", 3, "Requirement", "Rule", "Active"),
                         (carrier.atom_id, carrier.version, carrier.content_role, carrier.atom_type, carrier.status))
        self.assertEqual(hashlib.sha256(raw).hexdigest(), carrier.sha256)
        self.assertEqual(HEADER.rstrip("\n"), carrier.frontmatter)
        self.assertEqual(BODY, carrier.body)
        self.assertEqual(raw, self.path.read_bytes())
        self.assertEqual("OTHER-R-901", graph.top_scalar(carrier.frontmatter, "atom_id"))
        relations, diagnostics = graph.parse_subject_relations(carrier)
        self.assertEqual([], diagnostics)
        self.assertEqual("context.topics.main_subject", relations[0].source_schema_key)

    def test_fact_context_preserves_exact_lines_and_primary_contribution(self):
        raw = self.path.read_bytes()
        carriers, _ = graph.discover_atoms(self.root, self.selected)
        frontier = graph.source_frontier_for(self.root, self.selected)
        selection = {"atom_ids": ["OTHER-R-901"], "scope_unit_names": []}
        context = facts.prepare_fact_context(self.root, "entities", carriers, selection, frontier, carriers)
        self.assertEqual(frontier["source_frontier_sha256"],
                         context.as_dict()["source_binding"]["source_frontier_sha256"])
        lines, text, boundary, fields = facts._raw_parts(raw)
        self.assertEqual(raw, b"".join(lines))
        self.assertEqual("---", text[boundary])
        self.assertEqual(("OTHER-R-901", "3", "Requirement", "Rule", "Active"),
                         tuple(fields[key] for key in ("atom_id", "version", "content_role", "type", "status")))
        pin, _ = facts._carrier_pin(self.root, carriers[0])
        primary = facts._primary(pin, raw, "Requirement")["contribution"]
        selected = b"".join(lines[primary["start_line"] - 1:primary["end_line"]])
        self.assertEqual(b"Entity MEANS one grouped source.\n\n", selected)
        self.assertEqual(hashlib.sha256(selected).hexdigest(), primary["text_sha256"])

    def test_nested_topic_lists_keep_both_actual_source_property_paths(self):
        self.write(HEADER.replace("main_subject: Entity", 'main_subject: ["Entity"]')
                   .replace("dependencies: []", 'dependencies: ["Dependency"]'))
        carriers, _ = graph.discover_atoms(self.root, self.selected)
        relations, diagnostics = graph.parse_subject_relations(carriers[0])
        self.assertEqual([], diagnostics)
        self.assertEqual({("GOVERNS", "Entity", "context.topics.main_subject"),
                          ("DEPENDS_ON", "Dependency", "context.topics.dependencies")},
                         {(row.kind, row.subject_path, row.source_schema_key) for row in relations})

    def test_current_reader_keeps_raw_metadata_and_exact_mixed_body_endings(self):
        body = "# Summary\r\n\r\n## Claim\nEntity.\r\n"
        raw = self.write(body=body)
        carrier = read_current_carriers(self.selected, self.root)[0]
        self.assertEqual(("OTHER-R-901", 3), (carrier["source"]["atom_id"], carrier["source"]["version"]))
        self.assertEqual({"atom_id": "OTHER-R-901", "ref_id": "OTHER-R-901"}, carrier["metadata"]["identity"])
        self.assertNotIn("atom_id", carrier["metadata"])
        self.assertNotIn("status", carrier["metadata"])
        self.assertEqual("Active", carrier["read_view"]["status"])
        self.assertEqual(body, carrier["raw_body"])
        self.assertEqual(raw, carrier["raw"])
        self.assertEqual(hashlib.sha256(raw).hexdigest(), carrier["source"]["sha256"])
        self.assertEqual(["Entity"], [node["identity"] for node in build_current_graph(self.selected, self.root)[0]["nodes"]])

    def test_nested_lifecycle_excludes_draft_archived_and_keeps_done_current(self):
        for status in ("Draft", "Archived", "Done"):
            with self.subTest(status=status):
                self.write(HEADER.replace("status: Active", f"status: {status}"))
                current = read_current_carriers(self.selected, self.root)
                self.assertEqual(status == "Done", bool(current))
                with self.assertRaises(graph.EntityGraphError) as error:
                    graph.discover_atoms(self.root, self.selected)
                self.assertEqual("atom-set-empty", error.exception.code)

    def test_malformed_nested_noncanonical_atom_is_not_silently_skipped(self):
        self.write(HEADER.replace("atom_id: OTHER-R-901", "atom_id: [broken"))
        with self.assertRaises(CarrierError):
            read_current_carriers(self.selected, self.root)

    def test_explicit_nested_draft_cfel_preview_keeps_identity_and_hash(self):
        raw = self.write(HEADER.replace("status: Active", "status: Draft"),
                         "## Claim\n~~~CFEL\nEntity.Property: [string]{:1};\n~~~\n")
        records, diagnostics = preview_constraints_from_paths([self.path], repository=self.root)
        self.assertEqual([], diagnostics)
        self.assertEqual("property_constraint", records[0]["kind"])
        self.assertEqual({"atom_id": "OTHER-R-901", "version": 3, "path": "selected/unchanged.md",
                          "sha256": hashlib.sha256(raw).hexdigest()}, records[0]["source"])
        self.assertEqual(raw, self.path.read_bytes())

    def test_owned_scope_selection_binds_container_id_to_declaration(self):
        control = self.root / ".caprmedio_fixture"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[project]\nname = "fixture"\n[paths]\ncontrol_root = ".caprmedio_fixture"\n'
            'projection_root = ".caprmedio_fixture/_projection"\n', encoding="utf-8")
        write_scope_unit_declarations(self.root, (
            {"scope_unit_name": "OWNED", "parent": "PROJECT"},
            {"scope_unit_name": "FOREIGN", "parent": "PROJECT"},
        ), control_root=control)
        foreign = HEADER.replace("OTHER-R-901", "OTHER-R-902").replace("TEST-SU-1", "TEST-SU-2")
        (self.selected / "foreign.md").write_text("---\n" + foreign + "---\n" + BODY, encoding="utf-8")
        result = prepare_owned_scope_selection(self.root, self.selected, "OWNED")
        self.assertEqual("prepared", result["outcome"], result["diagnostics"])
        self.assertEqual(["OTHER-R-901"], result["selection"]["atom_ids"])
        support = result["inventory"]["support_sources"]
        self.assertEqual({"scope_unit": "TEST-SU-2"}, support[0]["container"])
        self.assertNotIn("current_scope_unit", support[0])
        self.write(HEADER.replace("  container:\n    scope_unit: TEST-SU-1", "  container: broken")
                   + "current_scope_unit: OWNED\n")
        rejected = prepare_owned_scope_selection(self.root, self.selected, "OWNED")
        self.assertEqual("failed", rejected["outcome"])
        self.assertEqual("owned-scope-property-missing", rejected["diagnostics"][-1]["code"])


if __name__ == "__main__":
    unittest.main()
