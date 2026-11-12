# CA-R-2726@6
# CA-M-500@11
# CA-D-672@21

"""Compile and validate the delivered, source-derived Workbench schema asset."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import re
from pathlib import Path
from typing import Any

from .content_schema import ContentRule, ContentSchema, DeclarationSource, _schema_from_rules
from .declared_header_rules import HeaderRule, compile_header_rules
from .header_columns import HeaderColumn, HeaderSchema, declared_header_schema, infer_header_schema
from .relations import canonical


DEFAULT_SCHEMA_PATH = Path(__file__).with_name("workbench_schema.json")


@dataclass(frozen=True)
class SchemaCompilation:
    """The two admitted Header modes plus one declared Content schema."""

    mode_one: HeaderSchema
    mode_two: HeaderSchema
    content: ContentSchema
    status_groups: tuple[tuple[str, str, str], ...] = ()
    role_folders: tuple[tuple[str, str], ...] | None = None

    def header(self, mode: int) -> HeaderSchema:
        if mode == 1:
            return self.mode_one
        if mode == 2:
            return self.mode_two
        raise ValueError("workbench.schema_mode must be 1 or 2")


def compile_schema(
    atoms: list[dict[str, Any]], content: ContentSchema, declared_header: HeaderSchema | None = None,
    status_groups: tuple[tuple[str, str, str], ...] = (),
    role_folders: tuple[tuple[str, str], ...] | None = None,
) -> SchemaCompilation:
    """Build both projections from the one accepted source capture."""
    return SchemaCompilation(
        declared_header or declared_header_schema(compile_header_rules(atoms)),
        infer_header_schema(atoms), content, status_groups, role_folders,
    )


_STATUS_GROUP = re.compile(
    r'Atom/\(\.Header\.(?:Context\.)?Role\s*:=\s*([A-Za-z][A-Za-z0-9 _-]*)\)'
    r'/\(\.Header\.(?:State\.)?Status\s*:=\s*([A-Za-z][A-Za-z0-9 _-]*)\)'
    r'\.Header\.(?:State\.)?Status\s*>\|\s*Status Group\s*==\s*([A-Za-z][A-Za-z0-9 _-]*)\s*'
)


def compile_status_groups(statements) -> tuple[tuple[str, str, str], ...]:
    groups = {}
    for statement, _source in statements:
        match = _STATUS_GROUP.fullmatch(statement)
        if match:
            role, status, group = (part.strip() for part in match.groups())
            previous = groups.setdefault((role, status), group)
            if previous != group:
                raise ValueError(f"conflicting Status Groups for {role}/{status}")
    return tuple(sorted((role, status, group) for (role, status), group in groups.items()))


def schema_asset(
    atoms: list[dict[str, Any]], compilation: SchemaCompilation,
) -> bytes:
    """Serialize a deterministic schema asset without retaining source bodies."""
    payload: dict[str, Any] = {
        "schema_version": 2,
        "modes": {
            "1": {"header": compilation.mode_one.asset(), "content": _content_asset(compilation.content)},
            "2": {"header": compilation.mode_two.asset(), "content": _content_asset(compilation.content)},
        },
        "sources": sorted((_source_pin(row) for row in atoms), key=lambda source: source["path"]),
    }
    if compilation.status_groups:
        payload["schema_version"] = 3
        payload["status_groups"] = [list(row) for row in compilation.status_groups]
    if compilation.role_folders is not None:
        payload["schema_version"] = 4
        payload["status_groups"] = [list(row) for row in compilation.status_groups]
        payload["role_folders"] = [list(row) for row in compilation.role_folders]
    payload["input_digest"] = hashlib.sha256(canonical(payload).encode("utf-8")).hexdigest()
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"


def _content_asset(schema: ContentSchema) -> dict[str, object]:
    payload = schema.asset()
    payload["rules"] = [
        {
            "path": list(rule.path),
            "roles": sorted(rule.roles) if rule.roles is not None else None,
            "forms": sorted(rule.forms) if rule.forms is not None else None,
            "value_bearing": rule.value_bearing,
            "prohibited": rule.prohibited,
            "source": rule.source.asset(),
            "provenance": [source.asset() for source in rule.provenance],
        }
        for rule in schema.rules
    ]
    return payload


def load_image_schema(path: Path = DEFAULT_SCHEMA_PATH) -> SchemaCompilation:
    """Load and validate the self-contained schema delivered in the image.

    This checks the asset itself, never the current source tree. A missing or
    invalid image asset is an error and requires rebuilding the image.
    """
    try:
        if path.is_symlink() or not path.is_file():
            raise ValueError("schema asset is missing or is a symlink")
        payload = json.loads(path.read_bytes())
        if not isinstance(payload, dict) or set(payload) not in ({"schema_version", "modes", "sources", "input_digest"}, {"schema_version", "modes", "sources", "input_digest", "status_groups"}, {"schema_version", "modes", "sources", "input_digest", "status_groups", "role_folders"}):
            raise ValueError("invalid schema asset shape")
        digest = payload.pop("input_digest")
        if not isinstance(digest, str) or digest != hashlib.sha256(canonical(payload).encode("utf-8")).hexdigest():
            raise ValueError("schema asset digest mismatch")
        if (type(payload["schema_version"]) is not int or payload["schema_version"] not in (2, 3, 4)
                or (payload["schema_version"] >= 3) != ("status_groups" in payload)
                or (payload["schema_version"] == 4) != ("role_folders" in payload)):
            raise ValueError("unsupported schema asset version")
        groups = payload.get("status_groups", [])
        if (not isinstance(groups, list) or any(not isinstance(row, list) or len(row) != 3
                or any(not isinstance(value, str) or not value for value in row) for row in groups)
                or groups != sorted(groups) or len({tuple(row[:2]) for row in groups}) != len(groups)):
            raise ValueError("invalid Status Groups")
        folders = payload.get("role_folders")
        if folders is not None and (not isinstance(folders, list) or any(
                not isinstance(row, list) or len(row) != 2 or any(not isinstance(value, str) or not value for value in row)
                for row in folders) or folders != sorted(folders)
                or len({row[0] for row in folders}) != len(folders) or len({row[1] for row in folders}) != len(folders)):
            raise ValueError("invalid Role folders")
        _validate_source_pins(payload["sources"])
        modes = payload["modes"]
        if not isinstance(modes, dict) or set(modes) != {"1", "2"}:
            raise ValueError("invalid schema modes")
        if any(not isinstance(mode, dict) or set(mode) != {"header", "content"} for mode in modes.values()):
            raise ValueError("invalid schema mode")
        content = _content_schema(modes["1"]["content"])
        if modes["2"]["content"] != _content_asset(content):
            raise ValueError("inconsistent content schemas")
        headers = [_header_schema(modes[mode]["header"]) for mode in ("1", "2")]
        if any(headers[index].asset() != modes[mode]["header"] for index, mode in enumerate(("1", "2"))):
            raise ValueError("invalid header schema shape")
        return SchemaCompilation(headers[0], headers[1], content, tuple(map(tuple, groups)),
                                 None if folders is None else tuple(map(tuple, folders)))
    except (OSError, KeyError, TypeError, UnicodeError, ValueError) as exc:
        raise ValueError(f"invalid delivered Workbench schema: {exc}") from exc


def _validate_source_pins(value: object) -> None:
    sources = value
    if not isinstance(sources, list):
        raise ValueError("invalid schema source pins")
    for source in sources:
        if (not isinstance(source, dict) or set(source) != {"atom_id", "version", "path", "fingerprint"}
            or source["atom_id"] is not None and (not isinstance(source["atom_id"], str) or not source["atom_id"])
            or source["version"] is not None and (type(source["version"]) is not int or source["version"] < 1)
            or not isinstance(source["path"], str) or not source["path"]
            or not isinstance(source["fingerprint"], str) or len(source["fingerprint"]) != 64
            or any(c not in "0123456789abcdef" for c in source["fingerprint"])):
            raise ValueError("invalid schema source pin")
    if sources != sorted(sources, key=lambda source: source["path"]):
        raise ValueError("invalid schema source pin order")


def _content_schema(payload: object) -> ContentSchema:
    if not isinstance(payload, dict) or not isinstance(payload.get("rules"), list):
        raise ValueError("invalid delivered Content schema")
    rules = []
    for item in payload["rules"]:
        if not isinstance(item, dict) or set(item) != {"path", "roles", "forms", "value_bearing", "prohibited", "source", "provenance"}:
            raise ValueError("invalid delivered Content rule")
        path = item["path"]
        if (not isinstance(path, list) or not path or not all(isinstance(part, str) and part for part in path)
            or type(item["value_bearing"]) is not bool or type(item["prohibited"]) is not bool
            or not isinstance(item["provenance"], list)):
            raise ValueError("invalid delivered Content rule")
        source = _content_source(item["source"])
        provenance = tuple(_content_source(value) for value in item["provenance"])
        if len(set(provenance)) != len(provenance):
            raise ValueError("duplicate delivered Content provenance")
        rules.append(ContentRule(tuple(path), _selector(item["roles"]), _selector(item["forms"]),
                                 item["value_bearing"], source, item["prohibited"], provenance))
    schema = _schema_from_rules(rules)
    if _content_asset(schema) != payload:
        raise ValueError("invalid delivered Content schema shape")
    return schema


def _content_source(value: object) -> DeclarationSource:
    if not isinstance(value, dict) or set(value) != {"reference", "version", "source_path"}:
        raise ValueError("invalid delivered Content source")
    reference, version, source_path = value["reference"], value["version"], value["source_path"]
    if (reference is not None and not isinstance(reference, str)
        or version is not None and (type(version) is not int or version < 1)
        or source_path is not None and not isinstance(source_path, str)):
        raise ValueError("invalid delivered Content source")
    return DeclarationSource(reference, version, source_path)


def _source_pin(row: dict[str, Any]) -> dict[str, Any]:
    body = row.get("_content_bytes")
    path = row.get("source_path")
    atom_id = row.get("id")
    version = row.get("version")
    if not isinstance(body, bytes):
        raise ValueError(f"{path}: captured Markdown is unavailable")
    if not isinstance(path, str) or not path:
        raise ValueError("schema source pin needs a source path")
    return {
        "atom_id": atom_id if isinstance(atom_id, str) and atom_id else None,
        "version": version if type(version) is int and version > 0 else None,
        "path": path,
        "fingerprint": hashlib.sha256(canonical({
            "header": row.get("header_json"), "body_sha256": hashlib.sha256(body).hexdigest(),
        }).encode("utf-8")).hexdigest(),
    }


def _header_schema(payload: object) -> HeaderSchema:
    if not isinstance(payload, dict) or payload.get("version") != 1:
        raise ValueError("invalid delivered Header schema")
    columns = payload.get("header_columns")
    if not isinstance(columns, list):
        raise ValueError("invalid delivered Header columns")
    result = []
    for item in columns:
        if not isinstance(item, dict):
            raise ValueError("invalid delivered Header column")
        path = item.get("path")
        name = item.get("name")
        format_name = item.get("format")
        populated = item.get("populated")
        reader = item.get("reader")
        if (
            not isinstance(path, list) or not path or not all(isinstance(part, str) and part for part in path)
            or not isinstance(name, str) or not name.startswith("header.")
            or not isinstance(format_name, str) or type(populated) is not bool
            or reader is not None and not isinstance(reader, str)
        ):
            raise ValueError("invalid delivered Header column")
        rules = item.get("rules", [])
        if not isinstance(rules, list):
            raise ValueError("invalid delivered Header rules")
        result.append(HeaderColumn(
            tuple(path), name, format_name, populated, reader,
            tuple(_header_rule(rule) for rule in rules),
        ))
    return HeaderSchema(tuple(result))


def _header_rule(payload: object) -> HeaderRule:
    if not isinstance(payload, dict):
        raise ValueError("invalid delivered Header declaration rule")
    path = payload.get("path")
    format_name = payload.get("format")
    roles = _selector(payload.get("roles"))
    forms = _selector(payload.get("forms"))
    source = payload.get("source")
    if (
        not isinstance(path, list) or not path or not all(isinstance(part, str) and part for part in path)
        or not isinstance(format_name, str) or not isinstance(source, dict)
    ):
        raise ValueError("invalid delivered Header declaration rule")
    reference = source.get("reference")
    version = source.get("version")
    source_path = source.get("source_path")
    if (
        reference is not None and not isinstance(reference, str)
        or version is not None and (type(version) is not int or version < 1)
        or source_path is not None and not isinstance(source_path, str)
    ):
        raise ValueError("invalid delivered Header declaration source")
    raw_provenance = payload.get("provenance")
    if not isinstance(raw_provenance, list):
        raise ValueError("invalid delivered Header provenance")
    provenance = tuple(_content_source(value) for value in raw_provenance)
    if len(set(provenance)) != len(provenance):
        raise ValueError("duplicate delivered Header provenance")
    format_source = payload.get("format_source")
    if format_source is not None:
        if not isinstance(format_source, dict) or set(format_source) != {"reference", "version", "source_path"}:
            raise ValueError("invalid delivered Header format source")
        format_reference, format_version, format_path = (
            format_source["reference"], format_source["version"], format_source["source_path"]
        )
        if (format_reference is not None and not isinstance(format_reference, str)
            or format_version is not None and (type(format_version) is not int or format_version < 1)
            or format_path is not None and not isinstance(format_path, str)):
            raise ValueError("invalid delivered Header format source")
        format_source = DeclarationSource(format_reference, format_version, format_path)
    return HeaderRule(
        tuple(path), format_name, roles, forms,
        DeclarationSource(reference, version, source_path), format_source, provenance,
    )


def _selector(value: object) -> frozenset[str] | None:
    if value is None:
        return None
    if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
        raise ValueError("invalid delivered Header declaration selector")
    return frozenset(value)
