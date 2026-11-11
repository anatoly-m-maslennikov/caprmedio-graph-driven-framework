# CA-R-970308648@1
# CA-R-970308649@1
# CA-R-970308650@1
# CA-M-549@1
# CA-D-715@2
"""Query-visible diagnostics derived from the selected Atom source scan."""

from __future__ import annotations

from pathlib import Path
import os
import sys
from typing import Any, Iterable, Mapping

from .errors import WorkbenchUnavailableError
from .content_schema import ContentSchema, _declared_children, _records_by_path, _value
from .markdown_content import content_lines, source_markdown
from .source_inventory import filename_candidate, filename_role_matches, filename_marker

TOOLS = Path(__file__).resolve().parents[3] / "FEATURE_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from header_groups import header_value  # noqa: E402
from artifact_metadata import atom_identifier  # noqa: E402


TABLES = ("atom_content_issues", "atom_declared_carrier_issues", "atom_physical_carrier_issues")
COLUMNS = ("reference", "relative_path", "filename", "issue_category", "property", "observed", "expected", "diagnostic")


def create_tables(connection: Any) -> None:
    for table in TABLES:
        connection.execute(f"DROP TABLE IF EXISTS main.{table}")
        connection.execute(f"CREATE TABLE main.{table} ({', '.join(f'{name} VARCHAR' for name in COLUMNS)})")


def update_tables(
    connection: Any, issues: Mapping[str, list[tuple[str | None, ...]]],
    *, paths: Iterable[str] | None,
) -> None:
    """Replace only changed source diagnostics; a full scan replaces all three tables."""
    selected = None if paths is None else tuple(paths)
    for table in TABLES:
        if selected is None:
            connection.execute(f"DELETE FROM main.{table}")
        elif selected:
            connection.execute(
                f"DELETE FROM main.{table} WHERE (relative_path, filename) IN "
                "(SELECT unnest(?::VARCHAR[]), unnest(?::VARCHAR[]))",
                [[Path(path).parent.as_posix() for path in selected], [Path(path).name for path in selected]],
            )
        rows = issues.get(table, [])
        if rows:
            connection.execute(
                f"INSERT INTO main.{table} SELECT " + ", ".join("unnest(?::VARCHAR[])" for _ in COLUMNS),
                [[row[index] for row in rows] for index in range(len(COLUMNS))],
            )


def publish(connection: Any, issues: Mapping[str, list[tuple[str | None, ...]]],
            paths: Iterable[str] | None, *, available: bool) -> None:
    if not available:
        raise WorkbenchUnavailableError("query store unavailable; Workbench restart required")
    try:
        connection.execute("BEGIN TRANSACTION")
        update_tables(connection, issues, paths=paths)
        connection.execute("COMMIT")
    except Exception as error:
        connection.execute("ROLLBACK")
        raise WorkbenchUnavailableError("Atom audit refresh failed") from error


def collect_issues(
    root: Path, control_root: Path, source_paths: set[Path], selected: set[str] | None,
    cached: Mapping[Path, tuple[Any, dict[str, Any]]], diagnostics: Mapping[Path, str],
    accepted: set[Path], scopes: Iterable[dict[str, Any]], project_scope_id: str,
    schema: ContentSchema | None, public_atoms: Mapping[tuple[str, str], Mapping[str, Any]],
) -> dict[str, list[tuple[str | None, ...]]]:
    scope_paths = {
        key: item["authority_path"] for item in scopes
        for key in (item["scope_unit_name"], item["scope_unit_id"]) if isinstance(key, str)
    }
    scope_paths[project_scope_id] = control_root.relative_to(root).as_posix()
    paths = source_paths if selected is None else {root / path for path in selected}
    result: dict[str, list[tuple[str | None, ...]]] = {table: [] for table in TABLES}
    layouts: dict[tuple[str | None, str | None], dict[tuple[str, ...], str]] = {}
    for path in sorted(paths & source_paths):
        row = cached.get(path, (None, None))[1]
        relative = path.relative_to(root)
        public = public_atoms.get((relative.parent.as_posix(), path.name))
        issues = issues_for_source(path.relative_to(root).as_posix(), row, diagnostics.get(path),
                                   accepted=path in accepted, scope_paths=scope_paths)
        if row is not None and path in accepted and not diagnostics.get(path):
            issues[TABLES[0]].extend(_content_issues(relative, row, schema, public, layouts))
        for table, records in issues.items():
            result[table].extend(records)
    return result


