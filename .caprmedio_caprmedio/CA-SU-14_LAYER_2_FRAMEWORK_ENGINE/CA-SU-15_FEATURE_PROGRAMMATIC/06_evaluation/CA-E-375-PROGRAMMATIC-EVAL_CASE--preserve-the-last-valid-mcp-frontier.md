---
cce_version: cce_1
cce_form: evaluation
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
version: 21
updated_at: 2026-10-27 19:59:34 +0400
relations:
  evaluation_for:
  - CA-M-193
  derived_from:
  - CA-A-058
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-375
ref_id: CA-E-375
status: Active
role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
form: Eval Case
tier: 5
container:
  scope_unit: CA-SU-15
---
# Preserve the last valid MCP frontier

## Claim checked

one invalid MCP frontier refresh preserves the preceding complete valid frontier
bytes for recovery **and** reports the invalid active Tool **without** presenting
that previous frontier as current.

## Test case

start with one valid exposed Tool frontier, **then** refresh from a candidate set
containing one active Tool with a colliding endpoint identity.

## Acceptance criteria

pass **only** **when** the candidate frontier is rejected, the collision is reported,
**and** the preceding frontier bytes remain unchanged for recovery. no new
current registry is published **and** the preceding registry is **not** presented as
current, under CA-R-1110; byte retention alone does **not** authorize call admission.

## Failure disposition

reject the refresh path **until** replacement is atomic at the validated frontier
boundary.

## Sources

- [CA-M-193 — Supply the active Tool frontier to MCP](../05_method/CA-M-193-PROGRAMMATIC-ENG_DECISION--supply-the-active-tool-frontier-to-mcp.md)
