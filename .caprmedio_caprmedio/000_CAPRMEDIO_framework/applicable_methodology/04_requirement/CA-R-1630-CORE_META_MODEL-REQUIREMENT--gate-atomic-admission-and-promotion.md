---
subjects:
  governs: "lifecycle"
  depends_on:
    ["Entity/Continuant/Object/Project.Framework Settings", "Default Settings"]
version: 28
updated_at: "2026-10-15 18:45:07 +0000"
relations:
  relates_to:
    - "CA-R-1439"
    - "CA-R-1655"
    - "CA-M-279"
atom_id: "CA-R-1630"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1630-CORE_META_MODEL-REQUIREMENT--gate-atomic-admission-and-promotion.md
  source_atom_id: CA-R-1630
  source_atom_revision: 28
  source_sha256: 869ba0ef5a767b8302be453ed9be4a17f00df22ed9f8b2a3a5f0a1a147425299
  original_relations_sha256: 80b2f5265b62c0afd0761c4128afd064ed11e545823c5d03cd99765f9d07b0cd
---
# Summary

Gate atomic admission and promotion

## Scope

atomic admission strictness settings and one-step promotion eligibility.

## Claim

the effective atomic admission strictness setting **must** be **in** (`medium`, `high`).

**at** medium strictness, CAPRMEDIO requires accepted authority, **`=1`** primary Claim, **`=1`** enabled Artifact Type, owning Scope, creation provenance, material relations, priority for Concern Atoms **only**, **and** sufficient precision **to** establish a stable Artifact identity **and** initial accepted Revision. optional non-authoritative context **may** remain explicitly unknown.

**at** high strictness, CAPRMEDIO stops **before** emission while **any** material authority, definition, boundary, classification, Scope, lineage, Conflict, **or** Evaluation question remains ambiguous. it asks focused questions **until** the Atom meets the same one-primary-Claim identity standard.

the two levels assess one-step promotion eligibility. promotion is proposed **only** **when** the Claim applies unchanged at the broader enabled Scope **and** always requires explicit Operator acceptance.

admission does **not** prohibit later same-ID Revisions. **every** later change passes the atomic change-class gate; changing the primary Claim identity requires a replacement.

## Details
