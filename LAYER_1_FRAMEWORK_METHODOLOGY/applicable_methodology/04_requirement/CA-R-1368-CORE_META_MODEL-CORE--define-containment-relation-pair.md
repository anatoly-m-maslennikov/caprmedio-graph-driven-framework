---
subjects:
  governs: "Entity/Relation/Type: CONTAINS"
  depends_on:
  - "Entity/Node/Continuant/Atom.Enabled Relations.Contains"
  - "Entity/Node/Continuant/Scope Unit"
version: 14
updated_at: "2026-10-20 00:10:16 +0400"
relations: {}
atom_id: "CA-R-1368"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1368-CORE_META_MODEL-CORE--define-containment-relation-pair.md
  source_atom_id: CA-R-1368
  source_atom_revision: 14
  source_sha256: f39b45ea73dc1d13097a05981fda331deba98feb7d7a5e8a360b0ef460c73cec
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Containment Relation Pair

## Scope

Direct containment and its derived inverse, including Scope Unit containment and enabled Atom containment.

## Claim

the Containment Relation Pair **means** direct relation `IS_CONTAINED_BY` from a contained entity to its containing entity **and** inverse-derived relation `CONTAINS` from the containing entity to the contained entity.

## Details

IS_CONTAINED_BY is the direct child-to-parent direction; CONTAINS is its derived inverse and is not independently authored.

Endpoint permissions are separate constraints, not part of this definition. Existing Scope Unit capability is described by CA-R-1757; CA-R-1656, CA-R-1756 and CA-R-1660 govern parent cardinality, immediate ownership and structural-parent direction. Atom containment capability and its default are governed by CA-R-1945, with the existing Plan, Workflow and Step permissions in CA-R-1990, CA-R-1991 and CA-R-1992. Their formal Graph Rule migration remains separate. Containment does not make a contained Atom part of the containing Atom's Substance or change its owning Scope Unit. This definition does not implement or require a construction graph projection.

