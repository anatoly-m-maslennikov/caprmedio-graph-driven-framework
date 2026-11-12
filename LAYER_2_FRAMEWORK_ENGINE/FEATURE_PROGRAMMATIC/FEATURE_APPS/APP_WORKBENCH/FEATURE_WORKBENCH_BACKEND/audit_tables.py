# CA-R-970308648@1
# CA-R-970308649@1
# CA-R-970308650@1
# CA-M-549@1
# CA-D-715@2
"""Query-visible diagnostics derived from the selected Atom source scan."""

from __future__ import annotations

from pathlib import Path
import os
import re
import sys
from typing import AbstractSet, Any, Iterable, Mapping

from .errors import WorkbenchUnavailableError
from .content_schema import ContentSchema, _declared_children, _records_by_path, _value
from .markdown_content import content_lines, source_markdown
from .source_inventory import filename_candidate, filename_role_matches, filename_marker

TOOLS = Path(__file__).resolve().parents[3] / "FEATURE_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from header_groups import header_value  # noqa: E402
from artifact_metadata import atom_identifier  # noqa: E402


PARSE_ISSUES = "atom_parse_issues"
SCHEMA_ISSUES = "atom_schema_issues"
DECLARED_CARRIER_ISSUES = "atom_declared_carrier_issues"
PHYSICAL_CARRIER_ISSUES = "atom_physical_carrier_issues"
TABLES = (PARSE_ISSUES, SCHEMA_ISSUES, DECLARED_CARRIER_ISSUES,
          PHYSICAL_CARRIER_ISSUES, "atom_duplicate_revision_issues")
COLUMNS = ("reference", "relative_path", "filename", "issue_category", "property", "observed", "expected", "diagnostic")


def create_tables(connection: Any) -> None:
    for table in TABLES:
        connection.execute(f"DROP TABLE IF EXISTS main.{table}")
        connection.execute(f"CREATE TABLE main.{table} ({', '.join(f'{name} VARCHAR' for name in COLUMNS)})")


def _clear(connection: Any, paths: tuple[str, ...] | None) -> None:
    """Replace only changed source diagnostics; a full scan replaces all audit tables."""
    for table in TABLES:
        if paths is None:
            connection.execute(f"DELETE FROM main.{table}")
        elif paths:
            connection.execute(
                f"DELETE FROM main.{table} WHERE (relative_path, filename) IN "
                "(SELECT unnest(?::VARCHAR[]), unnest(?::VARCHAR[]))",
                [[Path(path).parent.as_posix() for path in paths], [Path(path).name for path in paths]],
            )


def _insert(connection: Any, issues: Mapping[str, list[tuple[str | None, ...]]]) -> None:
    for table in TABLES:
        rows = issues.get(table, [])
        if rows:
            connection.execute(
                f"INSERT INTO main.{table} SELECT " + ", ".join("unnest(?::VARCHAR[])" for _ in COLUMNS),
                [[row[index] for row in rows] for index in range(len(COLUMNS))],
            )


def publish(connection: Any, issues: Mapping[str, list[tuple[str | None, ...]]] | Iterable[Mapping[str, list[tuple[str | None, ...]]]],
            paths: Iterable[str] | None, *, available: bool) -> None:
    if not available:
        raise WorkbenchUnavailableError("query store unavailable; Workbench restart required")
    try:
        connection.execute("BEGIN TRANSACTION")
        selected = None if paths is None else tuple(paths)
        affected = _affected_revisions(connection, selected) if selected is not None else None
        _clear(connection, selected)
        for batch in (issues,) if isinstance(issues, Mapping) else issues:
            _insert(connection, batch)
        _refresh_revision_issues(connection, affected)
        connection.execute("COMMIT")
    except Exception as error:
        connection.execute("ROLLBACK")
        raise WorkbenchUnavailableError("Atom audit refresh failed") from error


def revision_query(connection: Any, *, stable_only: bool = True) -> str:
    columns = {row[0] for row in connection.execute(
        "SELECT column_name FROM information_schema.columns WHERE table_schema='main' AND table_name='atoms'"
    ).fetchall()}
    ids = [f'try_cast("{name}" AS VARCHAR)' for name in ("header.identity.atom_id", "header.identity.id", "header.atom_id") if name in columns]
    versions = [f'try_cast("{name}" AS BIGINT)' for name in (
        "header.state.version", "header.state.version_number", "header.version", "header.version_number"
    ) if name in columns]
    identity = "coalesce(" + ", ".join([*ids, "reference"]) + ")"
    suffix = "try_cast(nullif(regexp_extract(reference, '@([1-9][0-9]*)(-draft)?$', 1), '') AS BIGINT)"
    version = "coalesce(" + ", ".join([*versions, suffix]) + ")"
    return (
        "SELECT reference, relative_path, filename, "
        f"regexp_replace({identity}, '@[1-9][0-9]*(-draft)?$', '') AS atom_id, "
        f"{version} AS version FROM main.atoms"
        + (" WHERE status_group IN ('Current', 'Archived')" if stable_only else "")
    )


