---
atom_id: CA-P-2311
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Scope Unit, Project Configuration, Evaluation, Plan]
version: 1
updated_at: "2026-10-13 16:35:00 +0400"
relations:
  is_decomposition_of: [CA-P-2307]
---
# Summary

Filter proposed reference validation to selected identities

## Objective

Stop rejecting unrelated, parseable legacy carriers merely because their unrelated target metadata is incomplete. Use explicit carried identity, never filenames. Keep requested targets and discovered Plan parents strict; preserve duplicate, inactive/archive, unsafe/malformed, bounded-read and currentness checks. Do not make genuinely inadmissible requested legacy targets pass.

## Details

Estimated own work: up to 15 minutes; decompose further before exceeding that bound. The Operator approved fixing the two existing validator gaps before TOMLKit implementation. Fix current-contract conformance only; any missing policy needs a separate decision. Root owns Plans and Git; parallel workers own disjoint production and independent test files. No legacy Atom rewrite, dependency change, live source publication, Core migration or installed activation.

### Definition of Done

The bounded change has an actual failing-before/passing-after regression, relevant refusal tests, current source/implementation pins and independent review. Remaining legitimate source defects or unsupported context are named, not silently accepted. No full source or runtime acceptance follows from focused tests.
