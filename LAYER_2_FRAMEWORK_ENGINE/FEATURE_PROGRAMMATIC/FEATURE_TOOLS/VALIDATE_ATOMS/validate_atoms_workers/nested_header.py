"""Finite admission of the reviewed nested Header; source mappings stay unchanged."""

from __future__ import annotations

import hashlib
from pathlib import PurePosixPath, PureWindowsPath
from typing import Any

from header_groups import GROUP_FIELDS, GROUP_ORDER, ROLE_FIELDS
from subject_notation import SubjectNotationError, parse_subject_expression

from .authority import Record
from .check_support import Check, _integer, _string, _strings

GROUPS = frozenset({"identity", "context", "state", "destination"})


def is_nested_header(metadata: Record) -> bool:
    return bool(GROUPS.intersection(metadata))


def _mapping(value: Any, path: str, check: Check) -> Record | None:
    if not isinstance(value, dict) or not value:
        check.fail("PROPERTY_TYPE", path, "A present Header group must be a nonempty mapping.")
        return None
    return value


def _children(group: Record, allowed: set[str], path: str, check: Check) -> None:
    for key in group.keys() - allowed:
        check.fail("PROPERTY_UNADMITTED", path + "." + str(key), "No reviewed declaration admits this Header path.")


def check_topics(topics: Any, check: Check) -> None:
    block = _mapping(topics, "context.topics", check)
    if block is None:
        return
    _children(block, {"main_subject", "dependencies"}, "context.topics", check)
    check.require(block, "main_subject", _string)
    dependencies = block.get("dependencies", [])
    if not _strings(dependencies):
        check.fail("PROPERTY_TYPE", "context.topics.dependencies", "Topics dependencies must be unique nonempty strings.")
    values = [("context.topics.main_subject", block.get("main_subject"))]
    if isinstance(dependencies, list):
        values.extend(("context.topics.dependencies", value) for value in dependencies)
    for path, value in values:
        if isinstance(value, str) and value:
            try:
                parse_subject_expression(value, subject_profile="approved")
            except SubjectNotationError as error:
                check.fail("SUBJECT_INVALID", path, str(error))


def _authority(check: Check) -> bool:
    from .check_fields import _D657_NESTED_BODY, encoding_authority

    authority = encoding_authority(check)
    text = authority[1].get("text") if authority else None
    if (authority is not None and authority[0] == "current" and isinstance(text, str)
            and hashlib.sha256(text.split("---", 2)[-1].encode()).hexdigest() == _D657_NESTED_BODY):
        return True
    check.gap("header", "Nested Header admission requires its exact reviewed encoding authority.")
    return False


def _role_context(context: Record, check: Check) -> None:
    for role_key, fields in ROLE_FIELDS.items():
        if role_key not in context:
            continue
        block = _mapping(context[role_key], "context." + role_key, check)
        if block is None:
            continue
        role = context.get("role")
        if not isinstance(role, str) or role.lower() != role_key:
            check.fail("PROPERTY_UNADMITTED", "context." + role_key, "This Context specialization belongs to another Role.")
        _children(block, set(fields), "context." + role_key, check)
        if role_key == "concern" and "priority" in block:
            check.require(block, "priority", lambda value: value in ("high", "medium", "low"))
        if "work_sequence_number" in block:
            check.require(block, "work_sequence_number", lambda value: _integer(value) and value > 0)
        if "ai_agent_confidence_threshold" in block:
            check.require(block, "ai_agent_confidence_threshold", lambda value: _integer(value) and 0 <= value <= 100)


def _context(raw: Record, check: Check) -> None:
    context = raw.get("context")
    if not isinstance(context, dict):
        check.fail("PROPERTY_REQUIRED", "context", "Current Header requires its Context group.")
        return
    for field in ("role", "form"):
        check.require(context, field, _string)
    if context.get("form") == "Project Goal":
        check.require(context, "tier", _integer)
        check.gap("context.tier", "Current Project Goal Tier needs its verified ownership and Tier authority.")
    else:
        check.require(context, "tier", lambda value: _integer(value) and value >= 0)
    if "label" in context:
        check.require(context, "label", _string)
    if "container" in context:
        container = _mapping(context["container"], "context.container", check)
        if container is not None:
            if set(container) not in ({"scope_unit"}, {"atom"}):
                check.fail("PROPERTY_TYPE", "context.container", "Container requires exactly one Scope Unit or Atom target.")
            for key in container:
                check.require(container, key, _string)
    _role_context(context, check)


def _identity_state(raw: Record, check: Check) -> None:
    identity = raw.get("identity")
    if isinstance(identity, dict):
        for field in identity:
            check.require(identity, field, _string)
    state = raw.get("state")
    if isinstance(state, dict):
        if "status" in state:
            check.require(state, "status", _string)
        if "version" in state:
            check.require(state, "version", lambda value: _integer(value) and value > 0)


def _destination(raw: Record, check: Check) -> None:
    destination = raw.get("destination")
    if not isinstance(destination, dict):
        return
    file = _mapping(destination.get("file"), "destination.file", check)
    if file is None:
        return
    _children(file, {"name", "path"}, "destination.file", check)
    for field in ("name", "path"):
        check.require(file, field, _string)
    name, path = file.get("name"), file.get("path")
    if isinstance(name, str) and name and (PurePosixPath(name).name != name or "\\" in name or not PurePosixPath(name).suffix):
        check.fail("PROPERTY_DOMAIN", "destination.file.name", "File Name must include its extension and no directory.")
    if isinstance(path, str) and path and (PurePosixPath(path).is_absolute() or PureWindowsPath(path).is_absolute()
                                         or ".." in PurePosixPath(path).parts or "\\" in path):
        check.fail("PROPERTY_DOMAIN", "destination.file.path", "File Path must be a repository-relative directory.")


def _relations(raw: Record, check: Check) -> None:
    if "relations" not in raw:
        return
    block = _mapping(raw["relations"], "relations", check)
    if block is not None:
        for name, targets in block.items():
            if not _strings(targets) or not targets:
                check.fail("PROPERTY_TYPE", "relations." + name, "A direct Relation requires nonempty unique Atom targets.")


def _root_residue(raw: Record, check: Check) -> None:
    preserved = check.inputs.get("_preserved_root_fields", {})
    for field in raw.keys() - GROUPS - {"relations", "projection"} - preserved.keys():
        if field in {"current_scope_unit", "claim_target_scope_unit"}:
            check.gap(field, "Preserved scope compatibility data needs its explicit migration disposition.")
        else:
            check.fail("PROPERTY_UNADMITTED", field, "Legacy root residue needs exact predecessor preservation admission.")


def check_nested_header(raw: Record, check: Check) -> None:
    if not _authority(check):
        return
    order = [name for name in raw if name in GROUP_ORDER]
    if order != [name for name in GROUP_ORDER if name in raw]:
        check.fail("PROPERTY_ENCODING", "header", "Header groups do not follow their declared serialization order.")
    for name in GROUPS.intersection(raw):
        group = _mapping(raw[name], name, check)
        if group is not None:
            allowed = set(GROUP_FIELDS.get(name, ()))
            if name == "context":
                allowed.update(ROLE_FIELDS)
            elif name == "destination":
                allowed = {"file"}
            _children(group, allowed, name, check)
    _context(raw, check)
    _identity_state(raw, check)
    _destination(raw, check)
    _relations(raw, check)
    _root_residue(raw, check)
