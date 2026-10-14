"""The connector's exact-state digest is not a general token exemption."""

import sys
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from workflow_run_support import SelectedRunError, _reject_secrets  # noqa: E402


class SelectedRunSecretBoundaryTests(unittest.TestCase):
    def test_exact_expected_source_digest_is_admitted(self):
        _reject_secrets({"expected_state": {"source_token": "a" * 64}})
        _reject_secrets({"expected_state": [{"source_token": "a" * 64}, {"source_token": "b" * 64}]})

    def test_source_digest_must_be_lowercase_sha256(self):
        for value in ("secret", "a" * 63, "a" * 65, "A" * 64, "g" * 64,
                      None, True, 123, {}, [], {"token": "a" * 64}):
            with self.subTest(value=value), self.assertRaises(SelectedRunError) as failure:
                _reject_secrets({"expected_state": {"source_token": value}})
            self.assertEqual("invalid-request", failure.exception.code)
            with self.subTest(row_value=value), self.assertRaises(SelectedRunError) as failure:
                _reject_secrets({"expected_state": [{"source_token": value}]})
            self.assertEqual("invalid-request", failure.exception.code)

    def test_token_exemption_does_not_extend_to_other_fields_or_locations(self):
        for value in (
            {"source_token": "a" * 64},
            {"expected_state": {"token": "a" * 64}},
            {"expected_state": {"Source_Token": "a" * 64}},
            {"expected_state": {"source_token": "a" * 64, "password": "hidden"}},
            {"context": {"expected_state": {"source_token": "a" * 64}}},
            {"expected_state[0]": {"source_token": "a" * 64}},
            {"expected_state[0].source_token": "a" * 64},
            {"expected_state": {"[0]": {"source_token": "a" * 64}}},
            {"expected_state": [[{"source_token": "a" * 64}]]},
            {"expected_state": [{"nested": {"source_token": "a" * 64}}]},
            {"expected_state": [{"source_token": "a" * 64, "password": "hidden"}]},
        ):
            with self.subTest(value=value), self.assertRaises(SelectedRunError) as failure:
                _reject_secrets(value)
            self.assertEqual("secret-input", failure.exception.code)
        for location in ("effects", "source observer observed"):
            with self.subTest(location=location), self.assertRaises(SelectedRunError):
                _reject_secrets({"expected_state": {"source_token": "a" * 64}}, location)


if __name__ == "__main__":
    unittest.main()
