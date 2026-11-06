# CA-R-2728@6
# CA-D-673@13

"""Admit one native read-only Workbench query without changing it."""

from __future__ import annotations

from .statements import token_spans


def is_duckdb_internal(error: Exception) -> bool:
    """Classify the native fatal boundary by exception type, never its message."""
    import duckdb

    return isinstance(error, duckdb.InternalException)


def is_one_tokenized_read_query(sql: str) -> bool:
    import duckdb

    try:
        spans = token_spans(sql)
    except Exception:
        return False
    words = [
        value.decode("utf-8").strip() for value, token_type in spans
        if token_type != duckdb.token_type.comment
    ]
    if not words:
        return False
    semicolons = [index for index, word in enumerate(words) if word == ";"]
    if semicolons and semicolons != [len(words) - 1]:
        return False
    return words[0].upper() in {"SELECT", "WITH", "FROM"}
