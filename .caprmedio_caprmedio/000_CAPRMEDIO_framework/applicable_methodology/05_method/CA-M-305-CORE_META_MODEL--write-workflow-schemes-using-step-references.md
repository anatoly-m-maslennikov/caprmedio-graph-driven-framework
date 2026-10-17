---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Object/Relation/Type: On Result"]
version: 6
updated_at: "2026-10-16 12:09:04 +0000"
relations: {"method_for": ["CA-R-1570"]}
atom_id: "CA-M-305"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/05_method/CA-M-305-CORE_META_MODEL--write-workflow-schemes-using-step-references.md
  source_atom_id: CA-M-305
  source_atom_revision: 6
  source_sha256: 38cbdf3dce76f71cc30c7f12dc6cb327a1f5888001164cac1cf7dfee968e7dba
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Write Workflow schemes using Step references

## Scope

Workflow schemes using Step references.

## Claim

**to** write a Workflow scheme, express the graph through references **to** its Step Atoms:

- use **`=1`** unambiguous reference for **every** graph node; readable node labels **may** accompany those references.
- state the entry, typed directed transitions, result conditions, **and** terminal outcomes against those nodes.
- place Action references **and** parameter/input bindings **in** the referenced Step Atoms rather than reproducing them **in** the scheme.
- reference reusable Action behavior from the Steps; do **not** paste it into either the Step **or** graph Claim.

## Details
