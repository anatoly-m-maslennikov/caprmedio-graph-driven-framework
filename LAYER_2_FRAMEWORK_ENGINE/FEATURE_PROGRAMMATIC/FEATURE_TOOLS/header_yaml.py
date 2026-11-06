"""Source-preserving scalar edits to declared grouped or historical Headers."""

# implementation of: CA-D-657

import json
from typing import Any

import yaml
from yaml.nodes import MappingNode, ScalarNode

from header_groups import header_field_paths, header_key_order, header_path
from header_yaml_nodes import _document, _metadata, _node
from header_yaml_nodes import header_scalar as header_scalar
from header_yaml_nodes import header_scalar_node as header_scalar_node
from header_yaml_nodes import parse_header as parse_header


def _line_start(text: str, position: int) -> int:
    return text.rfind("\n", 0, position) + 1


def _mapping_end(text: str, node: MappingNode) -> int:
    end = node.end_mark.index
    start = _line_start(text, end)
    return start if not text[start:end].strip() else end


def _insert(frontmatter: str, parent: MappingNode, path: tuple[str, ...], key: str, value: Any) -> str:
    newline = "\r\n" if "\r\n" in frontmatter else "\n"
    if parent.flow_style:
        position = parent.end_mark.index - 1
        addition = (", " if parent.value else "") + json.dumps(key) + ": " + json.dumps(value, ensure_ascii=False)
        return frontmatter[:position] + addition + frontmatter[position:]
    order = header_key_order(path)
    rank = order.index(key) if key in order else len(order)
    following = [node for node, _ in parent.value
                 if (order.index(node.value) if node.value in order else len(order)) > rank]
    position = _line_start(frontmatter, following[0].start_mark.index) if following else _mapping_end(frontmatter, parent)
    indent = parent.value[0][0].start_mark.column if parent.value else len(path) * 2
    rendered = yaml.safe_dump({key: value}, sort_keys=False, allow_unicode=True).rstrip("\n")
    addition = newline.join(" " * indent + line for line in rendered.splitlines())
    before = "" if position == 0 or frontmatter[position - 1] == "\n" else newline
    after = newline if position < len(frontmatter) or frontmatter.endswith("\n") else ""
    return frontmatter[:position] + before + addition + after + frontmatter[position:]


def _insert_path(frontmatter: str, document: MappingNode, path: tuple[str, ...], value: Any) -> str:
    parent = document
    for index, part in enumerate(path[:-1]):
        existing = _node(parent, (part,))
        if existing is None:
            for child in reversed(path[index + 1:]):
                value = {child: value}
            return _insert(frontmatter, parent, path[:index], part, value)
        if not isinstance(existing, MappingNode):
            raise ValueError("Header Property parent must be a mapping.")
        parent = existing
    return _insert(frontmatter, parent, path[:-1], path[-1], value)


def replace_header_scalar(frontmatter: str, name: str, value: str | int) -> str:
    """Replace actual scalar spans; missing fields follow the current Header layout."""
    if type(value) not in (str, int):
        raise ValueError("Header replacement must be a string or integer.")
    document = _document(frontmatter)
    metadata = _metadata(document)
    replacements = []
    for path in header_field_paths(name, metadata):
        node = _node(document, path)
        if node is not None:
            if not isinstance(node, ScalarNode):
                raise ValueError(f"Header {name} must be a scalar.")
            end = node.end_mark.index
            line_start = _line_start(frontmatter, end)
            if line_start > node.start_mark.index and not frontmatter[line_start:end].strip():
                end = line_start
            replacements.append((node.start_mark.index, end))
    rendered = (json.dumps(value, ensure_ascii=False) if name.split(".")[-1] == "updated_at" else
                yaml.safe_dump(value, allow_unicode=True, default_flow_style=True).removesuffix("...\n").rstrip("\n"))
    if not replacements:
        return _insert_path(frontmatter, document, header_path(name, metadata), value)
    for start, end in sorted(set(replacements), reverse=True):
        suffix = ("\r\n" if "\r\n" in frontmatter else "\n") if "\n" in frontmatter[start:end] else ""
        frontmatter = frontmatter[:start] + rendered + suffix + frontmatter[end:]
    return frontmatter


def _remove_path(frontmatter: str, document: MappingNode, path: tuple[str, ...]) -> str:
    parent = _node(document, path[:-1]) if len(path) > 1 else document
    if not isinstance(parent, MappingNode):
        raise ValueError("Header Property parent must be a mapping.")
    pair = next(((key, value) for key, value in parent.value if key.value == path[-1]), None)
    if pair is None:
        return frontmatter
    key, value = pair
    if len(parent.value) == 1 and len(path) > 1:
        return _remove_path(frontmatter, document, path[:-1])
    if parent.flow_style:
        index = parent.value.index(pair)
        start = key.start_mark.index
        end = value.end_mark.index
        if index + 1 < len(parent.value):
            end = parent.value[index + 1][0].start_mark.index
        elif index:
            previous = parent.value[index - 1][1].end_mark.index
            start = frontmatter.index(",", previous, start)
    else:
        start = _line_start(frontmatter, key.start_mark.index)
        end = value.end_mark.index
        end = _line_start(frontmatter, end) if not frontmatter[_line_start(frontmatter, end):end].strip() else end
        if end and frontmatter[end - 1:end] != "\n":
            newline = frontmatter.find("\n", end)
            end = len(frontmatter) if newline < 0 else newline + 1
    return frontmatter[:start] + frontmatter[end:]


def remove_header_scalar(frontmatter: str, name: str) -> str:
    """Remove the actual scalar and empty parent groups, preserving unrelated spans."""
    document = _document(frontmatter)
    paths = header_field_paths(name, _metadata(document))
    for path in paths:
        node = _node(document, path)
        if node is None:
            continue
        if not isinstance(node, ScalarNode):
            raise ValueError(f"Header {name} must be a scalar.")
        frontmatter = _remove_path(frontmatter, document, path)
        if not frontmatter.strip():
            return frontmatter.rstrip("\r\n")
        document = _document(frontmatter)
    return frontmatter.rstrip("\r\n")
