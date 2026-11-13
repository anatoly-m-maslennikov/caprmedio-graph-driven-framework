# CA-R-2729@8
# CA-R-2776@7
# CA-D-673@15
# CA-R-2728@8

"""Validate caret metadata while DuckDB admits one complete query."""

from __future__ import annotations

from typing import Any


def _utf8(sql: str) -> bytes:
    if not isinstance(sql, str):
        raise ValueError("SQL must be a string")
    try:
        return sql.encode("utf-8")
    except UnicodeEncodeError as error:
        raise ValueError("SQL must be valid UTF-8") from error


def _utf8_offset(sql: str, cursor_position: int) -> int:
    if isinstance(cursor_position, bool) or not isinstance(cursor_position, int):
        raise ValueError("cursor_position must be a UTF-16 integer")
    if cursor_position < 0:
        raise ValueError("cursor_position must be a UTF-16 integer")
    units = 0
    byte_offset = 0
    for character in sql:
        if units == cursor_position:
            return byte_offset
        width = 2 if ord(character) > 0xFFFF else 1
        units += width
        byte_offset += len(character.encode("utf-8"))
        if units > cursor_position:
            raise ValueError("cursor_position must be a UTF-16 boundary")
    if units == cursor_position:
        return byte_offset
    raise ValueError("cursor_position is outside SQL")


def token_spans(sql: str) -> list[tuple[bytes, Any]]:
    """Return native DuckDB tokens with their UTF-8 byte slices."""
    import duckdb

    raw = _utf8(sql)
    tokens = duckdb.tokenize(sql)
    return [
        (raw[position:tokens[index + 1][0] if index + 1 < len(tokens) else len(raw)], token_type)
        for index, (position, token_type) in enumerate(tokens)
    ]


def select_statement(sql: str, cursor_position: int | None = None) -> str:
    """Return the complete SQL; an optional caret is editor metadata only."""
    _utf8(sql)
    if cursor_position is not None:
        _utf8_offset(sql, cursor_position)
    return sql
