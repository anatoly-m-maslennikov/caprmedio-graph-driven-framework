---
subjects:
  governs: "IS_ALLOWED_VALUE_OF"
  depends_on:
    ["Property", "Entity/Node/Continuant/Projection/Type: Entities Graph", "Entity/Relation"]
version: 10
updated_at: "2026-10-19 15:53:04 +0400"
relations: {}
atom_id: "CA-R-1436"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1436-CORE_META_MODEL-CORE--define-is-allowed-value-of.md
  source_atom_id: CA-R-1436
  source_atom_revision: 10
  source_sha256: 605aa8acc2987b246fccede90a5ab99ce056c1d1e1265369d175265eda8f20d2
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define IS_ALLOWED_VALUE_OF

## Scope

the IS_ALLOWED_VALUE_OF Relation **in** the Entities Graph.

## Claim

an IS_ALLOWED_VALUE_OF Relation from value V **to** Property P **in** the Entities Graph **means** that governing authority admits V as a possible value of P **in** its qualified context; this Relation does **not** assign V **to** a particular Property occurrence **or** determine that Property's cardinality.

## Details

### relation admission

- Status: the IS_ALLOWED_VALUE_OF Relation Kind is Active.
