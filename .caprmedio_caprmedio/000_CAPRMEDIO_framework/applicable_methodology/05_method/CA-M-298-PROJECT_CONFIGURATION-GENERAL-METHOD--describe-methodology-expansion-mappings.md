---
subjects:
  governs: "Methodology Source.Expansion Mapping"
  depends_on:
    - "Methodology Source"
    - "Extension"
    - "Project Configuration"
    - "Core Meta-Model"
version: 7
updated_at: "2026-10-19 14:46:08 +0400"
relations: {child_of: [CA-M-006], method_for: [CA-R-1375]}
atom_id: "CA-M-298"
content_role: "Method"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/05_method/CA-M-298-PROJECT_CONFIGURATION-GENERAL-METHOD--describe-methodology-expansion-mappings.md
  source_atom_id: CA-M-298
  source_atom_revision: 7
  source_sha256: a51743a0f59b6e8a001359172d414f4edb17eeaf1c7a8056889c2fad9290f314
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
