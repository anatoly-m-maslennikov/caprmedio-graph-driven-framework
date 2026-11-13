# CA-R-2729@11
# CA-M-516@2
# CA-D-673@18
"""Export already-materialized query rows to disposable Project files."""

from __future__ import annotations

from collections.abc import Iterable, Iterator, Sequence
from contextlib import contextmanager
import csv
import json
import os
from pathlib import Path
import sys
from typing import Any, TextIO
import uuid

import toon_format

from .result_values import result_value

TOOLS = Path(__file__).resolve().parents[3] / "FEATURE_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
from project_runtime import _validate_directory_components  # noqa: E402


_RELATIVE_DIRECTORY = Path(".caprmedio_tmp/workbench/query_results")
_EXTENSIONS = {"json_matrix": "json", "csv": "csv", "toon": "toon"}


@contextmanager
def _directory_fd(root: Path) -> Iterator[int]:
    """Keep directory traversal beneath the selected root, including during races."""
    directory = root / _RELATIVE_DIRECTORY
    _validate_directory_components(root, directory)
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    descriptor = os.open(root, flags)
    try:
        for part in _RELATIVE_DIRECTORY.parts:
            try:
                os.mkdir(part, dir_fd=descriptor)
            except FileExistsError:
                pass
            child = os.open(part, flags, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = child
        yield descriptor
    finally:
        os.close(descriptor)


def _encoded_rows(rows: Iterable[Sequence[Any]], width: int) -> Iterator[list[Any]]:
    for row in rows:
        if not isinstance(row, Sequence) or isinstance(row, (str, bytes)) or len(row) != width:
            raise ValueError("result row width does not match column count")
        yield [result_value(value) for value in row]


def _write_json(stream: TextIO, columns: list[str], rows: Iterator[list[Any]]) -> int:
    stream.write('{"columns":')
    json.dump(columns, stream, ensure_ascii=False, separators=(",", ":"))
    stream.write(',"rows":[')
    count = 0
    for row in rows:
        if count:
            stream.write(",")
        json.dump(row, stream, ensure_ascii=False, separators=(",", ":"), allow_nan=False)
        count += 1
    stream.write("]}")
    return count


def _write_csv(stream: TextIO, columns: list[str], rows: Iterator[list[Any]]) -> int:
    writer = csv.writer(stream, quoting=csv.QUOTE_NOTNULL, lineterminator="\r\n")
    writer.writerow(columns)
    count = 0
    for row in rows:
        writer.writerow(
            [
                json.dumps(value, ensure_ascii=False, separators=(",", ":"))
                if isinstance(value, (list, dict))
                else value
                for value in row
            ]
        )
        count += 1
    return count


def write_result_file(
    project_root: Path | str,
    columns: Sequence[str],
    rows: Iterable[Sequence[Any]],
    *,
    result_format: str = "json_matrix",
    offset: int = 0,
    has_more: bool = False,
) -> dict[str, Any]:
    """Write column names and positional rows; the caller owns query execution and paging."""
    if (
        not isinstance(columns, Sequence)
        or isinstance(columns, (str, bytes))
        or any(not isinstance(name, str) for name in columns)
    ):
        raise ValueError("columns must be a sequence of names")
    if not isinstance(result_format, str) or result_format not in _EXTENSIONS:
        raise ValueError("unsupported result format")
    if type(offset) is not int or offset < 0 or type(has_more) is not bool:
        raise ValueError("invalid result page metadata")
    names = list(columns)
    if not Path(project_root).is_absolute():
        raise ValueError("Project root must be an absolute selected path")
    root = Path(project_root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError("Project root must be a directory")
    filename = f"{uuid.uuid7()}.{_EXTENSIONS[result_format]}"
    with _directory_fd(root) as directory:
        flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW
        file_descriptor = os.open(filename, flags, 0o644, dir_fd=directory)
        try:
            with os.fdopen(file_descriptor, "w", encoding="utf-8", newline="") as stream:
                encoded_rows = _encoded_rows(rows, len(names))
                if result_format == "json_matrix":
                    count = _write_json(stream, names, encoded_rows)
                elif result_format == "csv":
                    count = _write_csv(stream, names, encoded_rows)
                else:
                    matrix = list(encoded_rows)
                    stream.write(toon_format.dumps({"columns": names, "rows": matrix}))
                    count = len(matrix)
        except BaseException:
            os.unlink(filename, dir_fd=directory)
            raise
    return {
        "path": (_RELATIVE_DIRECTORY / filename).as_posix(),
        "format": result_format,
        "row_count": count,
        "column_count": len(names),
        "offset": offset,
        "has_more": has_more,
    }
