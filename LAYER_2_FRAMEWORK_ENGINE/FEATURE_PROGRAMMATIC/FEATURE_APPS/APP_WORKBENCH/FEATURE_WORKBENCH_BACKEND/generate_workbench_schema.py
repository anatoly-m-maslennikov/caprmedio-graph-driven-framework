# CA-M-500@11
# CA-D-672@21

"""Generate the deterministic Workbench schema asset from one Project capture."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

if __package__:
    from .content_schema import _is_declaration, content_schema_from_statements, declaration_statements
    from .declared_header_rules import header_rules_from_statements
    from .header_columns import declared_header_schema
    from .source_reader import SourceReader
    from .source_selection import first_reference_rows
    from .workbench_schema_asset import compile_schema, compile_status_groups, schema_asset
else:  # pragma: no cover - direct image-build invocation
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from FEATURE_WORKBENCH_BACKEND.content_schema import _is_declaration, content_schema_from_statements, declaration_statements
    from FEATURE_WORKBENCH_BACKEND.declared_header_rules import header_rules_from_statements
    from FEATURE_WORKBENCH_BACKEND.header_columns import declared_header_schema
    from FEATURE_WORKBENCH_BACKEND.source_reader import SourceReader
    from FEATURE_WORKBENCH_BACKEND.source_selection import first_reference_rows
    from FEATURE_WORKBENCH_BACKEND.workbench_schema_asset import (
        compile_schema,
        compile_status_groups,
        schema_asset,
    )

from role_directory_rules import compile_role_folders


def compile_project_schema(project_root: Path) -> bytes:
    """Capture one Project and compile both admitted Workbench schema modes."""
    reader = SourceReader(Path(project_root), include_archived=False)
    atoms, _scopes = reader.capture()
    pins = {row["source_path"]: row for row in atoms}
    statements = []
    for row in first_reference_rows(reader.model_rows(atoms, _is_declaration)):
        claim = declaration_statements(row)
        if claim:
            statements.extend(claim)
            pins[row["source_path"]] = row
    content = content_schema_from_statements(statements)
    header = declared_header_schema(header_rules_from_statements(statements))
    folders = compile_role_folders(statements)
    role_folders = tuple(sorted((role, folder) for role, (folder, _source) in folders.items())) if folders else None
    return schema_asset(list(pins.values()), compile_schema(atoms, content, header, compile_status_groups(statements), role_folders))


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
