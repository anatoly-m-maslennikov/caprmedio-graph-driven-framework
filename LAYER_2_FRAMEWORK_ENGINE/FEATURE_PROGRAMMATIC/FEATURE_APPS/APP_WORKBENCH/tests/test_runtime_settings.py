# CA-D-675@13
# CA-E-785@1

from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(APP_ROOT))

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.runtime_settings import (  # noqa: E402
    DEFAULT_RESULT_TTL_SECONDS,
    result_ttl_seconds,
)


class RuntimeSettingsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.path = self.root / ".caprmedio_runtime" / "caprmedio_runtime_settings.toml"

    def test_missing_file_uses_the_declared_default(self) -> None:
        self.assertEqual(DEFAULT_RESULT_TTL_SECONDS, result_ttl_seconds(self.root))

    def test_positive_configured_ttl_is_read_once_at_start(self) -> None:
        self.path.parent.mkdir(parents=True)
        self.path.write_text("[workbench]\nresult_ttl_seconds = 1\n", encoding="utf-8")
        self.assertEqual(1, result_ttl_seconds(self.root))

    def test_existing_invalid_ttl_is_not_silently_defaulted(self) -> None:
        self.path.parent.mkdir(parents=True)
        self.path.write_text("[workbench]\nresult_ttl_seconds = 0\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "positive integer"):
            result_ttl_seconds(self.root)

if __name__ == "__main__":
    unittest.main()
