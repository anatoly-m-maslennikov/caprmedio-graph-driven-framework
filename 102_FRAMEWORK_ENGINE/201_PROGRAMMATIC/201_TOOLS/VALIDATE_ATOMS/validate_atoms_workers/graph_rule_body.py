"""Structural validation for the declared Graph Rule body carrier."""

from __future__ import annotations

import re
from typing import Any

import yaml
from pydantic import BaseModel, ConfigDict, ValidationError

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


def _payload(body: str, check: Check) -> str | None:
    lines = body.splitlines()
    summary_heading = next((i for i, line in enumerate(lines) if line.strip()), None)
    if summary_heading is None or lines[summary_heading] != "# Summary":
        check.fail("GRAPH_RULE_BODY", "body", "Graph Rule body must start with literal # Summary.")
        return None
    fence_pattern = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
    opening = next(
        (i for i in range(summary_heading + 1, len(lines)) if fence_pattern.match(lines[i])), None
    )
    if opening is None:
        check.fail(
            "GRAPH_RULE_BODY", "body", "Graph Rule body requires exactly one fenced yaml block."
        )
        return None
    opener = fence_pattern.match(lines[opening])
    assert opener is not None
    marker, info = opener[1], opener[2].strip()
    if info != "yaml":
        check.fail("GRAPH_RULE_BODY", "body", "Graph Rule operative block must be fenced as yaml.")
        return None
    closing = next(
        (
            i
            for i in range(opening + 1, len(lines))
            if (match := fence_pattern.match(lines[i]))
            and match[1][0] == marker[0]
            and len(match[1]) >= len(marker)
            and not match[2].strip()
        ),
        None,
    )
    if closing is None:
        check.fail("GRAPH_RULE_BODY", "body", "Graph Rule yaml block must use one matching fence.")
        return None
    summary = lines[summary_heading + 1 : opening]
    if not any(line.strip() for line in summary) or any(
        re.match(r"^ {0,3}#{1,6}[ \t]+", line) for line in summary
    ):
        check.fail(
            "GRAPH_RULE_BODY", "Summary", "Graph Rule Summary must contain prose and no extra sections."
        )
        return None
    if any(line.strip() for line in lines[closing + 1 :]):
        check.fail("GRAPH_RULE_BODY", "body", "No prose or sections may follow the Graph Rule yaml block.")
        return None
    return "\n".join(lines[opening + 1 : closing])


def _mapping(value: object) -> bool:
    return isinstance(value, dict) and all(isinstance(key, str) for key in value)


def _valid_subjects(subjects: list[str]) -> bool:
    for subject in subjects:
        try:
            parse_subject(subject, subject_profile="approved")
        except SubjectNotationError:
            return False
    return True


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


def validate_graph_rule_body(body: str, check: Check) -> None:
    """Check the declared carrier and whitelist shape; do not evaluate a rule."""
    if len(body) > CEILINGS["max_file_bytes"]:
        check.fail("GRAPH_RULE_BODY", "body", "Graph Rule body exceeds the host parser byte ceiling.")
        return
    try:
        body_size = len(body.encode("utf-8"))
    except UnicodeEncodeError:
        check.fail("GRAPH_RULE_BODY", "body", "Graph Rule body is not valid UTF-8 text.")
        return
    if body_size > CEILINGS["max_file_bytes"]:
        check.fail("GRAPH_RULE_BODY", "body", "Graph Rule body exceeds the host parser byte ceiling.")
        return
    payload = _payload(body, check)
    if payload is None:
        return
    try:
        check_yaml_resources(payload)
        rule = yaml.load(payload, Loader=UniqueSafeLoader)
    except (CarrierError, yaml.YAMLError, RuntimeError, ValueError):
        check.fail("GRAPH_RULE_BODY", "body", "Graph Rule operative block must be safe, valid YAML.")
        return
    if not _mapping(rule):
        check.fail("GRAPH_RULE_BODY", "body", "Graph Rule yaml must be one mapping.")
        return
    try:
        payload_model = _GraphRulePayload.model_validate(rule)
    except ValidationError:
        check.fail("GRAPH_RULE_BODY", "body", "Graph Rule yaml has an invalid top-level shape.")
        return
    if payload_model.graph_rule_type not in _RULE_TYPES:
        check.fail("GRAPH_RULE_BODY", "graph_rule_type", "Graph Rule type must be one declared string.")
        return
    if payload_model.graph_rule_type != "whitelist":
        check.gap(
            "graph_rule_type",
            "The declared Graph Rule type has no complete structural schema for this validator.",
        )
        return
    _validate_whitelist(payload_model, check)
