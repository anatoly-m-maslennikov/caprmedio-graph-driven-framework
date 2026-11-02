---
subjects:
  governs: Entity
  depends_on:
  - Entity/Carrier
  - Entity/Term//Artifact
version: 27
updated_at: 2026-10-30 00:13:29 +0400
relations: {}
atom_id: CA-R-1747@27-draft
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Distinguish native targets from governed Artifacts

## Claim scope

native project targets, admitted Entity instances, and their Carrier representation.

## Claim

a native file, folder, database row, or other project target does not by itself admit an Entity instance or establish a Carrier binding. When an Entity instance is already admitted and represented in a Carrier, it keeps that identity and may be referred to by the Artifact Term; no separate Artifact identity is required. A native Implementation Entity instance may be an Artifact when it is admitted and represented, and Implementation and Artifact are not disjoint kinds.

## Semantics

Native existence, Entity admission, and Carrier binding remain distinct facts. The Artifact Term names the admitted, represented Entity instance without adding another ID, classification axis, or Artifact branch.

## Details

Current source support: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1994-CORE_META_MODEL--define-entity-node.md`, CA-R-1994@14, SHA-256 `41b8b0ef51a71969db07cec2008a19e3c6372e90ae9cc66727de31287d722ce8`. Its Claim and Semantics keep an Entity's description and Carrier separate and define Artifact as a Term for a Node instance delivered into Carrier instances.

The pending [Artifact Term Definition](../../05_method/draft/CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-artifact.md) owns the lexical meaning. This Rule does not make file existence into Entity admission, Carrier binding, or a second identity.

### Withdrawn from active packet

This successor is withdrawn from the active packet because its Claim is consolidated into the pending [Artifact Term Definition](../../05_method/draft/CA-M-draft-CORE_META_MODEL-TERM_DEFINITION--define-artifact.md) and [Entity Definition](CA-R-1248@24-draft-CORE_META_MODEL-DEFINITION--define-entity.md). Its original Claim, Summary, Role, Type, Version, Status, and source pin remain preserved here; it introduces no active replacement authority.

### Draft source pin

Proposed N+1 successor of `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1747-CORE_META_MODEL--distinguish-native-targets-from-governed-artifacts.md`, Version 26, SHA-256 `5efa75b803aa4aa036e6c0c1209d43b604be491275f7c4684f9e33b75cb038a4`. Summary, Content Role and Rule Type are preserved; this Draft changes no Current source.
