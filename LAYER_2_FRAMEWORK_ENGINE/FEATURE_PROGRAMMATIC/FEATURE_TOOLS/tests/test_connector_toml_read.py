from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from connector_toml_read import read_configuration


class CompleteReadTests(unittest.TestCase):
    def setUp(self):
        root = Path(__file__).resolve().parents[4] / ".caprmedio_tmp"
        root.mkdir(exist_ok=True)
        self.directory = tempfile.TemporaryDirectory(prefix="connector-toml-", dir=root)
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "config.toml"
        self.payload = b'# exact\r\nschema_version = 1\r\n[unrelated]\r\noptional = "present"\r\n'
        self.path.write_bytes(self.payload)

    def read(self, identity="Project Structure", **changes):
        arguments = {"read_bytes": self.path.read_bytes, "identity": identity,
                     "project": "fixture", "source_view": "current",
                     "validate_document": self.validate, "expected_state": None}
        arguments.update(changes)
        return read_configuration(**arguments)

    @staticmethod
    def validate(document):
        if document.get("schema_version") != 1:
            raise ValueError("Wrong declared schema version")

    def test_both_configurations_read_all_content_without_effects(self):
        for identity in ("Project Structure", "Project Settings"):
            result = self.read(identity)
            self.assertEqual(result["errors"], [])
            self.assertEqual(result["effects"], [])
            self.assertEqual(result["data"]["source_text"].encode(), self.payload)
            self.assertEqual(result["data"]["document"]["unrelated"], {"optional": "present"})
            self.assertEqual(result["current_state"]["sha256"], hashlib.sha256(self.payload).hexdigest())
            self.assertEqual(self.path.read_bytes(), self.payload)

    def test_exact_pin_and_historical_view(self):
        state = self.read()["current_state"]
        self.assertEqual(self.read(expected_state=state)["errors"], [])
        historical = {**state, "source_view": "revision-1"}
        self.assertEqual(self.read(source_view="revision-1", expected_state=historical)["errors"], [])
        self.assertEqual(self.read(expected_state={**state, "sha256": "stale"})["errors"][0]["code"], "stale_state")

    def test_missing_current_and_history_are_distinct_failures(self):
        def absent():
            raise FileNotFoundError()
        for view, code in (("current", "target_not_found"), ("revision-1", "backend_failure")):
            result = self.read(read_bytes=absent, source_view=view)
            self.assertIsNone(result["data"])
            self.assertEqual(result["errors"][0]["code"], code)
        self.assertEqual(self.path.read_bytes(), self.payload)

    def test_invalid_schema_duplicate_keys_and_backend_failure(self):
        for payload in (b'schema_version = 2', b'schema_version = 1\nx = 1\nx = 2'):
            result = self.read(read_bytes=lambda: payload)
            self.assertIsNone(result["data"])
            self.assertEqual(result["errors"][0]["code"], "schema_invalid")
        def unavailable():
            raise OSError("fixture failure")
        self.assertEqual(self.read(read_bytes=unavailable)["errors"][0]["code"], "backend_failure")
        self.assertEqual(self.path.read_bytes(), self.payload)

    def test_source_change_does_not_mix_observations(self):
        payloads = iter((self.payload, self.payload + b'x = 2\n'))
        result = self.read(read_bytes=lambda: next(payloads))
        self.assertIsNone(result["data"])
        self.assertEqual(result["errors"][0]["code"], "stale_state")


if __name__ == "__main__":
    unittest.main()
