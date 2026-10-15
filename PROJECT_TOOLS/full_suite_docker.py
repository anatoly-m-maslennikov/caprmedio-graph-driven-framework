"""One current-source test image, never a running Project MCP installation."""

from __future__ import annotations

from contextlib import contextmanager
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import uuid

APP = Path("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR")
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / APP / "docker"))
from runtime_images import ImageManager, _bounded_run  # noqa: E402

ATTEMPT_LABEL = "org.caprmedio.full-test-suite.attempt"
LAUNCHER_TIMEOUT_SECONDS = 1980


def _executor(attempt: str):
    def execute(argv, **kwargs):
        build = argv[:2] == ["docker", "build"]
        if build:
            argv = [*argv[:2], "--label", f"{ATTEMPT_LABEL}={attempt}", *argv[2:]]
        return _bounded_run(
            argv,
            cwd=kwargs["cwd"],
            timeout=kwargs["timeout"],
            capture_stdout=not build,
            buildx_config=kwargs.get("env", {}).get("BUILDX_CONFIG"),
        )

    return execute


def _remove_owned_image(root: Path, image: str, attempt: str) -> None:
    """An in-use image is retained; no container is removed by this owner."""
    try:
        observed = _bounded_run(["docker", "image", "inspect", image], cwd=root, timeout=30)
        if observed.returncode != 0:
            raise OSError("test image inspection failed")
        labels = json.loads(observed.stdout)[0]["Config"]["Labels"]
        if not isinstance(labels, dict) or labels.get(ATTEMPT_LABEL) != attempt:
            raise OSError("test image attribution differs")
        containers = _bounded_run(
            ["docker", "container", "ls", "--all", "--filter", f"ancestor={image}", "--quiet"],
            cwd=root,
            timeout=30,
        )
        if containers.returncode != 0 or containers.stdout.strip():
            raise OSError("test image may still be in use; retained")
        removed = _bounded_run(["docker", "image", "rm", image], cwd=root, timeout=30)
        if removed.returncode != 0:
            raise OSError("non-force test image removal failed; retained")
    except (
        OSError,
        ValueError,
        KeyError,
        IndexError,
        TypeError,
        subprocess.TimeoutExpired,
    ) as error:
        print(f"Test image cleanup: {image}: {error}", file=sys.stderr)


@contextmanager
def current_code_test_image(root: Path):
    parent = root / ".caprmedio_tmp/tests/full-suite-integration"
    for component in (root / ".caprmedio_tmp", parent.parent, parent):
        if component.is_symlink():
            raise OSError("test scratch must remain inside the selected Project")
    parent.mkdir(parents=True, exist_ok=True)
    if parent.resolve(strict=True) != parent or parent.is_symlink():
        raise OSError("test scratch must remain inside the selected Project")
    scratch = Path(tempfile.mkdtemp(prefix="attempt-", dir=parent))
    attempt = uuid.uuid4().hex
    manager = ImageManager(root, executor=_executor(attempt), build_temp_root=scratch)
    image = manager._build(manager.identity())
    environment = {
        "CAPRMEDIO_IMAGE": image,
        "CAPRMEDIO_FIRST_CUT_HTTP_IMAGE": image,
        "CAPRMEDIO_FIRST_CUT_HTTP_SCRATCH": str(scratch),
        "CAPRMEDIO_DOCKER_QUERY_IMAGE": image,
        "TMPDIR": str(scratch),
        "CAPRMEDIO_PROJECT_LAUNCHER_DOCKER_E2E": "1",
    }
    try:
        yield environment
    finally:
        _remove_owned_image(root, image, attempt)


def run_launcher(root: Path, environment: dict[str, str]) -> bool:
    """The launcher's real two-group CLI proof is not a unittest fixture case."""
    result = subprocess.run(
        [
            sys.executable,
            "-B",
            str(root / APP / "tests/test_project_launcher_docker_e2e.py"),
            "--source-root",
            str(root),
            "--scratch",
            environment["CAPRMEDIO_FIRST_CUT_HTTP_SCRATCH"],
            "--image",
            environment["CAPRMEDIO_FIRST_CUT_HTTP_IMAGE"],
            "--group",
            "all",
        ],
        cwd=root,
        env=environment,
        timeout=LAUNCHER_TIMEOUT_SECONDS,
        capture_output=True,
        text=True,
        check=False,
    )
    print(result.stdout, end="", flush=True)
    print(result.stderr, end="", file=sys.stderr, flush=True)
    return result.returncode == 0
