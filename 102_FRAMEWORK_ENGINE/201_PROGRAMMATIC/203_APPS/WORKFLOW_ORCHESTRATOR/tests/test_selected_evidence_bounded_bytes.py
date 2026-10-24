"""Safe byte-carrier regressions independent of live Project authority."""

from pathlib import Path
import os
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

from selected_evidence_io import bounded_bytes  # noqa: E402
from selected_execution_contracts import SelectedExecutionError  # noqa: E402


class BoundedBytesTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.path = self.root / "evidence.json"
        self.path.write_bytes(b'{"value":1}')

    def test_reads_regular_carrier_and_refuses_oversize_or_invalid_limit(self) -> None:
        self.assertEqual(self.path.read_bytes(), bounded_bytes(self.path, 32))
        for limit in (1, 0, True):
            with self.subTest(limit=limit), self.assertRaises(SelectedExecutionError):
                bounded_bytes(self.path, limit)

    def test_refuses_links_and_nonregular_carriers(self) -> None:
        link = self.root / "link"
        link.symlink_to(self.path)
        for carrier in (link, self.root):
            with self.subTest(carrier=carrier), self.assertRaises(SelectedExecutionError):
                bounded_bytes(carrier, 32)
        link.unlink()
        link.symlink_to(self.root / "absent")
        with self.assertRaises(SelectedExecutionError):
            bounded_bytes(link, 32)

    def test_growth_after_stat_is_still_bounded(self) -> None:
        mode = self.path.stat().st_mode
        with patch("os.fstat", return_value=SimpleNamespace(st_mode=mode, st_size=0)):
            with self.assertRaisesRegex(SelectedExecutionError, "oversized"):
                bounded_bytes(self.path, 3)

    def test_read_failure_closes_the_same_descriptor(self) -> None:
        with patch("os.close", wraps=os.close) as close, patch("os.read", side_effect=OSError):
            with self.assertRaises(SelectedExecutionError):
                bounded_bytes(self.path, 32)
        close.assert_called_once()
        descriptor = close.call_args.args[0]
        with self.assertRaises(OSError):
            os.fstat(descriptor)


if __name__ == "__main__":
    unittest.main()
