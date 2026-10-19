"""Current-source CLI output preserves source and unrelated output bytes."""

import datetime as dt
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml


SCRIPT = Path(__file__).resolve().parents[1] / "render_entity_tree.py"
TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp/tests/test_render_entity_tree"


def atom(version=7, subject="Alpha.Label"):
    return (
        f"---\natom_id: CA-R-9001\nversion: {version}\nstatus: Active\n"
        "content_role: Requirement\nsubjects:\n"
        f"  governs: {json.dumps(subject)}\n  depends_on: []\n---\n# Source\n"
    )


class RenderEntityTreeTests(unittest.TestCase):
    def setUp(self):
        TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / ".git").mkdir()
        self.projection = self.root / ".caprmedio_caprmedio/_projection"
        self.projection.mkdir(parents=True)
        settings = self.projection.parent / "caprmedio_project_settings.toml"
        settings.write_text('[artifact_timestamps]\ntimezone = "UTC"\n', encoding="utf-8")
        self.source = self.root / "sources/CA-R-9001.md"
        self.source.parent.mkdir()
        self.source.write_text(atom(), encoding="utf-8")
        self.snapshot = self.projection / "graph.json"
        self.snapshot.write_text('{"stale": "irrelevant old graph"}', encoding="utf-8")
        self.output = self.projection / "CA-PROJ-901-CORE--Entities-Graph--Current-Atoms.md"

    def run_cli(self, output=None, source_root=None, *, view="inherency", selection="Current Atoms"):
        command = [
            sys.executable, "-B", str(SCRIPT), str(source_root or self.source.parent),
            "--projection-id", "CA-PROJ-901", "--named-selection", selection,
            "--scope-name", "CORE", "--view", view,
        ]
        if output is not None:
            command.extend(["--output", str(output)])
        return subprocess.run(command, cwd=self.root, text=True, capture_output=True, timeout=30)

    def source_bytes(self):
        return [path.read_bytes() for path in (self.source, self.snapshot)]

    def test_stdout_and_published_markdown_use_current_atoms_and_preserve_inputs(self):
        before = self.source_bytes()
        started = dt.datetime.now(dt.UTC).replace(microsecond=0)
        stdout = self.run_cli()
        self.assertEqual(0, stdout.returncode, stdout.stderr)
        self.assertFalse(self.output.exists())
        published = self.run_cli(self.output)
        self.assertEqual(0, published.returncode, published.stderr)
        self.assertEqual("", published.stdout)
        document = self.output.read_text(encoding="utf-8")
        metadata = yaml.safe_load(document.split("---\n", 2)[1])
        moment = dt.datetime.strptime(metadata["updated_at"], "%Y-%m-%d %H:%M:%S %z")
        self.assertLessEqual(started, moment)
        self.assertLessEqual(moment, dt.datetime.now(dt.UTC))
        self.assertEqual(dt.timedelta(0), moment.utcoffset())
        self.assertEqual(["CA-R-9001@7"], metadata["sources"])
        self.assertEqual("CA-PROJ-901", metadata["projection_id"])
        self.assertEqual("Current Atoms", metadata["named_selection"])
        self.assertEqual(["sources"], metadata["source_of_truth"])
        self.assertEqual(stdout.stdout.split("---\n", 2)[2], document.split("---\n", 2)[2])
        self.assertIn("sources", document)
        self.assertNotIn("Saved snapshot", document)
        self.assertIn("### Alpha", document)
        self.assertIn("\t. Alpha.Label", document)
        self.assertIn("Native admission: not_performed", document)
        self.assertEqual(before, self.source_bytes())

    def test_declaration_view_excludes_live_atom_relation_tuples(self):
        self.source.write_text(
            atom(subject="Entity/Relation/Type: Custom").replace(
                "\n---\n# Source", "\nrelations: {depends_on: [CA-R-123]}\n---\n# Source"
            ), encoding="utf-8",
        )
        before = self.source_bytes()
        result = self.run_cli(view="declarations", selection="Relation Types and Graph Rules")
        self.assertEqual(0, result.returncode, result.stderr)
        for heading in ("## Relation Types", "## Graph Rules", "## Source limitations"):
            self.assertIn(heading, result.stdout)
        self.assertIn("Custom", result.stdout)
        self.assertIn("empty for the selected source set", result.stdout)
        self.assertNotIn("CA-R-123", result.stdout)
        self.assertEqual(before, self.source_bytes())

    def test_identity_mismatch_or_wrong_filename_preserves_existing_output(self):
        self.assertEqual(0, self.run_cli(self.output).returncode)
        document = self.output.read_bytes()
        renamed = self.run_cli(self.output, selection="Other Atoms")
        self.assertEqual(1, renamed.returncode)
        self.assertIn("Projection filename must be", renamed.stderr)
        self.assertEqual(document, self.output.read_bytes())
        other_view = self.run_cli(self.output, view="declarations")
        self.assertEqual(1, other_view.returncode)
        self.assertIn("distinct Projection identity", other_view.stderr)
        self.assertEqual(document, self.output.read_bytes())
        self.output.write_bytes(document.replace(b"projection_id: CA-PROJ-901", b"projection_id: CA-PROJ-902"))
        mismatched = self.output.read_bytes()
        result = self.run_cli(self.output)
        self.assertEqual(1, result.returncode)
        self.assertIn("Existing Projection identity", result.stderr)
        self.assertEqual(mismatched, self.output.read_bytes())

    def test_next_run_reflects_live_subject_version_and_ignores_stale_snapshot(self):
        first = self.run_cli(self.output)
        self.assertEqual(0, first.returncode, first.stderr)
        self.source.write_text(atom(8, "Beta.Code"), encoding="utf-8")
        before = self.source_bytes()
        second = self.run_cli(self.output)
        self.assertEqual(0, second.returncode, second.stderr)
        document = self.output.read_text(encoding="utf-8")
        self.assertIn("CA-R-9001@8", document)
        self.assertIn("Beta.Code", document)
        self.assertNotIn("Alpha.Label", document)
        self.assertNotIn("CA-R-9001@7", document)
        self.assertEqual(before, self.source_bytes())

    def test_missing_source_folder_preserves_existing_output(self):
        self.output.write_bytes(b"prior projection\n")
        before = self.source_bytes()
        result = self.run_cli(self.output, self.root / "missing")
        self.assertEqual(1, result.returncode)
        self.assertIn("Cannot render Entities Graph", result.stderr)
        self.assertEqual(b"prior projection\n", self.output.read_bytes())
        self.assertEqual(before, self.source_bytes())

    def test_invalid_source_metadata_preserves_existing_output(self):
        self.output.write_bytes(b"prior projection\n")
        for malformed in (atom(version=0), "---\natom_id: [broken\n---\n# Source\n"):
            self.source.write_text(malformed, encoding="utf-8")
            before = self.source_bytes()
            result = self.run_cli(self.output)
            with self.subTest(source=malformed):
                self.assertEqual(1, result.returncode)
                self.assertIn("Cannot render Entities Graph", result.stderr)
                self.assertEqual(b"prior projection\n", self.output.read_bytes())
                self.assertEqual(before, self.source_bytes())

    def test_outside_projection_and_symlink_outputs_are_rejected(self):
        outside = self.root / "unrelated.md"
        outside.write_bytes(b"unrelated bytes\n")
        self.output.symlink_to(outside)
        before = self.source_bytes()
        for destination in (outside, self.output):
            result = self.run_cli(destination)
            with self.subTest(destination=destination.name):
                self.assertEqual(1, result.returncode)
                self.assertIn("Output must be a non-symlink path", result.stderr)
                self.assertEqual(b"unrelated bytes\n", outside.read_bytes())
                self.assertTrue(self.output.is_symlink())
                self.assertEqual(before, self.source_bytes())


if __name__ == "__main__":
    unittest.main()
