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
status: Done
subjects:
  governs: Projection
  depends_on: [Entity, Term, Atom, Property, Carrier, Plan]
version: 3
updated_at: "2026-10-10 02:49:20 +0400"
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

### Verified execution receipt

Bounded design: `.caprmedio_caprmedio/_projection/core-entity-review/design/structure.design.json`, SHA-256 `10733c9f1b6b8d5946acdc469e7cfe3ee710ed515f1de77eed765c2252652b9e`. Independent read-only acceptance verifies identical temporary/durable output and emit-only reproduction, all 35 Main Content spans and 951 current Core pins, ten correctly owned Term relations and seven conditional common constraints. Display memberships: 17 Continuant and three Occurrent; six memberships are confirmed by the bounded Operator display convention. Coverage: 24 assessed identities; 682 other nodes and 326 roots remain explicitly outside this review.

The Operator answered “yes, they are Continuant.” Actor, Carrier and Scope Unit use that local display convention. Operator, File Carrier and Directory Carrier follow only their separately evidenced subtype links. The reply is recorded separately from Core evidence; no blanket descendant rule or native temporal taxonomy is adopted. Session is a proposed example outside the baseline; the proposed ephemerality and Journal-only storage rules remain unadopted. Core, Subjects, baseline, history and runtime are unchanged.

### Definition of Done

the Plan is **not** Done **if** ((grouping is mistaken for admitted taxonomy **or** an inherited constraint lacks evidence **or** concrete Carrier identity is inherited **or** unresolved coverage is hidden) **or** (a required start prerequisite is **not** Done) **or** (the stated output or handoff is missing) **or** (uncertainty below 90% is silently decided or its question is not put to the Operator) **or** (source pins or checks are stale) **or** (the exclusive boundary is exceeded) **or** (any direct decomposing Plan is **not** Done)).
