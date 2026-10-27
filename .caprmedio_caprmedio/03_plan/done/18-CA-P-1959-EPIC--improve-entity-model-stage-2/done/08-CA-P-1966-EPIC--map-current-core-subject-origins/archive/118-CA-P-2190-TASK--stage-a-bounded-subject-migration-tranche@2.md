---
atom_id: CA-P-2190
content_role: Plan
type: Plan
label: Task
work_sequence_number: 118
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Subject
  depends_on: [Atom, Entity, Projection, Plan, Tool, Operator]
version: 2
updated_at: "2026-10-12 16:31:39 +0400"
relations:
  is_decomposition_of: [CA-P-1966]
  blocks: [CA-P-2191]
---
# Summary

Stage a bounded Subject migration tranche

## Objective

Export one exact supported Subject-only tranche into independently checkable temporary candidates.

## Details

Estimated own work: 15 minutes for one AI Agent and one Root-frozen tranche of at most 20 sources, with validation time checked before execution. Required inputs: CA-P-2189 Done, CA-P-2183's verified staging capability, the exact tranche source list and current accepted patch/profile pins. This Task is not executable until that bounded tranche is assigned; allocate separate bounded continuation Tasks for the remainder. No partial tranche completes the full migration.

CA-P-2189's receipt must reconcile the complete 907-source/4534-occurrence review, not only this tranche. Under the [approved content-conflict exclusions](../../../../.caprmedio_tmp/stage2-migration-20261012/model/content-conflict-decision.md), SHA-256 `6f5bdf81ae3861bd2141df69ba7ffa936f78cf7fef0ac0b8f2ae8290c17d09fc`, omit each confirmed content-conflict Atom wholly from the staged payload and preserve its original bytes; retain its evidenced ID/Version/hash/reason and CA-P-1970 queue plus visible unmigrated inventory/graph coverage. Stage other owners only when their whole-Subject changes are fully supported and independently accepted. Uncertainty, omissions or weak evidence do not qualify as content-conflict exemptions and retain their existing hold/Operator gates.

Use explicit local `ATOM_UPDATE run --stage-preview` and existing proposed_carrier bytes. Stage only supported Subject replacements with required illustrative Version/time under fresh generated `.caprmedio_tmp/subject-preview/<id>/` paths. Preserve source identities/Status and all Summary, Substance, scope, Semantics, Details, body and unrelated metadata. Recheck pins, validate/read back actual candidates and retain their manifests/hashes. Below-90% or unresolved mappings stay untouched pending the Operator.

Root records the assigned tranche and actual output paths under `.caprmedio_tmp/stage2-migration-20261012/staging/` for CA-P-2191. Export/check failure is not success; report truthful retained artifacts without overwriting externally changed files. No original/history/Journal/publication effects, route bypass or content migration. Split a concrete overrun before execution.

### Definition of Done

Not Done if assigned tranche/inputs exceed the bounded scope, current pins or actual validation fail, candidate bytes change outside allowed Subjects/illustrative metadata, uncertainty is adopted or mislabeled as a content conflict, an excluded owner enters the staged payload or loses its evidenced queue/unchanged inventory and graph coverage, outputs or preservation are unverified, live effects are inferred or own work exceeds 15 minutes without decomposition.
