---
subjects:
  governs: "Navigation Projection Derivation"
  depends_on:
    ["Entity/Node/Continuant/Atom.Substance", "Entity/Node/Continuant/Atom.Summary"]
version: 21
updated_at: "2026-10-19 15:54:42 +0400"
relations: {}
atom_id: "CA-M-231"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/05_method/CA-M-231-CORE_META_MODEL--derive-navigation-projections-from-the-cce-claim.md
  source_atom_id: CA-M-231
  source_atom_revision: 21
  source_sha256: 15cb19675421b7900cea3cc6ad649a4158c13ca4c883fce2c4f5545c1d970964
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Derive Navigation Projections from the CCE Claim

## Scope

derivation of an Atom's navigation values from its authoritative content.

## Claim

**to** derive an Atom's navigation values, derive them from authoritative content rather than another navigation value:

- derive a new Atom's Summary from its finalized primary contribution within its applicability under CA-R-1465 **and** CA-M-111. for RMED, use Claim read within Scope, **not** Scope alone.
- derive **every** requested Projection from its applicable complete source content, including relevant textual applicability restrictions, **not** from the Summary.
- for an existing Atom identity, retain its Summary **and** check source faithfulness. a needed Summary change follows CA-R-1464 **and** **must not** be applied as a same-identity refresh.

## Details
