from __future__ import annotations

import asyncio
from dataclasses import replace
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from jsonschema import Draft202012Validator
from mcp import types

MCP = Path(__file__).resolve().parents[1]
TOOLS = MCP.parent / "201_TOOLS"
sys.path[:0] = [str(MCP), str(TOOLS), str(TOOLS / "VALIDATE_ATOMS")]

from host_runtime_config import load_host_runtime_config  # noqa: E402
import shared_project_catalog as catalog  # noqa: E402
from shared_project_catalog import (  # noqa: E402
    SharedToolFrontier,
    _candidate_paths,
    discover_frontier,
    public_tool,
)


def _tool(name="echo", schema=None):
    return types.Tool(
        name=name,
        inputSchema=schema
        or {
            "type": "object",
            "properties": {"request": {"type": "string"}},
            "required": ["request"],
            "additionalProperties": False,
        },
        outputSchema={"type": "object"},
    )


class _Gateway:
    behavior = "ok"
    close_error = False
    instances = []
    tools = []

    def __init__(self, root, *, selection):
        self.root = Path(root)
        self.selection = selection
        self.active = SimpleNamespace(tools=list(self.tools))
        self.tool_blacklist = frozenset()
        self.closed = False
        self.instances.append(self)

    async def initialize(self):
        if self.behavior == "error":
            raise RuntimeError("initialize failed")
        if self.behavior == "cancel":
            raise asyncio.CancelledError

    async def close(self):
        self.closed = True
        if self.close_error:
            raise RuntimeError("close failed")


class SharedProjectCatalogTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.projects = self.base / "My_Repos"
        self.projects.mkdir()
        self.roots = [self._project(name) for name in ("alpha", "beta")]
        self.config_path = self.base / "runtime.toml"
        self.config_path.write_text(
            "schema_version = 1\n[shared_mcp]\n"
            f'projects_root = "{self.projects}"\nhttp_port = 8092\n',
            encoding="utf-8",
        )
        self.config = load_host_runtime_config(self.config_path)
        _Gateway.behavior, _Gateway.close_error = "ok", False
        _Gateway.instances, _Gateway.tools = [], [_tool()]

    def _project(self, name):
        root = self.projects / name
        control = root / f".caprmedio_{name}"
        control.mkdir(parents=True)
        (control / "caprmedio_project_settings.toml").write_text(
            f'[project]\nname = "{name}"\n[artifacts.identity]\n'
            f'project_prefix = "{name.upper()}"\n[paths]\ncontrol_root = "{control.name}"\n',
            encoding="utf-8",
        )
        (control / "project_structure.toml").write_text(
            "schema_version = 1\nscope_units = []\n", encoding="utf-8"
        )
        return root

    def test_public_schema_keeps_nested_defs_and_is_valid(self):
        native = _tool(
            "nested",
            {
                "type": "object",
                "properties": {"payload": {"$ref": "#/$defs/Payload"}},
                "required": ["payload"],
                "additionalProperties": False,
                "$defs": {
                    "Payload": {
                        "type": "object",
                        "properties": {"value": {"type": "string"}},
                        "required": ["value"],
                        "additionalProperties": False,
                    }
                },
            },
        )
        public = public_tool(native)
        Draft202012Validator.check_schema(public.input_schema)
        Draft202012Validator(public.input_schema).validate(
            {"payload": {"value": "ok"}, "project_root": str(self.roots[0])}
        )
        self.assertEqual("#/$defs/Payload", public.input_schema["properties"]["payload"]["$ref"])

    def test_warning_keeps_secondary_diagnostic_failure_visible(self):
        frontier = SharedToolFrontier()
        with patch.object(catalog, "report_failure", return_value=(None, "sink failed")):
            frontier.warning("PROJECT_CATALOG_READ_FAILED", self.roots[0])
        self.assertEqual("sink failed", frontier.warnings[0]["diagnostic_error"])

    async def test_unadaptable_root_schemas_are_rejected_and_not_advertised(self):
        for key, value in (("$ref", "#/$defs/Args"), ("allOf", [{"type": "object"}])):
            with self.subTest(key=key), self.assertRaises(ValueError):
                public_tool(_tool(key, {key: value}))

        invalid = [
            _tool("root_ref", {"$ref": "#/$defs/Args"}),
            _tool("root_all_of", {"allOf": [{"type": "object"}]}),
        ]
        _Gateway.tools = invalid
        frontier = await discover_frontier(self.config, _Gateway)
        self.assertNotIn("root_ref", frontier.tools)
        self.assertNotIn("root_all_of", frontier.tools)
        self.assertEqual(
            2 * len(self.roots),
            sum(row["code"] == "PROJECT_TOOL_CONTRACT_INVALID" for row in frontier.warnings),
        )

    async def test_initialize_failure_closes_gateway_and_cancellation_rethrows(self):
        _Gateway.behavior = "error"
        failed = await discover_frontier(self.config, _Gateway)
        self.assertTrue(all(instance.closed for instance in _Gateway.instances))
        self.assertIn("PROJECT_CANDIDATE_INVALID", [row["code"] for row in failed.warnings])

        _Gateway.instances = []
        _Gateway.behavior = "cancel"
        with self.assertRaises(asyncio.CancelledError):
            await discover_frontier(self.config, _Gateway)
        self.assertTrue(all(instance.closed for instance in _Gateway.instances))

    async def test_close_failure_is_visible_as_warning(self):
        _Gateway.close_error = True
        frontier = await discover_frontier(self.config, _Gateway)
        self.assertIn("PROJECT_CANDIDATE_CLOSE_FAILED", [row["code"] for row in frontier.warnings])

    def test_scan_bound_counts_direct_candidate_dirs_not_valid_projects(self):
        scan_root = self.base / "scan-root"
        scan_root.mkdir()
        for index in range(256):
            (scan_root / f"empty-{index:03d}").mkdir()
        late = scan_root / "late-project"
        late.mkdir()
        (late / ".caprmedio_late").mkdir()
        bounded_config = replace(self.config, projects_root=scan_root)
        frontier = SharedToolFrontier()
        self.assertLessEqual(len(_candidate_paths(bounded_config, frontier)), 1)
        self.assertIn(
            "PROJECT_CATALOG_SCAN_BOUND_REACHED", [row["code"] for row in frontier.warnings]
        )


if __name__ == "__main__":
    unittest.main()
