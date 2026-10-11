---
atom_id: CA-P-2163
content_role: Plan
type: Plan
label: Task
work_sequence_number: 26
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Atom
  depends_on: [Subject, Carrier, Revision, Operator, Plan]
version: 1
updated_at: "2026-10-11 17:45:11 +0400"
relations:
  is_decomposition_of: [CA-P-1959]
  depends_on: [CA-P-2162]
---
# Summary

Implement case-sensitive Atom selectors

## Objective

The approved selector and metadata changes have the exact, verified effect assigned to this Task.

## Details

Own work: at most fifteen minutes; create bounded children if this own-work limit is exceeded. Implement the reviewed selector contract in shared syntax, structural lookup, sealed preview and internal graph parsing. Preserve the whole selector token and its owner identity; do not infer native admission. Atom and atom must remain distinct. Reject malformed/unknown/duplicate/mixed selectors, eval, wildcards and unsupported operators. Verify focused regression tests and preserve existing apply guard and stale-source checks. Own code only after CA-P-2162 passes.

Root owns Git, Plan lifecycle and shared Journal recording. Workers are not alone; preserve unrelated release changes. Scratch and caches stay in `.caprmedio_tmp`; use uv. No unsupported MCP/FPF, general migration framework, runtime/release activation or Step 2 body sweep.

### Definition of Done

Not Done if the assigned effect is unverified, source pins are stale, Atom and atom are conflated, unrelated work changes, exact prior source history is lost, execution evidence is fabricated, or completion claims exceed the assigned increment.
