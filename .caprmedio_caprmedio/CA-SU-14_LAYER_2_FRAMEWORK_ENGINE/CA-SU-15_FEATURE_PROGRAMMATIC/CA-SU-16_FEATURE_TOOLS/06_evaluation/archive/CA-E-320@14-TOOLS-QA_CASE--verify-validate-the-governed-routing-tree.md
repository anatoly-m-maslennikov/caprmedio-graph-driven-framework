---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Graph/Rule
  depends_on: []
version: 14
updated_at: 2026-10-24 02:14:24 +0400
relations:
  evaluation_for:
  - CA-M-202
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-320@14
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 3
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
