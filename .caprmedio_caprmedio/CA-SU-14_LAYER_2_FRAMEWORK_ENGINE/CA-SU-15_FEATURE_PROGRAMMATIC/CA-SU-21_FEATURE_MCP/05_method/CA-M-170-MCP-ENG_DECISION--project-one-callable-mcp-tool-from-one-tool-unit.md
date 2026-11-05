---
atom_id: CA-M-170
ref_id: CA-M-170
container:
  scope_unit: CA-SU-21
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
tier: 2
relations:
  method_for:
  - CA-R-1108
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
# Project one callable MCP Tool from one Tool unit

## Applicable when

Apply **when** a validated active immediate Tool unit is selected for MCP exposure.

## Procedure

1. Derive one stable MCP identity from the canonical Tool identity.
2. Project the validated Tool contract **without** splitting, aliasing, **or** aggregating it.
3. Verify that no other source Tool projects **to** the same callable MCP identity.

## Outcome

One valid active Tool unit has exactly one unambiguous callable MCP projection.

## Failure or stop

Stop publication on a missing source, duplicate identity, alias, **or** attempted aggregation.
