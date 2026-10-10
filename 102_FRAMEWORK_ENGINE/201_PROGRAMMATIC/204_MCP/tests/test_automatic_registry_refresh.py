"""Protocol contract for a generated, fail-closed installed Tool registry."""

from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from mcp import Client, StdioServerParameters


MCP_ROOT = Path(__file__).resolve().parents[1]
if str(MCP_ROOT) not in sys.path:
    sys.path.insert(0, str(MCP_ROOT))

import registered_tool_registry as registry  # noqa: E402


ENTRYPOINT_PREFIX = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC"


class AutomaticRegistryRefresh(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.programmatic = self.root / "installed" / "201_PROGRAMMATIC"
        self.provider_dir = self.programmatic / "mock"
        self.provider_dir.mkdir(parents=True)
        self.invocations = self.root / "invocations.jsonl"

    def binding(self, name: str, *, version: str = "A", invalid: bool = False) -> dict[str, object]:
        filename = f"{name}.py"
        self.write_provider(name, version=version, invalid=invalid)
        return {
            "name": name.upper(),
            "mcp_name": f"mock_{name}",
            "source_atom": f"CA-D-{name.upper()}",
            "source_path": f"sources/{name}.md",
            "sha256": "a" * 64,
            "action_ids": [f"CA-O-{name.upper()}"],
            "entrypoint": f"{ENTRYPOINT_PREFIX}/mock/{filename}",
        }

    def write_provider(self, name: str, *, version: str, invalid: bool = False) -> None:
        """Write the same descriptor provider shape for valid and bad candidates."""
        destination = self.provider_dir / f"{name}.py"
        if invalid:
            destination.write_text("def describe_tool(): return {'broken': True}\n", encoding="utf-8")
            return
        destination.write_text(
            "from pathlib import Path\n"
            "from pydantic import BaseModel\n"
            f"NAME = {name.upper()!r}\n"
            f"MCP_NAME = {'mock_' + name!r}\n"
            f"VERSION = {version!r}\n"
            f"SOURCE_ATOM = {'CA-D-' + name.upper()!r}\n"
            f"ACTION_ID = {'CA-O-' + name.upper()!r}\n"
            f"ENTRYPOINT = {ENTRYPOINT_PREFIX + '/mock/' + name + '.py'!r}\n"
            "class Input(BaseModel):\n    value: str\n"
            "class Result(BaseModel):\n    value: str\n    version: str\n"
            "def describe_tool():\n"
            "    return {'schema_version': 1, 'identity': {'name': NAME, "
            "'tool_version': 1, 'title': NAME, 'description': NAME, 'purpose': NAME}, "
            "'binding': {'delivery_atom_id': SOURCE_ATOM, 'action_ids': [ACTION_ID], "
            "'implementation_entrypoint': ENTRYPOINT}, 'models': {'input': {'module': ENTRYPOINT, "
            "'symbol': 'Input'}, 'output': {'module': ENTRYPOINT, 'symbol': 'Result'}}, "
            "'callable': {'module': ENTRYPOINT, 'symbol': 'create_adapter'}, 'effect_hints': "
            "{'read_only_hint': False, 'destructive_hint': False, 'idempotent_hint': True, "
            "'open_world_hint': False}, 'permissions': {'execution': 'operator_authorized', "
            "'enforcement': 'canonical_action_boundary', 'metadata_grants_permission': False}, "
            "'source_pins': {'delivery_atom_id': SOURCE_ATOM, 'action_ids': [ACTION_ID]}, "
            "'admission': {'module': ENTRYPOINT, 'symbol': 'binding_is_admitted', "
            "'refresh_after_success': False}, 'diagnostics': {'discovery_is_effect_free': True}, "
            "'failure_contract': {'invokes_on_discovery': False}}\n"
            "def binding_is_admitted(binding):\n"
            "    return binding.get('name') == NAME and binding.get('mcp_name') == MCP_NAME\n"
            "class Adapter:\n"
            "    def __init__(self, root): self.root = Path(root)\n"
            "    def invoke(self, request):\n"
            "        with (self.root / 'invocations.jsonl').open('a', encoding='utf-8') as stream:\n"
            "            stream.write(NAME + ':' + request.value + '\\n')\n"
            "        return {'value': request.value, 'version': VERSION}\n"
            "def create_adapter(root): return Adapter(root)\n",
            encoding="utf-8",
        )

    def compile(self, bindings: list[dict[str, object]]):
        with (patch.object(registry, "_PROGRAMMATIC_ROOT", self.programmatic),
              patch.object(registry, "_MODULE_CACHE", {})):
            return registry.compile_registry(self.root, bindings)

    def server_parameters(self, bindings: list[dict[str, object]]) -> StdioServerParameters:
        binding_path = self.root / "bindings.json"
        binding_path.write_text(json.dumps(bindings), encoding="utf-8")
        script = self.root / "candidate_registry_server.py"
        script.write_text(
            "import json, sys\n"
            "from pathlib import Path\n"
            "sys.path.insert(0, sys.argv[1])\n"
            "import registered_tool_registry as registry\n"
            "from mcp.server import MCPServer\n"
            "registry._PROGRAMMATIC_ROOT = Path(sys.argv[2])\n"
            "registry._MODULE_CACHE.clear()\n"
            "bindings = json.loads(Path(sys.argv[4]).read_text())\n"
            "def binding_is_fresh(_root, expected):\n"
            "    return sum(all(item.get(key) == value for key, value in expected.items()) for item in bindings) == 1\n"
            "registry._binding_is_fresh = binding_is_fresh\n"
            "server = MCPServer('candidate-registry')\n"
            "registry.register_catalog_tools(server, Path(sys.argv[3]), bindings)\n"
            "server.run(transport='stdio')\n",
            encoding="utf-8",
        )
        return StdioServerParameters(
            command=sys.executable,
            args=[str(script), str(MCP_ROOT), str(self.programmatic), str(self.root), str(binding_path)],
        )

    async def tools_and_call(self, bindings: list[dict[str, object]], name: str) -> tuple[set[str], dict[str, object]]:
        async with Client(self.server_parameters(bindings), cache=None) as client:
            names = {tool.name for tool in (await client.list_tools()).tools}
            response = await client.call_tool(name, {"request": {"value": "fixture"}})
            self.assertFalse(response.is_error, response)
            return names, response.structured_content

    async def test_generated_registry_refreshes_new_and_updated_tools_quarantines_bad_candidate(self) -> None:
        alpha_a = self.binding("alpha", version="A")
        initial = self.compile([alpha_a])
        self.assertEqual({"mock_alpha"}, initial.registered_names)
        self.assertEqual((), initial.quarantined)
        self.assertFalse(self.invocations.exists(), "compile must not invoke a Tool")

        names, result = await self.tools_and_call([alpha_a], "mock_alpha")
        self.assertEqual({"mock_alpha"}, names)
        self.assertEqual({"value": "fixture", "version": "A"}, result)

        alpha_b = self.binding("alpha", version="B")
        beta_b = self.binding("beta", version="B")
        invalid = self.binding("quarantined", version="B", invalid=True)
        refreshed = self.compile([alpha_b, beta_b, invalid])
        self.assertEqual({"mock_alpha", "mock_beta"}, refreshed.registered_names)
        self.assertEqual(1, len(refreshed.quarantined))
        self.assertEqual("QUARANTINED", refreshed.quarantined[0]["source"]["name"])
        self.assertEqual(["ALPHA:fixture"], self.invocations.read_text(encoding="utf-8").splitlines())

        names, result = await self.tools_and_call([alpha_b, beta_b, invalid], "mock_alpha")
        self.assertEqual({"mock_alpha", "mock_beta"}, names)
        self.assertEqual({"value": "fixture", "version": "B"}, result)
        self.assertNotIn("mock_quarantined", names)
        beta_names, beta_result = await self.tools_and_call([alpha_b, beta_b, invalid], "mock_beta")
        self.assertEqual({"mock_alpha", "mock_beta"}, beta_names)
        self.assertEqual({"value": "fixture", "version": "B"}, beta_result)
        self.assertEqual(
            ["ALPHA:fixture", "ALPHA:fixture", "BETA:fixture"],
            self.invocations.read_text(encoding="utf-8").splitlines(),
        )


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
