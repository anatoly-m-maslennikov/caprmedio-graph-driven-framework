"""Historical fixture paths still require exact original source bytes."""
from __future__ import annotations

import hashlib
from pathlib import Path
import tempfile
import unittest

from selected_workflows_docker_fixture import (
    GoldenCase,
    GoldenCorpusError,
    GoldenProject,
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


if __name__ == "__main__":
    unittest.main()
