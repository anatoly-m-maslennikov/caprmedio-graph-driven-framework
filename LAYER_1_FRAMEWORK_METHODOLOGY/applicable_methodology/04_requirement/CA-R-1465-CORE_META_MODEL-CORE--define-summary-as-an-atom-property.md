---
subjects:
  governs: "Entity/Node/Continuant/Atom.Summary"
  depends_on:
    ["Entity/Node/Continuant/Atom", "Property", "Entity/Node/Continuant/Atom.Substance", "Atom/Content Role", "Markdown Atom Carrier.Main Content"]
version: 12
updated_at: "2026-10-20 03:03:18 +0400"
relations: {}
atom_id: "CA-R-1465"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1465-CORE_META_MODEL-CORE--define-summary-as-an-atom-property.md
  source_atom_id: CA-R-1465
  source_atom_revision: 12
  source_sha256: a81b93e3073aa3e24cb91b103924be9cebf9af3e022ee8627e8135e61760756f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Summary as an Atom Property

## Scope

the Summary Property of an Atom.

## Claim

a Summary **means** a short, non-authoritative navigation Property of **`=1`** Atom, derived from the finalized primary contribution registered for its Content Role, read within its applicability. it belongs **to** that Atom **without** independent identity, lifecycle, **or** authority.

## Details

for ordinary RMED, the source is Claim read within Scope, **not** Scope alone; for Analysis, Question; for Concern, Concern; for Plan, Objective; for Operations, Operation. For a formal R/Type: Graph Rule, the source is the operative structured YAML under CA-D-637; Claim and Substance sections are not required or supplied by this definition. Summary is written last but remains displayed first. Analysis TLDR summarizes its Results; it is **not** the Atom Summary **and** does **not** replace Question as the Summary source.
