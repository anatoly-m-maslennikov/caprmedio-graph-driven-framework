"""Structural validation for the declared Graph Rule body carrier."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, cast

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError

from .check_support import Check
from .parsing import CarrierError, UniqueSafeLoader, check_yaml_resources
from .settings import CEILINGS
from subject_notation import SubjectNotationError, parse_subject


_RULE_TYPES = {
    "whitelist",
    "blacklist",
    "cardinality",
    "value_constraint",
    "topology_constraint",
    "endpoint_constraint",
}


class _GraphRulePayload(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")

    graph_rule_type: str
    applies_to: dict[str, Any]
    condition: dict[str, Any]
    default_value: Any = None


class _WhitelistAppliesTo(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")

    relation_type: str


class _WhitelistCondition(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")

    source: list[str]
    target: list[str]


class _CardinalityAppliesTo(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")

    node: str
    relation_type: str
    direction: str


class _CardinalityCondition(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")

    other_endpoint: list[str]
    minimum: int = Field(ge=0)
    maximum: int | None = Field(ge=0)


@dataclass(frozen=True)
class ValidatedGraphRulePayload:
    summary: str
    operative_block: str
    operative_yaml: str
    payload: dict[str, Any]


def _line_content(line: str) -> str:
    return line.rstrip("\r\n")


def _support_sections_valid(body: str, closing: int, check: Check) -> bool:
    from .check_sections import _headings

    lines = body.splitlines()
    sections: list[tuple[str, int]] = []
    seen: set[str] = set()
    active = False
    for level, title, index in _headings(body):
        if index <= closing:
            continue
        if level <= 2:
            active = level == 2 and title in {"Semantics", "Details"} and title not in seen
            if active:
                seen.add(title)
                sections.append((title, index))
            else:
                check.fail(
                    "GRAPH_RULE_BODY",
                    "body",
                    "Only one optional ## Semantics and ## Details section may follow the operative block.",
                )
                return False
        elif not active:
            check.fail(
                "GRAPH_RULE_BODY", "body", "Unsectioned content may not follow the operative block."
            )
            return False
    if not sections:
        if any(line.strip() for line in lines[closing + 1 :]):
            check.fail(
                "GRAPH_RULE_BODY", "body", "Unsectioned content may not follow the operative block."
            )
            return False
        return True
    if any(line.strip() for line in lines[closing + 1 : sections[0][1]]):
        check.fail(
            "GRAPH_RULE_BODY",
            "body",
            "Only optional ## Semantics or ## Details sections may follow the operative block.",
        )
        return False
    return True


def _carrier_parts(body: str, check: Check) -> tuple[str, str, str] | None:
    lines = body.splitlines(keepends=True)
    starts: list[int] = []
    offset = 0
    for line in lines:
        starts.append(offset)
        offset += len(line)
    summary_heading = next(
        (i for i, line in enumerate(lines) if _line_content(line).strip()), None
    )
    if summary_heading is None or _line_content(lines[summary_heading]) != "# Summary":
        check.fail("GRAPH_RULE_BODY", "body", "Graph Rule body must start with literal # Summary.")
        return None
    fence_pattern = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
    opening = next(
        (
            i
            for i in range(summary_heading + 1, len(lines))
            if fence_pattern.match(_line_content(lines[i]))
        ),
        None,
    )
    if opening is None:
        check.fail(
            "GRAPH_RULE_BODY", "body", "Graph Rule body requires exactly one fenced yaml block."
        )
        return None
    opener = fence_pattern.match(_line_content(lines[opening]))
    assert opener is not None
    marker, info = opener[1], opener[2].strip()
    if info != "yaml":
        check.fail("GRAPH_RULE_BODY", "body", "Graph Rule operative block must be fenced as yaml.")
        return None
    closing = next(
        (
            i
            for i in range(opening + 1, len(lines))
            if (match := fence_pattern.match(_line_content(lines[i])))
            and match[1][0] == marker[0]
            and len(match[1]) >= len(marker)
            and not match[2].strip()
        ),
        None,
    )
    if closing is None:
        check.fail("GRAPH_RULE_BODY", "body", "Graph Rule yaml block must use one matching fence.")
        return None
    summary = body[starts[summary_heading] + len(lines[summary_heading]) : starts[opening]]
    if not any(line.strip() for line in summary.splitlines()) or any(
        re.match(r"^ {0,3}#{1,6}[ \t]+", line) for line in summary.splitlines()
    ):
        check.fail(
            "GRAPH_RULE_BODY", "Summary", "Graph Rule Summary must contain prose and no extra sections."
        )
        return None
    if not _support_sections_valid(body, closing, check):
        return None
    closing_end = starts[closing] + len(lines[closing])
    return (
        summary,
        body[starts[opening] : closing_end],
        body[starts[opening] + len(lines[opening]) : starts[closing]],
    )


def _mapping(value: object) -> bool:
    return isinstance(value, dict) and all(isinstance(key, str) for key in value)


def _valid_subjects(subjects: list[str]) -> bool:
    for subject in subjects:
        try:
            parse_subject(subject, subject_profile="approved")
        except SubjectNotationError:
            return False
    return True


def _within_body_limit(body: str, check: Check) -> bool:
    if len(body) > CEILINGS["max_file_bytes"]:
        check.fail("GRAPH_RULE_BODY", "body", "Graph Rule body exceeds the host parser byte ceiling.")
        return False
    try:
        body_size = len(body.encode("utf-8"))
    except UnicodeEncodeError:
        check.fail("GRAPH_RULE_BODY", "body", "Graph Rule body is not valid UTF-8 text.")
        return False
    if body_size > CEILINGS["max_file_bytes"]:
        check.fail("GRAPH_RULE_BODY", "body", "Graph Rule body exceeds the host parser byte ceiling.")
        return False
    return True


def _parse_rule(payload: str, check: Check) -> dict[str, Any] | None:
    try:
        check_yaml_resources(payload)
        rule = yaml.load(payload, Loader=UniqueSafeLoader)
    except (CarrierError, yaml.YAMLError, RuntimeError, ValueError):
        check.fail("GRAPH_RULE_BODY", "body", "Graph Rule operative block must be safe, valid YAML.")
        return None
    if not _mapping(rule):
        check.fail("GRAPH_RULE_BODY", "body", "Graph Rule yaml must be one mapping.")
        return None
    return cast(dict[str, Any], rule)


def _validate_whitelist(rule: _GraphRulePayload, check: Check) -> None:
    try:
        applies_to = _WhitelistAppliesTo.model_validate(rule.applies_to)
        condition = _WhitelistCondition.model_validate(rule.condition)
    except ValidationError:
        check.fail("GRAPH_RULE_BODY", "body", "Whitelist fields do not match the declared schema.")
        return
    if not applies_to.relation_type.strip():
        check.fail("GRAPH_RULE_BODY", "applies_to", "Whitelist relation_type must be a string.")
    if not _valid_subjects(condition.source) or not _valid_subjects(condition.target):
        check.fail(
            "GRAPH_RULE_BODY", "condition", "Whitelist source and target must use Subject notation."
        )


def _validate_cardinality(rule: _GraphRulePayload, payload: dict[str, Any], check: Check) -> None:
    if "default_value" in payload:
        check.fail("GRAPH_RULE_BODY", "default_value", "Cardinality does not allow default_value.")
        return
    try:
        applies_to = _CardinalityAppliesTo.model_validate(rule.applies_to)
        condition = _CardinalityCondition.model_validate(rule.condition)
    except ValidationError:
        check.fail("GRAPH_RULE_BODY", "body", "Cardinality fields do not match the declared schema.")
        return
    if not applies_to.node.strip() or not _valid_subjects([applies_to.node]):
        check.fail("GRAPH_RULE_BODY", "applies_to.node", "Cardinality node must use Subject notation.")
    if not applies_to.relation_type.strip():
        check.fail("GRAPH_RULE_BODY", "applies_to.relation_type", "Cardinality relation_type must be nonempty.")
    if applies_to.direction not in {"outgoing", "incoming"}:
        check.fail("GRAPH_RULE_BODY", "applies_to.direction", "Cardinality direction must be outgoing or incoming.")
    if not _valid_subjects(condition.other_endpoint):
        check.fail("GRAPH_RULE_BODY", "condition.other_endpoint", "Cardinality endpoints must use Subject notation.")
    if condition.maximum is not None and condition.maximum < condition.minimum:
        check.fail("GRAPH_RULE_BODY", "condition.maximum", "Cardinality maximum must be at least minimum.")


def validated_graph_rule_payload(
    body: str, check: Check
) -> ValidatedGraphRulePayload | None:
    """Return source-exact carrier text and parsed data for a supported rule."""
    if not _within_body_limit(body, check):
        return None
    parts = _carrier_parts(body, check)
    if parts is None:
        return None
    summary, operative_block, operative_yaml = parts
    rule = _parse_rule(operative_yaml, check)
    if rule is None:
        return None
    try:
        payload_model = _GraphRulePayload.model_validate(rule)
    except ValidationError:
        check.fail("GRAPH_RULE_BODY", "body", "Graph Rule yaml has an invalid top-level shape.")
        return None
    if payload_model.graph_rule_type not in _RULE_TYPES:
        check.fail("GRAPH_RULE_BODY", "graph_rule_type", "Graph Rule type must be one declared string.")
        return None
    if payload_model.graph_rule_type == "cardinality":
        findings_before = len(check.findings)
        _validate_cardinality(payload_model, rule, check)
        if len(check.findings) > findings_before:
            return None
        return ValidatedGraphRulePayload(summary, operative_block, operative_yaml, rule)
    if payload_model.graph_rule_type != "whitelist":
        check.gap(
            "graph_rule_type",
            "The declared Graph Rule type has no complete structural schema for this validator.",
        )
        return None
    findings_before = len(check.findings)
    _validate_whitelist(payload_model, check)
    if len(check.findings) > findings_before:
        return None
    return ValidatedGraphRulePayload(summary, operative_block, operative_yaml, rule)


def validate_graph_rule_body(body: str, check: Check) -> None:
    """Check the declared carrier and supported Type shape, without evaluation."""
    validated_graph_rule_payload(body, check)
