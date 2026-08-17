---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-092
scope_path: layer:meta
subject_scope: assurance
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-048
  child_of:
    - CAPRMADIO-REQUIREMENT-META-091-authority-assurance-and-ops-remain-distinct
---
# Requirement — Separate Analysis from factual Ops records

Ops records what occurred, was measured, or was reported during enacted execution or operation, with its available provenance and context. Examples include logs, complaints, tickets, errors, execution outputs, measurements, delivery outcomes, and externally received operational reports.

An Ops record does not explain causes, justify a choice, synthesize implications, or prescribe a required outcome, method, assurance mechanism, or delivery path.

Analysis interprets Concerns, Ops records, Requirements, Methods, Assurance, Delivery, or Implementations. It may compare alternatives, investigate causes, synthesize findings, explain implications, and provide rationale for a Requirement, Method, Assurance rule, or Delivery rule.

When one carrier mixes factual input with interpretation, the factual Ops record and interpretive Analysis are separate governed artifacts linked by explicit relations.

## Primary claim

Factual Ops records and interpretive Analysis are separate semantic contributions.
