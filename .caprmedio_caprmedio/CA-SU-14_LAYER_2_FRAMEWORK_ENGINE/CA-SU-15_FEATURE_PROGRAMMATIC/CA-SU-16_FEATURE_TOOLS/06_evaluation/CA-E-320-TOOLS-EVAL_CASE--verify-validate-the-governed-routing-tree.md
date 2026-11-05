---
atom_id: CA-E-320
ref_id: CA-E-320
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Rule
tier: 3
relations:
  evaluation_for:
  - CA-M-202
status: Active
version: 18
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Verify validate the governed routing tree

## Claim checked

CA-M-202 deterministically blocks routing whenever the governed routing tree violates a declared structural constraint.

## Applicable when

apply **before** **any** changed routing-tree authority is used for route selection.

## Test case

start with one valid routing tree, **then** introduce **in** the same fixture an unreachable leaf, a prohibited cycle, an ambiguous root, an unresolved target, **and** an incomplete fallback. validate twice **without** changing inputs.

## Acceptance criteria

the valid tree permits routing; the invalid tree blocks it **and** emits **=1** stable attributable issue for **every** introduced violation; repeated validation preserves issue identity **and** order.

## Failure disposition

reject the validator **and** preserve the routing frontier, declared constraints, expected violations, observed issues, verdict, **and** repeat-run comparison.
