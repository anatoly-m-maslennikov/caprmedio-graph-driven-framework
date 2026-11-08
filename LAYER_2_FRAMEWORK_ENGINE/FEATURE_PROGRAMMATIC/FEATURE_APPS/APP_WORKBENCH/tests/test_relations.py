# CA-E-676@6
# CA-E-677@14
"""Runtime facts and hashes, independent of the repository's Atom contents."""

from pathlib import Path
from contextlib import redirect_stderr
from io import StringIO
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relations import (
    canonical, materialize, materialize_with_registry, relation_registry,
)


def atom(ref, *, relation=None, form="Rule", body="## Claim\nOne claim.\n"):
    return {"source_path": ref + ".md", "status_group": "Current", "id": ref, "ref": ref,
            "version": 1, "status": "Active", "current_scope_unit": None,
            "claim_target_scope_unit": None, "role": "Requirement", "form": form,
            "tier": 1, "updated_at": None, "header_json": {"relations": relation or {}},
            "content_markdown": body, "content_properties_json": [],
            "relation_edges_json": [], "hash": None}


def relation_declaration(ref, name, binding=""):
    body = f"```CFEL\n{binding}\n```\n" if binding else "## Claim\n"
    row = atom(ref, form="Declaration", body=body)
    row["header_json"]["subjects"] = {
        "active": "CAPRMEDIO_MODEL <+ CFEL <+ Relation//" + name,
    }
    return row


def declarations():
    return [
        relation_declaration("CA-R-1", "IS_CONTAINED_BY",
                             "Relation//IS_CONTAINED_BY ((HAS_INVERSE)) Relation//CONTAINS;"),
        relation_declaration("CA-R-2", "CONTAINS",
                             "Relation//CONTAINS <((HAS_INVERSE)) Relation//IS_CONTAINED_BY;"),
    ]


