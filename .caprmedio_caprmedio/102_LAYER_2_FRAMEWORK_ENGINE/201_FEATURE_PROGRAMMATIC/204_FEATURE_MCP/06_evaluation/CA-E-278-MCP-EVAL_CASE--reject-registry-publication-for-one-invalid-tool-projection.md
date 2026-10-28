---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Validation
  depends_on: []
version: 16
updated_at: 2026-10-27 19:59:31 +0400
relations:
  evaluation_for:
  - CA-M-172
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-278
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: MCP
type: Eval Case
tier: 3
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
