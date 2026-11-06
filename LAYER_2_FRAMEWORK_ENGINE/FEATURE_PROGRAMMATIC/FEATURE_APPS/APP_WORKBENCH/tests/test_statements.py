# CA-E-785@1
"""Native statement selection keeps SQL lexical boundaries authoritative."""

from pathlib import Path
import sys
import unittest


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(APP_ROOT))

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.statements import select_statement  # noqa: E402


def _utf16_position(value: str, text: str) -> int:
    return len(value[:value.index(text)].encode("utf-16-le")) // 2


class StatementTests(unittest.TestCase):
    def test_cursor_is_metadata_and_the_complete_script_is_preserved(self):
        sql = "select '😀;'; -- ;\n  select $$;$$ as value; /* ; */"
        self.assertEqual(sql, select_statement(sql, _utf16_position(sql, "value")))

    def test_multiple_statements_remain_visible_for_native_admission(self):
        sql = "select '😀';  select 2"
        self.assertEqual(sql, select_statement(sql, _utf16_position(sql, "2")))

    def test_invalid_sql_with_a_cursor_is_preserved_for_native_admission(self):
        sql = "select 'unterminated"
        self.assertEqual(sql, select_statement(sql, 0))

    def test_cursor_rejects_a_surrogate_interior_and_outside_text(self):
        sql = "select '😀'"
        with self.assertRaisesRegex(ValueError, "boundary"):
            select_statement(sql, _utf16_position(sql, "😀") + 1)
        with self.assertRaisesRegex(ValueError, "outside"):
            select_statement(sql, 100)
