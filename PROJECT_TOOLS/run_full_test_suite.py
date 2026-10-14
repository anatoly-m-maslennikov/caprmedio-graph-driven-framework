"""Run every source test module in a fresh interpreter; report skips honestly."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import nullcontext
import json
import os
from pathlib import Path
import subprocess
import sys
import time

from full_suite_docker import APP, current_code_test_image, run_launcher

CODE_ROOTS = ("102_FRAMEWORK_ENGINE", "PROJECT_TOOLS")
MODULE_TIMEOUT_SECONDS = 1800
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


def run_module(
    root: Path, module: Path, environment=None
) -> tuple[bool, int, int, str, str, float, str | None]:
    """Return one isolated module's result and output for coherent reporting."""
    started = time.monotonic()
    environment = {
        **(os.environ if environment is None else environment),
        "CAPRMEDIO_DOCKER_E2E": "1",
        "CAPRMEDIO_DOCKER_QUERY_E2E": "1",
    }
    try:
        result = subprocess.run(
            (sys.executable, "-B", "-c", CHILD, str(module.parent), module.stem),
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
            timeout=MODULE_TIMEOUT_SECONDS,
            env=environment,
        )
        counts = [
            line[len(RESULT_MARKER) :]
            for line in result.stdout.splitlines()
            if line.startswith(RESULT_MARKER)
        ]
        observed = json.loads(counts[-1]) if counts else {"tests": 0, "skipped": 0}
        return (
            result.returncode == 0 and bool(counts),
            observed["tests"],
            observed["skipped"],
            result.stdout,
            result.stderr,
            time.monotonic() - started,
            None,
        )
    except (OSError, subprocess.TimeoutExpired, ValueError) as error:
        stdout = _output_text(error.stdout) if isinstance(error, subprocess.TimeoutExpired) else ""
        stderr = _output_text(error.stderr) if isinstance(error, subprocess.TimeoutExpired) else ""
        return False, 0, 0, stdout, stderr, time.monotonic() - started, str(error)


def _docker_module(root: Path, module: Path) -> bool:
    return module.parent == root / APP / "tests" and (
        module.stem.endswith("_docker_e2e") or module.stem == "test_selected_query_mcp_e2e"
    )


def run_full_suite(root: Path) -> int:
    """Attempt the complete discovered suite and fail on test or import errors."""
    modules = discover_test_modules(root)
    if not modules:
        print("No source test modules found", file=sys.stderr)
        return 1
    integration = any(_docker_module(root, module) for module in modules)
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


def _output_text(output: str | bytes | None) -> str:
    return output.decode("utf-8", errors="replace") if isinstance(output, bytes) else output or ""


def _run_modules(root: Path, modules: list[Path], environment: dict, integration: bool) -> int:
    failed = []
    tests = skipped = 0
    with ThreadPoolExecutor(max_workers=4) as ordinary, ThreadPoolExecutor(max_workers=2) as docker:
        pending = {
            (docker if _docker_module(root, module) else ordinary).submit(
                run_module, root, module, environment
            ): module
            for module in sorted(
                modules,
                key=lambda module: (
                    module != root / APP / "tests/test_selected_workflows_docker_e2e.py"
                ),
            )
        }
        for future in as_completed(pending):
            module = pending.pop(future)
            successful, count, skips, stdout, stderr, elapsed, diagnostic = future.result()
            print(f"Test module: {module.relative_to(root)}", flush=True)
            print(stdout, end="", flush=True)
            print(stderr, end="", file=sys.stderr, flush=True)
            if diagnostic is not None:
                print(
                    f"Test module failed: {module.relative_to(root)}: {diagnostic}", file=sys.stderr
                )
            print(f"Module time: {module.relative_to(root)}: {elapsed:.3f}s", flush=True)
            tests += count
            skipped += skips
            if not successful:
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
