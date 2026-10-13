"""Pure, byte-preserving Property preparation against supplied YAML carriers."""

from __future__ import annotations

import hashlib
import json
import re
from copy import deepcopy
from dataclasses import replace
from pathlib import Path

import yaml
from yaml.nodes import MappingNode, SequenceNode
from yaml.tokens import ScalarToken

from connector_property_parse import PropertyEditError, _entry_index, _parent, _same, apply_property_edits
from VALIDATE_ATOMS.validate_atoms_workers.parsing import CarrierError, parse_carrier


def _parse(raw: bytes):
    try:
        parsed = parse_carrier(raw, Path("supplied-atom.md"))
        start = parsed.text.index("\n") + 1
        closing = re.search(r"(?m)^---\r?$", parsed.text[start:])
        if closing is None:
            raise PropertyEditError("schema_invalid", "Carrier frontmatter is not closed.")
        end = start + closing.start()
        frontmatter = parsed.text[start:end]
        parsed = replace(parsed, frontmatter=frontmatter,
                         body=parsed.text[start + closing.end() + 1:])
        document = yaml.compose(frontmatter, Loader=yaml.SafeLoader)
        if not isinstance(document, MappingNode):
            raise PropertyEditError("schema_invalid", "Carrier frontmatter must be a mapping.")
        return parsed, start, end, frontmatter, document
    except (CarrierError, yaml.YAMLError, ValueError) as error:
        if isinstance(error, PropertyEditError):
            raise
        raise PropertyEditError("schema_invalid", "Supplied carrier is not valid unambiguous YAML.") from error


def _nodes(document: MappingNode, path: tuple[str, ...]):
    parent = document
    for part in path[:-1]:
        matches = [value for key, value in parent.value if key.value == part]
        if len(matches) != 1 or not isinstance(matches[0], MappingNode):
            raise PropertyEditError("schema_invalid", "Property parent has no unique mapping span.")
        parent = matches[0]
    matches = [(key, value) for key, value in parent.value if key.value == path[-1]]
    if len(matches) > 1:
        raise PropertyEditError("target_ambiguous", "Property has multiple source spans.")
    return parent, matches[0] if matches else None


def _json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, allow_nan=False)


def _comments(frontmatter: str, start: int, end: int, newline: str) -> str:
    scalar_spans = [(token.start_mark.index, token.end_mark.index)
                    for token in yaml.scan(frontmatter, Loader=yaml.SafeLoader)
                    if isinstance(token, ScalarToken)]
    comments = []
    for match in re.finditer(r"#[^\r\n]*", frontmatter[start:end]):
        offset = start + match.start()
        if any(left <= offset < right for left, right in scalar_spans):
            continue
        line_start = frontmatter.rfind("\n", 0, offset) + 1
        indent = re.match(r"[ \t]*", frontmatter[line_start:offset]).group()
        comments.append(indent + match.group() + newline)
    return "".join(comments)


def _replace_value(frontmatter: str, node, value: object, newline: str) -> str:
    start, end = node.start_mark.index, node.end_mark.index
    comments = _comments(frontmatter, start, end, newline)
    replacement = _json(value)
    if node.end_mark.column == 0:
        replacement += newline
    if comments:
        if not replacement.endswith(newline):
            replacement += newline
        replacement += comments
    return frontmatter[:start] + replacement + frontmatter[end:]


