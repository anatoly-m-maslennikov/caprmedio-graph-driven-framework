---
atom_id: CA-P-2295
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Tool
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Engineering/Workflow
  - Subject/Graph Node/Engineering/Project Structure Declaration
  - Subject/Graph Node/Engineering/Project Settings Snapshot
  - Subject/Graph Node/Engineering/Scope Unit Query Adapter Construction
  - Subject/Graph Node/Engineering/Scope Unit Declaration Read Adapter Construction
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
version: 10
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-2254
tier: 3
---
# Summary

Bind Scope Unit reads to admitted sources

## Objective

Bind the pure Scope Unit parser and selectors to the accepted Structure/Settings sources and existing receiving admission. Prove full independent Read, query frontier, missing/ambiguous/stale/denied behavior and zero effects. Reuse current schema authority rather than a guessed partial schema.

## Details

### Bounded receiving decomposition — 2026-10-13 22:46:01 +0400

CA-P-2359 implements only the private O211 Scope Unit Query receiving binding; CA-P-2360 independently verifies that bounded outcome. Implementation is assigned to the settings_rules lane and independent checks to nested_ops. Reuse the accepted current Structure/Settings declaration schema and actual selected Action/Session/source context. Preserve existing O212 implementation and its separate P2340/P2341 acceptance; these children do not duplicate or complete that Read work. Source-bound acceptance waits for final reviewed pins; independent fixture preparation may proceed while implementation runs. Broader Read/Query parent acceptance and runtime readiness remain separate. Keep this parent Active.

Each new child has an own-work bound of up to 15 minutes and must be split before exceeding it. Root owns Plans and Git; workers preserve unrelated edits. No new public route, manifest, runtime activation, live Settings change or existing-caller migration is authorized by this decomposition.

Estimated own work: 15 minutes. Split larger work into bounded children before execution. Inherit the parent Task's accepted contracts, current-source checks and authority boundaries. Internal helpers are not newly admitted Tools. Keep parsing, reading, writing and CLI responsibilities separate. The integration owner controls Plans and Git; parallel implementation owns disjoint files only.

### Definition of Done

The Plan is not Done until exact implementation/source pins, focused positive/refusal/no-op checks and an independent review establish this child's bounded outcome. Preparation alone, invented public bindings, source-policy changes, deferred publication or live Core migration do not satisfy it. Parent-wide and runtime completion remain separate.

### Concrete receiving continuation — 2026-10-13

Current D625/D626/D627/D527 and O211/O212 already define the logical map and receiving responsibilities. The missing work is production wiring, not a new map-authority decision. P2340 implements the actual private O212 receiver and P2341 independently tests genuine admission and source preservation. O211 Query and Atom O047/O046 are following bounded slices; this parent remains Active until complete Read/query receiving evidence exists.
