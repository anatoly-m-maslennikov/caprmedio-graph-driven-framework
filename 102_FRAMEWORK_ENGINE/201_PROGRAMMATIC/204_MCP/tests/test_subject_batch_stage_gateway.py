"""A real connected batch stage still authorizes only its selected one-Atom Action."""

from pathlib import Path
from functools import partial
import sys
import unittest
from unittest.mock import patch

from mcp.client._memory import InMemoryTransport
from mcp.client.session import ClientSession

sys.path.insert(0, str(Path(__file__).resolve().parent))
import test_subject_publication_gateway as fixtures  # noqa: E402
from lifecycle_intents import carrier_descriptor  # noqa: E402


class SubjectBatchStageGatewayTests(unittest.IsolatedAsyncioTestCase):
    async def test_two_atom_stage_then_only_selected_atom_publication(self) -> None:
        fixture = fixtures.SubjectPublicationGatewayTests("runTest")
        scratch = Path(__file__).resolve().parents[4] / ".caprmedio_tmp/tests/subject-batch-gateway"
        scratch.mkdir(parents=True, exist_ok=True)
        temporary = partial(fixtures.tempfile.TemporaryDirectory, dir=scratch)
        with patch.object(fixtures.tempfile, "TemporaryDirectory", temporary):
            fixture.setUp()
        for callback, arguments, keywords in fixture._cleanups:
            self.addCleanup(callback, *arguments, **keywords)
        fixture._cleanups.clear()
        other = fixture.fixture.golden.status_atom("Requirement", "Active", number=8101)
        before = other.read_bytes()
        target = carrier_descriptor(
            fixture.fixture.root, other.relative_to(fixture.fixture.root).as_posix()
        )
        fixture.preparation_request["atoms"].append(
            {
                "atom_id": target["atom_id"],
                "version": target["version"],
                "sha256": target["digest"],
                "subject_patches": fixture.fixture.patches,
            }
        )
        async with InMemoryTransport(
            fixture.gateway.build_server(), raise_exceptions=True
        ) as streams:
            async with ClientSession(*streams, elicitation_callback=fixture.elicit) as client:
                await client.initialize()
                staged = await fixture.stage(client)
                self.assertEqual(staged["preview"]["count"], 2)
                response = await client.call_tool("update_atom", {"request": fixture.request})
        self.assertEqual(response.structured_content["status"], "dispatched")
        self.assertEqual(len(fixture.forms), 1)
        self.assertIn(staged["staging"]["manifest_path"], fixture.forms[0].message)
        self.assertEqual(other.read_bytes(), before)
        self.assertEqual(fixture.fixture.archive.read_bytes(), fixture.fixture.before)
        self.assertNotEqual(fixture.fixture.path.read_bytes(), fixture.fixture.before)


if __name__ == "__main__":
    unittest.main()
