---
cce_version: cce_1
cce_form: method
subjects:
  governs: feature-boundary
  depends_on: []
version: 12
updated_at: 2026-10-24 00:51:05 +0400
relations:
  method_for:
  - CA-R-1154
  derived_from:
  - CA-A-058
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-M-253@12
status: Archived
content_role: Method
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Check one target set against registered Evaluations

## Applicable when

use this Method **when** `GRAPH_CHECK` **must** apply selected registered Evaluation criteria **to** one previously sealed target set.

## Procedure

1. confirm that `GRAPH_CHECK` is registered as one `unordered_unit` Checker owned immediately by `TOOLS` at Structural level `4`, with prefix `GRAPH_CHECK`, address `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GRAPH_CHECK`, **and** realization path `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GRAPH_CHECK/`.
2. resolve one sealed target-set identity **and** selected registered Evaluation criteria.
3. confirm that the target set retains its recorded membership, source frontier, **and** digest **before** beginning evaluation.
4. apply **every** selected criterion **to** **every** applicable target **and** retain attributable issue, evidence, **and** verdict records **in** deterministic target-and-criterion order.
5. distinguish satisfied, unsatisfied, inapplicable, blocked, **and** error verdicts, **and** return the complete result **without** changing governed Atoms, Journals, native Implementation, **or** derived outputs.

## Outcome

one read-only `GRAPH_CHECK` result provides stable attributable issues, evidence, **and** verdicts for the selected registered criteria over one sealed target set.

## Failure or stop

do **not** evaluate a stale **or** unresolved target set **and** do **not** mutate **any** governed carrier; return explicit blocked **or** error verdicts instead.
