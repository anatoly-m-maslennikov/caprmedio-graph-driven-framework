"""Private writer integration with real selected admission on isolated carriers."""

from __future__ import annotations

import builtins
import hashlib
import unittest
from unittest.mock import patch

import test_connector_toml_shared as shared_fixture


class MaterializationIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.fixture = shared_fixture.SharedConnectorTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)

    def edit(self, action, mode, **values):
        return {"action": action, "mode": mode, "field": "members", **values}

    def modify(self, source, edits=None, identity="Project Structure"):
        self.fixture.source.write_bytes(source)
        request = self.fixture.request("modify", identity)
        if edits is not None:
            request["delta"] = {"edits": edits}
        return self.fixture.run_request(request)

    def assert_effect(self, result, before, after):
        self.assertEqual(result["errors"], [])
        self.assertEqual(self.fixture.source.read_bytes(), after)
        self.assertEqual(result["data"]["source_text"].encode(), after)
        self.assertEqual(result["current_state"]["sha256"], hashlib.sha256(after).hexdigest())
        self.assertEqual(result["effects"][0]["state"], "known")
        self.assertEqual(result["effects"][0]["evidence"], {
            "before_sha256": hashlib.sha256(before).hexdigest(),
            "after_sha256": hashlib.sha256(after).hexdigest(),
            "proposed_sha256": hashlib.sha256(after).hexdigest(),
        })

    def test_scalar_both_identities_lf_crlf_exact_source_and_effects(self):
        for identity in ("Project Structure", "Project Settings"):
            for newline in (b"\n", b"\r\n"):
                with self.subTest(identity=identity, newline=newline):
                    source = self.fixture.payload.replace(b"schema_version = 1", b"schema_version = 0x1")
                    source = source.replace(b"\n", newline)
                    result = self.modify(source, identity=identity)
                    self.assert_effect(result, source, source.replace(b'"before"', b'"after"'))
                    self.assertEqual(len(result["data"]["effective_diff"]), 1)

    def test_item_and_explicit_set_operations_preserve_other_carrier_bytes(self):
        cases = [
            (self.edit("add", "item", value="c"), b'["a", "b", "c"]'),
            (self.edit("replace", "item", current="b", value="c"), b'["a", "c"]'),
            (self.edit("remove", "item", current="b"), b'["a"]'),
            (self.edit("add", "set", value=["b", "c"]), b'["a", "b", "c"]'),
            (self.edit("replace", "set", value=["c", "d"]), b'["c", "d"]'),
            (self.edit("remove", "set", value=["a", "b"]), b'[]'),
        ]
        for edit, replacement in cases:
            with self.subTest(edit=edit):
                source = self.fixture.payload
                result = self.modify(source, [edit])
                self.assert_effect(result, source, source.replace(b'["a", "b"]', replacement))
                self.assertEqual(result["data"]["effective_diff"][0]["mode"], edit["mode"])

    def test_commented_collection_replacement_is_occurrence_local(self):
        source = self.fixture.payload.replace(b'["a", "b"]', b'[\n  "a", # first\n  "b", # second\n]')
        result = self.modify(source, [self.edit("replace", "item", current="b", value="c")])
        self.assert_effect(result, source, source.replace(b'"b", # second', b'"c", # second'))

    def test_read_and_noop_need_no_tomlkit_import_or_writer(self):
        real_import = builtins.__import__
        def deny_tomlkit(name, *args, **kwargs):
            if name == "tomlkit" or name.startswith("tomlkit."):
                raise AssertionError("Read/no-op must not load materialization dependency")
            return real_import(name, *args, **kwargs)
        with patch("builtins.__import__", side_effect=deny_tomlkit), patch(
            "connector_toml_write.replace_source", side_effect=AssertionError("Unexpected effect")
        ) as writer:
            read = self.fixture.run_request(self.fixture.request())
            request = self.fixture.request("modify", value="before")
            result = self.fixture.run_request(request)
        writer.assert_not_called()
        self.assertEqual(read["errors"], [])
        self.assertEqual(result["errors"], [])
        self.assertEqual(result["effects"], [])
        self.assertEqual(result["data"]["effective_diff"], [])
        self.assertEqual(self.fixture.source.read_bytes(), self.fixture.payload)

    def test_proposed_schema_and_lossy_layout_refuse_before_effect(self):
        for kind in ("schema", "layout"):
            with self.subTest(kind=kind):
                source = self.fixture.payload
                if kind == "layout":
                    source = source.replace(b'["a", "b"]', b'["a", "b",]')
                    edits = [self.edit("remove", "item", current="a")]
                else:
                    edits = [{"action": "replace", "mode": "value", "field": "name", "value": 3}]
                with patch("connector_toml_write.replace_source", side_effect=AssertionError("Unexpected effect")) as writer:
                    result = self.modify(source, edits)
                writer.assert_not_called()
                self.assertEqual(result["errors"][0]["code"], "schema_invalid")
                self.assertEqual(result["effects"], [])
                self.assertEqual(self.fixture.source.read_bytes(), source)

    def test_authority_drift_during_proposed_schema_check_refuses(self):
        request = self.fixture.request("modify")
        bindings = self.fixture.bindings(request)
        def validate_and_change(document):
            self.fixture.validate(document)
            if document["name"] == "after":
                (self.fixture.root / "schema.json").write_bytes(b'{"changed":true}')
        result = self.fixture.run_request(request, bindings, validate_document=validate_and_change)
        self.assertEqual(result["errors"][0]["code"], "stale_state")
        self.assertEqual(result["effects"], [])
        self.assertEqual(self.fixture.source.read_bytes(), self.fixture.payload)


if __name__ == "__main__":
    unittest.main()
