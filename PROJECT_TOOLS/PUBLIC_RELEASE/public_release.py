"""Small, callback-wired public-release flow for this Project.

The caller supplies the concrete GitHub, test, prompt, and journal adapters.
This module only orders their work and writes the three declared release
documents.  It deliberately never invokes Git, GitHub, or a test runner by
itself.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Protocol, Sequence
import tomllib


class PublicReleaseError(ValueError):
    """A release input or callback result cannot safely continue."""


class PublicReleaseHooks(Protocol):
    def prompt(self, project_root: Path, version: str, changes: Sequence[str]) -> Mapping[str, object]: ...

    def test(self, project_root: Path, candidate_root: Path) -> object: ...

    def commit(self, project_root: Path, paths: Sequence[str], message: str) -> object: ...

    def push(self, project_root: Path, branch: str) -> object: ...

    def pr(self, project_root: Path, branch: str, base: str, body: str) -> Mapping[str, object]: ...

    def journal(self, event: Mapping[str, object]) -> None: ...


@dataclass(frozen=True)
class _Config:
    branch: str
    base: str
    release_paths: tuple[str, ...]
    readme_path: str
    notes_path: str
    version_history_path: str
    candidate_root: str
    changes: tuple[str, ...]


def _non_empty_string(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip() or value != value.strip() or "\n" in value or "\r" in value:
        raise PublicReleaseError(f"{label} must be one non-empty line")
    return value


def _relative_path(value: object, label: str) -> str:
    text = _non_empty_string(value, label)
    path = Path(text)
    if path.is_absolute() or ".." in path.parts:
        raise PublicReleaseError(f"{label} must stay under the Project root")
    return path.as_posix()


def _string_list(value: object, label: str, *, allow_empty: bool = False) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)) or (not value and not allow_empty):
        raise PublicReleaseError(f"{label} must be a non-empty list")
    result = tuple(_non_empty_string(item, f"{label}[{index}]") for index, item in enumerate(value))
    if len(set(result)) != len(result):
        raise PublicReleaseError(f"{label} must not repeat values")
    return result


def _config(value: Mapping[str, object]) -> _Config:
    required = {
        "branch",
        "base",
        "release_paths",
        "readme_path",
        "notes_path",
        "version_history_path",
        "candidate_root",
        "changes",
    }
    if set(value) != required:
        raise PublicReleaseError(f"config must contain exactly: {', '.join(sorted(required))}")
    branch = _non_empty_string(value["branch"], "config.branch")
    base = _non_empty_string(value["base"], "config.base")
    if branch != "amm/dev" or base != "main":
        raise PublicReleaseError("public release requires branch amm/dev and base main")
    release_paths = tuple(_relative_path(item, f"config.release_paths[{index}]")
                          for index, item in enumerate(value["release_paths"] if isinstance(value["release_paths"], (list, tuple)) else ()))
    if not release_paths or len(set(release_paths)) != len(release_paths):
        raise PublicReleaseError("config.release_paths must be a non-empty unique list")
    readme_path = _relative_path(value["readme_path"], "config.readme_path")
    notes_path = _relative_path(value["notes_path"], "config.notes_path")
    version_history_path = _relative_path(value["version_history_path"], "config.version_history_path")
    if {readme_path, notes_path, version_history_path} - set(release_paths):
        raise PublicReleaseError("release_paths must include the README, notes, and Version History paths")
    return _Config(
        branch=branch,
        base=base,
        release_paths=release_paths,
        readme_path=readme_path,
        notes_path=notes_path,
        version_history_path=version_history_path,
        candidate_root=_relative_path(value["candidate_root"], "config.candidate_root"),
        changes=_string_list(value["changes"], "config.changes", allow_empty=True),
    )


def _inside(root: Path, relative: str, label: str) -> Path:
    root = root.resolve()
    path = (root / relative).resolve()
    if root != path and root not in path.parents:
        raise PublicReleaseError(f"{label} escapes the Project root")
    return path


def _read_version(project_root: Path) -> str:
    version_path = _inside(project_root, "version.toml", "version.toml")
    try:
        document = tomllib.loads(version_path.read_text(encoding="utf-8"))
        version = document["framework"]["version"]
    except (FileNotFoundError, KeyError, TypeError, tomllib.TOMLDecodeError) as error:
        raise PublicReleaseError("version.toml must declare [framework].version") from error
    return _non_empty_string(version, "version.toml [framework].version")


def _prompt_result(value: Mapping[str, object]) -> tuple[tuple[str, ...], tuple[str, ...], tuple[str, ...]]:
    if set(value) != {"whats_new", "whats_fixed", "version_history_bullets"}:
        raise PublicReleaseError("prompt result must contain exactly whats_new, whats_fixed, and version_history_bullets")
    return (
        _string_list(value["whats_new"], "prompt.whats_new"),
        _string_list(value["whats_fixed"], "prompt.whats_fixed"),
        _string_list(value["version_history_bullets"], "prompt.version_history_bullets"),
    )


def _bullet_section(title: str, lines: Sequence[str]) -> str:
    return "\n".join((f"## {title}", *(f"- {line}" for line in lines)))


def _body(whats_new: Sequence[str], whats_fixed: Sequence[str]) -> str:
    return _bullet_section("What's new", whats_new) + "\n\n" + _bullet_section("What's fixed", whats_fixed) + "\n"


def _require_passed(result: object) -> None:
    if result is not True and (not isinstance(result, Mapping) or result.get("passed") is not True):
        raise PublicReleaseError("configured full test suite did not report passed")


def _pr_url(value: Mapping[str, object]) -> str:
    url = value.get("url")
    if not isinstance(url, str) or not url.startswith("https://") or any(char in url for char in "\r\n"):
        raise PublicReleaseError("PR hook must return an https url")
    return url


def _write(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8")


def _require_hooks(hooks: PublicReleaseHooks) -> None:
    missing = tuple(
        name for name in ("prompt", "test", "commit", "push", "pr", "journal")
        if not callable(getattr(hooks, name, None))
    )
    if missing:
        raise PublicReleaseError(f"hooks must provide callable: {', '.join(missing)}")


def _journal(hooks: PublicReleaseHooks, run_id: str, phase: str, **details: object) -> None:
    hooks.journal({"run_id": run_id, "phase": phase, **details})


def run_public_release(project_root: Path, *, run_id: str, hooks: PublicReleaseHooks,
                       config: Mapping[str, object]) -> dict[str, object]:
    """Run one Public release, stopping at the first failed callback.

    The only permitted post-PR transition writes the verified PR URL into the
    pre-existing Version History entry, then commits and pushes that one file.
    It intentionally does not invoke the full suite again for that metadata
    insertion.
    """
    root = Path(project_root).resolve()
    if not root.is_dir():
        raise PublicReleaseError("project_root must be an existing directory")
    release_run_id = _non_empty_string(run_id, "run_id")
    parsed = _config(config)
    _require_hooks(hooks)
    version = _read_version(root)
    candidate_root = _inside(root, parsed.candidate_root, "config.candidate_root")
    if not candidate_root.is_dir():
        raise PublicReleaseError("config.candidate_root must be an existing directory")
    readme = _inside(root, parsed.readme_path, "config.readme_path")
    notes = _inside(root, parsed.notes_path, "config.notes_path")
    history = _inside(root, parsed.version_history_path, "config.version_history_path")
    if not readme.is_file() or not history.is_file():
        raise PublicReleaseError("configured README and Version History files must already exist")

    prompted = hooks.prompt(root, version, parsed.changes)
    if not isinstance(prompted, Mapping):
        raise PublicReleaseError("prompt hook must return a mapping")
    whats_new, whats_fixed, history_bullets = _prompt_result(prompted)
    body = _body(whats_new, whats_fixed)
    release_marker = f"<!-- public-release:{release_run_id} -->"
    if release_marker in readme.read_text(encoding="utf-8"):
        raise PublicReleaseError("run_id already appears in the configured README")
    history_marker = f"<!-- public-release:{release_run_id} -->"
    if history_marker in history.read_text(encoding="utf-8"):
        raise PublicReleaseError("run_id already appears in Version History")

    _write(notes, f"# Public release {version}\n\n{body}")
    _write(readme, readme.read_text(encoding="utf-8").rstrip() +
           f"\n\n{release_marker}\nLatest public release: **{version}**. See [{notes.name}]({parsed.notes_path}).\n")
    history_heading = f"## {version}"
    history_entry = "\n".join(f"- {bullet}" for bullet in history_bullets)
    _write(history, history.read_text(encoding="utf-8").rstrip() +
           f"\n\n{history_marker}\n{history_heading}\n{history_entry}\n")
    _journal(hooks, release_run_id, "documents_applied", version=version, paths=list(parsed.release_paths))

    _require_passed(hooks.test(root, candidate_root))
    _journal(hooks, release_run_id, "full_suite_passed", version=version)
    hooks.commit(root, parsed.release_paths, f"release: public v{version}")
    hooks.push(root, parsed.branch)
    pr = hooks.pr(root, parsed.branch, parsed.base, body)
    if not isinstance(pr, Mapping):
        raise PublicReleaseError("PR hook must return a mapping")
    url = _pr_url(pr)
    _journal(hooks, release_run_id, "pr_upserted", url=url)

    history_contents = history.read_text(encoding="utf-8")
    original = f"{history_marker}\n{history_heading}"
    finalized = f"{history_marker}\n{history_heading} [PR]({url})"
    if history_contents.count(original) != 1:
        raise PublicReleaseError("Version History entry changed before PR URL insertion")
    _write(history, history_contents.replace(original, finalized, 1))
    hooks.commit(root, (parsed.version_history_path,), f"docs: record public v{version} PR URL")
    hooks.push(root, parsed.branch)
    _journal(hooks, release_run_id, "published", url=url)
    return {
        "run_id": release_run_id,
        "version": version,
        "branch": parsed.branch,
        "base": parsed.base,
        "url": url,
        "status": "published",
    }
