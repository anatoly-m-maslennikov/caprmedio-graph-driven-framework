---
atom_id: CA-P-2067
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
status: Done
subjects:
  governs: Tool
  depends_on: [Subject, Atom, Term, Projection, Plan]
version: 2
updated_at: "2026-10-11 04:57:20 +0400"
relations:
  is_decomposition_of: [CA-P-1965]
---
# Summary

Implement shared Subject notation

## Objective

Realize this bounded part of the independently accepted grammar-aware Subject Tool contract.

## Details

Estimated own work: 15 minutes. Prerequisite: CA-P-2062 (Done, c6b4525d7). New subject_notation.py and ATOM_SEARCH/tests/test_subject_notation.py only. Implement the settled API in grammar-tools.implementation-lanes.md: strict immutable legacy/approved profiles, parse_subject tuples and fresh five-pin evidence. Syntax/direction only; no endpoint registry, escaping, selector grammar, migration API or source writes. Test explicit/default profiles, dot literals, mixed operators, malformed inputs, unsupported @/escapes/selectors, immutable pins and fresh evidence.

Use the compiled subject-tools.grammar-contract.md and current implementation-lanes.md under Stage 2. The small shared API is fixed; code lanes may work in parallel against it, but final tests wait for dependencies. Preserve other lanes; no Git, Plans, governing sources, Journal, runtime, MCP or FPF writes by workers. Root owns integration and each completed Task commit. If own work exceeds 15 minutes, decompose the remaining bounded work before executing it.

### Completion

Completed at 2026-10-11 04:57:20 +0400. Focused checks and independent review passed at the exact implementation pins in `stage2/task-2067.receipt.json`. No authoritative Core Subjects were changed. Final whole-code acceptance remains CA-P-1975.

### Definition of Done

Not Done if focused independent expected tests fail, the shared contract is inconsistent, unrelated code/source/guard behavior changes, current pins are stale, or evidence overstates syntax support as native admission or migration. Final whole-code acceptance remains CA-P-1975.
