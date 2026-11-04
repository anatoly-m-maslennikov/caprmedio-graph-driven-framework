# CA-E-676@7

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
    def test_without_a_cursor_preserves_the_original_script(self):
        sql = " select 1; -- trailing\n"
        self.assertEqual(sql, select_statement(sql))

    def test_cursor_uses_native_tokens_for_unicode_strings_comments_and_dollar_quotes(self):
        sql = "select '😀;'; -- ;\n  select $$;$$ as value; /* ; */"
        cursor = _utf16_position(sql, "value")
        self.assertEqual(" -- ;\n  select $$;$$ as value; /* ; */", select_statement(sql, cursor))

    def test_semicolon_belongs_to_the_left_statement_and_leading_space_to_the_right(self):
        sql = "select '😀';  select 2"
        semicolon = _utf16_position(sql, ";")
        second = _utf16_position(sql, "2")
        self.assertEqual("select '😀';", select_statement(sql, semicolon))
        self.assertEqual("select '😀';", select_statement(sql, semicolon + 1))
        self.assertEqual("  select 2", select_statement(sql, second))

    def test_final_comments_belong_to_the_final_statement(self):
        sql = "select 1; /* final comment */  \n"
        cursor = len(sql.encode("utf-16-le")) // 2
        self.assertEqual(sql, select_statement(sql, cursor))

    def test_invalid_sql_with_a_cursor_is_saved_as_the_original_for_later_admission(self):
        sql = "select 'unterminated"
        self.assertEqual(sql, select_statement(sql, 0))

    def test_cursor_rejects_a_surrogate_interior_and_outside_text(self):
        sql = "select '😀'"
        with self.assertRaisesRegex(ValueError, "boundary"):
            select_statement(sql, _utf16_position(sql, "😀") + 1)
        with self.assertRaisesRegex(ValueError, "outside"):
            select_statement(sql, 100)
