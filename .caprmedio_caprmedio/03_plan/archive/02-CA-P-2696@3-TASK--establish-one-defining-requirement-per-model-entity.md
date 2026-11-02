---
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: 2026-10-29 15:27:34 +0400
subjects:
  governs: Entity
atom_id: CA-P-2696@3
content_role: Plan
type: Plan
label: Task
tier: 4
relations:
  IS_CONTAINED_BY:
  - CA-P-2694
---
## Summary

Establish one defining Requirement per model Entity

## Objective

Every declared model Entity has exactly one defining R/Entity Definition. Other Rs may constrain or refer to the Entity without becoming additional defining Atoms. IS_DEFINED_BY is a derived relation, not another stored link.

## Details

The stronger check is separate from P2695's dependency-only coverage. Actual source readback finds 337 primary-kind/property paths: 180 have one exact-Governs R/Entity Definition, 24 have multiple candidates, and 133 are currently supplied through shared/formal declarations rather than an exact governing Definition. The last count is not automatically 133 missing Definitions.

Review [the thin duplicate table](definition-ownership-duplicates.tsv). Distinguish an actual Entity Definition from a Rule, a reference, a field constraint or a supporting clause. Preserve useful content and consumers. Reuse/consolidate the defining source before adding new Atoms; avoid duplicate field schemas merely to satisfy a text match. Do not choose ownership by timestamp, Tier, list order or an arbitrary first match.

Derive IS_DEFINED_BY from the qualifying defining Requirement's governing link. Keep source authority in the defining R; do not store a duplicate reverse relation. The Operator confirmed that Relation Definition counts through its specialized Entity Definition template. Keep the current Types; subtype restructuring is deferred. Define the main direction once and retain only a short derived-counterpart reference to it. Also make ownership of entities introduced in shared formal declarations explicit before calling the derived view unambiguous.

Prepare/review Draft corrections and Definition/relation RMED, apply the agreed ownership fixes, rebuild views, and independently verify exactly one owner for every in-scope model Entity. Keep actual Scope Unit/Action instances distinct from definitions of their kinds. Terms Graph implementation and Engine/code migration remain separate.

## Definition of Done

The Definition-family and derivation semantics are explicit; each selected model Entity has one unambiguous defining R; no competing Definition is hidden by projection filtering. Applicable Rules/references remain distinct, required consumers are repaired, and the source-backed graph and derived ownership view pass readback.

## Progress

Active — initial ownership audit complete; 24 duplicate target groups identified. Definition-family question is resolved; the main/counterpart DRY template is drafted and subtype restructuring is deferred. No canonical owner was selected and no competing Definition retired by this audit.
