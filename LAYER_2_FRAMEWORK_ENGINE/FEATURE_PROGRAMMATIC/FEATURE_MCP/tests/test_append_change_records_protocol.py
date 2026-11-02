"""Real generic-registry SDK checks for plain Journal appends."""

import unittest

from append_change_records_protocol_fixture import (
    AppendChangeRecordsProtocolFixture,
    SOURCE_PINS,
    work_journal,
)


class AppendChangeRecordsProtocolTests(
    AppendChangeRecordsProtocolFixture, unittest.IsolatedAsyncioTestCase
):
    async def test_actual_sources_register_closed_sdk_schema_once(self):
        async with self.session() as client:
            tools = (await client.list_tools()).tools
            self.assertEqual(["append_change_records"], [tool.name for tool in tools])
            tool = tools[0]
            schema = tool.input_schema
            self.assertEqual(["request"], schema["required"])
            self.assertEqual({"request"}, set(schema["properties"]))
            request = schema["properties"]["request"]
            while "$ref" in request:
                resolved = schema
                for part in request["$ref"].split("/")[1:]:
                    resolved = resolved[part]
                request = resolved
            self.assertEqual({"context", "apply"}, set(request["properties"]))
            self.assertEqual(["context"], request["required"])
            self.assertFalse(request["additionalProperties"])
            self.assertEqual("boolean", request["properties"]["apply"]["type"])
            self.assertIs(False, request["properties"]["apply"]["default"])
            self.assertFalse(tool.annotations.read_only_hint)
            self.assertFalse(tool.annotations.destructive_hint)
            self.assertFalse(tool.annotations.idempotent_hint)
            self.assertIsNotNone(tool.output_schema)

    async def test_default_dry_run_returns_original_events_without_effects(self):
        async with self.session() as client:
            result = self.success(await self.call(client, {"context": self.context}, pure=True))
        self.assertEqual("dry-run", result["mode"])
        self.assertEqual(
            self.context["predictions"]["journal_records"],
            result["result"]["planned_effects"]["journal_records"],
        )
        self.assertFalse((self.root / ".caprmedio_caprmedio/_journal").exists())
        self.assertFalse((self.root / ".caprmedio_runtime").exists())

    async def test_apply_returns_locations_and_repeated_calls_append_again(self):
        artifact = self.fixture.artifact.read_bytes()
        index = (self.root / ".git/index").read_bytes()
        head = (self.root / ".git/HEAD").read_bytes()
        async with self.session() as client:
            first = self.success(await self.call(client, {"context": self.context, "apply": True}))
            second = self.success(await self.call(client, {"context": self.context, "apply": True}))
        self.assertEqual("apply", first["mode"])
        self.assertEqual("complete", first["result"]["state"])
        self.assertEqual(1, len(first["result"]["receipts"]))
        receipt = first["result"]["receipts"][0]
        event = self.context["predictions"]["journal_records"][0]
        raw = (self.root / receipt["carrier"]).read_bytes()
        self.assertEqual((work_journal.canonical_json_bytes(event) + b"\n") * 2, raw)
        self.assertEqual(event["event_id"], receipt["event_id"])
        self.assertEqual(event["action_id"], receipt["action_id"])
        self.assertEqual(event["event_digest"], receipt["event_digest"])
        self.assertEqual(1, receipt["line"])
        self.assertEqual(2, second["result"]["receipts"][0]["line"])
        self.assertNotIn("previous_carrier_digest", receipt)
        self.assertNotIn("appended_carrier_digest", receipt)
        self.assertEqual([event, event], work_journal.read_records(self.root))
        self.assertFalse((self.root / ".caprmedio_runtime").exists())
        self.assertEqual(artifact, self.fixture.artifact.read_bytes())
        self.assertEqual(index, (self.root / ".git/index").read_bytes())
        self.assertEqual(head, (self.root / ".git/HEAD").read_bytes())
        self.assertFalse((self.root / ".caprmedio_runtime/state/commit_change_set").exists())
        self.assertFalse((self.root / ".caprmedio_runtime/state/commit_trigger").exists())

    async def test_strict_boolean_and_unknown_request_fields_refuse_without_effects(self):
        requests = (
            [{"context": self.context, "apply": value} for value in (0, 1, "true", None)]
            + [
                {"context": self.context, field: value}
                for field, value in (
                    ("root", str(self.root)),
                    ("event", {}),
                    ("wait_seconds", 0),
                    ("authorized", True),
                )
            ]
            + [{}]
        )
        async with self.session() as client:
            for request in requests:
                with self.subTest(request=request.keys()):
                    response = await self.call(client, request, pure=True)
                    self.assertTrue(response.is_error, response)

    async def test_source_binding_drift_refuses_before_any_append(self):
        async with self.session() as client:
            source = self.root / SOURCE_PINS[0][2]
            original = source.read_bytes()
            source.write_bytes(original + b"\nsource drift\n")
            response = await self.call(client, {"context": self.context, "apply": True}, pure=True)
            self.assertTrue(response.is_error, response)
            source.write_bytes(original)
        self.assertFalse((self.root / ".caprmedio_caprmedio/_journal").exists())


if __name__ == "__main__":
    unittest.main()
