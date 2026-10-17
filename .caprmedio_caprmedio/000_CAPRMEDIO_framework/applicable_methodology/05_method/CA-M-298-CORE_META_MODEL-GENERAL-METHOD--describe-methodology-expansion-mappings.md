---
subjects:
  governs: "Methodology Source.Expansion Mapping"
  depends_on:
    - "Methodology Source"
    - "Extension"
    - "Project Configuration"
    - "Core Meta-Model"
version: 6
updated_at: "2026-10-15 12:20:00 +0000"
relations: {child_of: [CA-M-006], method_for: [CA-R-1375]}
atom_id: "CA-M-298"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/05_method/CA-M-298-CORE_META_MODEL-GENERAL-METHOD--describe-methodology-expansion-mappings.md
  source_atom_id: CA-M-298
  source_atom_revision: 6
  source_sha256: 1a651f5cfa58b453cc9a1d038274e518bc36c8b7e5f37786404debd6bad83f1d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Describe methodology expansion mappings

## Scope

Methodology Source expansion mappings.

## Claim

**to** describe a Methodology Source expansion mapping, use **`=1`** explicit mapping description that identifies:

- the source element **and** its provenance;
- the exact canonical target;
- the mapping rule;
- the intended scope of application;
- the applicable Core Meta-Model distinctions at **any** Local Tier.

apply this same mapping convention **to** Extension **and** Project Configuration sources regardless of provenance. the convention supports CA-R-1375-CORE_META_MODEL-CORE-REQUIREMENT--restrict-methodology-source-expansion-to-core-permission's expansion boundary; it does **not** admit activation **or** reliance. CA-O-054-CORE_META_MODEL-ACTION--admit-methodology-expansion-mappings owns that admission Action **and** re-evaluation following material changes.

## Details
