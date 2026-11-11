"""Mechanical carrier effects use exact pins and report partial outcomes."""
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
ROOT = TOOLS.parents[2]
sys.path.insert(0, str(TOOLS))
from ATOM_LIFECYCLE import effects  # noqa: E402


def digest(value):
    return hashlib.sha256(value).hexdigest()


class LifecycleEffectsTest(unittest.TestCase):
    def setUp(self):
        parent = ROOT / ".caprmedio_tmp/CA-P-2791/CA-P-2934/carrier-effects"
        parent.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=parent)
        self.directory = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)

    def test_create_no_overwrite_replace_noop_and_remove(self):
        path = self.directory / "carrier.md"
        self.assertEqual([], effects.create(ROOT, path, b"one").errors)
        collision = effects.create(ROOT, path, b"two")
        self.assertTrue(collision.errors)
        self.assertEqual(b"one", path.read_bytes())
        stale = effects.replace(ROOT, path, digest(b"old"), b"two")
        self.assertTrue(stale.errors)
        self.assertEqual(b"one", path.read_bytes())
        self.assertEqual([], effects.replace(ROOT, path, digest(b"one"), b"one").effects)
        changed = effects.replace(ROOT, path, digest(b"one"), b"two")
        self.assertEqual("known", changed.effects[0]["state"])
        self.assertEqual(b"two", path.read_bytes())
        self.assertTrue(effects.remove(ROOT, path, digest(b"one")).errors)
        self.assertEqual([], effects.remove(ROOT, path, digest(b"two")).errors)
        self.assertFalse(path.exists())

    def test_relocate_reports_created_destination_if_source_became_stale(self):
        source = self.directory / "source.md"
        destination = self.directory / "target.md"
        source.write_bytes(b"one")
        real_remove = effects.remove
        def change_then_remove(root, path, expected):
            path.write_bytes(b"changed")
            return real_remove(root, path, expected)
        with patch.object(effects, "remove", side_effect=change_then_remove):
            result = effects.relocate(ROOT, source, digest(b"one"), destination)
        self.assertEqual(["create"], [effect["operation"] for effect in result.effects])
        self.assertEqual("stale_state", result.errors[0]["code"])
        self.assertEqual(b"changed", source.read_bytes())
        self.assertEqual(b"one", destination.read_bytes())

    def test_readback_failure_reports_unknown_effect(self):
        path = self.directory / "carrier.md"
        with patch.object(effects, "_read", side_effect=OSError("readback unavailable")):
            result = effects.create(ROOT, path, b"one")
        self.assertEqual("unknown", result.effects[0]["state"])
        self.assertEqual("effect_uncertain", result.errors[0]["code"])
        self.assertEqual(b"one", path.read_bytes())

    def test_parent_symlink_and_project_escape_are_refused(self):
        directory = self.directory / "real"
        directory.mkdir()
        original = directory / "original.md"
        original.write_bytes(b"one")
        alias = self.directory / "alias"
        alias.symlink_to(directory, target_is_directory=True)
        for result in (
            effects.create(ROOT, alias / "new.md", b"two"),
            effects.replace(ROOT, alias / "original.md", digest(b"one"), b"two"),
            effects.remove(ROOT, alias / "original.md", digest(b"one")),
            effects.create(ROOT, ROOT / ".." / "escape.md", b"two"),
            effects.remove(ROOT, ROOT.parent / "escape.md", digest(b"one")),
        ):
            self.assertTrue(result.errors)
            self.assertFalse(result.effects)
            self.assertNotIn(str(ROOT), str(result.errors))
        self.assertEqual(b"one", original.read_bytes())
        self.assertFalse((directory / "new.md").exists())

    def test_effect_targets_are_project_relative(self):
        path = self.directory / "carrier.md"
        result = effects.create(ROOT, path, b"one")
        self.assertEqual(path.relative_to(ROOT).as_posix(), result.effects[0]["target"])
        self.assertNotIn(str(ROOT), str(result.effects))

    def test_symlink_source_is_refused(self):
        target = self.directory / "target"
        link = self.directory / "link"
        target.write_bytes(b"one")
        link.symlink_to(target)
        result = effects.remove(ROOT, link, digest(b"one"))
        self.assertTrue(result.errors)
        self.assertEqual(b"one", target.read_bytes())
        self.assertTrue(link.is_symlink())


if __name__ == "__main__":
    unittest.main()
