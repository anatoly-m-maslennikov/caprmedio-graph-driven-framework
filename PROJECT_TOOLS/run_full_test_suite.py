"""Run every source test module in a fresh interpreter; report skips honestly."""

from __future__ import annotations

import argparse
from contextlib import nullcontext
import json
import os
from pathlib import Path
import subprocess
import sys

from full_suite_docker import APP, current_code_test_image, run_launcher

CODE_ROOTS = ("102_FRAMEWORK_ENGINE", "PROJECT_TOOLS")
MODULE_TIMEOUT_SECONDS = 600
RESULT_MARKER = "CAPRMEDIO_TEST_COUNTS "
CHILD = """
import json, sys, unittest
sys.path.insert(0, sys.argv[1])
suite = unittest.defaultTestLoader.loadTestsFromName(sys.argv[2])
count = suite.countTestCases()
result = unittest.TextTestRunner(verbosity=2).run(suite)
required_skips = [(test.id(), reason) for test, reason in result.skipped
                  if "_e2e" in sys.argv[2] or "_e2e." in test.id()]
if required_skips:
    print("Required integration tests skipped: " + repr(required_skips), file=sys.stderr)
print("CAPRMEDIO_TEST_COUNTS " + json.dumps({"tests": result.testsRun, "skipped": len(result.skipped)}))
if not count:
    print("No test cases loaded", file=sys.stderr)
sys.exit(0 if count and result.wasSuccessful() and not required_skips else 1)
"""


def discover_test_modules(root: Path) -> list[Path]:
    """Select source modules, not caches or copied tests inside test fixtures."""

    def failed(error: OSError) -> None:
        raise error

    modules = []
    for name in CODE_ROOTS:
        source = root / name
        if source.is_symlink() or not source.is_dir():
            raise OSError(f"source test root is unavailable: {source}")
        for folder, directories, filenames in os.walk(source, followlinks=False, onerror=failed):
            parts = Path(folder).relative_to(source).parts
            directories[:] = [
                entry
                for entry in directories
                if not entry.startswith(".")
                and entry != "__pycache__"
                and not (entry == "tests" and "tests" in parts)
            ]
            for entry in directories:
                if (Path(folder) / entry).is_symlink():
                    raise OSError(
                        f"source test directory is a symbolic link: {Path(folder) / entry}"
                    )
            for filename in filenames:
                path = Path(folder) / filename
                if (
                    filename.startswith("test_")
                    and path.suffix == ".py"
                    and path.stem.isidentifier()
                ):
                    if path.is_symlink():
                        raise OSError(f"test module is a symbolic link: {path}")
                    modules.append(path)
    return sorted(modules)


def run_module(root: Path, module: Path, environment=None) -> tuple[bool, int, int]:
    """Execute one unittest module without sharing imported sibling modules."""
    environment = {
        **(os.environ if environment is None else environment),
        "CAPRMEDIO_DOCKER_E2E": "1",
        "CAPRMEDIO_DOCKER_QUERY_E2E": "1",
    }
    result = subprocess.run(
        (sys.executable, "-B", "-c", CHILD, str(module.parent), module.stem),
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
        timeout=MODULE_TIMEOUT_SECONDS,
        env=environment,
    )
    print(result.stdout, end="", flush=True)
    print(result.stderr, end="", file=sys.stderr, flush=True)
    counts = [
        line[len(RESULT_MARKER) :]
        for line in result.stdout.splitlines()
        if line.startswith(RESULT_MARKER)
    ]
    if not counts:
        return False, 0, 0
    observed = json.loads(counts[-1])
    return result.returncode == 0, observed["tests"], observed["skipped"]


def run_full_suite(root: Path) -> int:
    """Attempt the complete discovered suite and fail on test or import errors."""
    modules = discover_test_modules(root)
    if not modules:
        print("No source test modules found", file=sys.stderr)
        return 1
    integration = any(
        module.parent == root / APP / "tests"
        and (module.stem.endswith("_docker_e2e") or module.stem == "test_selected_query_mcp_e2e")
        for module in modules
    )
    context = current_code_test_image(root) if integration else nullcontext({})
    try:
        with context as additions:
            environment = {**os.environ, **additions}
            if integration:
                environment.pop("CAPRMEDIO_RELEASE_E2E_CONTEXT", None)
                environment.pop("CAPRMEDIO_CANDIDATE_IMAGE_DIGEST", None)
            return _run_modules(root, modules, environment, integration)
    except Exception as error:
        print(f"Required test environment failed: {error}", file=sys.stderr)
        return 1


def _run_modules(root: Path, modules: list[Path], environment: dict, integration: bool) -> int:
    failed = []
    tests = skipped = 0
    for module in modules:
        print(f"Test module: {module.relative_to(root)}", flush=True)
        try:
            successful, count, skips = run_module(root, module, environment)
            tests += count
            skipped += skips
            if not successful:
                failed.append(module.relative_to(root).as_posix())
        except (OSError, subprocess.TimeoutExpired, ValueError) as error:
            print(f"Test module failed: {module.relative_to(root)}: {error}", file=sys.stderr)
            failed.append(module.relative_to(root).as_posix())
    if integration:
        try:
            if not run_launcher(root, environment):
                failed.append("project_launcher_docker_e2e CLI")
        except (OSError, subprocess.TimeoutExpired) as error:
            print(f"Required launcher integration failed: {error}", file=sys.stderr)
            failed.append("project_launcher_docker_e2e CLI")
    if failed:
        print("Failed test modules: " + ", ".join(failed), file=sys.stderr)
    print(
        f"Modules: {len(modules)}; tests run: {tests}; skipped: {skipped}; failed modules: {len(failed)}"
    )
    return int(bool(failed))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    arguments = parser.parse_args()
    return run_full_suite(arguments.project_root.resolve(strict=True))


if __name__ == "__main__":
    raise SystemExit(main())
