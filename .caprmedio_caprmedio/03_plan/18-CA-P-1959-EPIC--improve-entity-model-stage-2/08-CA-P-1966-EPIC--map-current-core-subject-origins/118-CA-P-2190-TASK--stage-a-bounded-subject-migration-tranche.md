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
version: 3
updated_at: "2026-10-12 17:03:21 +0400"
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

CA-P-2189's receipt must reconcile the complete 907-source/4534-occurrence review, not only this tranche. Under the [approved content-conflict exclusions](../../../../.caprmedio_tmp/stage2-migration-20261012/model/content-conflict-decision.md), SHA-256 `6f5bdf81ae3861bd2141df69ba7ffa936f78cf7fef0ac0b8f2ae8290c17d09fc`, omit each confirmed content-conflict Atom wholly from the staged payload and preserve its original bytes; retain its evidenced ID/Version/hash/reason and CA-P-1970 queue plus visible unmigrated inventory/graph coverage. Stage other owners only when their whole-Subject changes are fully supported and independently accepted. Uncertainty, omissions or weak evidence must not be mislabeled as content conflicts; reviewed unresolved whole owners instead follow the separate approved unchanged-owner disposition below.

Bind the [approved unchanged unresolved-owner decision](../../../../.caprmedio_tmp/stage2-migration-20261012/model/unresolved-owner-decision.md), SHA-256 `d325383d4d4b049347bc77381e3f17616d3a473d93fce587c6b23a11e0ad9912`, separately from confirmed content conflicts. The accepted complete ledger must separately identify every unresolved whole owner by exact Atom ID, Version, source path/hash, affected occurrences, reason and open question. Omit each such owner wholly from the staged payload, including its supported rows; keep its original bytes unchanged and its BEFORE/AFTER inventory/graph presence. Do not auto-queue unresolved owners to CA-P-1970. This does not relax full 907-owner/4534-occurrence review, independent CA-P-2188/2189 disposition acceptance, or the source/preview checks for other fully supported whole owners.

Use explicit local `ATOM_UPDATE run --stage-preview` and existing proposed_carrier bytes. Stage only supported Subject replacements with required illustrative Version/time under fresh generated `.caprmedio_tmp/subject-preview/<id>/` paths. Preserve source identities/Status and all Summary, Substance, scope, Semantics, Details, body and unrelated metadata. Recheck pins, validate/read back actual candidates and retain their manifests/hashes. Below-90% or unresolved mappings stay untouched pending the Operator.

Root records the assigned tranche and actual output paths under `.caprmedio_tmp/stage2-migration-20261012/staging/` for CA-P-2191. Export/check failure is not success; report truthful retained artifacts without overwriting externally changed files. No original/history/Journal/publication effects, route bypass or content migration. Split a concrete overrun before execution.

### Definition of Done

Not Done if assigned tranche/inputs exceed the bounded scope, current pins or actual validation fail, candidate bytes change outside allowed Subjects/illustrative metadata, uncertainty is adopted or mislabeled as a content conflict, a confirmed-conflict or unresolved owner enters the staged payload, a confirmed conflict loses its evidenced CA-P-1970 queue, or either unchanged-owner disposition loses its exact pins/reason and required separate list or inventory/BEFORE/AFTER graph coverage, outputs or preservation are unverified, live effects are inferred or own work exceeds 15 minutes without decomposition.
