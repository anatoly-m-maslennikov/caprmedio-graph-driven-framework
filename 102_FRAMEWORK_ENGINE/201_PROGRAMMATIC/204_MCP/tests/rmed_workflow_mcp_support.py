# implementation of:
# Method: CA-M-395, CA-M-431
# Evaluation: CA-E-567
from collections.abc import AsyncIterator, Callable
from contextlib import asynccontextmanager, redirect_stderr
import io
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from typing import Any
from unittest.mock import patch

from mcp import Client, StdioServerParameters
from mcp.client.stdio import stdio_client
ROOT = Path(__file__).resolve().parents[4]
SERVER = ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py"

# CA-D-548's stable helpers plus the gateway controls remain required.
D548_REQUIRED_TOOLS = frozenset(
    {
        "rmed_atoms_base_revise",
        "discover_tools",
        "discover_operations",
        "get_execution_context",
        "get_execution_status",
        "resume_execution_context",
        "watch_execution",
        "workflow_orchestrator",
        "reload_mcp_implementation",
        "get_mcp_reload_status",
    }
)

# CA-D-547 v5 is independently fixed rather than derived from registration.
D547_ADMITTED_SELECTED_ROUTES = (
    "create_atom",
    "update_atom",
    "replace_atom",
    "change_atom_status",
    "create_scope_unit",
    "rename_scope_unit",
    "move_scope_unit",
    "remove_scope_unit",
    "run_implementation_workflow",
    "revert_changes",
    "build_entities_graph",
    "build_terms_graph",
    "build_applicable_methodology",
    "find_and_fetch_artifacts",
    "find_and_fetch_journal_events",
)
D547_SELECTED_CONTROL_TOOLS = frozenset(
    {"get_selected_workflow_run", "get_selected_action_run"}
)
D547_DIRECT_RELEASE_TOOLS = frozenset({"release_version", "public.release"})

HELPER_DECLARATION_IDS = (
    "CA-D-512",
    "CA-D-513",
    "CA-D-514",
    "CA-D-515",
    "CA-D-516",
    "CA-D-517",
    "CA-D-518",
    "CA-D-551",
    "CA-D-557",
)

# The disposable harness already budgets 120 seconds for a cold startup.  The
# MCP SDK's discover probe is patched to that same finite allowance by the
# owning workflow test; production gateway deadlines remain unchanged.
GATEWAY_STARTUP_TIMEOUT_SECONDS = 120
_STARTUP_TELEMETRY_LINE = re.compile(
    r"^caprmedio_mcp_startup phase=(?:initial_fingerprint|reload_fingerprint|fingerprint_verify|"
    r"child_handshake|list_tools|generation_ready|schema_validation|implementation_import|"
    r"selected_registration|catalog|catalog_registration) "
    r"outcome=(?:completed|failed) elapsed_ms=[0-9]+$"
)


def _forward_startup_telemetry(stderr: io.TextIOBase) -> None:
    """Expose only accepted opt-in timing records after a client run."""

    if os.environ.get("CAPRMEDIO_STARTUP_TELEMETRY") != "1":
        return
    stderr.seek(0)
    for line in stderr.read().splitlines():
        if _STARTUP_TELEMETRY_LINE.fullmatch(line):
            print(line, file=sys.stderr, flush=True)


def _server_parameters(root: Path) -> StdioServerParameters:
    return StdioServerParameters(
        command=sys.executable,
        args=["-B", str(SERVER), "--project-root", str(root)],
        env={"CAPRMEDIO_STARTUP_TELEMETRY": "1"},
    )


@asynccontextmanager
async def bounded_server_client(
    root: Path,
    *,
    cache: object | None = None,
    stdio_client_factory: Callable[..., Any] = stdio_client,
    client_factory: Callable[..., Any] = Client,
    telemetry_forwarder: Callable[[io.TextIOBase], None] = _forward_startup_telemetry,
) -> AsyncIterator[Any]:
    """Run one stdio client with the finite disposable startup allowance."""

    with tempfile.TemporaryFile(mode="w+", encoding="utf-8") as stderr:
        try:
            with (
                patch.dict(os.environ, {"CAPRMEDIO_STARTUP_TELEMETRY": "1"}),
                patch(
                    "mcp.client.session.DISCOVER_TIMEOUT_SECONDS",
                    GATEWAY_STARTUP_TIMEOUT_SECONDS,
                ),
            ):
                transport = stdio_client_factory(_server_parameters(root), errlog=stderr)
                async with client_factory(
                    transport,
                    cache=cache,
                    read_timeout_seconds=GATEWAY_STARTUP_TIMEOUT_SECONDS,
                ) as client:
                    yield client
        except BaseException as error:
            with patch.dict(os.environ, {"CAPRMEDIO_STARTUP_TELEMETRY": "1"}):
                telemetry_forwarder(stderr)
            stderr.seek(0)
            detail = stderr.read()[-4096:]
            if detail:
                raise AssertionError(
                    f"MCP stdio startup failed; stderr follows:\n{detail}"
                ) from error
            raise
        else:
            telemetry_forwarder(stderr)


class InstalledLayoutImport(unittest.TestCase):
    def test_startup_telemetry_forwarding_is_opt_in_and_filters_untrusted_stderr(
        self,
    ) -> None:
        valid = "caprmedio_mcp_startup phase=list_tools outcome=completed elapsed_ms=17"
        captured = io.StringIO(f"{valid}\n/secret/path --project-root source-content\n")
        forwarded = io.StringIO()
        with patch.dict(os.environ, {"CAPRMEDIO_STARTUP_TELEMETRY": "1"}), redirect_stderr(
            forwarded
        ):
            _forward_startup_telemetry(captured)
        self.assertEqual(forwarded.getvalue(), valid + "\n")

        captured = io.StringIO(valid + "\n")
        forwarded = io.StringIO()
        with patch.dict(os.environ, {}, clear=False), redirect_stderr(forwarded):
            os.environ.pop("CAPRMEDIO_STARTUP_TELEMETRY", None)
            _forward_startup_telemetry(captured)
        self.assertEqual(forwarded.getvalue(), "")

    def test_startup_allowance_uses_the_disposable_harness_budget(self) -> None:
        self.assertEqual(120, GATEWAY_STARTUP_TIMEOUT_SECONDS)

    def test_implementation_imports_from_framework_engine_layout(self) -> None:
        """The release copies the Engine without the source-tree numeric prefix."""

        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as temporary:
            installed = Path(temporary) / "opt/caprmedio-framework/FRAMEWORK_ENGINE"
            shutil.copytree(
                ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC",
                installed / "201_PROGRAMMATIC",
                ignore=shutil.ignore_patterns("__pycache__", ".caprmedio_tmp"),
            )
            shutil.copytree(
                ROOT / "102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/RMED_ATOM_REVIEW",
                installed / "202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/RMED_ATOM_REVIEW",
                ignore=shutil.ignore_patterns("__pycache__", ".mypy_cache"),
            )
            implementation = installed / "201_PROGRAMMATIC/204_MCP/implementation_server.py"
            result = subprocess.run(
                [
                    sys.executable,
                    "-B",
                    "-c",
                    "import runpy, sys; sys.path.insert(0, "
                    + repr(str(implementation.parent))
                    + "); runpy.run_path("
                    + repr(str(implementation))
                    + ")",
                ],
                capture_output=True,
                text=True,
            )
            self.assertEqual(0, result.returncode, result.stderr)
