# CA-M-500@10
# CA-D-672@20

"""Generate the deterministic Workbench schema asset from one Project capture."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

if __package__:
    from .source_reader import SourceReader
    from .workbench_schema_asset import compile_schema, schema_asset
else:  # pragma: no cover - direct image-build invocation
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from FEATURE_WORKBENCH_BACKEND.source_reader import SourceReader
    from FEATURE_WORKBENCH_BACKEND.workbench_schema_asset import (
        compile_schema,
        schema_asset,
    )


def compile_project_schema(project_root: Path) -> bytes:
    """Capture one Project and compile both admitted Workbench schema modes."""
    reader = SourceReader(Path(project_root))
    atoms, _scopes = reader.capture()
    content = reader.content_schema
    if content is None:
        raise ValueError("source capture did not compile a Content schema")
    header = reader.header_schema
    if header is None:
        raise ValueError("source capture did not compile a Header schema")
    return schema_asset(atoms, compile_schema(atoms, content, header))


def write_schema(output: Path, data: bytes) -> None:
    """Write the caller-selected generated-asset target."""
    Path(output).write_bytes(data)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args(argv)
    write_schema(args.output, compile_project_schema(args.project_root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
