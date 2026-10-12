"""Pure registration guards for independent current Release snapshot admission."""
from __future__ import annotations

import sys
import types
import unittest
from unittest.mock import patch


MCP = __import__("pathlib").Path(__file__).resolve().parents[1]
if str(MCP) not in sys.path:
    sys.path.insert(0, str(MCP))

from selected_routes import (  # noqa: E402
    SELECTED_ROUTE_NAMES,
    SelectedRouteError,
    register_selected_routes,
)


class _ToolAnnotations:
    def __init__(self, **values: object) -> None:
        self.values = values


class _Server:
    def __init__(self) -> None:
        self.names: list[str] = []

    def tool(self, *, name: str, structured_output: bool, annotations: object):
        del structured_output, annotations

        def decorate(function):
            self.names.append(name)
            return function

        return decorate


def _manifest(names: tuple[str, ...]) -> dict[str, object]:
    return {"routes": [{"route": name} for name in names]}


class ReleasePublicRegistrationTest(unittest.TestCase):
    def register(self, loaded: object, *, snapshot: object = None) -> list[str]:
        server = _Server()
        mcp_module = types.ModuleType("mcp")
        types_module = types.ModuleType("mcp.types")
        types_module.ToolAnnotations = _ToolAnnotations
        mcp_module.types = types_module
        with patch.dict(sys.modules, {"mcp": mcp_module, "mcp.types": types_module}), \
                patch("selected_routes.load_selected_manifest", return_value=loaded), \
                patch("selected_routes.load_release_execution_manifest",
                      side_effect=(snapshot if isinstance(snapshot, Exception) else None),
                      return_value=snapshot):
            register_selected_routes(server, ".")
        return server.names

    def test_static_fifteen_names_remain_unchanged(self) -> None:
        self.assertEqual(15, len(SELECTED_ROUTE_NAMES))
        self.assertNotIn("release_version", SELECTED_ROUTE_NAMES)

    def test_current_fifteen_manifest_omits_release_when_current_snapshot_is_unavailable(self) -> None:
        names = self.register(_manifest(SELECTED_ROUTE_NAMES), snapshot=SelectedRouteError("required current source missing"))
        self.assertEqual(list(SELECTED_ROUTE_NAMES), names[:len(SELECTED_ROUTE_NAMES)])
        self.assertNotIn("release_version", names)

    def test_current_release_snapshot_registers_without_requiring_sixteen_route_portfolio(self) -> None:
        names = self.register(_manifest(SELECTED_ROUTE_NAMES), snapshot=_manifest(("release_version",)))
        self.assertEqual([*SELECTED_ROUTE_NAMES, "release_version"], names[:16])
        self.assertEqual(1, names.count("release_version"))

    def test_invalid_or_stale_current_snapshot_omits_release_even_with_old_portfolio_route(self) -> None:
        for error in (
            SelectedRouteError("release-source-pin-stale: source pin is stale"),
            SelectedRouteError("selected workflow binding manifest is invalid"),
        ):
            server = _Server()
            mcp_module = types.ModuleType("mcp")
            types_module = types.ModuleType("mcp.types")
            types_module.ToolAnnotations = _ToolAnnotations
            mcp_module.types = types_module
            with self.subTest(error=str(error)), \
                    patch.dict(sys.modules, {"mcp": mcp_module, "mcp.types": types_module}), \
                    patch("selected_routes.load_selected_manifest",
                          return_value=_manifest((*SELECTED_ROUTE_NAMES, "release_version"))), \
                    patch("selected_routes.load_release_execution_manifest", side_effect=error):
                register_selected_routes(server, ".")
            self.assertEqual(list(SELECTED_ROUTE_NAMES), server.names[:len(SELECTED_ROUTE_NAMES)])
            self.assertNotIn("release_version", server.names)

    def test_stale_unrelated_portfolio_does_not_withhold_current_release_snapshot(self) -> None:
        server = _Server()
        mcp_module = types.ModuleType("mcp")
        types_module = types.ModuleType("mcp.types")
        types_module.ToolAnnotations = _ToolAnnotations
        mcp_module.types = types_module
        with patch.dict(sys.modules, {"mcp": mcp_module, "mcp.types": types_module}), \
                patch("selected_routes.load_selected_manifest", side_effect=SelectedRouteError("unrelated O030 pin is stale")), \
                patch("selected_routes.load_release_execution_manifest", return_value=_manifest(("release_version",))):
            register_selected_routes(server, ".")
        self.assertEqual([*SELECTED_ROUTE_NAMES, "release_version"], server.names[:16])
        self.assertEqual(1, server.names.count("release_version"))


if __name__ == "__main__":
    unittest.main()