def _affected_revisions(connection: Any, paths: tuple[str, ...]) -> set[tuple[str, int]]:
    if not paths:
        return set()
    arguments = [[Path(path).parent.as_posix() for path in paths], [Path(path).name for path in paths]]
    path_filter = "(relative_path, filename) IN (SELECT unnest(?::VARCHAR[]), unnest(?::VARCHAR[]))"
    previous = connection.execute(
        f"SELECT observed, try_cast(expected AS BIGINT) FROM main.atom_duplicate_revision_issues "
        f"WHERE issue_category = 'duplicate_atom_revision' AND {path_filter}", arguments,
    ).fetchall()
    current = connection.execute(
        f"SELECT atom_id, version FROM ({revision_query(connection)}) WHERE {path_filter}", arguments,
    ).fetchall()
    return {(identity, version) for identity, version in [*previous, *current]
            if identity is not None and version is not None}


def _refresh_revision_issues(connection: Any, affected: set[tuple[str, int]] | None) -> None:
    if affected is not None and not affected:
        return
    arguments: list[Any] = []
    restriction = ""
    if affected is not None:
        keys = sorted(affected)
        arguments = [[identity for identity, _ in keys], [version for _, version in keys]]
        connection.execute(
            "DELETE FROM main.atom_duplicate_revision_issues WHERE issue_category = 'duplicate_atom_revision' "
            "AND (observed, try_cast(expected AS BIGINT)) IN "
            "(SELECT unnest(?::VARCHAR[]), unnest(?::BIGINT[]))", arguments,
        )
        restriction = "AND (atom_id, version) IN (SELECT unnest(?::VARCHAR[]), unnest(?::BIGINT[]))"
    connection.execute(
        f"INSERT INTO main.atom_duplicate_revision_issues "
        f"WITH revisions AS ({revision_query(connection)}), collisions AS ("
        "SELECT atom_id, version FROM revisions "
        "WHERE regexp_full_match(atom_id, '.+-[A-Z]-[0-9]+') AND version > 0 "
        f"{restriction} GROUP BY atom_id, version HAVING count(*) > 1) "
        "SELECT revisions.reference, revisions.relative_path, revisions.filename, "
        "'duplicate_atom_revision', 'atom_id,version', revisions.atom_id, "
        "cast(revisions.version AS VARCHAR), 'Multiple Atom files share this Atom ID and Version.' "
        "FROM revisions JOIN collisions USING (atom_id, version)", arguments,
    )


def collect_issues(
    root: Path, control_root: Path, source_paths: AbstractSet[Path], selected: set[str] | None,
    cached: Mapping[Path, tuple[Any, dict[str, Any]]], diagnostics: Mapping[Path, str],
    accepted: AbstractSet[Path], scopes: Iterable[dict[str, Any]], project_scope_id: str,
    schema: ContentSchema | None, public_atoms: Mapping[tuple[str, str], Mapping[str, Any]],
    role_folders=None, schema_audit=None, placement_audit=None, schema_invalid=frozenset(),
) -> dict[str, list[tuple[str | None, ...]]]:
    scope_paths = {
        key: item["authority_path"] for item in scopes
        for key in (item["scope_unit_name"], item["scope_unit_id"]) if isinstance(key, str)
    }
    scope_paths[project_scope_id] = control_root.relative_to(root).as_posix()
    paths = source_paths if selected is None else {root / path for path in selected}
    result: dict[str, list[tuple[str | None, ...]]] = {table: [] for table in TABLES}
    layouts: dict[tuple[str | None, str | None], dict[tuple[str, ...], str]] = {}
    prefix = re.escape(project_scope_id.removesuffix("-SU-00"))
    atom_name = re.compile(rf"(?:[1-9][0-9]*-)?{prefix}-[A-Z]-[0-9]+")
    for path in sorted(paths & source_paths):
        row = cached.get(path, (None, None))[1]
        relative = path.relative_to(root)
        public = public_atoms.get((relative.parent.as_posix(), path.name))
        diagnostic = diagnostics.get(path)
        if row is None and path not in schema_invalid and not atom_name.match(path.name):
            continue
        issues = issues_for_source(relative.as_posix(), row, diagnostic,
                                   scope_paths=scope_paths, role_folders=role_folders,
                                   schema_error=path in schema_invalid, schema_audit=schema_audit,
                                   placement_audit=placement_audit)
        if (row is not None and row.get("status_group") != "Archived" and path in accepted
                and not issues[SCHEMA_ISSUES] and not diagnostic):
            issues[SCHEMA_ISSUES].extend(_content_issues(relative, row, schema, public, layouts))
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
    *, scope_paths: Mapping[str, str], role_folders=None, schema_error=False,
    schema_audit=None, placement_audit=None,
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

    if diagnostic:
        if schema_error:
            add(SCHEMA_ISSUES, "schema_invalid", None, None, None, diagnostic)
        else:
            add(PARSE_ISSUES, "parse_failed", None, None, None, diagnostic)
        return result
    if row is None:
        return result
    if error := row.get("_source_schema_error"):
        add(SCHEMA_ISSUES, "schema_invalid", None, None, None, str(error))
        return result
    if schema_audit is not None:
        for issue in schema_audit(row):
            add(SCHEMA_ISSUES, "schema_invalid", issue["field"], issue.get("observed"),
                issue.get("expected"), issue["message"])
        if result[SCHEMA_ISSUES]:
            return result
    _placement_issues(row, file, scope_paths, role_folders, placement_audit, add, result)
    return result


