---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Governing Configuration
version: 37
updated_at: 2026-10-27 19:59:59 +0400
relations: {}
atom_id: CA-R-1630
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Rule
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
