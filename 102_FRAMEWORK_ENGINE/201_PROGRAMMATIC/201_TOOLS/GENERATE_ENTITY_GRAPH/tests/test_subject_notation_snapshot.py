"""As-declared Core snapshot boundaries and create-only publication."""

from __future__ import annotations

import hashlib
import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


TOOL_DIRECTORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOL_DIRECTORY))
import graph_fact_context as facts  # noqa: E402
import subject_notation_snapshot as snapshot  # noqa: E402

TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp/tests/test_subject_notation_snapshot"
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


def atom(atom_id, target, dependencies=(), *, status="Active", owner="CORE_META_MODEL", target_scope="CORE_META_MODEL"):
    dependency_lines = "" if dependencies is None else "  depends_on: [" + ", ".join(json.dumps(value) for value in dependencies) + "]\n"
    return (f"---\natom_id: {atom_id}\nversion: 1\ncontent_role: Requirement\ntype: Demand\nstatus: {status}\n"
            f"current_scope_unit: {owner}\nclaim_target_scope_unit: {target_scope}\nsubjects:\n  governs: {json.dumps(target)}\n"
            f"{dependency_lines}---\n# Summary\n\nSource summary\n\n## Scope\n\nSelected source.\n\n## Claim\n\n"
            "No Main Content or native model validity is inferred by this snapshot.\n\n## Details\n")


class SubjectNotationSnapshotTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.repository = Path(self.temporary.name)
        self.control = self.repository / ".caprmedio_caprmedio"
        self.core = self.control / "core"
        self.core.mkdir(parents=True)
        (self.control / "caprmedio_project_settings.toml").write_text(
            "[paths]\ncontrol_root = '.caprmedio_caprmedio'\nprojection_root = '.caprmedio_caprmedio/_projection'\n", encoding="utf-8")
        self.structure = self.control / "project_structure.toml"
        self.structure.write_text("[[scope_units]]\nscope_unit_name = 'CORE_META_MODEL'\nauthority_path = '.caprmedio_caprmedio/core'\nauthority_mode = 'strict'\n", encoding="utf-8")
        self.first = self.core / "CA-R-9101.md"
        self.first.write_text(atom("CA-R-9101", "Atom/Status: Active", ("Artifact/Atom", "CA-R-9102"), target_scope="ANOTHER_TARGET_SCOPE"), encoding="utf-8")
        (self.core / "CA-R-9102.md").write_text(atom("CA-R-9102", "Atom", None), encoding="utf-8")
        (self.core / "CA-R-9103.md").write_text(atom("CA-R-9103", "LowercaseStatusObject", status="active"), encoding="utf-8")
        (self.core / "CA-R-9104.md").write_text(atom("CA-R-9104", "ForeignOwnerObject", owner="FOREIGN"), encoding="utf-8")
        self.outputs = [self.repository / snapshot._OUTPUT_DIRECTORY / name for name in snapshot._OUTPUT_NAMES]

    def prepare(self):
        carriers, frontier, selection = snapshot.current_core_inputs(self.repository)
        return snapshot.prepare_subject_notation_snapshot(self.repository, carriers, frontier, selection)

    def source_bytes(self):
        return {path.relative_to(self.repository).as_posix(): path.read_bytes() for path in self.core.glob("*.md")}

    def test_full_targets_support_prefixes_and_all_steps_are_unclassified(self) -> None:
        before = self.source_bytes()
        prepared = self.prepare()
        data = prepared.as_dict()
        self.assertEqual({"frontier_sources": 4, "selected_sources": 2, "excluded_sources": 2, "occurrences": 4,
                          "full_target_nodes": 4, "support_only_nodes": 2, "nodes": 6, "source_links": 4,
                          "unclassified_steps": 3, "component_pairs": 3}, data["counts"])
        self.assertEqual({"Atom", "Atom/Status", "Atom/Status: Active", "Artifact", "Artifact/Atom", "CA-R-9102"},
                         {node["identity"] for node in data["nodes"]})
        self.assertNotIn("CA-R-9101", {node["identity"] for node in data["nodes"]})
        self.assertNotIn("ForeignOwnerObject", str(data["nodes"]))
        self.assertNotIn("LowercaseStatusObject", str(data["nodes"]))
        self.assertEqual({"status-not-exact-Active", "owner-not-CORE_META_MODEL"}, {row["reason"] for row in data["excluded_sources"]})
        self.assertTrue(data["diagnostic_only"])
        self.assertEqual([], data["native_facts"])
        self.assertEqual("not_performed", data["semantic_admission"])
        self.assertTrue(all(row["classification"] == "UNCLASSIFIED" for row in data["qualification_steps"]))
        self.assertEqual({("/", "Atom", "Status"), ("/", "Artifact", "Atom"), (":", "Status", "Active")},
                         {(pair["separator"], pair["left_component"], pair["right_component"]) for pair in data["pair_inventory"]})
        for row in [*data["nodes"], *data["qualification_steps"], *data["pair_inventory"]]:
            self.assertTrue(row["lineages"])
            self.assertTrue(all(lineage["source_ref"]["atom_id"] in {"CA-R-9101", "CA-R-9102"} for lineage in row["lineages"]))
        self.assertEqual(before, self.source_bytes())
        self.assertTrue(prepared.raw_frontmatter("CA-R-9101").startswith(b"atom_id:"))
        self.assertIn(b'governs: "Atom/Status: Active"', prepared.raw_frontmatter("CA-R-9101"))
        body = dict(data)
        digest = body.pop("snapshot_sha256")
        self.assertEqual(hashlib.sha256(facts.canonical_bytes(body)).hexdigest(), digest)

    def test_exact_owned_active_selection_and_registered_frontier_required(self) -> None:
        carriers, frontier, selection = snapshot.current_core_inputs(self.repository)
        for invalid in ({"atom_ids": ["CA-R-9101"], "scope_unit_names": ["CORE_META_MODEL"]},
                        {"atom_ids": ["CA-R-9101", "CA-R-9102", "CA-R-9103"], "scope_unit_names": ["CORE_META_MODEL"]},
                        {"atom_ids": ["CA-R-9101", "CA-R-9102", "CA-R-9104"], "scope_unit_names": ["CORE_META_MODEL"]},
                        {"atom_ids": selection["atom_ids"], "scope_unit_names": []}):
            with self.subTest(selection=invalid), self.assertRaises(snapshot.SubjectNotationSnapshotError):
                snapshot.prepare_subject_notation_snapshot(self.repository, carriers, frontier, invalid)
        with self.assertRaises(ValueError):
            snapshot.prepare_subject_notation_snapshot(self.repository, carriers,
                {key: value for key, value in frontier.items() if key != "project_structure"}, selection)

    def test_unsupported_source_form_keeps_diagnostic_and_other_source(self) -> None:
        self.first.write_text(atom("CA-R-9101", "Object", ("Parent", "Parent")), encoding="utf-8")
        data = self.prepare().as_dict()
        self.assertEqual("incomplete", data["coverage"]["disposition"])
        self.assertEqual(1, data["coverage"]["unresolved_source_count"])
        self.assertEqual(["Atom"], [node["identity"] for node in data["nodes"]])
        self.assertTrue(data["diagnostics"])
        self.assertEqual([], data["native_facts"])

    def test_default_cli_is_dry_and_dot_keeps_separate_source_namespace(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            result = snapshot.main(["--repository", str(self.repository)])
        self.assertEqual(0, result)
        self.assertEqual("dry_run", json.loads(output.getvalue())["outcome"])
        self.assertFalse(any(path.exists() for path in self.outputs))
        dot = snapshot.snapshot_dot(self.prepare())
        target_hash = hashlib.sha256(b"CA-R-9102").hexdigest()
        self.assertIn("object_" + target_hash, dot)
        self.assertIn("source_" + target_hash, dot)
        self.assertIn("UNCLASSIFIED", dot)
        self.assertIn("ATOM INCIDENCE GOVERNS", dot)
        self.assertNotIn("NARROWER_THAN", dot)
        self.assertNotIn("IS_BORNE_BY", dot)

    def test_create_only_publication_preserves_sources_and_returns_actual_hashes(self) -> None:
        before = self.source_bytes()
        prepared = self.prepare()
        receipt = snapshot.persist_subject_notation_snapshot(prepared)
        self.assertEqual("diagnostic_snapshot_created", receipt["outcome"])
        self.assertEqual("not_performed", receipt["run_recording"])
        self.assertEqual(prepared.snapshot_sha256, json.loads(self.outputs[0].read_bytes())["snapshot_sha256"])
        for record in receipt["outputs"]:
            self.assertEqual(hashlib.sha256((self.repository / record["path"]).read_bytes()).hexdigest(), record["sha256"])
        existing = [path.read_bytes() for path in self.outputs]
        with self.assertRaises(snapshot.SubjectNotationSnapshotError) as failure:
            snapshot.persist_subject_notation_snapshot(prepared)
        self.assertEqual("snapshot-output-exists", failure.exception.code)
        self.assertEqual(existing, [path.read_bytes() for path in self.outputs])
        self.assertEqual(before, self.source_bytes())

    def test_one_existing_output_prevents_both_writes(self) -> None:
        prepared = self.prepare()
        self.outputs[1].parent.mkdir(parents=True)
        self.outputs[1].write_bytes(b"preexisting user artifact\n")
        with self.assertRaises(snapshot.SubjectNotationSnapshotError):
            snapshot.persist_subject_notation_snapshot(prepared)
        self.assertFalse(self.outputs[0].exists())
        self.assertEqual(b"preexisting user artifact\n", self.outputs[1].read_bytes())

    def test_write_failure_reports_and_preserves_the_created_partial_file(self) -> None:
        prepared = self.prepare()
        original = Path.open

        class FailingWriter:
            def __init__(self, handle):
                self.handle = handle

            def __enter__(self):
                return self

            def __exit__(self, *unused):
                self.handle.close()

            def write(self, payload):
                self.handle.write(payload[:32])
                raise OSError("simulated write failure")

        def opened(path, *args, **kwargs):
            handle = original(path, *args, **kwargs)
            return FailingWriter(handle) if path == self.outputs[0] and args == ("xb",) else handle

        with patch.object(Path, "open", autospec=True, side_effect=opened):
            with self.assertRaises(snapshot.SubjectNotationSnapshotError) as failure:
                snapshot.persist_subject_notation_snapshot(prepared)
        self.assertEqual("snapshot-publication-incomplete", failure.exception.code)
        self.assertEqual((self.outputs[0].relative_to(self.repository).as_posix(),), failure.exception.created_paths)
        self.assertEqual(32, self.outputs[0].stat().st_size)
        self.assertFalse(self.outputs[1].exists())

    def test_stale_source_added_member_and_structure_stop_before_publication(self) -> None:
        prepared = self.prepare()
        original = self.first.read_bytes()
        self.first.write_bytes(original + b"\nchanged after snapshot\n")
        with self.assertRaises(ValueError):
            snapshot.persist_subject_notation_snapshot(prepared)
        self.assertFalse(any(path.exists() for path in self.outputs))
        self.first.write_bytes(original)
        added = self.core / "CA-R-9105.md"
        added.write_text(atom("CA-R-9105", "NewObject"), encoding="utf-8")
        with self.assertRaises(ValueError):
            snapshot.persist_subject_notation_snapshot(prepared)
        added.unlink()
        self.structure.write_bytes(self.structure.read_bytes() + b"\n# changed structure\n")
        with self.assertRaises(ValueError):
            snapshot.persist_subject_notation_snapshot(prepared)
        self.assertFalse(any(path.exists() for path in self.outputs))

    def test_output_symlink_cannot_write_into_source_authority(self) -> None:
        prepared = self.prepare()
        self.outputs[0].parent.mkdir(parents=True)
        self.outputs[0].symlink_to(self.first)
        before = self.first.read_bytes()
        with self.assertRaises(ValueError):
            snapshot.persist_subject_notation_snapshot(prepared)
        self.assertEqual(before, self.first.read_bytes())
        self.assertFalse(self.outputs[1].exists())

    def test_snapshot_is_detached_not_caller_minted_and_code_drift_is_stale(self) -> None:
        prepared = self.prepare()
        detached = prepared.as_dict()
        detached["nodes"][0]["identity"] = "caller invented"
        self.assertNotEqual(detached, prepared.as_dict())
        with self.assertRaises(snapshot.SubjectNotationSnapshotError):
            snapshot.SubjectNotationSnapshot(b"{}", self.repository, (), b"{}", b"{}", ())
        original = Path.read_bytes
        changed = snapshot._IMPLEMENTATION_PATH.read_bytes() + b"\n# code drift\n"
        with patch.object(Path, "read_bytes", autospec=True, side_effect=lambda path: changed if path == snapshot._IMPLEMENTATION_PATH else original(path)):
            with self.assertRaises(snapshot.SubjectNotationSnapshotError) as failure:
                snapshot.persist_subject_notation_snapshot(prepared)
            self.assertEqual("profile-stale", failure.exception.code)


if __name__ == "__main__":
    unittest.main()
