from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from connector_bindings import BoundRequest, ConnectorBindingError, capture_source
from connector_section_parse import SectionError
from connector_section_read import read_section_source


RAW = b"---\natom_id: CA-R-1\nversion: 1\n---\n# Summary\n\nTitle\n\n## Details\n\nContent\n"


class SectionReadTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="section-read-", dir=TOOLS.parents[2] / ".caprmedio_tmp")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.path = self.root / "source.md"
        self.path.write_bytes(RAW)
        self.source = capture_source(self.root, "source.md")

    def test_bound_read_preserves_bytes_and_rechecks_binding_without_writes(self):
        # Unit IO check only: actual selected admission is independently tested.
        bound = BoundRequest({}, (self.source,), None)
        before = self.path.stat()
        with patch.object(BoundRequest, "revalidate_before_effect") as recheck:
            raw, sections = read_section_source(bound)
        self.assertEqual(raw, RAW)
        self.assertEqual([section.title for section in sections], ["Summary", "Details"])
        recheck.assert_called_once_with()
        self.assertEqual(self.path.read_bytes(), RAW)
        self.assertEqual(self.path.stat().st_mtime_ns, before.st_mtime_ns)

    def test_stale_source_refuses_before_admission_recheck(self):
        self.path.write_bytes(RAW + b"drift\n")
        with patch.object(BoundRequest, "revalidate_before_effect") as recheck:
            with self.assertRaises(ConnectorBindingError) as error:
                read_section_source(BoundRequest({}, (self.source,), None))
            recheck.assert_not_called()
        self.assertEqual(error.exception.code, "stale_state")

    def test_unbound_missing_or_ambiguous_source_refuses(self):
        for value in (None, True, object()):
            with self.assertRaises(SectionError) as error:
                read_section_source(value)
            self.assertEqual(error.exception.code, "permission_denied")
        for sources, code in (((), "target_not_found"), ((self.source, self.source), "target_ambiguous")):
            with self.assertRaises(SectionError) as error:
                read_section_source(BoundRequest({}, sources, None))
            self.assertEqual(error.exception.code, code)


if __name__ == "__main__":
    unittest.main()