def _transform(frontmatter: str, document: MappingNode, path: tuple[str, ...],
               edit: dict, old: dict, new: dict, is_entry: bool, newline: str) -> str:
    parent_node, pair = _nodes(document, path)
    old_parent, key = _parent(old, path)
    new_parent, _ = _parent(new, path)
    if pair is None:
        if parent_node.flow_style:
            position = parent_node.end_mark.index - 1
            addition = (", " if parent_node.value else "") + _json(key) + ": " + _json(new_parent[key])
        else:
            position = parent_node.end_mark.index
            indent = parent_node.value[0][0].start_mark.column if parent_node.value else 0
            addition = " " * indent + _json(key) + ": " + _json(new_parent[key]) + newline
        return frontmatter[:position] + addition + frontmatter[position:]
    key_node, node = pair
    if key not in new_parent:
        if parent_node.flow_style:
            # shortcut: flow-map key removal is refused, extend when an admitted carrier needs it.
            raise PropertyEditError("schema_invalid", "Flow mapping Property removal has an unsupported source span.")
        start, end = key_node.start_mark.index, node.end_mark.index
        return frontmatter[:start] + _comments(frontmatter, start, end, newline) + frontmatter[end:]
    operation = edit["operation"]
    if is_entry and isinstance(node, SequenceNode):
        values = old_parent[key]
        if operation == "replace":
            selected = node.value[_entry_index(values, edit["old"])]
            return _replace_value(frontmatter, selected, edit["new"], newline)
        if operation == "add":
            if node.flow_style:
                position = node.end_mark.index - 1
                addition = (", " if node.value else "") + _json(edit["value"])
            else:
                position = node.end_mark.index
                indent = node.value[0].start_mark.column - 2
                addition = " " * indent + "- " + _json(edit["value"]) + newline
            return frontmatter[:position] + addition + frontmatter[position:]
        if operation == "remove" and not node.flow_style:
            selected = node.value[_entry_index(values, edit["value"])]
            line_start = frontmatter.rfind("\n", 0, selected.start_mark.index) + 1
            prefix = frontmatter[line_start:selected.start_mark.index]
            if not re.fullmatch(r" *- +", prefix) or selected.start_mark.line != selected.end_mark.line:
                # shortcut: multiline block-entry removal is refused, extend with exact span fixtures.
                raise PropertyEditError("schema_invalid", "List removal has an unsupported or ambiguous entry span.")
            if len(values) == 1:
                return _replace_value(frontmatter, node, [], newline)
            remainder = frontmatter[selected.end_mark.index:]
            if remainder.startswith(" #"):
                remainder = remainder[1:]
            return frontmatter[:line_start] + " " * (len(prefix) - 2) + remainder
    return _replace_value(frontmatter, node, new_parent[key], newline)


def prepare_property_carrier(raw: bytes, edits: list, *, expected_sha256: str,
                             field_paths: dict, list_fields: set, list_entry_edit,
                             validate_final) -> bytes:
    """Return exact proposed bytes; private schema bindings supply edit granularity.

    The complete validator receives metadata and the untouched body. No storage,
    permission, lifecycle, Version/time, history or publication is performed.
    """
    if type(raw) is not bytes or hashlib.sha256(raw).hexdigest() != expected_sha256:
        raise PropertyEditError("stale_state", "Supplied carrier differs from its exact expected source pin.")
    parsed, _, _, _, _ = _parse(raw)
    kwargs = {"field_paths": field_paths, "list_fields": list_fields,
              "list_entry_edit": list_entry_edit}
    proposed = apply_property_edits(parsed.metadata, edits, **kwargs,
                                    validate_final=lambda value: validate_final(value, parsed.body))
    if _same(parsed.metadata, proposed):
        return raw
    result = raw
    for edit in edits:
        current, start, end, frontmatter, document = _parse(result)
        next_value = apply_property_edits(current.metadata, [edit], **kwargs,
                                         validate_final=lambda value: None)
        if _same(current.metadata, next_value):
            continue
        newline = "\r\n" if "\r\n" in frontmatter else "\n"
        transformed = _transform(frontmatter, document, field_paths[edit["field"]], edit,
                                 current.metadata, next_value, list_entry_edit(deepcopy(edit)), newline)
        result = (current.text[:start] + transformed + current.text[end:]).encode("utf-8")
        observed, _, _, _, _ = _parse(result)
        if not _same(observed.metadata, next_value):
            raise PropertyEditError("schema_invalid", "Prepared carrier does not match the exact proposed Property state.")
    observed, _, _, _, _ = _parse(result)
    if not _same(observed.metadata, proposed) or observed.body != parsed.body:
        raise PropertyEditError("schema_invalid", "Prepared carrier changed data outside the requested Property delta.")
    if validate_final(deepcopy(observed.metadata), observed.body) is not None:
        raise PropertyEditError("schema_invalid", "Complete validator must raise on refusal or return None.")
    return result
