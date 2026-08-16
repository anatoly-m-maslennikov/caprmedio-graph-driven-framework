---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-158
scope_path: layer:meta
subject_scope: authority
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-116-preserve-strict-semantic-distinctions
---

# Requirement — Separate authority, applicability, and currentness

Authority is an Artifact's governed capacity to establish meaning of a declared
kind. Applicability determines whether that meaning governs a particular
structural scope, profile, environment, version, time boundary, or other
declared context. Currentness determines which exact applicable Artifact
revision is presently effective in that context.

These properties are orthogonal. An authoritative Artifact may be inapplicable
to a given context; an applicable historical revision may no longer be current;
and a current Projection may accurately report state without possessing
semantic authority. Acceptance, provenance, implementation, evidence, and
assurance do not silently establish authority, applicability, or currentness.

Precedence and conflict resolution select among otherwise authoritative and
applicable claims; they do not merge these properties. GOV owns the concrete
rules and generated views used to resolve and report them.

## Primary claim

CAPRMADIO evaluates authority, applicability, and currentness as separate
governed properties rather than treating any one as proof of the others.
