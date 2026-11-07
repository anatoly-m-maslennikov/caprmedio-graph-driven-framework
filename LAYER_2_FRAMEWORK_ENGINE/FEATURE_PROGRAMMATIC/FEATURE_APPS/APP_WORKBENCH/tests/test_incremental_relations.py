# CA-E-677@18
# CA-E-780@7
from __future__ import annotations

from pathlib import Path
import random
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.incremental_relations import materialize_delta  # noqa: E402
from APP_WORKBENCH.tests.test_relations import atom, declarations  # noqa: E402


class IncrementalRelationTests(unittest.TestCase):
    def test_unique_deleted_sources_leave_no_relation_cache_keys(self):
        sources = declarations() + [atom("CA-P-100")]
        _rows, _scopes, _registered, _inverse, state, _delta = materialize_delta(sources, [])
        baseline = dict(state.outgoing)
        for number in range(200, 220):
            row = atom(f"CA-P-{number}", relation={"IS_CONTAINED_BY": ["CA-P-100"]})
            _rows, _scopes, _registered, _inverse, state, _delta = materialize_delta(
                sources + [row], [], state, {row["source_path"]: row},
            )
            rows, _scopes, _registered, _inverse, state, delta = materialize_delta(
                sources, [], state, {row["source_path"]: None},
            )
            self.assertEqual(baseline, state.outgoing)
            self.assertIn("CA-P-100.md", delta.new_atoms)
            self.assertIn(row["source_path"], delta.old_atoms)
            self.assertNotIn(row["source_path"], delta.new_atoms)
            target = next(item for item in rows if item["ref"] == "CA-P-100")
            self.assertEqual([], target["relation_edges_json"])

    def test_relation_cache_keeps_other_children_until_last_delete(self):
        sources = declarations() + [atom("CA-P-100")]
        _rows, _scopes, _registered, _inverse, state, _delta = materialize_delta(sources, [])
        children = [atom(f"CA-P-{number}", relation={"IS_CONTAINED_BY": ["CA-P-100"]}) for number in range(200, 203)]
        for child in children:
            sources.append(child)
            _rows, _scopes, _registered, _inverse, state, _delta = materialize_delta(
                sources, [], state, {child["source_path"]: child},
            )
        for index, child in enumerate(children):
            sources.remove(child)
            rows, _scopes, _registered, _inverse, state, _delta = materialize_delta(
                sources, [], state, {child["source_path"]: None},
            )
            target = next(item for item in rows if item["ref"] == "CA-P-100")
            self.assertEqual(2 - index, len(target["relation_edges_json"]))
            self.assertTrue(all(state.outgoing.values()))
        self.assertEqual({}, state.outgoing)

    def test_change_updates_source_and_inverse_neighbours_only(self):
        old = atom("CA-P-1")
        new = atom("CA-P-3")
        task = atom("CA-P-2", relation={"is_contained_by": ["CA-P-1"]})
        rows, _scopes, _registered, _inverse, state, delta = materialize_delta(declarations() + [old, task, new], [])
        self.assertIsNone(delta)
        changed = atom("CA-P-2", relation={"is_contained_by": ["CA-P-3"]})
        rows, _scopes, _registered, _inverse, state, delta = materialize_delta(
            declarations() + [old, changed, new], [], state, {"CA-P-2.md": changed},
        )
        self.assertEqual({"CA-P-1.md", "CA-P-2.md", "CA-P-3.md"}, set(delta.old_atoms))
        self.assertEqual(set(delta.old_atoms), set(delta.new_atoms))
        by_ref = {row["ref"]: row for row in rows}
        self.assertEqual([], by_ref["CA-P-1"]["relation_edges_json"])
        self.assertEqual("CONTAINS", by_ref["CA-P-3"]["relation_edges_json"][0]["relation_type"])

    def test_delete_returns_old_row_and_prunes_state(self):
        source = atom("CA-P-1")
        rows, _scopes, _registered, _inverse, state, _delta = materialize_delta(declarations() + [source], [])
        rows, _scopes, _registered, _inverse, state, delta = materialize_delta(
            declarations(), [], state, {"CA-P-1.md": None},
        )
        self.assertIn("CA-P-1.md", delta.old_atoms)
        self.assertNotIn("CA-P-1.md", delta.new_atoms)
        self.assertNotIn("CA-P-1.md", state.raw_by_path)
        self.assertNotIn("CA-P-1", [row["ref"] for row in rows])

    def test_relation_registry_change_uses_full_boundary(self):
        source = atom("CA-P-1")
        metadata = declarations()
        _rows, _scopes, _registered, _inverse, state, _delta = materialize_delta(metadata + [source], [])
        changed = dict(metadata[0], content_markdown="## Claim\n", header_json={"relations": {}})
        _rows, _scopes, _registered, _inverse, _state, delta = materialize_delta(
            [changed, metadata[1], source], [], state, {changed["source_path"]: changed},
        )
        self.assertIsNone(delta)

    def test_registry_source_prose_change_keeps_incremental_delta(self):
        metadata = declarations()
        source = atom("CA-P-1")
        _rows, _scopes, _registered, _inverse, state, _delta = materialize_delta(metadata + [source], [])
        changed = dict(metadata[0], content_markdown=metadata[0]["content_markdown"] + "\nProse only.\n")
        _rows, _scopes, _registered, _inverse, _state, delta = materialize_delta(
            [changed, metadata[1], source], [], state, {changed["source_path"]: changed},
        )
        self.assertIsNotNone(delta)

    def test_ordinary_change_parses_only_the_changed_source(self):
        import APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.incremental_relations as incremental

        first = atom("CA-P-1")
        second = atom("CA-P-2")
        original = incremental._atom_facts
        calls = 0

        def counted(*args):
            nonlocal calls
            calls += 1
            return original(*args)

        incremental._atom_facts = counted
        try:
            _rows, _scopes, _registered, _inverse, state, _delta = materialize_delta(
                declarations() + [first, second], [],
            )
            first_changed = dict(first, content_markdown="## Claim\nChanged.\n")
            materialize_delta(
                declarations() + [first_changed, second], [], state, {"CA-P-1.md": first_changed},
            )
        finally:
            incremental._atom_facts = original
        self.assertEqual(5, calls)

    def test_duplicate_reference_changes_use_full_membership_boundary(self):
        first = atom("CA-R-X")
        second = dict(atom("CA-R-X"), source_path="second.md")
        _rows, _scopes, _registered, _inverse, state, _delta = materialize_delta([first, second], [])
        self.assertEqual(frozenset({"CA-R-X.md", "second.md"}), state.excluded_paths)

        still_duplicate = dict(first, content_markdown="## Claim\nChanged.\n")
        rows, _scopes, _registered, _inverse, state, delta = materialize_delta(
            [still_duplicate, second], [], state, {"CA-R-X.md": still_duplicate},
        )
        self.assertIsNone(delta)
        self.assertEqual([], rows)

        third = dict(atom("CA-R-X"), source_path="third.md")
        rows, _scopes, _registered, _inverse, state, delta = materialize_delta(
            [still_duplicate, second, third], [], state, {"third.md": third},
        )
        self.assertIsNone(delta)
        self.assertEqual([], rows)

        renamed = dict(still_duplicate, id="CA-R-Y", ref="CA-R-Y")
        rows, _scopes, _registered, _inverse, _state, delta = materialize_delta(
            [renamed, second], [], state, {"CA-R-X.md": renamed},
        )
        self.assertIsNone(delta)
        self.assertEqual({"CA-R-X", "CA-R-Y"}, {row["ref"] for row in rows})

    def test_draft_without_reference_is_materialized_by_an_ordinary_delta(self):
        draft = dict(atom("draft"), id=None, ref=None, status_group="Draft")
        rows, _scopes, _registered, _inverse, state, _delta = materialize_delta([draft], [])
        self.assertEqual(1, len(rows))
        changed = dict(draft, content_markdown="## Claim\nChanged draft.\n")
        rows, _scopes, _registered, _inverse, _state, delta = materialize_delta(
            [changed], [], state, {"draft.md": changed},
        )
        self.assertIn("draft.md", delta.old_atoms)
        self.assertIn("draft.md", delta.new_atoms)
        self.assertEqual("Changed draft.", rows[0]["content_markdown"].splitlines()[-1])

    def test_unrelated_outgoing_sets_keep_their_identity(self):
        first = atom("CA-P-1")
        second = atom("CA-P-2", relation={"is_contained_by": ["CA-P-1"]})
        third = atom("CA-P-3")
        fourth = atom("CA-P-4", relation={"is_contained_by": ["CA-P-3"]})
        _rows, _scopes, _registered, _inverse, state, _delta = materialize_delta(
            declarations() + [first, second, third, fourth], [],
        )
        untouched = state.outgoing[("Atom", "CA-P-3")]
        changed = atom("CA-P-2")
        _rows, _scopes, _registered, _inverse, next_state, _delta = materialize_delta(
            declarations() + [first, changed, third, fourth], [], state, {"CA-P-2.md": changed},
        )
        self.assertIs(untouched, next_state.outgoing[("Atom", "CA-P-3")])

    def test_rename_with_same_reference_stays_incremental(self):
        source = atom("CA-P-1")
        _rows, _scopes, _registered, _inverse, state, _delta = materialize_delta([source], [])
        moved = dict(source, source_path="moved.md")
        rows, _scopes, _registered, _inverse, state, delta = materialize_delta(
            [moved], [], state, {"CA-P-1.md": None, "moved.md": moved},
        )
        self.assertIsNotNone(delta)
        self.assertIn("CA-P-1.md", delta.old_atoms)
        self.assertIn("moved.md", delta.new_atoms)
        self.assertEqual(["moved.md"], list(state.atom_order))
        self.assertEqual(["moved.md"], [row["source_path"] for row in rows])

    def test_same_reference_rename_keeps_edges_in_both_change_orders(self):
        target = atom("CA-P-1")
        source = atom("CA-P-2", relation={"is_contained_by": ["CA-P-1"]})
        initial = declarations() + [target, source]
        moved = dict(source, source_path="moved.md")
        expected, _scopes, _types, _inverse, _state, _delta = materialize_delta(
            declarations() + [target, moved], [],
        )

        entries = [("CA-P-2.md", None), ("moved.md", moved)]
        for seed in range(8):
            shuffled = list(entries)
            random.Random(seed).shuffle(shuffled)
            changes = dict(shuffled)
            _rows, _scopes, _types, _inverse, state, _delta = materialize_delta(initial, [])
            rows, _scopes, _types, _inverse, _state, delta = materialize_delta(
                declarations() + [target, moved], [], state, changes,
            )
            self.assertIsNotNone(delta)
            self.assertEqual(expected, rows)
            by_ref = {row["ref"]: row for row in rows}
            self.assertEqual("IS_CONTAINED_BY", by_ref["CA-P-2"]["relation_edges_json"][0]["relation_type"])
            self.assertEqual("CONTAINS", by_ref["CA-P-1"]["relation_edges_json"][0]["relation_type"])

    def test_new_duplicate_forces_full_but_ignored_delete_does_not(self):
        first = atom("CA-P-1")
        _rows, _scopes, _registered, _inverse, state, _delta = materialize_delta([first], [])
        second = dict(atom("CA-P-2"), source_path="second.md")
        third = dict(atom("CA-P-2"), source_path="third.md")
        rows, _scopes, _registered, _inverse, state, delta = materialize_delta(
            [first, second, third], [], state, {"second.md": second, "third.md": third},
        )
        self.assertIsNone(delta)
        self.assertEqual(["CA-P-1"], [row["ref"] for row in rows])

        changed = dict(first, content_markdown="## Claim\nChanged.\n")
        rows, _scopes, _registered, _inverse, _state, delta = materialize_delta(
            [changed], [], state, {"ignored.md": None, "CA-P-1.md": changed},
        )
        self.assertIsNotNone(delta)
        self.assertEqual("Changed.", rows[0]["content_markdown"].splitlines()[-1])


if __name__ == "__main__":
    unittest.main()
