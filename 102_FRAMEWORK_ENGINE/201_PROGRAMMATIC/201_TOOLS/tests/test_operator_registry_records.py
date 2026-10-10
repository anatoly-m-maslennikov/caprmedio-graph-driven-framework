"""Pure record validation for Project-root Operator registries."""

from __future__ import annotations

import unittest

from operator_registry import OperatorRegistryError, OperatorRegistryRecord, parse_operators_registry


REGISTRY = b'''[[operators]]
name = "Display Name"
role = "project owner"
journal_author = "display-name"

[[operators]]
name = "Legacy Display Name"
role = "reviewer"
'''


class OperatorRegistryRecordTests(unittest.TestCase):
    def test_returns_immutable_records_and_preserves_exact_display_name(self) -> None:
        self.assertEqual(
            parse_operators_registry(REGISTRY),
            (
                OperatorRegistryRecord("Display Name", "project owner", "display-name"),
                OperatorRegistryRecord("Legacy Display Name", "reviewer", None),
            ),
        )

    def test_journal_author_must_be_unique_valid_github_username(self) -> None:
        for journal_author in ("-bad", "bad-", "a" * 40):
            with self.subTest(journal_author=journal_author):
                raw = REGISTRY.replace(
                    b'journal_author = "display-name"',
                    b'journal_author = "' + journal_author.encode() + b'"',
                )
                with self.assertRaisesRegex(OperatorRegistryError, "malformed") as caught:
                    parse_operators_registry(raw)
                self.assertEqual(caught.exception.code, "operator-registry-invalid")
        duplicate = REGISTRY.replace(
            b'name = "Legacy Display Name"\nrole = "reviewer"',
            b'name = "Legacy Display Name"\nrole = "reviewer"\njournal_author = "display-name"',
        )
        with self.assertRaises(OperatorRegistryError):
            parse_operators_registry(duplicate)

    def test_closed_schema_rejects_unknown_keys_empty_rows_and_aliases(self) -> None:
        invalid = (
            b"",
            b"operators = []\n",
            b"[[operators]]\nname = 'Name'\nrole = 'role'\nextra = true\n",
            b"[[operators]]\noperator_name = 'Name'\nrole = 'role'\n",
            b"[[operators]]\nname = 'Name'\nrole = 'role'\n\n[[operators]]\nname = 'Name'\nrole = 'other'\n",
            b"[[operators]]\nname = 'Name'\nrole = 'role'\n\nunexpected = true\n",
        )
        for payload in invalid:
            with self.subTest(payload=payload):
                with self.assertRaises(OperatorRegistryError) as caught:
                    parse_operators_registry(payload)
                self.assertEqual(caught.exception.code, "operator-registry-invalid")


if __name__ == "__main__":
    unittest.main()
