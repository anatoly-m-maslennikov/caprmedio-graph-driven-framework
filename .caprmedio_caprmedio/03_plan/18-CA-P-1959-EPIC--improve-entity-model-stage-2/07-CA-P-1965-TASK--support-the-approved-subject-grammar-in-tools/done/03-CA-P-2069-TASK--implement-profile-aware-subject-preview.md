---
atom_id: CA-P-2069
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Tool
  depends_on: [Subject, Atom, Term, Projection, Plan]
version: 2
updated_at: "2026-10-11 04:57:47 +0400"
relations:
  is_decomposition_of: [CA-P-1965]
---
# Summary

Implement profile-aware Subject preview

## Objective

Realize this bounded part of the independently accepted grammar-aware Subject Tool contract.

## Details

Estimated own work: 15 minutes. Prerequisite: CA-P-2062 (Done, c6b4525d7). Own atom_subject_patch.py and ATOM_UPDATE/tests/test_subject_patch_preview.py only. Add keyword-only subject_profile legacy default; validate all source and resulting Subjects under one selected profile around unchanged finite complete-carrier validation. Seal profile/evidence in every preview including no-op. Preserve all stale/no-follow/byte/duplicate/CRLF/Unicode guards; no apply or migration API. Final checks wait for the shared module.

Use the compiled subject-tools.grammar-contract.md and current implementation-lanes.md under Stage 2. The small shared API is fixed; code lanes may work in parallel against it, but final tests wait for dependencies. Preserve other lanes; no Git, Plans, governing sources, Journal, runtime, MCP or FPF writes by workers. Root owns integration and each completed Task commit. If own work exceeds 15 minutes, decompose the remaining bounded work before executing it.

### Completion

Completed at 2026-10-11 04:57:47 +0400. Focused checks and independent review passed at the exact implementation pins in `stage2/task-2069.receipt.json`. No authoritative Core Subjects were changed. Final whole-code acceptance remains CA-P-1975.

### Definition of Done

Not Done if focused independent expected tests fail, the shared contract is inconsistent, unrelated code/source/guard behavior changes, current pins are stale, or evidence overstates syntax support as native admission or migration. Final whole-code acceptance remains CA-P-1975.