def _content_issues(
    path: Path, row: Mapping[str, Any], schema: ContentSchema | None, public: Mapping[str, Any] | None,
    layouts: dict[tuple[str | None, str | None], dict[tuple[str, ...], str]],
) -> list[tuple[str | None, ...]]:
    reference = row.get("ref") if isinstance(row.get("ref"), str) else None
    prefix = (reference, path.parent.as_posix(), path.name, "query_inaccessible_atom")
    if public is None:
        return [(*prefix, None, None, None, "Accepted Atom source has no queryable row.")]
    if schema is None:
        return []
    role = row.get("role") if isinstance(row.get("role"), str) else None
    form = row.get("form") if isinstance(row.get("form"), str) else None
    key = (role, form)
    if key not in layouts:
        layouts[key] = {
            rule.path: "content." + ".".join(rule.path)
            for rule in schema.rules if rule.value_bearing and rule.applies(row)
            and not any(part in {"*", "**"} for part in rule.path)
        }
    records = row.get("content_properties_json")
    if not isinstance(records, list):
        return []
    present = {
        tuple(record["property_path"]) for record in records if isinstance(record, dict)
        and isinstance(record.get("property_path"), list)
        and all(isinstance(part, str) for part in record["property_path"])
    }
    candidates = [
        (column_path, name) for column_path, name in layouts[key].items()
        if (column_path in present or column_path[-1:] == ("prose_claim",) and column_path[:-1] in present)
    ]
    if not candidates:
        return []
    records_by_path = _records_by_path(records)
    body = source_markdown(row)
    lines = content_lines(body) if body is not None else None
    result = []
    for column_path, name in candidates:
        expected = _value(records_by_path, column_path, True, _declared_children(schema.rules, column_path, row), lines)
        actual = public.get(name)
        if actual != expected:
            result.append((*prefix, name, _text(actual), _text(expected),
                           "Declared Content differs from the query projection."))
    return result



def issues_for_source(
    path: str, row: Mapping[str, Any] | None, diagnostic: str | None,
    *, accepted: bool, scope_paths: Mapping[str, str],
) -> dict[str, list[tuple[str | None, ...]]]:
    result: dict[str, list[tuple[str | None, ...]]] = {table: [] for table in TABLES}
    file = Path(path)
    relative = file.parent.as_posix()
    reference = row.get("ref") if row else None
    reference = reference if isinstance(reference, str) else None

    def add(table: str, category: str, property: str | None, observed: object,
            expected: object, message: str) -> None:
        result[table].append((reference, relative, file.name, category, property,
                              _text(observed), _text(expected), message))

    if diagnostic or row is not None and not accepted:
        add(TABLES[0], "query_inaccessible_atom", None, None, None,
            diagnostic or "Source has a duplicate Atom reference.")
        return result
    if row is None:
        return result
    header = row.get("header_json")
    if not isinstance(header, dict):
        return result
    _, destination = header_value(header, "destination")
    declared = destination.get("file") if isinstance(destination, dict) else None
    declared = declared if isinstance(declared, dict) else {}
    for key, actual in (("name", file.name), ("path", relative)):
        expected = declared.get(key)
        if expected != actual:
            add(TABLES[2], "physical_carrier_mismatch", f"file.{key}", actual, expected,
                f"Actual carrier {key} differs from its declaration.")

    declared_path = declared.get("path")
    if issue := _declared_filename_issue(declared.get("name"), declared_path, row):
        add(TABLES[1], "declared_carrier_inconsistency", *issue)
    _, container = header_value(header, "container")
    owner = container.get("scope_unit") if isinstance(container, dict) else None
    owner_path = scope_paths.get(owner) if isinstance(owner, str) else None
    if owner_path is not None and isinstance(declared_path, str) and not Path(os.path.normpath(declared_path)).is_relative_to(Path(os.path.normpath(owner_path))):
        add(TABLES[1], "declared_carrier_inconsistency", "file.path", declared_path, owner_path,
            "Declared carrier path is outside its owning Scope Unit.")
    return result


def _declared_filename_issue(
    name: object, declared_path: object, row: Mapping[str, Any],
) -> tuple[str, object, object, str] | None:
    declared = Path(declared_path) / name if isinstance(declared_path, str) and isinstance(name, str) else None
    if declared is not None and filename_candidate(declared) and not filename_role_matches(declared):
        return ("file.name", name, declared_path,
                "The declared filename role conflicts with its declared role directory.")
    if not isinstance(name, str):
        return None
    identity = row.get("id")
    if isinstance(identity, str) and atom_identifier(identity) == identity and identity.startswith("CA-"):
        if atom_identifier(name) != identity:
            return "file.name", name, identity, "Declared filename identifies a different Atom."
    role = row.get("role")
    marker = filename_marker(Path(name))
    if marker and isinstance(role, str) and role and marker != role[0].upper():
        return "file.name", name, role, "Declared filename role conflicts with Header Role."
    return None


def _text(value: object) -> str | None:
    return None if value is None else str(value)


def query_content_rows(connection: Any, paths: set[str] | None) -> dict[tuple[str, str], dict[str, Any]]:
    """Read actual projected values for only affected source paths."""
    if paths is not None and not paths:
        return {}
    names = [row[0] for row in connection.execute(
        "SELECT column_name FROM information_schema.columns WHERE table_schema='main' AND table_name='atoms'"
    ).fetchall() if row[0].startswith("content.")]
    columns = ["relative_path", "filename", *names]
    sql = "SELECT " + ", ".join('"' + c.replace('"', '""') + '"' for c in columns) + " FROM main.atoms"
    args = []
    if paths is not None:
        sql += ' WHERE ("relative_path", filename) IN (SELECT unnest(?::VARCHAR[]), unnest(?::VARCHAR[]))'
        args = [[Path(p).parent.as_posix() for p in paths], [Path(p).name for p in paths]]
    return {(row[0], row[1]): dict(zip(names, row[2:])) for row in connection.execute(sql, args).fetchall()}
