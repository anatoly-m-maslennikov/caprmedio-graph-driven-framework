"""Observe build provenance from the owning Project, never the copied package."""

from collections.abc import Mapping
from pathlib import Path
import re
import subprocess
from typing import Protocol

from release_cleanup_identity import Runner


class SelectedProject(Protocol):
    @property
    def instance_id(self) -> str: ...
    @property
    def control_relative(self) -> Path: ...
    @property
    def settings(self) -> Mapping[str, object]: ...


def release_image_provenance(
    root: Path,
    selection: SelectedProject,
    runner: Runner | None = None,
) -> dict[str, str]:
    project = selection.settings.get("project")
    name = project.get("name") if isinstance(project, Mapping) else None
    if not isinstance(name, str) or not name.strip():
        raise ValueError("local-release-project-name-invalid")
    argv = ("git", "rev-parse", "--verify", "HEAD")
    result = (
        runner(argv, root)
        if runner
        else subprocess.run(
            argv,
            cwd=root,
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
    )
    head = result.stdout.strip()
    if result.returncode != 0 or re.fullmatch(r"(?:[0-9a-f]{40}|[0-9a-f]{64})", head) is None:
        raise ValueError("local-release-head-commit-unavailable")
    return {
        "project_id": selection.instance_id,
        "project_root": str(root),
        "control_root": selection.control_relative.as_posix(),
        "project_name": name,
        "head_commit": head,
    }
