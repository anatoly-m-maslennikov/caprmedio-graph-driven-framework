"""Direct-MCP registration follows the current Service catalog only."""

from __future__ import annotations

from pathlib import Path
import shutil
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch


MCP_ROOT = Path(__file__).resolve().parents[1]
PROGRAMMATIC_ROOT = MCP_ROOT.parent
TOOLS_ROOT = PROGRAMMATIC_ROOT / "201_TOOLS"
REPOSITORY_ROOT = PROGRAMMATIC_ROOT.parents[1]
for directory in (MCP_ROOT, TOOLS_ROOT, TOOLS_ROOT / "VALIDATE_ATOMS", TOOLS_ROOT / "RELEASE_VERSION"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))
DISCOVERY_TESTS_ROOT = TOOLS_ROOT / "capability_discovery"
if str(DISCOVERY_TESTS_ROOT) not in sys.path:
    sys.path.insert(0, str(DISCOVERY_TESTS_ROOT))

from capability_discovery.service import Context, Query, Service as DiscoveryService  # noqa: E402
from framework_runtime_installation_mcp import (  # noqa: E402
    MCP_NAME as RUNTIME_INSTALLATION_MCP_NAME,
    TOOL_NAME as RUNTIME_INSTALLATION_TOOL_NAME,
    input_schema as runtime_installation_input_schema,
)
import implementation_server  # noqa: E402
from source_admission_mcp import MCP_NAME, TOOL_NAME  # noqa: E402
from test_service import seed_selected_runtime_binding_package  # noqa: E402


