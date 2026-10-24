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
status: Canceled
subjects:
  governs: Subject
  depends_on: [Atom, Entity, Projection, Plan, Tool, Operator]
version: 8
updated_at: "2026-10-22 17:49:02 +0000"
relations:
  is_decomposition_of: [CA-P-1966]
---
# Summary

Stage a bounded Subject migration tranche

## Objective

Export one exact supported Subject-only tranche into independently checkable temporary candidates.

## Details

Estimated own work: 15 minutes for one AI Agent and one Root-frozen tranche of at most 20 sources, with validation time checked before execution. Required inputs: CA-P-1966's current mapping-disposition outputs and independent checks satisfying CA-P-2189's Subjects-only slice without declaring its old children Done, CA-P-2183's verified staging capability, the exact tranche source list and current accepted patch/profile pins. This Task is not executable until that bounded tranche is assigned; allocate separate bounded continuation Tasks for the remainder. No partial tranche completes the full migration.

Apply inherited CA-P-1959/2193 guidance against [Candidate #4](../../../_projection/core-entity-review/presentation/operator.model.candidate-4.md), SHA-256 `a23019a1ee6cd3586640d6c3d9e211091f3683ac5f136058d745650570e78ca7`. Entity is only the umbrella. The three top-level branches are Occurrent, Continuant and Carrier. Continuant explicitly excludes Carrier and contains Object, Actor, History, Projection and Selection. Object is authoritative content about what/how; Actor is who. Actual executions and sessions are Occurrents, not their Journal records. History contains Journals, records and Revisions; Projections are derived content, including Terms Graph. A Selection is a rule/expression; running it is an Occurrent, and a saved/tracked result is a Projection. A Carrier bears a representation without becoming that content. Term annotations preserve source meanings, allowed values and derived vocabulary, not another root. No new native Relation semantics, parser/schema change or Core adoption follows from this candidate. Consume CA-P-1966's completed current mapping-disposition and independent current-source-rebinding evidence under CA-P-1959's latest Subjects-only override. Its current checkpoint supersedes old deep re-review/adaptation/re-pin prerequisites for this slice. Historical analytical PASS remains bound to its original bytes; no full FPF rerun, Core adoption or migration is implied. Recheck the current mapping-disposition and source-rebinding evidence; keep older model/report pins historical and unchanged.

CA-P-1966's current outputs and independent checks satisfy CA-P-2189's mapping-disposition slice across all 906 sources/4530 occurrences, not only this tranche; consume their current bindings without reopening old deep-review prerequisites. Under the [approved content-conflict exclusions](../../../../.caprmedio_tmp/stage2-migration-20261012/model/content-conflict-decision.md), SHA-256 `6f5bdf81ae3861bd2141df69ba7ffa936f78cf7fef0ac0b8f2ae8290c17d09fc`, omit each confirmed content-conflict Atom wholly from the staged payload and preserve its original bytes; retain its evidenced ID/Version/hash/reason and CA-P-1970 queue plus visible unmigrated inventory/graph coverage. Stage other owners only when their whole-Subject changes are fully supported and independently accepted. Uncertainty, omissions or weak evidence must not be mislabeled as content conflicts; reviewed unresolved whole owners instead follow the separate approved unchanged-owner disposition below.

Bind the [approved unchanged unresolved-owner decision](../../../../.caprmedio_tmp/stage2-migration-20261012/model/unresolved-owner-decision.md), SHA-256 `d325383d4d4b049347bc77381e3f17616d3a473d93fce587c6b23a11e0ad9912`, separately from confirmed content conflicts. The accepted complete ledger must separately identify every unresolved whole owner by exact Atom ID, Version, source path/hash, affected occurrences, reason and open question. Omit each such owner wholly from the staged payload, including its supported rows; keep its original bytes unchanged and its BEFORE/AFTER inventory/graph presence. Do not auto-queue unresolved owners to CA-P-1970. This does not relax full 906-owner/4530-occurrence review, the current independently checked CA-P-1966 mapping-disposition evidence satisfying the CA-P-2188/2189 slice, or the source/preview checks for other fully supported whole owners.

Use a currently advertised and admitted staging capability only after discovery and its exact execution context confirm the authorized staging binding, inputs and boundaries. If none is available, use only an already admitted, explicitly authorized local staging method with the same preservation and stale-source guards; an unavailable MCP binding does not authorize a guessed route, copied procedure or raw-file bypass. Stop if neither method is admitted. Use existing proposed_carrier bytes. Stage only supported Subject replacements with required illustrative Version/time under fresh generated `.caprmedio_tmp/subject-preview/<id>/` paths. Preserve source identities/Status and all Summary, Substance, scope, Semantics, Details, body and unrelated metadata. Recheck pins, validate/read back actual candidates and retain their manifests/hashes. Below-90% or unresolved mappings stay untouched pending the Operator.

Root records the assigned tranche and actual output paths under `.caprmedio_tmp/stage2-migration-20261012/staging/` for CA-P-2191. Export/check failure is not success; report truthful retained artifacts without overwriting externally changed files. No original/history/Journal/publication effects, route bypass or content migration. Split a concrete overrun before execution.

### Definition of Done

Not Done if assigned tranche/inputs exceed the bounded scope, current pins or actual validation fail, candidate bytes change outside allowed Subjects/illustrative metadata, uncertainty is adopted or mislabeled as a content conflict, a confirmed-conflict or unresolved owner enters the staged payload, a confirmed conflict loses its evidenced CA-P-1970 queue, or either unchanged-owner disposition loses its exact pins/reason and required separate list or inventory/BEFORE/AFTER graph coverage, outputs or preservation are unverified, live effects are inferred or own work exceeds 15 minutes without decomposition.
