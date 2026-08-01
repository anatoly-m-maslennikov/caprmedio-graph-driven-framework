---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-092
scope_path: layer:meta
subject_scopes:
  - artifact-model
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-REQUIREMENT-META-048
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-086
---

# Requirement — Separate Analysis from factual Ops records

Ops records what occurred, was measured, or was reported during enacted execution or operation, with its available provenance and context. Examples include logs, complaints, tickets, errors, execution outputs, measurements, delivery outcomes, and externally received operational reports.

An Ops record does not explain causes, justify a choice, synthesize implications, or prescribe a required outcome, method, assurance mechanism, or delivery path.

Analysis interprets Concerns, Ops records, Requirements, Methods, Assurance, Delivery, or Implementations. It may compare alternatives, investigate causes, synthesize findings, explain implications, and provide rationale for a Requirement, Method, Assurance rule, or Delivery rule.

When one carrier mixes factual input with interpretation, the factual Ops record and interpretive Analysis are separate governed artifacts linked by explicit relations.

## Primary claim

Factual Ops records and interpretive Analysis are separate semantic contributions.

## Rationale

Separating enacted or measured facts from interpretation preserves evidence provenance and makes later reasoning reviewable without rewriting the original Ops record.
