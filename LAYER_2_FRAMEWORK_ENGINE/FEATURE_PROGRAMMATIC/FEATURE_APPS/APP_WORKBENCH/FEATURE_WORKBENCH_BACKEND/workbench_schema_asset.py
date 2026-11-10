# CA-R-2726@6
# CA-M-500@3
# CA-D-672@14

"""Compile and validate the delivered, source-derived Workbench schema asset."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
from typing import Any

from .content_schema import ContentSchema, DeclarationSource
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

    def header(self, mode: int) -> HeaderSchema:
        if mode == 1:
            return self.mode_one
        if mode == 2:
            return self.mode_two
        raise ValueError("workbench.schema_mode must be 1 or 2")


def compile_schema(
    atoms: list[dict[str, Any]], content: ContentSchema, declared_header: HeaderSchema | None = None,
) -> SchemaCompilation:
    """Build both projections from the one accepted source capture."""
    return SchemaCompilation(
        declared_header or declared_header_schema(compile_header_rules(atoms)),
        infer_header_schema(atoms), content,
    )


def schema_asset(
    atoms: list[dict[str, Any]], compilation: SchemaCompilation,
) -> bytes:
    """Serialize a deterministic schema asset without retaining source bodies."""
    payload: dict[str, Any] = {
        "schema_version": 1,
        "modes": {
            "1": {"header": compilation.mode_one.asset(), "content": compilation.content.asset()},
            "2": {"header": compilation.mode_two.asset(), "content": compilation.content.asset()},
        },
        "sources": sorted((_source_pin(row) for row in atoms), key=lambda source: source["path"]),
    }
    payload["input_digest"] = hashlib.sha256(canonical(payload).encode("utf-8")).hexdigest()
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"


def load_schema_asset(
    path: Path, atoms: list[dict[str, Any]], compilation: SchemaCompilation,
) -> SchemaCompilation | None:
    """Consume a delivered schema only when it exactly matches current source inputs."""
    try:
        if path.is_symlink() or not path.is_file():
            return None
        raw = path.read_bytes()
        if raw != schema_asset(atoms, compilation):
            return None
        payload = json.loads(raw)
        modes = payload["modes"]
        return SchemaCompilation(
            _header_schema(modes["1"]["header"]),
            _header_schema(modes["2"]["header"]),
            compilation.content,
        )
    except (KeyError, OSError, TypeError, UnicodeError, ValueError, json.JSONDecodeError):
        return None


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
    return HeaderRule(
        tuple(path), format_name, roles, forms,
        DeclarationSource(reference, version, source_path),
    )


def _selector(value: object) -> frozenset[str] | None:
    if value is None:
        return None
    if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
        raise ValueError("invalid delivered Header declaration selector")
    return frozenset(value)


def header_schema(atoms, content, declared_header, mode):
    """Prefer the build asset when it matches the source declarations."""
    compilation = compile_schema(atoms, content, declared_header)
    delivered = load_schema_asset(DEFAULT_SCHEMA_PATH, atoms, compilation)
    return (delivered or compilation).header(mode)
