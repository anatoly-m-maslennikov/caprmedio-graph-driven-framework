"""Directory moves preserve assets and report incomplete operations."""
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
ROOT = TOOLS.parents[2]
sys.path.insert(0, str(TOOLS))
from ATOM_LIFECYCLE import directory_effect, effects  # noqa: E402


class DirectoryEffectTest(unittest.TestCase):
    def setUp(self):
        parent = ROOT / ".caprmedio_tmp/CA-P-2791/CA-P-2934/carrier-effects"
        parent.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=parent)
        self.base = Path(self.temp.name)
        self.addCleanup(self.temp.cleanup)
        self.source = self.base / "source"
        self.source.mkdir()
        (self.source / "empty").mkdir()
        (self.source / "nested").mkdir()
        (self.source / "nested" / "asset.bin").write_bytes(b"\x00\xffasset")
        self.destination = self.base / "destination"

    def test_move_preserves_bytes_and_empty_directories(self):
        result = directory_effect.move_directory(ROOT, self.source, self.destination)
        self.assertEqual([], result.errors)
        self.assertFalse(self.source.exists())
        self.assertTrue((self.destination / "empty").is_dir())
        self.assertEqual(b"\x00\xffasset", (self.destination / "nested" / "asset.bin").read_bytes())
        self.assertTrue(all(effect["state"] == "known" for effect in result.effects))
        self.assertNotIn(str(ROOT), str(result.effects))

    def test_existing_destination_and_unsafe_paths_are_refused(self):
        self.destination.mkdir()
        (self.destination / "keep").write_bytes(b"keep")
        alias = self.base / "alias"
        alias.symlink_to(self.source, target_is_directory=True)
        for source, destination in ((self.source, self.destination), (alias, self.base / "other"),
                                    (self.source, ROOT / ".." / "escape"),
                                    (self.source, self.source / "inside")):
            result = directory_effect.move_directory(ROOT, source, destination)
            self.assertTrue(result.errors)
            self.assertFalse(result.effects)
        self.assertEqual(b"keep", (self.destination / "keep").read_bytes())
        self.assertTrue(self.source.exists())

    def test_symlink_inside_source_is_refused_before_writes(self):
        (self.source / "link").symlink_to(self.source / "empty")
        result = directory_effect.move_directory(ROOT, self.source, self.destination)
        self.assertTrue(result.errors)
        self.assertFalse(result.effects)
        self.assertFalse(self.destination.exists())

    def test_rewrite_pinned_asset_and_preserve_other_assets(self):
        (self.source / "history.bin").write_bytes(b"history")
        asset = Path("nested/asset.bin")
        pin = hashlib.sha256(b"\x00\xffasset").hexdigest()
        result = directory_effect.move_directory(
            ROOT, self.source, self.destination, rewrites={asset: (pin, b"updated")})
        self.assertEqual([], result.errors)
        self.assertFalse(self.source.exists())
        self.assertEqual(b"updated", (self.destination / asset).read_bytes())
        self.assertEqual(b"history", (self.destination / "history.bin").read_bytes())
        self.assertTrue((self.destination / "empty").is_dir())

    def test_invalid_rewrite_preflight_leaves_source_and_destination_untouched(self):
        pin = hashlib.sha256(b"\x00\xffasset").hexdigest()
        for rewrites in ({Path("nested/asset.bin"): ("stale", b"new")},
                         {Path("missing"): (pin, b"new")},
                         {Path("../escape"): (pin, b"new")}):
            result = directory_effect.move_directory(ROOT, self.source, self.destination, rewrites=rewrites)
            self.assertTrue(result.errors)
            self.assertFalse(result.effects)
            self.assertFalse(self.destination.exists())
            self.assertEqual(b"\x00\xffasset", (self.source / "nested/asset.bin").read_bytes())

    def test_rewrite_verification_failure_preserves_source_and_reports_destination(self):
        asset = Path("nested/asset.bin")
        pin = hashlib.sha256(b"\x00\xffasset").hexdigest()
        real_read_tree = directory_effect._read_tree
        def bad_destination(root, path):
            directories, files = real_read_tree(root, path)
            if path == self.destination:
                files[asset] = "incorrect"
            return directories, files
        with patch.object(directory_effect, "_read_tree", side_effect=bad_destination):
            result = directory_effect.move_directory(
                ROOT, self.source, self.destination, rewrites={asset: (pin, b"updated")})
        self.assertTrue(result.errors)
        self.assertTrue(result.effects)
        self.assertEqual(b"\x00\xffasset", (self.source / asset).read_bytes())
        self.assertEqual(b"updated", (self.destination / asset).read_bytes())

    def test_asset_and_tree_limits_refuse_before_writes(self):
        for limits in ({"max_file_bytes": 2}, {"max_total_read_bytes": 2}):
            with patch.dict(directory_effect.CEILINGS, limits):
                result = directory_effect.move_directory(ROOT, self.source, self.destination)
            self.assertTrue(result.errors)
            self.assertFalse(result.effects)
            self.assertFalse(self.destination.exists())
            self.assertTrue(self.source.exists())

    def test_removal_failure_reports_completed_destination(self):
        failed = effects.Result(errors=[{"code": "backend_failure", "message": "failure", "field": None}])
        with patch.object(effects, "remove", return_value=failed):
            result = directory_effect.move_directory(ROOT, self.source, self.destination)
        self.assertTrue(result.errors)
        self.assertTrue(result.effects)
        self.assertTrue(self.source.exists())
        self.assertEqual(b"\x00\xffasset", (self.destination / "nested" / "asset.bin").read_bytes())


if __name__ == "__main__":
    unittest.main()
