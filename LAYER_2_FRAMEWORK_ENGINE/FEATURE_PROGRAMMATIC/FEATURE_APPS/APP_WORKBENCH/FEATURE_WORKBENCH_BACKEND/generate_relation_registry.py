# CA-M-509@1
# CA-D-705@1

"""Generate the deterministic relation-registry asset from one Project capture."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
from typing import Any

if __package__:
    from .relation_registry import RegistryCompilation, compile_registry, is_registry_declaration
    from .relations import canonical
    from .source_reader import SourceReader
else:  # pragma: no cover - direct build-hook invocation
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from FEATURE_WORKBENCH_BACKEND.relation_registry import (
        RegistryCompilation,
        compile_registry,
        is_registry_declaration,
    )
    from FEATURE_WORKBENCH_BACKEND.relations import canonical
    from FEATURE_WORKBENCH_BACKEND.source_reader import SourceReader


DEFAULT_REGISTRY_PATH = Path(__file__).with_name("canonical_relation_registry.json")


def _source_pin(row: dict[str, Any]) -> dict[str, Any]:
    body = row.get("_content_bytes")
    if not isinstance(body, bytes):
        raise ValueError(f"{row.get('source_path')}: captured Markdown is unavailable")
    source = row.get("source_path")
    atom_id = row.get("id")
    version = row.get("version")
    if not isinstance(source, str) or not source:
        raise ValueError("registry source pin needs a source path")
    if not isinstance(atom_id, str) or not atom_id:
        raise ValueError(f"{source}: registry source pin needs an Atom ID")
    if type(version) is not int or version <= 0:
        raise ValueError(f"{source}: registry source pin needs a positive integer Version")
    return {
        "atom_id": atom_id,
        "version": version,
        "path": source,
        "fingerprint": hashlib.sha256(
            canonical(
                {
                    "header": row.get("header_json"),
                    "body_sha256": hashlib.sha256(body).hexdigest(),
                }
            ).encode("utf-8")
        ).hexdigest(),
    }


def registry_asset(
    atoms: list[dict[str, Any]], compilation: RegistryCompilation | None = None,
) -> bytes:
    """Serialize the captured registry compiler output without retaining source bytes."""
    compiled = compile_registry(atoms) if compilation is None else compilation
    registry = compiled.registry
    sources = sorted(
        (_source_pin(row) for row in compiled.declaration_rows),
        key=lambda source: source["path"],
    )
    payload = {
        "schema_version": 1,
        "registered_names": sorted(registry.names),
        "inverse_bindings": [
            {"direct": direct, "inverse": inverse}
            for direct, inverse in sorted(registry.inverse.items())
        ],
        "inverse_aliases": [
            {"alias": alias, "canonical": canonical_name}
            for alias, canonical_name in sorted(registry.aliases.items())
        ],
        "sources": sources,
    }
    payload["input_digest"] = hashlib.sha256(canonical(payload).encode("utf-8")).hexdigest()
    return (
        json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode("utf-8")


def compile_project_registry(project_root: Path) -> bytes:
    """Capture one Project and compile its current relation registry as JSON bytes."""
    reader = SourceReader(Path(project_root))
    atoms, _scopes = reader.capture()
    return registry_asset(reader.model_rows(atoms, is_registry_declaration))


def write_registry(output: Path, data: bytes) -> None:
    """Write one explicit generated-asset target."""
    Path(output).write_bytes(data)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args(argv)
    write_registry(args.output, compile_project_registry(args.project_root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