def _placement_issues(row, file, scope_paths, role_folders, placement_audit, add, result):
    header = row.get("header_json")
    if not isinstance(header, dict):
        return
    _, destination = header_value(header, "destination")
    declared = destination.get("file") if isinstance(destination, dict) else None
    declared = declared if isinstance(declared, dict) else {}
    declared_path = declared.get("path")
    expected_name, expected_path = placement_audit(row) if placement_audit is not None else (None, None)
    if expected_name is not None and declared.get("name") != expected_name:
        add(DECLARED_CARRIER_ISSUES, "declared_carrier_inconsistency", "file.name", declared.get("name"),
            expected_name, "Declared filename differs from the placement formula.")
    elif expected_name is None and (issue := _declared_filename_issue(declared.get("name"), declared_path, row, role_folders)):
        add(DECLARED_CARRIER_ISSUES, "declared_carrier_inconsistency", *issue)
    _, container = header_value(header, "container")
    owner = container.get("scope_unit") if isinstance(container, dict) else None
    owner_path = scope_paths.get(owner) if isinstance(owner, str) else None
    if expected_path is not None and declared_path != expected_path:
        add(DECLARED_CARRIER_ISSUES, "declared_carrier_inconsistency", "file.path", declared_path,
            expected_path, "Declared path differs from the placement formula.")
    elif expected_path is None and owner_path is not None and isinstance(declared_path, str) and not Path(os.path.normpath(declared_path)).is_relative_to(Path(os.path.normpath(owner_path))):
        add(DECLARED_CARRIER_ISSUES, "declared_carrier_inconsistency", "file.path", declared_path, owner_path,
            "Declared carrier path is outside its owning Scope Unit.")
    if not result[DECLARED_CARRIER_ISSUES]:
        for key, actual in (("name", file.name), ("path", file.parent.as_posix())):
            expected = declared.get(key)
            if expected != actual:
                add(PHYSICAL_CARRIER_ISSUES, "physical_carrier_mismatch", f"file.{key}", actual, expected,
                    f"Actual carrier {key} differs from its declaration.")


def _declared_filename_issue(
    name: object, declared_path: object, row: Mapping[str, Any], role_folders=None,
) -> tuple[str, object, object, str] | None:
    declared = Path(declared_path) / name if isinstance(declared_path, str) and isinstance(name, str) else None
    if declared is not None and filename_candidate(declared) and not filename_role_matches(declared, role_folders):
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
    sql = ("SELECT " + ", ".join('"' + c.replace('"', '""') + '"' for c in columns)
           + " FROM main.atoms WHERE status_group <> 'Archived'")
    args = []
    if paths is not None:
        sql += ' AND ("relative_path", filename) IN (SELECT unnest(?::VARCHAR[]), unnest(?::VARCHAR[]))'
        args = [[Path(p).parent.as_posix() for p in paths], [Path(p).name for p in paths]]
    return {(row[0], row[1]): dict(zip(names, row[2:])) for row in connection.execute(sql, args).fetchall()}
