"""Prevent direct Tool wrappers from losing their original CLI bodies."""

from __future__ import annotations

import ast
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


TOOLS = Path(__file__).resolve().parents[1]
TEST_TEMP_ROOT = TOOLS.parents[2] / ".caprmedio_tmp" / "tests" / Path(__file__).stem
FIXTURE = json.loads((Path(__file__).with_name("fixtures") / "image_tool_cli.json").read_text())
WRAPPER_SCRIPTS = FIXTURE["wrappers"]
CALLBACK_ENTRYPOINT_GROUPS = FIXTURE["callback_entrypoint_groups"]
IMPORTED_CALLBACKS = FIXTURE["imported_callbacks"]
SPECIAL_CALLBACK_BODIES = FIXTURE["special_callback_bodies"]
MALFORMED_CLI_CASES = (
    ("artifact_metadata.py", ()),
    ("MIGRATE_ATOM_IDENTITY/migrate_atom_identity.py", ()),
    ("migrations/apply_fpf_audit_repairs.py", ("--unknown",)),
)


def _main_guard(node: ast.stmt) -> bool:
    return (
        isinstance(node, ast.If)
        and isinstance(node.test, ast.Compare)
        and isinstance(node.test.left, ast.Name)
        and node.test.left.id == "__name__"
        and len(node.test.ops) == len(node.test.comparators) == 1
        and isinstance(node.test.ops[0], ast.Eq)
        and isinstance(node.test.comparators[0], ast.Constant)
        and node.test.comparators[0].value == "__main__"
    )


def _expected_callback_body(relative: str) -> list[ast.stmt]:
    if relative in SPECIAL_CALLBACK_BODIES:
        source = SPECIAL_CALLBACK_BODIES[relative]
    elif relative in IMPORTED_CALLBACKS:
        source = f"from {IMPORTED_CALLBACKS[relative]} import cli\nreturn cli()"
    else:
        entrypoint = next(
            (
                expression
                for expression, scripts in CALLBACK_ENTRYPOINT_GROUPS.items()
                if relative in scripts
            ),
            "main()",
        )
        source = f"return {entrypoint}"
    return ast.parse(source).body


class ImageToolCliBoundaryTests(unittest.TestCase):
    def test_all_wrappers_close_the_original_cli_inside_the_callback(self) -> None:
        for relative in WRAPPER_SCRIPTS:
            with self.subTest(script=relative):
                source = (TOOLS / relative).read_text(encoding="utf-8")
                module = ast.parse(source, filename=relative)
                callbacks = [
                    node
                    for node in module.body
                    if isinstance(node, ast.FunctionDef) and node.name == "_image_main"
                ]
                self.assertEqual(1, len(callbacks))
                guards = [node for node in module.body if _main_guard(node)]
                self.assertEqual(1, len(guards))
                self.assertEqual(
                    [
                        ast.dump(statement, include_attributes=False)
                        for statement in _expected_callback_body(relative)
                    ],
                    [
                        ast.dump(statement, include_attributes=False)
                        for statement in callbacks[0].body
                    ],
                )
                self.assertFalse(
                    any(
                        _main_guard(node)
                        for node in ast.walk(callbacks[0])
                        if isinstance(node, ast.stmt)
                    )
                )
                statement = guards[0].body[-1]
                self.assertIsInstance(statement, ast.Raise)
                call = statement.exc
                self.assertIsInstance(call, ast.Call)
                self.assertIsInstance(call.func, ast.Name)
                self.assertEqual("SystemExit", call.func.id)
                self.assertEqual(1, len(call.args))
                boundary = call.args[0]
                self.assertIsInstance(boundary, ast.Call)
                self.assertIsInstance(boundary.func, ast.Name)
                self.assertEqual("run_process", boundary.func.id)
                self.assertIsInstance(boundary.args[0], ast.Name)
                self.assertEqual("_image_main", boundary.args[0].id)

    def test_malformed_direct_cli_flows_fail_without_traceback(self) -> None:
        TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
        for relative, arguments in MALFORMED_CLI_CASES:
            with (
                self.subTest(script=relative),
                tempfile.TemporaryDirectory(
                    dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True
                ) as directory,
            ):
                environment = {
                    **os.environ,
                    "PYTHONDONTWRITEBYTECODE": "1",
                    "PYTHONPYCACHEPREFIX": str(Path(directory) / "pycache"),
                }
                result = subprocess.run(
                    [sys.executable, str(TOOLS / relative), *arguments],
                    cwd=directory,
                    env=environment,
                    capture_output=True,
                    text=True,
                    check=False,
                    timeout=15,
                )
                self.assertEqual(2, result.returncode, result.stderr)
                self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
