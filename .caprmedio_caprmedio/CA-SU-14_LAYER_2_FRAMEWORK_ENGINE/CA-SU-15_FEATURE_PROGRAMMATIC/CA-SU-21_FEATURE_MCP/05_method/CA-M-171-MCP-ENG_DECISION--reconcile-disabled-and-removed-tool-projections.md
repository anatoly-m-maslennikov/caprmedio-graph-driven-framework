---
atom_id: CA-M-171
ref_id: CA-M-171
container:
  scope_unit: CA-SU-21
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Output Publication
tier: 2
relations:
  method_for:
  - CA-R-1109
  derived_from:
  - CA-A-057
status: Active
version: 18
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
---
# Reconcile disabled and removed Tool projections

## Applicable when

Apply **when** the current Tool source set **or** its enablement decisions change.

## Procedure

1. Resolve the complete current source set **before** changing the registry.
2. Add newly eligible Tools, exclude explicitly disabled Tools, **and** remove projections **without** current sources.
3. Publish **only** the resulting complete set rather than retaining a separate allowlist.

## Outcome

the registry has no stale, disabled, **or** independently configured Tool projection.

## Failure or stop

Stop **when** source discovery is incomplete **or** **any** resulting projection cannot be classified.
