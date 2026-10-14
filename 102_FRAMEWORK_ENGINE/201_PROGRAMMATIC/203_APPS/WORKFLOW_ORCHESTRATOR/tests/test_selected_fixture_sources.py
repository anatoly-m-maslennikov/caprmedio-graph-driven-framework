"""Historical fixture paths still require exact original source bytes."""

from __future__ import annotations

import hashlib
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from selected_workflows_docker_fixture import (
    GoldenCase,
    GoldenCorpusError,
    GoldenProject,
    SEMANTIC_ASSESSMENT_AUTHORITIES,
    STATUS_DOMAINS,
    _CA_O_030_PATH,
    _CURRENT_METHODOLOGY_SOURCES,
    _HISTORICAL_CA_O_030_DIGEST,
    _HISTORICAL_METHODOLOGY_SOURCES,
)


REPOSITORY = Path(__file__).resolve().parents[5]


class SelectedFixtureSourcesTests(unittest.TestCase):
    def setUp(self) -> None:
        parent = REPOSITORY / ".caprmedio_tmp/tests/selected-fixture-sources"
        parent.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=parent)
        self.addCleanup(temporary.cleanup)
        self.source = Path(temporary.name) / "source"
        self.root = Path(temporary.name) / "fixture"
        self.source.mkdir()
        self.root.mkdir()
        self.project = GoldenProject(self.source, self.root, GoldenCase("W02", "update_atom"))

    def test_w02_prepared_parameters_are_deep_copied_without_a_descriptor_scan(self) -> None:
        prepared = {"target": {"path": "prepared-subject.md"}}
        self.project._semantic_update_parameters = prepared
        with patch.object(
            self.project, "_descriptor", side_effect=AssertionError("unused scan")
        ) as descriptor:
            first = self.project.native_parameters()
            self.assertEqual(prepared, first)
            first["target"]["path"] = "caller-change.md"
            self.assertEqual(prepared, self.project.native_parameters())
        self.assertEqual("prepared-subject.md", prepared["target"]["path"])
        descriptor.assert_not_called()

    def test_w02_missing_preparation_still_refuses_without_a_descriptor_scan(self) -> None:
        with patch.object(
            self.project, "_descriptor", side_effect=AssertionError("unused scan")
        ) as descriptor:
            with self.assertRaisesRegex(
                GoldenCorpusError, "semantic assessment carrier was not prepared"
            ):
                self.project.native_parameters()
        descriptor.assert_not_called()

    def test_other_target_route_reopens_current_descriptor_and_propagates_failure(self) -> None:
        project = GoldenProject(self.source, self.root, GoldenCase("W04", "change_atom_status"))
        observations = [
            {"path": "first.md"},
            {"path": "changed.md"},
            GoldenCorpusError("missing current target"),
        ]
        with patch.object(project, "_descriptor", side_effect=observations) as descriptor:
            self.assertEqual(
                {"target": observations[0], "status": "Archived"}, project.native_parameters()
            )
            self.assertEqual(
                {"target": observations[1], "status": "Archived"}, project.native_parameters()
            )
            with self.assertRaisesRegex(GoldenCorpusError, "missing current target"):
                project.native_parameters()
        self.assertEqual([("CA-R-100",)] * 3, [call.args for call in descriptor.call_args_list])

    def test_relocated_source_keeps_exact_pin_and_historical_fixture_path(self) -> None:
        suffix = Path("001_CORE_META_MODEL/07_delivery/CA-D-276--fixture.md")
        relative = _HISTORICAL_METHODOLOGY_SOURCES / suffix
        original = self.source / _CURRENT_METHODOLOGY_SOURCES / suffix
        original.parent.mkdir(parents=True)
        original.write_bytes(b"reviewed source")
        obsolete = self.source / relative
        obsolete.parent.mkdir(parents=True)
        obsolete.write_bytes(b"obsolete leftover")
        expected = hashlib.sha256(original.read_bytes()).hexdigest()

        self.project._copy_pinned(relative, expected)
        self.assertEqual(original.read_bytes(), (self.root / relative).read_bytes())
        original.write_bytes(b"changed source")
        with self.assertRaisesRegex(GoldenCorpusError, "unavailable or stale"):
            self.project._copy_pinned(relative, expected)

    def test_only_the_exact_historical_update_action_is_copied_from_archive(self) -> None:
        current = self.source / _CA_O_030_PATH
        current.parent.mkdir(parents=True)
        current.write_bytes(b"new update action")
        archive = current.parent / "archive" / f"{current.stem}@7.md"
        archive.parent.mkdir()
        reviewed = REPOSITORY / _CA_O_030_PATH.parent / "archive" / archive.name
        archive.write_bytes(reviewed.read_bytes())

        self.project._copy_pinned(_CA_O_030_PATH, _HISTORICAL_CA_O_030_DIGEST)
        self.assertEqual(reviewed.read_bytes(), (self.root / _CA_O_030_PATH).read_bytes())
        archive.write_bytes(b"changed archive")
        with self.assertRaisesRegex(GoldenCorpusError, "unavailable or stale"):
            self.project._copy_pinned(_CA_O_030_PATH, _HISTORICAL_CA_O_030_DIGEST)
        with self.assertRaisesRegex(GoldenCorpusError, "unavailable or stale"):
            self.project._copy_pinned(_CA_O_030_PATH, "0" * 64)

    def compiler_sources(self) -> dict[str, Path]:
        source = self.source / _CURRENT_METHODOLOGY_SOURCES / "001_CORE_META_MODEL"
        source.mkdir(parents=True)
        (source / "caprmedio_framework_default_settings.toml").write_text("[query]\n")
        required = [row[3] for row in STATUS_DOMAINS] + list(SEMANTIC_ASSESSMENT_AUTHORITIES)
        paths = {}
        for atom_id in required:
            path = source / "04_requirement" / f"{atom_id}--fixture.md"
            path.parent.mkdir(exist_ok=True)
            path.write_bytes(f"exact source bytes for {atom_id}\n".encode())
            paths[atom_id] = path
        return paths

    def test_compiler_authorities_use_one_walk_and_preserve_ten_exact_copies(self) -> None:
        paths = self.compiler_sources()
        archived = next(iter(paths.values())).parent / "archive"
        archived.mkdir()
        (archived / next(iter(paths.values())).name).write_bytes(b"archived duplicate")
        unrelated = archived.parent / "CA-R-13090--not-the-status-model.md"
        unrelated.write_bytes(b"different identity")
        with patch.object(Path, "rglob", autospec=True, side_effect=Path.rglob) as walking:
            self.project._write_compiler_authority()
        original = self.source / _CURRENT_METHODOLOGY_SOURCES
        walking.assert_called_once_with(original, "*.md")
        self.assertEqual(10, len(paths))
        for source in paths.values():
            target = self.project.compiler_source_dir / source.relative_to(original)
            self.assertEqual(source.read_bytes(), target.read_bytes())
        self.assertFalse(
            (self.project.compiler_source_dir / unrelated.relative_to(original)).exists()
        )

    def test_missing_or_duplicate_authority_remains_refused(self) -> None:
        paths = self.compiler_sources()
        for atom_id in (STATUS_DOMAINS[0][3], SEMANTIC_ASSESSMENT_AUTHORITIES[0]):
            source = paths[atom_id]
            original = source.read_bytes()
            with self.subTest(atom_id=atom_id, missing=True):
                source.unlink()
                with self.assertRaisesRegex(
                    GoldenCorpusError, f"current {atom_id} .* unavailable or ambiguous"
                ):
                    self.project._write_compiler_authority()
                source.write_bytes(original)
            with self.subTest(atom_id=atom_id, duplicate=True):
                duplicate = source.with_name(f"{atom_id}--duplicate.md")
                duplicate.write_bytes(original)
                with self.assertRaisesRegex(
                    GoldenCorpusError, f"current {atom_id} .* unavailable or ambiguous"
                ):
                    self.project._write_compiler_authority()
                duplicate.unlink()

    def test_later_preparation_observes_new_duplicate_without_a_cache(self) -> None:
        source = self.compiler_sources()[STATUS_DOMAINS[0][3]]
        self.project._write_compiler_authority()
        duplicate = source.with_name(f"{STATUS_DOMAINS[0][3]}--later.md")
        duplicate.write_bytes(source.read_bytes())
        with self.assertRaisesRegex(
            GoldenCorpusError, "status-model source is unavailable or ambiguous"
        ):
            self.project._write_compiler_authority()


if __name__ == "__main__":
    unittest.main()
