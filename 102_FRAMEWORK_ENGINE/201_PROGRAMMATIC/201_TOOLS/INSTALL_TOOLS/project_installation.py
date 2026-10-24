"""Small, Project-local CAPRMEDIO setup with no runtime or Git side effects."""

from __future__ import annotations
from collections import namedtuple
import json
import os
from pathlib import Path
import sys

TOOLS_ROOT = Path(__file__).resolve().parents[1]
FRAMEWORK_ROOT = Path(__file__).resolve().parents[4]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))
from INSTALL_TOOLS.host_installation_io import FileUpdate  # noqa: E402
from technical_diagnostics import _project_prefix  # noqa: E402
from INSTALL_TOOLS.project_installation_sources import (  # noqa: E402
    ProjectInstallationError,
    _fail,
    canonical,
    directory_target,
    project_path,
    project_prefix,
    read_skill_source,
    rollback,
    select_project,
    skill_updates,
)

SETTINGS, STRUCTURE, CONTROL_PREFIX = (
    "caprmedio_project_settings.toml",
    "project_structure.toml",
    ".caprmedio_",
)


_Plan = namedtuple("_Plan", "root control name prefix existing directories updates")


def _snapshot_update(path: Path, content: bytes, expected: bytes | None) -> FileUpdate:
    update = FileUpdate(path, content, mode=0o644)
    if update.previous_content != expected:
        _fail("concurrent-change", f"Project file changed during preflight: {path}")
    return update


def _fresh(root: Path, prefix: str | None) -> tuple[Path, str, str, tuple[tuple[Path, bytes], ...]]:
    if root == FRAMEWORK_ROOT:
        _fail("framework-source-fresh", "framework source cannot be initialized as a fresh Project")
    name = root.name
    control = project_path(root, f"{CONTROL_PREFIX}{name}", "control-root")
    if os.path.lexists(control):
        _fail("control-root-conflict", "fresh Project control root already exists")
    selected = project_prefix(prefix)
    settings = (
        f'schema_version = "2.0"\n\n[project]\nname = {json.dumps(name)}\n\n[paths]\ncontrol_root = {json.dumps(control.name)}\n\n[artifacts.identity]\n'
        f'project_prefix = "{selected}"\n'
    ).encode()
    return (
        control,
        name,
        selected,
        (
            (control / SETTINGS, settings),
            (control / STRUCTURE, b"schema_version = 1\nscope_units = []\n"),
        ),
    )


def _plan(project_root: Path, prefix: str | None, source_root: Path | None) -> _Plan:
    root = canonical(project_root, "project-root")
    bundle = Path(__file__).resolve().parents[2] / "SKILLS/ca"
    source = canonical(
        source_root
        or (
            bundle
            if bundle.is_dir()
            and not bundle.is_symlink()
            and all(
                (bundle / item).is_file() and not (bundle / item).is_symlink()
                for item in ("SKILL.md", "agents/openai.yaml")
            )
            else FRAMEWORK_ROOT
        ),
        "source-root",
    )
    source_bytes = read_skill_source(source)
    selection = select_project(root, CONTROL_PREFIX)
    if selection is None:
        control, name, selected, updates = _fresh(root, prefix)
        existing = False
    else:
        name, selected, control = (
            selection.settings["project"]["name"],
            _project_prefix(selection.settings),
            selection.control_root,
        )
        if prefix is not None and project_prefix(prefix) != selected:
            _fail(
                "project-prefix-mismatch",
                "requested prefix differs from authoritative Project prefix",
            )
        updates, existing = (), True
    directory_target(control, "control-root")
    skill = project_path(root, ".agents/skills/ca", "skill-target")
    parents = tuple(
        project_path(root, relative, "skill-parent") for relative in (".agents", ".agents/skills")
    )
    directories = tuple(
        path
        for path in (
            control,
            control / "_journal",
            control / "_projection",
            *parents,
            skill,
            skill / "agents",
        )
        if directory_target(path)
    )
    raw_updates = tuple((path, content, None) for path, content in updates)
    raw_updates += skill_updates(skill, source_bytes)
    planned_updates = tuple(
        _snapshot_update(path, content, expected) for path, content, expected in raw_updates
    )
    return _Plan(
        root,
        control,
        str(name),
        selected,
        existing,
        directories,
        planned_updates,
    )


def _apply(plan: _Plan) -> None:
    created, applied = [], []
    try:
        for path in plan.directories:
            if not path.exists():
                path.mkdir()
                state = path.stat()
                created.append((path, (state.st_dev, state.st_ino)))
        for update in plan.updates:
            update.apply()
            if update.changed:
                applied.append(update)
    except BaseException as error:
        retained, conflicts = rollback(created, applied)
        if conflicts or retained:
            detail = "; ".join(
                (
                    f"rollback_conflicts={conflicts}" if conflicts else "",
                    f"retained_dirs={retained}" if retained else "",
                )
            ).strip("; ")
            raise ProjectInstallationError("restore-conflict", detail) from error
        raise


def install_project(
    project_root: Path,
    *,
    prefix: str | None = None,
    apply: bool = False,
    source_root: Path | None = None,
) -> dict[str, object]:
    plan = _plan(project_root, prefix, source_root)
    changed = [path.relative_to(plan.root).as_posix() for path in plan.directories]
    changed += [
        update.path.relative_to(plan.root).as_posix() for update in plan.updates if update.changed
    ]
    if apply:
        _apply(plan)
    return {
        "ok": True,
        "mode": "apply" if apply else "dry_run",
        "project_root": plan.root.as_posix(),
        "control_root": plan.control.relative_to(plan.root).as_posix(),
        "project_name": plan.name,
        "project_prefix": plan.prefix,
        "existing_project": plan.existing,
        "planned_changes": sorted(changed),
        "changed": sorted(changed) if apply else [],
        "installed": bool(apply and changed),
        "no_op": not changed,
    }


__all__ = ["ProjectInstallationError", "install_project"]
