# CA-R-2726@6
# CA-M-500@3
# CA-D-672@14

"""Narrow literal-CFEL primitives shared by declared Content and Header schemas."""

from __future__ import annotations

from collections.abc import Sequence
import re

from .markdown_content import content_key


ROLE_SETS = {"RMED": frozenset({"Requirement", "Method", "Evaluation", "Delivery"})}


def model_statements(body: str) -> list[str]:
    lines = body.splitlines()
    model_start = next((index for index, line in enumerate(lines) if line.strip().casefold() == "# model"), None)
    if model_start is None:
        return []
    model_lines = []
    for line in lines[model_start + 1 :]:
        if line.strip().startswith("#"):
            break
        model_lines.append(line)
    return [
        statement.strip()
        for statement in re.split(r";(?!>)", "\n".join(model_lines))
        if statement.strip()
    ]


def segments(tail: str) -> tuple[list[str], str]:
    result: list[str] = []
    index = 0
    while index < len(tail) and tail[index] == ".":
        index += 1
        end = _segment_end(tail, index)
        raw = tail[index:end].strip()
        if not raw:
            return [], tail[index:]
        result.append(raw if raw in {"*", "**"} else _key(raw))
        index = end
    return result, tail[index:]


def filters(prefix: str, field: str) -> frozenset[str] | None:
    groups = _filter_groups(prefix)
    _reject_unsupported_filters(groups)
    matches = [item for item in groups if _selector_field(item) == field]
    if not matches:
        return None
    values = [_filter_values(item, field) for item in matches]
    if len(values) != 1:
        raise ValueError(f"unsupported Content declaration: multiple Header.{field} filters")
    return values[0]


def allowed_children(remainder: str) -> tuple[str, ...]:
    match = re.search(r"\bin\s*\(([^)]*)\)", remainder)
    if match is None:
        return ()
    return tuple(_key(item.strip()) for item in match.group(1).split(",") if item.strip())


def container(remainder: str) -> bool:
    return bool(re.search(r"::\s*\[\s*\]", remainder))


def _segment_end(value: str, start: int) -> int:
    candidates = [len(value)]
    for token in (".", "[", "{", ";"):
        found = value.find(token, start)
        if found >= 0:
            candidates.append(found)
    colon = value.find("::", start)
    if colon >= 0:
        candidates.append(colon)
    return min(candidates)


def _key(value: str) -> str:
    try:
        return content_key(value)
    except ValueError as error:
        raise ValueError(f"Content declaration property has no usable key: {value!r}") from error


def _filter_groups(prefix: str) -> list[str]:
    groups: list[str] = []
    index = 0
    while True:
        start = prefix.find("/(" , index)
        if start < 0:
            return groups
        depth = 1
        end = start + 2
        while end < len(prefix) and depth:
            if prefix[end] == "(":
                depth += 1
            elif prefix[end] == ")":
                depth -= 1
            end += 1
        if depth:
            raise ValueError("unsupported Content declaration: unclosed Header filter")
        groups.append(prefix[start + 2 : end - 1].strip())
        index = end


def _reject_unsupported_filters(groups: Sequence[str]) -> None:
    for expression in groups:
        if _selector_field(expression, complete=True) is not None:
            continue
        known = re.match(r"\.Header\.(?:Context\.)?(Role|Form)\b", expression)
        if known is not None:
            raise ValueError(
                f"unsupported Content declaration Header.{known.group(1)} filter: {expression}"
            )
        raise ValueError(f"unsupported Content declaration selector: {expression}")


def _selector_field(expression: str, *, complete: bool = False) -> str | None:
    pattern = (
        r"\.Header\.(?:Context\.)?(Role|Form)\s*(in|:=|=|:)\s*.+"
        if complete else r"\.Header\.(?:Context\.)?(Role|Form)\b"
    )
    match = re.fullmatch(pattern, expression) if complete else re.match(pattern, expression)
    return match.group(1) if match is not None else None


def _filter_values(expression: str, field: str) -> frozenset[str]:
    match = re.fullmatch(
        rf"\.Header\.(?:Context\.)?{field}\s*(in|:=|=|:)\s*(.+)", expression,
    )
    if match is None:
        raise ValueError(f"unsupported Content declaration Header.{field} filter: {expression}")
    operator, value = match.groups()
    value = value.strip()
    if operator == "in" and field == "Role" and value in ROLE_SETS:
        return ROLE_SETS[value]
    if value.startswith("("):
        if not value.endswith(")"):
            raise ValueError(f"unsupported Content declaration Header.{field} filter: {expression}")
        items = value[1:-1].split(",")
    elif operator == "in":
        raise ValueError(f"unsupported Content declaration Header.{field} filter: {expression}")
    else:
        items = (value,)
    result = frozenset(_unquote(item.strip()) for item in items if item.strip())
    if not result:
        raise ValueError(f"unsupported Content declaration Header.{field} filter: {expression}")
    return result


def _unquote(value: str) -> str:
    return value[1:-1] if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'" else value
