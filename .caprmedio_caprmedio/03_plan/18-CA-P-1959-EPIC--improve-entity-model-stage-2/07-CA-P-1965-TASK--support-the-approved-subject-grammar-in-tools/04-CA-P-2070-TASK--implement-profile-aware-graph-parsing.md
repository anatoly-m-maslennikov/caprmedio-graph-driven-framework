---
atom_id: CA-P-2070
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
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

Implement profile-aware graph parsing

## Objective

Realize this bounded part of the independently accepted grammar-aware Subject Tool contract.

## Details

Estimated own work: 15 minutes. Prerequisite: CA-P-2062 (Done, c6b4525d7). Own GENERATE_ENTITY_GRAPH/generate_entity_graph.py, subject_model_sources.py and new tests/test_subject_profiles.py only. Keyword-only internal selection, legacy default; propagate selected parser through prefixes/term/dependency extraction. Approved slash creates no native IS_BORNE_BY/NARROWER_THAN fact, dot gives dependent-to-bearer and colon value-to-property. Check current approved Core grammar pins before provider use; retain frozen D269/R1194 extraction evidence. No public selector, frozen Step1 rewrite, native-consumer switch or source/runtime changes. Final checks wait for shared module.

Use the compiled subject-tools.grammar-contract.md and current implementation-lanes.md under Stage 2. The small shared API is fixed; code lanes may work in parallel against it, but final tests wait for dependencies. Preserve other lanes; no Git, Plans, governing sources, Journal, runtime, MCP or FPF writes by workers. Root owns integration and each completed Task commit. If own work exceeds 15 minutes, decompose the remaining bounded work before executing it.

### Definition of Done

Not Done if focused independent expected tests fail, the shared contract is inconsistent, unrelated code/source/guard behavior changes, current pins are stale, or evidence overstates syntax support as native admission or migration. Final whole-code acceptance remains CA-P-1975.