class RelationTests(unittest.TestCase):
    def test_project_root_reference_has_derived_contains(self):
        from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.incremental_relations import materialize_delta

        root = {"name": "demo", "scope_unit_id": "DEMO-SU-00", "parent_name": None,
                "declared_label": None, "ordered": False, "order_number": None,
                "declaration_source_path": "project.md", "declaration_version": 1,
                "relation_edges_json": [], "hash": None}
        source = atom("CA-R-3")
        source["header_json"]["context"] = {"container": {"scope_unit": "DEMO-SU-00"}}
        sources = declarations() + [source]
        rows, scopes = materialize(sources, [root])
        edge = next(row for row in rows if row["ref"] == "CA-R-3")["relation_edges_json"][0]
        self.assertEqual(("Scope Unit", "demo"), (edge["target_kind"], edge["target_ref"]))
        self.assertEqual("CA-R-3", scopes[0]["relation_edges_json"][0]["target_ref"])
        self.assertTrue(scopes[0]["relation_edges_json"][0]["derived"])

        _, _, _, _, state, _ = materialize_delta(declarations(), [root])
        _, scopes, _, _, state, delta = materialize_delta(
            sources, [root], state, {source["source_path"]: source},
        )
        self.assertIsNotNone(delta)
        self.assertEqual("CA-R-3", scopes[0]["relation_edges_json"][0]["target_ref"])
        _, scopes, _, _, _, _ = materialize_delta(
            declarations(), [root], state, {source["source_path"]: None},
        )
        self.assertEqual([], scopes[0]["relation_edges_json"])

    def test_nested_header_container_atom_generates_both_directions(self):
        parent = atom("CA-P-1")
        child = atom("CA-P-2")
        child["header_json"]["context"] = {"container": {"atom": "CA-P-1"}}
        rows, _ = materialize(declarations() + [parent, child], [])
        by_ref = {row["ref"]: row for row in rows}
        direct = by_ref["CA-P-2"]["relation_edges_json"][0]
        inverse = by_ref["CA-P-1"]["relation_edges_json"][0]
        self.assertEqual(("IS_CONTAINED_BY", "CA-P-1", False),
                         (direct["relation_type"], direct["target_ref"], direct["derived"]))
        self.assertEqual(("CONTAINS", "CA-P-2", True),
                         (inverse["relation_type"], inverse["target_ref"], inverse["derived"]))
        self.assertEqual({}, child["header_json"]["relations"])
        self.assertEqual(1, parent["version"])

    def test_inverse_lives_on_counterpart_and_changes_its_hash(self):
        epic = atom("CA-P-1")
        task = atom("CA-P-2", relation={"is_contained_by": ["CA-P-1"]})
        rows, _ = materialize(declarations() + [epic, task], [])
        by_ref = {row["ref"]: row for row in rows}
        self.assertEqual("IS_CONTAINED_BY", by_ref["CA-P-2"]["relation_edges_json"][0]["relation_type"])
        self.assertEqual({"source_kind": "Atom", "source_ref": "CA-P-1",
                          "target_kind": "Atom", "target_ref": "CA-P-2",
                          "relation_type": "CONTAINS", "derived": True},
                         by_ref["CA-P-1"]["relation_edges_json"][0])
        before = by_ref["CA-P-1"]["hash"]
        changed, _ = materialize(declarations() + [epic, atom("CA-P-2")], [])
        after = next(row for row in changed if row["ref"] == "CA-P-1")
        self.assertNotEqual(before, after["hash"])
        self.assertEqual([], after["relation_edges_json"])
        self.assertIsNone(epic["hash"])
        self.assertEqual(1, epic["version"])

    def test_scope_rows_own_outgoing_inverse_facts(self):
        row = atom("CA-R-3")
        row["current_scope_unit"] = "ENGINE"
        scope = {"name": "ENGINE", "scope_unit_id": "CA-SU-1", "parent_name": None,
                 "declared_label": None, "ordered": False, "order_number": None,
                 "declaration_source_path": "scope.md", "declaration_version": 1,
                 "relation_edges_json": [], "hash": None}
        _, scopes = materialize(declarations() + [row], [scope])
        edge = scopes[0]["relation_edges_json"][0]
        self.assertEqual(("Scope Unit", "ENGINE", "Atom", "CA-R-3"),
                         tuple(edge[x] for x in ("source_kind", "source_ref", "target_kind", "target_ref")))
        self.assertEqual("CONTAINS", edge["relation_type"])
        self.assertTrue(edge["derived"])

    def test_scope_unit_id_relations_use_the_declared_scope_name(self):
        by_mapping = atom("CA-R-31", relation={"is_contained_by": {"scope_unit": "CA-SU-14"}})
        by_id = atom("CA-R-32", relation={"is_contained_by": "CA-SU-14"})
        unknown = atom("CA-R-33", relation={"is_contained_by": {"scope_unit": "CA-SU-999"}})
        parent = {"name": "CORE", "scope_unit_id": "CA-SU-9", "parent_name": None,
                  "declared_label": None, "ordered": False, "order_number": None,
                  "declaration_source_path": "core.md", "declaration_version": 1,
                  "relation_edges_json": [], "hash": None}
        scope = {"name": "FRAMEWORK_ENGINE", "scope_unit_id": "CA-SU-14", "parent_name": "CORE",
                 "declared_label": None, "ordered": False, "order_number": None,
                 "declaration_source_path": "engine.md", "declaration_version": 1,
                 "relation_edges_json": [], "hash": None}

        rows, scopes = materialize(declarations() + [by_mapping, by_id, unknown], [parent, scope])

        by_ref = {row["ref"]: row for row in rows}
        by_scope = {row["name"]: row for row in scopes}
        for ref in ("CA-R-31", "CA-R-32"):
            self.assertIn({"source_kind": "Atom", "source_ref": ref,
                           "target_kind": "Scope Unit", "target_ref": "FRAMEWORK_ENGINE",
                           "relation_type": "IS_CONTAINED_BY", "derived": False},
                          by_ref[ref]["relation_edges_json"])
        self.assertIn({"source_kind": "Atom", "source_ref": "CA-R-33",
                       "target_kind": "Scope Unit", "target_ref": "CA-SU-999",
                       "relation_type": "IS_CONTAINED_BY", "derived": False},
                      by_ref["CA-R-33"]["relation_edges_json"])
        self.assertIn({"source_kind": "Scope Unit", "source_ref": "FRAMEWORK_ENGINE",
                       "target_kind": "Scope Unit", "target_ref": "CORE",
                       "relation_type": "IS_CONTAINED_BY", "derived": False},
                      by_scope["FRAMEWORK_ENGINE"]["relation_edges_json"])
        self.assertIn({"source_kind": "Scope Unit", "source_ref": "FRAMEWORK_ENGINE",
                       "target_kind": "Atom", "target_ref": "CA-R-31",
                       "relation_type": "CONTAINS", "derived": True},
                      by_scope["FRAMEWORK_ENGINE"]["relation_edges_json"])
        self.assertEqual({"scope_unit": "CA-SU-14"}, by_mapping["header_json"]["relations"]["is_contained_by"])

    def test_only_current_literal_relation_metadata_establishes_inverses(self):
        rows = declarations()
        rows[0]["status_group"] = "Draft"
        registered, inverses = relation_registry(rows)
        self.assertNotIn("IS_CONTAINED_BY", registered)
        self.assertEqual({}, inverses)
        rows[0]["status_group"] = "Current"
        rows[0]["content_markdown"] += "\nRelation//A ((HAS_INVERSE)) Relation//B;\n"
        registered, inverses = relation_registry(rows)
        self.assertEqual({"IS_CONTAINED_BY": "CONTAINS"}, inverses)
        self.assertNotIn("A", registered)

    def test_relation_declaration_registers_direct_fact_but_draft_does_not(self):
        declaration = relation_declaration("CA-R-1", "IS_WORK_REPORT_FOR")
        declaration["form"] = "Relation Declaration"
        report = atom("CA-R-REPORT", relation={"IS_WORK_REPORT_FOR": ["CA-P-TASK"]})
        task = atom("CA-P-TASK")

        rows, _ = materialize([declaration, report, task], [])
        self.assertIn(
            {
                "source_kind": "Atom", "source_ref": "CA-R-REPORT",
                "target_kind": "Atom", "target_ref": "CA-P-TASK",
                "relation_type": "IS_WORK_REPORT_FOR", "derived": False,
            },
            next(row for row in rows if row["ref"] == "CA-R-REPORT")["relation_edges_json"],
        )

        draft = dict(declaration, status_group="Draft")
        self.assertNotIn("IS_WORK_REPORT_FOR", relation_registry([draft])[0])
        rows, _ = materialize([draft, report, task], [])
        self.assertEqual([], next(row for row in rows if row["ref"] == "CA-R-REPORT")["relation_edges_json"])

    def test_ambiguous_literal_inverses_warn_and_keep_direct_facts(self):
        metadata = [
            relation_declaration("A", "A", "Relation//A ((HAS_INVERSE)) Relation//B;"),
            relation_declaration("B", "B"),
            relation_declaration("C", "C", "Relation//C ((HAS_INVERSE)) Relation//B;"),
            relation_declaration("D", "D", "Relation//D ((HAS_INVERSE)) Relation//D;"),
            relation_declaration("E", "E", "Relation//E ((HAS_INVERSE)) Relation//F;"),
            relation_declaration("F", "F", "Relation//F ((HAS_INVERSE)) Relation//G;"),
            relation_declaration("G", "G"),
            relation_declaration("J", "J", "Relation//J ((HAS_INVERSE)) Relation//K;"),
            relation_declaration("K", "K", "Relation//K <((HAS_INVERSE)) Relation//J;"),
        ]
        errors = StringIO()
        with redirect_stderr(errors):
            registered, inverses = relation_registry(metadata)
        self.assertEqual({"J": "K"}, inverses)
        self.assertTrue({"A", "B", "C", "D", "E", "F", "G", "J", "K"} <= registered)
        self.assertIn("multiple direct owners A, C", errors.getvalue())
        self.assertIn("self-pair", errors.getvalue())
        self.assertIn("derived Relation F is declared direct", errors.getvalue())

        source = atom("CA-P-1", relation={"A": ["CA-P-2"], "J": ["CA-P-3"]})
        with redirect_stderr(StringIO()):
            rows, _ = materialize(metadata + [source, atom("CA-P-2"), atom("CA-P-3")], [])
        by_ref = {row["ref"]: row for row in rows}
        self.assertIn({"source_kind": "Atom", "source_ref": "CA-P-1",
                       "target_kind": "Atom", "target_ref": "CA-P-2",
                       "relation_type": "A", "derived": False},
                      by_ref["CA-P-1"]["relation_edges_json"])
        self.assertIn({"source_kind": "Atom", "source_ref": "CA-P-1",
                       "target_kind": "Atom", "target_ref": "CA-P-3",
                       "relation_type": "J", "derived": False},
                      by_ref["CA-P-1"]["relation_edges_json"])
        self.assertEqual([], by_ref["CA-P-2"]["relation_edges_json"])
        self.assertIn({"source_kind": "Atom", "source_ref": "CA-P-3",
                       "target_kind": "Atom", "target_ref": "CA-P-1",
                       "relation_type": "K", "derived": True},
                      by_ref["CA-P-3"]["relation_edges_json"])

    def test_ambiguous_normalized_header_relation_warns_and_skips_links(self):
        source = atom("CA-P-4", relation={"BlOcKs": ["CA-P-5"]})
        errors = StringIO()
        with redirect_stderr(errors):
            rows, _ = materialize([
                relation_declaration("UPPER", "BLOCKS"),
                relation_declaration("LOWER", "blocks"),
                source,
                atom("CA-P-5"),
            ], [])
        self.assertEqual([], next(row for row in rows if row["ref"] == "CA-P-4")["relation_edges_json"])
        self.assertIn("CA-P-4.md: ambiguous registered Relation BlOcKs", errors.getvalue())
        self.assertIn("candidates: BLOCKS, blocks; link skipped", errors.getvalue())

    def test_unregistered_relations_and_prose_do_not_create_facts(self):
        row = atom("CA-R-4", relation={"unknown_relation": ["CA-R-5"]},
                   body="CA-R-4 CONTAINS CA-R-5\n")
        rows, _ = materialize(declarations() + [row], [])
        self.assertEqual([], rows[-1]["relation_edges_json"])

    def test_hash_is_deterministic_and_excludes_only_hash_field(self):
        rows, _ = materialize([atom("CA-R-5")], [])
        import hashlib
        data = {key: value for key, value in rows[0].items() if key != "hash"}
        self.assertEqual(hashlib.sha256(canonical(data).encode()).hexdigest(), rows[0]["hash"])
        self.assertEqual(rows, materialize([atom("CA-R-5")], [])[0])

    def test_duplicate_references_are_excluded_with_their_supported_inverses(self):
        task = atom("CA-P-2", relation={"is_contained_by": ["CA-P-1"]})
        other = dict(task, source_path="another-draft.md")
        errors = StringIO()
        with redirect_stderr(errors):
            rows, _ = materialize(declarations() + [atom("CA-P-1"), task, other], [])
        self.assertEqual([], next(row for row in rows if row["ref"] == "CA-P-1")["relation_edges_json"])
        self.assertNotIn("CA-P-2", [row["ref"] for row in rows])
        self.assertIn("ambiguous duplicate reference CA-P-2", errors.getvalue())

    def test_unassigned_draft_references_are_not_duplicates(self):
        first = dict(atom("draft-1"), id=None, ref=None, status_group="Draft")
        second = dict(atom("draft-2"), id=None, ref=None, status_group="Draft")
        rows, _ = materialize([first, second], [])
        self.assertEqual(2, len(rows))

    def test_reuses_unchanged_rows_and_rebuilds_inverse_neighbours(self):
        epic = atom("CA-P-1")
        task = atom("CA-P-2", relation={"is_contained_by": ["CA-P-1"]})
        unrelated = atom("CA-P-3")
        rows, _scopes, _registered, _inverse, cache = materialize_with_registry(
            declarations() + [epic, task, unrelated], [],
        )
        original = {row["ref"]: row for row in rows}
        changed_task = atom("CA-P-2")
        next_rows, _scopes, _registered, _inverse, next_cache = materialize_with_registry(
            declarations() + [epic, changed_task, unrelated], [], cache,
        )
        current = {row["ref"]: row for row in next_rows}
        self.assertIs(original["CA-P-3"], current["CA-P-3"])
        self.assertIsNot(original["CA-P-1"], current["CA-P-1"])
        self.assertEqual([], current["CA-P-1"]["relation_edges_json"])
        self.assertIsNot(original["CA-P-2"], current["CA-P-2"])
        self.assertIn("CA-P-2.md", next_cache)
        self.assertIn("CA-P-3.md", next_cache)

    def test_cache_prunes_deleted_and_duplicate_rows(self):
        first = atom("CA-P-1")
        second = atom("CA-P-2")
        _rows, _scopes, _registered, _inverse, cache = materialize_with_registry([first, second], [])
        duplicate = dict(second, source_path="duplicate.md")
        _rows, _scopes, _registered, _inverse, next_cache = materialize_with_registry(
            [first, second, duplicate], [], cache,
        )
        self.assertEqual({"CA-P-1.md"}, set(next_cache))

    def test_registry_is_calculated_once_per_materialization(self):
        import APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relations as relations

        original = relations.relation_registry
        calls = 0

        def counted(rows):
            nonlocal calls
            calls += 1
            return original(rows)

        relations.relation_registry = counted
        try:
            materialize_with_registry(declarations() + [atom("CA-P-1")], [])
        finally:
            relations.relation_registry = original
        self.assertEqual(1, calls)

    def test_reuses_direct_facts_for_unchanged_rows(self):
        import APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relations as relations

        metadata = declarations()
        epic = atom("CA-P-1")
        task = atom("CA-P-2", relation={"is_contained_by": ["CA-P-1"]})
        unrelated = atom("CA-P-3")
        original = relations._atom_facts
        calls = 0

        def counted(*args):
            nonlocal calls
            calls += 1
            return original(*args)

        relations._atom_facts = counted
        try:
            _rows, _scopes, _registered, _inverse, cache = materialize_with_registry(
                metadata + [epic, task, unrelated], [],
            )
            initial_calls = calls
            materialize_with_registry(metadata + [epic, atom("CA-P-2"), unrelated], [], cache)
        finally:
            relations._atom_facts = original
        self.assertEqual(5, initial_calls)
        self.assertEqual(6, calls)

    def test_relation_target_change_rebuilds_old_and_new_inverse_neighbours(self):
        old = atom("CA-P-1")
        new = atom("CA-P-3")
        task = atom("CA-P-2", relation={"is_contained_by": ["CA-P-1"]})
        rows, _scopes, _registered, _inverse, cache = materialize_with_registry(
            declarations() + [old, task, new], [],
        )
        changed = atom("CA-P-2", relation={"is_contained_by": ["CA-P-3"]})
        rows, _scopes, _registered, _inverse, _cache = materialize_with_registry(
            declarations() + [old, changed, new], [], cache,
        )
        by_ref = {row["ref"]: row for row in rows}
        self.assertEqual([], by_ref["CA-P-1"]["relation_edges_json"])
        self.assertEqual("CONTAINS", by_ref["CA-P-3"]["relation_edges_json"][0]["relation_type"])

    def test_scope_alias_or_registry_change_reparses_facts(self):
        import APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relations as relations

        source = atom("CA-P-1", relation={"is_contained_by": {"scope_unit": "CA-SU-1"}})
        first_scope = {"name": "FIRST", "scope_unit_id": "CA-SU-1", "parent_name": None,
                       "declared_label": None, "ordered": False, "order_number": None,
                       "declaration_source_path": "first.md", "declaration_version": 1,
                       "relation_edges_json": [], "hash": None}
        second_scope = dict(first_scope, name="SECOND")
        original = relations._atom_facts
        calls = 0

        def counted(*args):
            nonlocal calls
            calls += 1
            return original(*args)

        relations._atom_facts = counted
        try:
            _rows, _scopes, _registered, _inverse, cache = materialize_with_registry(
                declarations() + [source], [first_scope],
            )
            rows, _scopes, _registered, _inverse, _cache = materialize_with_registry(
                declarations() + [source], [second_scope], cache,
            )
        finally:
            relations._atom_facts = original
        self.assertEqual(6, calls)
        edge = next(row for row in rows if row["ref"] == "CA-P-1")["relation_edges_json"][0]
        self.assertEqual("SECOND", edge["target_ref"])


if __name__ == "__main__":
    unittest.main()
