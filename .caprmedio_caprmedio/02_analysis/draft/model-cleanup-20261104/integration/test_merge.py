import hashlib
import tempfile
import unittest
from pathlib import Path

from merge import is_projection_form_edit, merge_text, read_pinned


class MergeTests(unittest.TestCase):
    def test_disjoint_edits_merge(self):
        before = "alpha\nbeta\n"
        left = "ALPHA\nbeta\n"
        right = "alpha\nBETA\n"
        merged, _ = merge_text(before, [("syntax", left), ("legacy", right)])
        self.assertEqual(merged, "ALPHA\nBETA\n")

    def test_overlapping_edits_fail(self):
        before = "alpha\nbeta\n"
        with self.assertRaisesRegex(ValueError, "overlapping source edits"):
            merge_text(before, [("syntax", "ALPHA\nbeta\n"), ("relations", "ALPHA!\nbeta\n")])

    def test_stale_pin_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "source.md"
            path.write_text("current")
            stale = hashlib.sha256(b"before").hexdigest()
            with self.assertRaisesRegex(ValueError, "stale source pin"):
                read_pinned(path, stale)

    def test_projection_form_scope_uses_only_current_allowed_values(self):
        allowed = {"Catalog", "Map", "Hub"}
        for value in allowed:
            edit = {"old": f"CAPRMEDIO_MODEL <+ Projection/(.Form: {value})", "new": "", "role": "passive"}
            self.assertTrue(is_projection_form_edit(edit, allowed))
        generic = {"old": "CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/Type",
                   "new": "CAPRMEDIO_MODEL <+ Projection.Form", "role": "passive"}
        self.assertTrue(is_projection_form_edit(generic, allowed))
        specific_old_value = {"old": "CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/Type: Scope Unit Graph",
                              "new": "CAPRMEDIO_MODEL <+ Projection.Form", "role": "passive"}
        self.assertFalse(is_projection_form_edit(specific_old_value, allowed))
        for value in {"Scope Unit Graph", "Terms Graph", "Applicable Methodology"}:
            edit = {"old": f"CAPRMEDIO_MODEL <+ Projection/(.Form: {value})",
                    "new": "CAPRMEDIO_MODEL <+ Projection/(.Form:=" + value + ")", "role": "passive"}
            self.assertFalse(is_projection_form_edit(edit, allowed))


if __name__ == "__main__":
    unittest.main()
