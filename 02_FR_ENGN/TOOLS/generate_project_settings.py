#!/usr/bin/env python3
"""Generate Project Settings and its source Map from active RMED authority."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
import tempfile
import tomllib
import uuid
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


sys.pycache_prefix = str(
    Path(__file__).resolve().parents[2] / ".caprmedio_runtime/cache/python"
)
TOOLS_ROOT = Path(__file__).resolve().parent
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))

from native_atom_revision import current_reference as native_atom_reference  # noqa: E402
from work_journal import append_record, event_record  # noqa: E402


CONTROL_ROOT = Path(".caprmedio")
TARGET = CONTROL_ROOT / "caprmedio_project_settings.toml"
FRAMEWORK_SETTINGS = Path("caprmedio_framework_settings.toml")
GENERATOR = Path(__file__).resolve().relative_to(
    Path(__file__).resolve().parents[2]
)
SOURCE_MAP = CONTROL_ROOT / "08_implementation/CAPRMEDIO-MAPS-001--project-settings-source-map.yaml"
GENERATOR_VERSION = 2
INACTIVE_FOLDERS = {"archive", "drafts", "done", "solved", "handled"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--session-id")
    parser.add_argument("root", nargs="?", default=".")
    return parser.parse_args()


def repository_root(start: Path) -> Path:
    for candidate in (start.resolve(), *start.resolve().parents):
        if (candidate / CONTROL_ROOT).is_dir() and (candidate / FRAMEWORK_SETTINGS).is_file():
            return candidate
    raise RuntimeError("cannot locate CAPRMEDIO project root")


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def atom_reference(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    version = re.findall(r"(?m)^version:\s*([1-9][0-9]*)\s*$", text)
    updated_at = re.findall(r"(?m)^updated_at:\s*([0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2})\s*$", text)
    if len(version) != 1 or len(updated_at) != 1:
        raise RuntimeError(f"{path}: missing or ambiguous Atom revision metadata")
    return f"{path.stem}@{version[0]},{updated_at[0]}"


def parse_yaml_scalar(path: Path, line_number: int, value: str) -> Any:
    if not value or value != value.strip() or "\t" in value:
        raise RuntimeError(f"{path}:{line_number}: invalid YAML scalar")
    if value == "true":
        return True
    if value == "false":
        return False
    if re.fullmatch(r"-?[0-9]+", value):
        return int(value)
    if not re.fullmatch(r"[A-Za-z0-9_./:@, -]+", value):
        raise RuntimeError(f"{path}:{line_number}: unsupported plain YAML scalar")
    return value


def parse_yaml_block(path: Path, lines: list[str], index: int, indent: int) -> tuple[dict[str, Any] | list[Any], int]:
    if index >= len(lines):
        raise RuntimeError(f"{path}: unexpected end of YAML")
    list_mode = lines[index][indent:].startswith("- ")
    container: dict[str, Any] | list[Any] = [] if list_mode else {}
    while index < len(lines):
        line = lines[index]
        actual_indent = len(line) - len(line.lstrip(" "))
        if actual_indent < indent:
            break
        if actual_indent != indent or actual_indent % 2:
            raise RuntimeError(f"{path}:{index + 1}: invalid YAML indentation")
        content = line[indent:]
        if list_mode:
            if not content.startswith("- ") or not content[2:]:
                raise RuntimeError(f"{path}:{index + 1}: expected non-empty YAML list item")
            assert isinstance(container, list)
            container.append(parse_yaml_scalar(path, index + 1, content[2:]))
            index += 1
            continue
        if content.startswith("- ") or ":" not in content:
            raise RuntimeError(f"{path}:{index + 1}: expected YAML mapping entry")
        key, value = content.split(":", 1)
        if not re.fullmatch(r"[a-z0-9_]+", key) or (value and not value.startswith(" ")):
            raise RuntimeError(f"{path}:{index + 1}: unsupported YAML mapping syntax")
        assert isinstance(container, dict)
        if key in container:
            raise RuntimeError(f"{path}:{index + 1}: duplicate YAML key")
        index += 1
        if value:
            container[key] = parse_yaml_scalar(path, index, value[1:])
            continue
        if index >= len(lines):
            raise RuntimeError(f"{path}:{index}: missing YAML child block")
        child_indent = len(lines[index]) - len(lines[index].lstrip(" "))
        if child_indent != indent + 2:
            raise RuntimeError(f"{path}:{index + 1}: expected one YAML indentation level")
        child, index = parse_yaml_block(path, lines, index, child_indent)
        container[key] = child
    if isinstance(container, list):
        rendered = [json.dumps(value, ensure_ascii=False, sort_keys=True) for value in container]
        if len(rendered) != len(set(rendered)):
            raise RuntimeError(f"{path}: duplicate project_settings list item")
    return container, index


def frontmatter_project_settings(path: Path) -> dict[str, Any] | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    boundary = text.find("\n---\n", 4)
    if boundary < 0:
        raise RuntimeError(f"{path}: unterminated YAML frontmatter")
    lines = text[4:boundary].splitlines()
    starts = [index for index, line in enumerate(lines) if line == "project_settings:"]
    if not starts:
        return None
    if len(starts) != 1:
        raise RuntimeError(f"{path}: duplicate project_settings blocks")
    if len(re.findall(r"(?m)^version: [1-9][0-9]*$", text[4:boundary])) != 1:
        raise RuntimeError(f"{path}: project_settings is permitted only on an Atom with one version")
    start = starts[0]
    end = start + 1
    while end < len(lines) and lines[end].startswith("  "):
        end += 1
    child_lines = [line[2:] for line in lines[start + 1:end]]
    if not child_lines or any(not line or "\t" in line or line.rstrip() != line for line in child_lines):
        raise RuntimeError(f"{path}: empty or malformed project_settings block")
    document, index = parse_yaml_block(path, child_lines, 0, 0)
    if index != len(child_lines) or not isinstance(document, dict) or not document:
        raise RuntimeError(f"{path}: project_settings must be one non-empty YAML map")
    return document


def active_rmed_atoms(root: Path) -> list[Path]:
    paths = []
    for path in (root / CONTROL_ROOT).rglob("*.md"):
        relative_parts = path.relative_to(root / CONTROL_ROOT).parts
        if INACTIVE_FOLDERS.intersection(relative_parts):
            continue
        paths.append(path)
    return sorted(paths, key=lambda item: item.as_posix())


def flatten_values(path: Path, node: dict[str, Any] | list[Any] | Any, prefix: tuple[str, ...] = ()) -> dict[str, Any]:
    if isinstance(node, dict):
        if not node:
            raise RuntimeError(f"{path}: empty project_settings map")
        flattened: dict[str, Any] = {}
        for key, child in node.items():
            flattened.update(flatten_values(path, child, (*prefix, key)))
        return flattened
    if not prefix:
        raise RuntimeError(f"{path}: project_settings requires a mapping root")
    if isinstance(node, list) and not node:
        raise RuntimeError(f"{path}: empty project_settings list")
    return {".".join(prefix): node}


def extract_contributions(root: Path) -> dict[str, list[tuple[str, str, Any]]]:
    contributions: dict[str, list[tuple[str, str, Any]]] = {}
    for path in active_rmed_atoms(root):
        document = frontmatter_project_settings(path)
        if document is None:
            continue
        reference = atom_reference(path)
        for setting, value in flatten_values(path, document).items():
            if setting == "projection" or setting.startswith("projection."):
                raise RuntimeError(f"{path}: projection is reserved output metadata")
            contributions.setdefault(setting, []).append((path.stem, reference, value))
    if not contributions:
        raise RuntimeError("no active RMED project_settings contributions found")
    return contributions


def compose(contributions: dict[str, list[tuple[str, str, Any]]]) -> tuple[dict[str, Any], dict[str, list[str]], list[str]]:
    values: dict[str, Any] = {}
    bindings: dict[str, list[str]] = {}
    frontier: set[str] = set()
    for setting, entries in sorted(contributions.items()):
        ordered = sorted(entries, key=lambda entry: entry[0])
        if len(ordered) == 1:
            value = ordered[0][2]
        else:
            if any(not isinstance(entry[2], list) for entry in ordered):
                raise RuntimeError(f"{setting}: scalar settings require exactly one contributor")
            value = []
            seen: set[str] = set()
            for _, _, fragment in ordered:
                for item in fragment:
                    marker = json.dumps(item, ensure_ascii=False, sort_keys=True)
                    if marker in seen:
                        raise RuntimeError(f"{setting}: duplicate composed list item {item!r}")
                    seen.add(marker)
                    value.append(item)
        values[setting] = value
        bindings[setting] = [entry[1] for entry in ordered]
        frontier.update(bindings[setting])
    if "schema_version" not in values or not isinstance(values["schema_version"], str):
        raise RuntimeError("schema_version requires exactly one string RMED contribution")
    return values, bindings, sorted(frontier)


def nested_bindings(bindings: dict[str, list[str]]) -> dict[str, Any]:
    root: dict[str, Any] = {}
    for dotted, value in sorted(bindings.items()):
        cursor = root
        parts = dotted.split(".")
        for part in parts[:-1]:
            child = cursor.setdefault(part, {})
            if not isinstance(child, dict):
                raise RuntimeError(f"binding path collision at {dotted}")
            cursor = child
        if parts[-1] in cursor:
            raise RuntimeError(f"duplicate binding path at {dotted}")
        cursor[parts[-1]] = value
    return root


def toml_value(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, list):
        return "[" + ", ".join(toml_value(item) for item in value) + "]"
    raise TypeError(f"unsupported TOML value: {value!r}")


def render_yaml_scalar(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str) and "\n" not in value and "\t" not in value:
        return value
    raise RuntimeError(f"unsupported Map YAML scalar: {value!r}")


def render_yaml_node(node: dict[str, Any] | list[Any], indent: int) -> list[str]:
    prefix = " " * indent
    if isinstance(node, list):
        return [f"{prefix}- {render_yaml_scalar(item)}" for item in node]
    lines: list[str] = []
    for key in sorted(node):
        child = node[key]
        if isinstance(child, (dict, list)):
            lines.append(f"{prefix}{key}:")
            lines.extend(render_yaml_node(child, indent + 2))
        else:
            lines.append(f"{prefix}{key}: {render_yaml_scalar(child)}")
    return lines


def state_digest(values: dict[str, Any], bindings: dict[str, list[str]], configuration_artifact: str, configuration_sha256: str, generator_sha256: str) -> str:
    payload = {
        "values": values,
        "bindings": bindings,
        "configuration_artifact": configuration_artifact,
        "configuration_sha256": configuration_sha256,
        "generator": GENERATOR.as_posix(),
        "generator_sha256": generator_sha256,
    }
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return sha256_bytes(encoded)


def render_source_map(bindings: dict[str, list[str]], frontier: list[str], frontier_sha256: str, generator_sha256: str, updated_at: str) -> str:
    document: dict[str, Any] = {
        "bindings": nested_bindings(bindings),
        "generator": GENERATOR.as_posix(),
        "generator_sha256": generator_sha256,
        "schema_version": 1,
        "source_frontier": frontier,
        "source_frontier_sha256": frontier_sha256,
        "updated_at": updated_at,
    }
    return "\n".join(render_yaml_node(document, 0)) + "\n"


def render_settings(values: dict[str, Any], bindings: dict[str, list[str]], frontier: list[str], frontier_sha256: str, configuration_artifact: str, generator_sha256: str, configuration_sha256: str, source_map_sha256: str, updated_at: str) -> str:
    tables: dict[str, dict[str, Any]] = {}
    for dotted, value in values.items():
        if dotted == "schema_version":
            continue
        table, separator, key = dotted.rpartition(".")
        if not separator or not table or not key:
            raise RuntimeError(f"{dotted}: non-schema settings require a TOML table")
        if key in tables.setdefault(table, {}):
            raise RuntimeError(f"duplicate TOML setting {dotted}")
        tables[table][key] = value
    lines = [
        "# Generated CAPRMEDIO Project Settings Projection.",
        "# Direct edits do not establish project authority.",
        "",
        f"schema_version = {toml_value(values['schema_version'])}",
        "",
        "[projection]",
        f"updated_at = {toml_value(updated_at)}",
        f"generator = {toml_value(GENERATOR.as_posix())}",
        f"generator_version = {GENERATOR_VERSION}",
        f"generator_sha256 = {toml_value(generator_sha256)}",
        f"source_map = {toml_value(SOURCE_MAP.as_posix())}",
        f"source_map_sha256 = {toml_value(source_map_sha256)}",
        f"configuration = {toml_value(FRAMEWORK_SETTINGS.as_posix())}",
        f"configuration_artifact = {toml_value(configuration_artifact)}",
        f"configuration_sha256 = {toml_value(configuration_sha256)}",
        f"source_frontier_sha256 = {toml_value(frontier_sha256)}",
        "source_frontier = [",
    ]
    lines.extend(f"  {toml_value(reference)}," for reference in frontier)
    lines.extend(["]", "", "[projection.bindings]"])
    for key in sorted(bindings):
        lines.append(f"{toml_value(key)} = {toml_value(bindings[key])}")
    for table in sorted(tables):
        lines.extend(["", f"[{table}]"])
        for key in sorted(tables[table]):
            lines.append(f"{key} = {toml_value(tables[table][key])}")
    return "\n".join(lines).rstrip() + "\n"


def governed_timestamp(values: dict[str, Any]) -> str:
    value = values.get("artifact_timestamps.timezone", "local")
    if value == "local":
        moment = dt.datetime.now().astimezone()
    elif value == "UTC":
        moment = dt.datetime.now(dt.UTC)
    elif isinstance(value, str):
        try:
            moment = dt.datetime.now(ZoneInfo(value))
        except ZoneInfoNotFoundError as error:
            raise RuntimeError(f"unknown Artifact timestamp timezone: {value}") from error
    else:
        raise RuntimeError("artifact_timestamps.timezone must be a string")
    return moment.strftime("%Y-%m-%d %H:%M:%S")


def previous_timestamp(root: Path, values: dict[str, Any]) -> str:
    target = root / TARGET
    if target.is_file():
        try:
            value = tomllib.loads(target.read_text(encoding="utf-8")).get("projection", {}).get("updated_at")
        except (tomllib.TOMLDecodeError, OSError):
            value = None
        if isinstance(value, str) and re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}", value):
            return value
    return governed_timestamp(values)


def prepare_temp(path: Path, payload: bytes) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    with os.fdopen(descriptor, "wb") as handle:
        handle.write(payload)
        handle.flush()
        os.fsync(handle.fileno())
    return temporary


def replace_pair(outputs: list[tuple[Path, bytes]]) -> None:
    prepared = [(path, prepare_temp(path, payload)) for path, payload in outputs]
    previous = [(path, path.read_bytes() if path.exists() else None) for path, _ in outputs]
    replaced: list[Path] = []
    try:
        for path, temporary in prepared:
            os.replace(temporary, path)
            replaced.append(path)
    except BaseException:
        for path, payload in reversed(previous):
            if path not in replaced:
                continue
            if payload is None:
                path.unlink(missing_ok=True)
            else:
                rollback = prepare_temp(path, payload)
                os.replace(rollback, path)
        raise
    finally:
        for _, temporary in prepared:
            try:
                os.unlink(temporary)
            except FileNotFoundError:
                pass


def main() -> int:
    args = parse_args()
    if args.apply and not args.session_id:
        raise RuntimeError("--session-id is required with --apply")
    root = repository_root(Path(args.root))
    values, bindings, frontier = compose(extract_contributions(root))
    configuration_artifact = native_atom_reference(root, "framework-settings")
    configuration_sha256 = sha256(root / FRAMEWORK_SETTINGS)
    generator_sha256 = sha256(root / GENERATOR)
    frontier_sha256 = state_digest(values, bindings, configuration_artifact, configuration_sha256, generator_sha256)
    timestamp = previous_timestamp(root, values)
    source_map = render_source_map(bindings, frontier, frontier_sha256, generator_sha256, timestamp)
    source_map_sha256 = sha256_bytes(source_map.encode())
    settings = render_settings(values, bindings, frontier, frontier_sha256, configuration_artifact, generator_sha256, configuration_sha256, source_map_sha256, timestamp)
    map_changed = not (root / SOURCE_MAP).is_file() or (root / SOURCE_MAP).read_text(encoding="utf-8") != source_map
    settings_changed = not (root / TARGET).is_file() or (root / TARGET).read_text(encoding="utf-8") != settings
    changed = map_changed or settings_changed
    if changed:
        timestamp = governed_timestamp(values)
        source_map = render_source_map(bindings, frontier, frontier_sha256, generator_sha256, timestamp)
        source_map_sha256 = sha256_bytes(source_map.encode())
        settings = render_settings(values, bindings, frontier, frontier_sha256, configuration_artifact, generator_sha256, configuration_sha256, source_map_sha256, timestamp)
    print(f"sources={len(frontier)} bindings={len(bindings)} map_changed={str(map_changed).lower()} settings_changed={str(settings_changed).lower()} changed={str(changed).lower()} apply={str(args.apply).lower()}")
    if args.apply and changed:
        action_id = str(uuid.uuid4())
        common = {
            "root": root,
            "action_id": action_id,
            "kind": "projection_rebuild",
            "scope": "project",
            "operation": "generate_project_settings",
            "session_id": args.session_id,
            "subjects": [configuration_artifact, *frontier],
        }
        started = event_record(event="started", outputs=[], preceding_event=None, details={"generator": GENERATOR.as_posix(), "frontier": frontier_sha256}, occurred_at=timestamp, **common)
        append_record(root, started)
        try:
            replace_pair([(root / SOURCE_MAP, source_map.encode()), (root / TARGET, settings.encode())])
        except BaseException:
            append_record(root, event_record(event="failed", outputs=[], preceding_event=str(started["event_id"]), details={"frontier": frontier_sha256}, occurred_at=timestamp, **common))
            raise
        append_record(root, event_record(event="completed", outputs=[SOURCE_MAP.as_posix(), TARGET.as_posix()], preceding_event=str(started["event_id"]), details={"frontier": frontier_sha256, "updated_at": timestamp}, occurred_at=timestamp, **common))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
