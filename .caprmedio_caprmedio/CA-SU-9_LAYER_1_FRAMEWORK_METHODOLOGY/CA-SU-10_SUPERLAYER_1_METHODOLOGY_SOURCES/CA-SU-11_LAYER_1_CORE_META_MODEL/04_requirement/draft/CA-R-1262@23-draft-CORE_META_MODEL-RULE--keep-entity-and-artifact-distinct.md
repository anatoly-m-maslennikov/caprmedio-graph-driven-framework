---
subjects:
  governs: Entity
  depends_on:
  - Entity/Carrier
  - Entity/Term//Artifact
version: 23
updated_at: 2026-10-30 00:13:29 +0400
relations: {}
atom_id: CA-R-1262@23-draft
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Keep Entity and Artifact Distinct

## Claim scope

the Artifact Term and an Entity instance represented in a Carrier.

## Claim

Artifact **must not** be equivalent **to** the Entity category. Artifact is a Term for an Entity instance represented in a Carrier; it does not create a separate Artifact Entity identity or a disjoint Entity kind.

## Semantics

An Entity instance may be referred to as an Artifact when it is represented in a Carrier such as a file, folder, or database row. The represented Entity instance remains the same Entity; the Artifact Term does not add another identity, branch, or classification axis.

## Details

Current source support: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1994-CORE_META_MODEL--define-entity-node.md`, CA-R-1994@14, SHA-256 `41b8b0ef51a71969db07cec2008a19e3c6372e90ae9cc66727de31287d722ce8`. Its Claim and Semantics establish that Artifact is a Term for a Node instance delivered into Carrier instances and not another Node kind or branch.

The pending [Artifact Term Definition](../../05_method/draft/CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-artifact.md) owns the reusable lexical meaning. This Rule governs only the category-versus-represented-instance distinction and does not admit a second Entity identity.

### Withdrawn from active packet

This successor is withdrawn from the active packet because its Claim is consolidated into the pending [Artifact Term Definition](../../05_method/draft/CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-artifact.md) and [Entity Definition](CA-R-1248@24-draft-CORE_META_MODEL-DEFINITION--define-entity.md). Its original Claim, Summary, Role, Type, Version, Status, and source pin remain preserved here; it introduces no active replacement authority.

### Draft source pin

Proposed N+1 successor of `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1262-CORE_META_MODEL-RULE--keep-entity-and-artifact-distinct.md`, Version 22, SHA-256 `398c6acd55c8b34e20eb1139d72383d9a47b17961a581ea289754118d9aec14a`. Summary, Content Role and Rule Type are preserved; this Draft changes no Current source.
