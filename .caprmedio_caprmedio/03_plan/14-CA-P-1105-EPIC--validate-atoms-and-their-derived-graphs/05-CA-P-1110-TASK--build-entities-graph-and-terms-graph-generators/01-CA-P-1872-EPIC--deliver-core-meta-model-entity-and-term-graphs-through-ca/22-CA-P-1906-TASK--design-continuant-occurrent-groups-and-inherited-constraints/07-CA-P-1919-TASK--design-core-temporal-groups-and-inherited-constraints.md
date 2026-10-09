---
atom_id: CA-P-1919
content_role: Plan
type: Plan
label: Task
work_sequence_number: 7
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Projection
  depends_on: [Entity, Term, Atom, Property, Carrier, Plan]
version: 1
updated_at: "2026-10-10 02:10:14 +0400"
relations:
  is_decomposition_of: [CA-P-1906]
  blocks: [CA-P-1921]
---
# Summary

Design Core temporal groups and inherited constraints

## Objective

Propose source-backed Continuant/Occurrent display groups and reusable inherited constraints, while preserving the complete reviewed baseline.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent.

Required start prerequisite: CA-P-1905. Inputs: the completed pinned baseline and the explicit partition or design contract.

Review major baseline families and current Core definitions. Separate reusable definitions and information artifacts from actual Runs. Treat Continuant/Occurrent as display grouping unless independently governed otherwise. Justify any synthesized taxonomy relation with Main Content. Preserve unresolved roots as questions rather than inventing an ancestor.

Declare common constraints once and preserve subtype differences; never inherit another Entity's concrete Carrier. Output `structure.design.json` in `.caprmedio_tmp/planning/core-entity-review/design/` with grouping proposals, separately evidenced additional relations, inherited constraints, before/candidate root-count method and explicit unreviewed or unresolved coverage. This bounded design does not perform CA-P-1907's complete node-disposition review.

Read current Core Main Content and verify exact source pins before proposing meaning. Earlier classification caches are preparation only. Below 90% confidence, leave a proposal unresolved, state the missing evidence and put the question to the Operator before deciding. A diagnostic or proposed view is not native admission. Preserve all qualified identities and do not infer Entity facts from source Atom metadata or Subject incidence. Work locally without MCP or FPF; do not change Core Atoms, Subjects, history, baseline outputs, implementation, runtime or unrelated work.

### Definition of Done

the Plan is **not** Done **if** ((grouping is mistaken for admitted taxonomy **or** an inherited constraint lacks evidence **or** concrete Carrier identity is inherited **or** unresolved coverage is hidden) **or** (a required start prerequisite is **not** Done) **or** (the stated output or handoff is missing) **or** (uncertainty below 90% is silently decided or its question is not put to the Operator) **or** (source pins or checks are stale) **or** (the exclusive boundary is exceeded) **or** (any direct decomposing Plan is **not** Done)).