D602_RELATIVE = Path(
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
    "201_FEATURE_TOOLS/07_delivery/"
    "CA-D-602-TOOLS-DELIVERY--encode-admitted-package-source-catalog.md"
)
O199_RELATIVE = Path(
    ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/"
    "003_PROJECT_CONFIGURATION/09_operations/"
    "CA-O-199-PROJECT_CONFIGURATION-ACTION--admit-local-package-sources.md"
)
O199_SOURCE = Path(
    ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
    "000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/09_operations/"
    "CA-O-199-PROJECT_CONFIGURATION-ACTION--admit-local-package-sources.md"
)
RUNTIME_INSTALLATION_DELIVERY = Path(
    ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/"
    "204_FEATURE_MCP/07_delivery/"
    "CA-D-620-MCP-DELIVERY--expose-direct-framework-runtime-installation.md"
)
RUNTIME_INSTALLATION_ACTION = Path(
    ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/"
    "003_PROJECT_CONFIGURATION/09_operations/"
    "CA-O-200-PROJECT_CONFIGURATION-ACTION--install-one-admitted-project-runtime.md"
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
        self._retain_fixture = False
        self.addCleanup(self._cleanup_fixture)
        self.root = Path(self.temporary.name)
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n', encoding="utf-8"
        )
        _Server.instances.clear()
        _CapturingService.instances.clear()

    def _cleanup_fixture(self) -> None:
        if self._retain_fixture:
            self.temporary._finalizer.detach()
            return
        self.temporary.cleanup()

    def _copy(self, relative: Path) -> None:
        destination = self.root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPOSITORY_ROOT / relative, destination)

    def _seed_o199_source(self, delivery: bytes | None = None) -> Path:
        destination_source = self.root / O199_RELATIVE
        destination_source.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPOSITORY_ROOT / O199_SOURCE, destination_source)
        destination = self.root / D602_RELATIVE
        if delivery is not None:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(delivery)
        return destination

    def _seed_o200_source(self, delivery: bytes | None = None) -> Path:
        self._copy(RUNTIME_INSTALLATION_ACTION)
        destination = self.root / RUNTIME_INSTALLATION_DELIVERY
        if delivery is not None:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(delivery)
        return destination

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

    def test_o199_internal_source_validation_is_not_registered_as_a_direct_adapter(self):
        self._seed_o199_source((REPOSITORY_ROOT / D602_RELATIVE).read_bytes())

        server, discovery = self._create_server()

        self.assertNotIn(MCP_NAME, self._registered_names(server))
        self.assertNotIn(MCP_NAME, discovery.exposed)
        context = discovery.context(Context(id="CA-O-199"))
        self.assertIsNone(context["input_schema"])

    def test_startup_uses_one_catalog_snapshot_for_optional_direct_adapters(self):
        self._seed_o200_source((REPOSITORY_ROOT / RUNTIME_INSTALLATION_DELIVERY).read_bytes())

        server, discovery = self._create_server()

        self.assertEqual(1, discovery.catalog_calls)
        self.assertIn(RUNTIME_INSTALLATION_MCP_NAME, self._registered_names(server))
        self.assertIn(RUNTIME_INSTALLATION_MCP_NAME, discovery.exposed)
        self.assertNotIn(MCP_NAME, self._registered_names(server))

    def test_o199_source_action_without_delivery_binding_is_not_registered_or_exposed(self):
        self._seed_o199_source()

        server, discovery = self._create_server()

        self.assertNotIn(MCP_NAME, self._registered_names(server))
        self.assertNotIn(MCP_NAME, discovery.exposed)
        self.assertIsNone(discovery.context(Context(id="CA-O-199"))["input_schema"])

    def test_o199_mismatched_delivery_binding_is_not_registered_or_exposed(self):
        delivery = (REPOSITORY_ROOT / D602_RELATIVE).read_bytes().replace(
            b'entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/source_admission_mcp.py"',
            b'entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/other.py"',
        )
        self._seed_o199_source(delivery)

        server, discovery = self._create_server()

        self.assertNotIn(MCP_NAME, self._registered_names(server))
        self.assertNotIn(MCP_NAME, discovery.exposed)
        self.assertIsNone(discovery.context(Context(id="CA-O-199"))["input_schema"])

    def test_o199_ambiguous_delivery_bindings_are_not_registered_or_exposed(self):
        delivery = (REPOSITORY_ROOT / D602_RELATIVE).read_bytes()
        canonical = self._seed_o199_source(delivery)
        duplicate = canonical.with_name("CA-D-603-TOOLS-DELIVERY--ambiguous-source-admission.md")
        duplicate.write_bytes(delivery.replace(b"atom_id: CA-D-602", b"atom_id: CA-D-603"))

        server, discovery = self._create_server()

        self.assertNotIn(MCP_NAME, self._registered_names(server))
        self.assertNotIn(MCP_NAME, discovery.exposed)
        self.assertIsNone(discovery.context(Context(id="CA-O-199"))["input_schema"])

    def test_o200_registers_from_the_exact_current_catalog_binding_and_exposes_its_schema(self):
        self._seed_o200_source((REPOSITORY_ROOT / RUNTIME_INSTALLATION_DELIVERY).read_bytes())

        server, discovery = self._create_server()

        self.assertIn(RUNTIME_INSTALLATION_MCP_NAME, self._registered_names(server))
        self.assertIn(RUNTIME_INSTALLATION_MCP_NAME, discovery.exposed)
        context = discovery.context(Context(id="CA-O-200"))
        operation = discovery.discover(Query(query="CA-O-200"), operations=True)["matches"]
        self.assertEqual(runtime_installation_input_schema(), context["input_schema"])
        self.assertEqual(["mcp"], [row["availability"] for row in operation])

    def test_o200_registers_from_selected_package_binding_without_current_delivery(self):
        self._retain_fixture = True
        seed_selected_runtime_binding_package(self.root)
        self.assertFalse((self.root / RUNTIME_INSTALLATION_DELIVERY).exists())

        server, discovery = self._create_server()

        self.assertIn(RUNTIME_INSTALLATION_MCP_NAME, self._registered_names(server))
        self.assertIn(RUNTIME_INSTALLATION_MCP_NAME, discovery.exposed)
        context = discovery.context(Context(id=RUNTIME_INSTALLATION_TOOL_NAME))
        self.assertEqual(runtime_installation_input_schema(), context["input_schema"])

    def test_o200_selected_package_duplicate_claim_from_other_delivery_is_not_registered(self):
        self._retain_fixture = True
        seed_selected_runtime_binding_package(self.root)
        duplicate = (self.root / RUNTIME_INSTALLATION_DELIVERY).with_name(
            "CA-D-621-MCP-DELIVERY--duplicate-runtime-installation.md"
        )
        duplicate.parent.mkdir(parents=True, exist_ok=True)
        duplicate.write_bytes(
            (REPOSITORY_ROOT / RUNTIME_INSTALLATION_DELIVERY).read_bytes().replace(
                b"atom_id: CA-D-620", b"atom_id: CA-D-621", 1,
            )
        )

        server, discovery = self._create_server()

        self.assertNotIn(RUNTIME_INSTALLATION_MCP_NAME, self._registered_names(server))
        self.assertNotIn(RUNTIME_INSTALLATION_MCP_NAME, discovery.exposed)
        self.assertIn(
            "ambiguous package binding: CA-D-620",
            discovery.discover(Query(query=RUNTIME_INSTALLATION_TOOL_NAME))["coverage_issues"],
        )

    def test_o200_source_action_without_delivery_binding_is_not_registered_or_exposed(self):
        self._seed_o200_source()

        server, discovery = self._create_server()

        self.assertNotIn(RUNTIME_INSTALLATION_MCP_NAME, self._registered_names(server))
        self.assertNotIn(RUNTIME_INSTALLATION_MCP_NAME, discovery.exposed)
        self.assertIsNone(discovery.context(Context(id="CA-O-200"))["input_schema"])

    def test_o200_mismatched_delivery_binding_is_not_registered_or_exposed(self):
        delivery = (REPOSITORY_ROOT / RUNTIME_INSTALLATION_DELIVERY).read_bytes().replace(
            b'entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/framework_runtime_installation_mcp.py"',
            b'entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/other.py"',
        )
        self._seed_o200_source(delivery)

        server, discovery = self._create_server()

        self.assertNotIn(RUNTIME_INSTALLATION_MCP_NAME, self._registered_names(server))
        self.assertNotIn(RUNTIME_INSTALLATION_MCP_NAME, discovery.exposed)
        self.assertIsNone(discovery.context(Context(id="CA-O-200"))["input_schema"])

    def test_o200_ambiguous_delivery_bindings_are_not_registered_or_exposed(self):
        delivery = (REPOSITORY_ROOT / RUNTIME_INSTALLATION_DELIVERY).read_bytes()
        canonical = self._seed_o200_source(delivery)
        duplicate = canonical.with_name("CA-D-611-MCP-DELIVERY--ambiguous-runtime-installation.md")
        duplicate.write_bytes(delivery.replace(b"atom_id: CA-D-620", b"atom_id: CA-D-621"))

        server, discovery = self._create_server()

        self.assertNotIn(RUNTIME_INSTALLATION_MCP_NAME, self._registered_names(server))
        self.assertNotIn(RUNTIME_INSTALLATION_MCP_NAME, discovery.exposed)
        self.assertIsNone(discovery.context(Context(id="CA-O-200"))["input_schema"])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
