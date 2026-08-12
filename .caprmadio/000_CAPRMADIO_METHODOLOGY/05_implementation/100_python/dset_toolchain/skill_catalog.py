"""Provide DSET skill catalog behavior."""

from __future__ import annotations

# PUBLIC_SKILL_WORKFLOWS defines public skill workflows; this module owns the default.
PUBLIC_SKILL_WORKFLOWS = {
    "caprmadio": "lifecycle-orchestration",
    "ca-init": "initialize",
    "ca-repair-governance": "repair-governance",
    "ca-decompose": "decompose",
    "ca-diagnose": "diagnosis",
    "ca-clarify": "domain-clarification",
    "ca-landscape": "landscape",
    "ca-prototype": "prototyping",
    "ca-decisions": "decisions",
    "ca-compile": "compile",
    "ca-plan-proof": "plan-proof",
    "ca-plan-implementation": "plan-implementation",
    "ca-implement": "implement",
    "ca-verify": "verify",
    "ca-configure": "configure",
    "ca-overview": "overview",
    "ca-triage": "work-triage",
    "ca-release": "release",
    "ca-complete": "complete",
}

# PUBLIC_SKILL_MODES defines public skill modes; this module owns the default.
PUBLIC_SKILL_MODES = {
    "caprmadio": None,
    "ca-init": "initialize",
    "ca-repair-governance": "repair-governance",
    "ca-decompose": "decompose",
    "ca-diagnose": "diagnose",
    "ca-clarify": "clarify",
    "ca-landscape": "landscape",
    "ca-prototype": "prototype",
    "ca-decisions": "decisions",
    "ca-compile": "compile",
    "ca-plan-proof": "plan-proof",
    "ca-plan-implementation": "plan-implementation",
    "ca-implement": "implement",
    "ca-verify": "verify",
    "ca-configure": "configure",
    "ca-overview": "overview",
    "ca-triage": "triage-work",
    "ca-release": "release",
    "ca-complete": "complete",
}

# PRE_RESOLUTION_SKILLS defines pre resolution skills; this module owns the default.
PRE_RESOLUTION_SKILLS = frozenset({"ca-init", "ca-repair-governance"})

# SKILL_INVOCATION_MARKERS defines skill invocation markers; this module owns the default.
SKILL_INVOCATION_MARKERS = {
    skill_id: f"skills context --skill {skill_id} --target TARGET"
    for skill_id in PUBLIC_SKILL_WORKFLOWS
}

# REGISTERED_SKILL_WORKFLOWS defines registered skill workflows; this module owns the default.
REGISTERED_SKILL_WORKFLOWS = {
    skill_id: workflow_id
    for skill_id, workflow_id in PUBLIC_SKILL_WORKFLOWS.items()
    if skill_id not in PRE_RESOLUTION_SKILLS
}
