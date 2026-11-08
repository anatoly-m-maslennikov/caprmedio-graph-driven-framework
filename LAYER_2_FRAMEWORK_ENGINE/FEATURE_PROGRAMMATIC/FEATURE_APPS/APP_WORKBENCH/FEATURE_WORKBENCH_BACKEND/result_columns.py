# CA-D-673@15
# CA-M-493@2
# CA-D-697@2

"""Column visibility over the complete stored result, independent of pagination."""

from .graph_store import quote_identifier


def _has_value(name: str, kind: str) -> str:
    column = quote_identifier(name)
    present = f"{column} IS NOT NULL"
    if kind == "VARCHAR" or kind.startswith("ENUM("):
        present += f" AND {column}::VARCHAR != ''"
    elif kind == "JSON":
        present += f" AND json({column})::VARCHAR NOT IN ('null', '\"\"', '[]', '{{}}')"
    elif kind.endswith("]"):
        present += f" AND len({column}) > 0"
    elif kind.startswith("MAP("):
        present += f" AND cardinality({column}) > 0"
    return f"count(*) FILTER (WHERE {present}) > 0"


def result_columns(
    connection, table: str, columns: list[dict], *, private_ordinal: bool = False,
) -> tuple[list[dict], int]:
    # CTAS may rename duplicate aliases; bind counts by physical column position.
    stored_names = connection.sql(f"SELECT * FROM workbench_results.{table}").columns
    if private_ordinal:
        stored_names = stored_names[1:]
    counts = ", ".join(_has_value(name, column["type"])
                       for name, column in zip(stored_names, columns, strict=True))
    result = connection.execute(
        f"SELECT count(*), {counts} FROM workbench_results.{table}"
    ).fetchone()
    row_count, *has_values = result
    return [dict(column, has_values=row_count == 0 or present)
            for column, present in zip(columns, has_values, strict=True)], row_count
