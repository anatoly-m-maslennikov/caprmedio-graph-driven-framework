---
atom_id: CA-E-278
ref_id: CA-E-278
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Validation
tier: 3
relations:
  evaluation_for:
  - CA-M-172
  derived_from:
  - CA-A-057
status: Active
version: 17
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
---
# Reject registry publication for one invalid Tool projection

## Claim checked

An invalid selected Tool projection prevents publication of a partial current registry.

## Test case

Introduce one source Tool with an invalid schema into an **otherwise** valid selected frontier.

## Acceptance criteria

No new registry is published **and** the invalid source receives an explicit diagnostic.

## Failure disposition

Preserve the defect for repair; do **not** silently skip it.
