---
subjects:
  governs: Subject/Graph Node/Engineering/Authoring
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Expansion Boundary
  - Subject/Graph Node/Product/Extension
  - Subject/Graph Node/Domain/Continuant/Scope Unit//PROJECT_CONFIGURATION
  - Subject/Graph Node/Domain/Continuant/Scope Unit//CORE_META_MODEL
version: 18
updated_at: 2026-10-27 06:04:45 +0400
relations:
  child_of:
  - CA-M-006
  method_for:
  - CA-R-1375
atom_id: CA-M-298@18
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Implementation Method
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
