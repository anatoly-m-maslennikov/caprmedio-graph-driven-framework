---
atom_id: CA-P-2068
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Subject, Atom, Term, Projection, Plan]
version: 1
updated_at: "2026-10-11 04:46:20 +0400"
relations:
  is_decomposition_of: [CA-P-1965]
---
# Summary

Implement profile-aware Subject lookup

## Objective

Realize this bounded part of the independently accepted grammar-aware Subject Tool contract.

## Details

Estimated own work: 15 minutes. Prerequisite: CA-P-2062 (Done, c6b4525d7). Own atom_subject_lookup.py and ATOM_SEARCH/tests/test_subject_lookup.py only. Consume the shared API, validate requested/source syntax, selected lexical prefix boundaries, reject malformed profiles, retain all filters/source diagnostics/pins/no-write properties and echo exactly subject_profile plus subject_profile_evidence. No inferred semantic-conformance attestation or Core-root assumption. Final checks wait for the shared module.

Use the compiled subject-tools.grammar-contract.md and current implementation-lanes.md under Stage 2. The small shared API is fixed; code lanes may work in parallel against it, but final tests wait for dependencies. Preserve other lanes; no Git, Plans, governing sources, Journal, runtime, MCP or FPF writes by workers. Root owns integration and each completed Task commit. If own work exceeds 15 minutes, decompose the remaining bounded work before executing it.

### Definition of Done

Not Done if focused independent expected tests fail, the shared contract is inconsistent, unrelated code/source/guard behavior changes, current pins are stale, or evidence overstates syntax support as native admission or migration. Final whole-code acceptance remains CA-P-1975.
