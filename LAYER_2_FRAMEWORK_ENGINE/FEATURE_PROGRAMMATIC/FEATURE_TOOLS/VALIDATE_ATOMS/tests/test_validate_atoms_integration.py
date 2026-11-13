"""Check the historical golden fixture fingerprint utility."""

from pathlib import Path
import tempfile
import unittest

from golden_fixtures import fingerprint


class FixtureFingerprintTests(unittest.TestCase):
    def test_ignores_ds_store_but_detects_content_change(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "carrier.md"
            target.write_text("original")
            before = fingerprint(root)
            (root / ".DS_Store").write_bytes(b"finder metadata")
            self.assertEqual(before, fingerprint(root))
            target.write_text("changed")
            self.assertNotEqual(before, fingerprint(root))


if __name__ == "__main__":
    unittest.main()
