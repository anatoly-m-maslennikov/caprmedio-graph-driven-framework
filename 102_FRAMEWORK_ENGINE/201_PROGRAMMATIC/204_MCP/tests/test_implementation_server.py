"""Direct-MCP registration follows the current Service catalog only."""

from __future__ import annotations

from pathlib import Path
import shutil
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import jsonschema

MCP_ROOT = Path(__file__).resolve().parents[1]
PROGRAMMATIC_ROOT = MCP_ROOT.parent
TOOLS_ROOT = PROGRAMMATIC_ROOT / "201_TOOLS"
REPOSITORY_ROOT = PROGRAMMATIC_ROOT.parents[1]
for directory in (MCP_ROOT, TOOLS_ROOT, TOOLS_ROOT / "VALIDATE_ATOMS", TOOLS_ROOT / "RELEASE_VERSION"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

from capability_discovery.service import Context, Service as DiscoveryService  # noqa: E402
import implementation_server  # noqa: E402
from ATOM_UPDATE.atom_update import (  # noqa: E402
    SubjectPreparationRequest,
    describe_tool as describe_subject_preparation_tool,
)

DISCOVERY_DELIVERY = Path(
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
    "201_FEATURE_TOOLS/DISCOVER_TOOLS/07_delivery/"
    "CA-D-512-DISCOVER_TOOLS--encode-discover-tools-bindings.md"
)
DISCOVERY_ACTION = Path(
    ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/"
    "003_PROJECT_CONFIGURATION/09_operations/"
    "CA-O-112-PROJECT_CONFIGURATION-ACTION--discover-tools.md"
)


class _Server:
    instances: list["_Server"] = []

    def __init__(self, *_args, **_kwargs) -> None:
        self.registered: list[tuple[dict, object]] = []
        self.__class__.instances.append(self)

    def tool(self, **metadata):
        def decorate(function):
            self.registered.append((metadata, function))
            return function
        return decorate

    def add_tool(self, function, **metadata):
        self.registered.append((metadata, function))


class _CapturingService(DiscoveryService):
    instances: list["_CapturingService"] = []

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.catalog_calls = 0
        self.__class__.instances.append(self)

    def catalog(self):
        self.catalog_calls += 1
        return super().catalog()


class ImplementationServerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n', encoding="utf-8"
        )
        _Server.instances.clear()
        _CapturingService.instances.clear()


    def _copy(self, relative: Path) -> None:
        destination = self.root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPOSITORY_ROOT / relative, destination)



    def _create_server(self) -> tuple[_Server, _CapturingService]:
        with (
            patch.object(implementation_server, "MCPServer", _Server),
            patch.object(implementation_server, "Service", _CapturingService),
            patch.object(
                implementation_server,
                "register_selected_routes",
                return_value=SimpleNamespace(public_route_names=frozenset()),
            ),
        ):
            server = implementation_server.create_server(self.root)
        self.assertIsInstance(server, _Server)
        self.assertEqual(1, len(_CapturingService.instances))
        return server, _CapturingService.instances[0]

    @staticmethod
    def _registered_names(server: _Server) -> set[str]:
        return {metadata["name"] for metadata, _function in server.registered}


    def test_startup_uses_one_catalog_snapshot_for_optional_direct_adapters(self):
        self._copy(DISCOVERY_DELIVERY)
        self._copy(DISCOVERY_ACTION)

        server, discovery = self._create_server()

        self.assertEqual(1, discovery.catalog_calls)
        self.assertIn("discover_tools", self._registered_names(server))
        self.assertIn("discover_tools", discovery.exposed)






    def test_context_envelope_hoists_current_subject_preparation_defs(self):
        """The generic context envelope preserves RootModel refs at its root."""

        discovery = DiscoveryService(self.root)
        projection = {
            "input_schema": SubjectPreparationRequest.model_json_schema(),
            "output_schema": {"type": "object"},
            "descriptor": describe_subject_preparation_tool(),
        }
        tool = {"name": "ATOM_UPDATE", "action_ids": [], "workflow_ids": []}
        with (
            patch.object(discovery, "catalog", return_value=({}, [tool], [])),
            patch.object(discovery, "_tool_projection", return_value=projection),
        ):
            schema = discovery.context(Context(id="ATOM_UPDATE"))["input_schema"]

        self.assertIn("$defs", schema)
        request = {"operation": "preview_subjects", "subject_profile": "approved",
                   "atoms": [{"atom_id": "CA-R-001", "version": 1,
                              "sha256": "a" * 64, "subject_patches": []}]}
        jsonschema.validate({"request": request}, schema)
        jsonschema.validate({"request": {
            **request, "operation": "stage_subjects", "preview_sha256": "b" * 64,
            "illustrative_updated_at": "2026-10-14 12:00:00 +0400",
        }}, schema)






if __name__ == "__main__":  # pragma: no cover
    unittest.main()
