---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary
version: 27
updated_at: 2026-10-27 19:59:39 +0400
relations: {}
atom_id: CA-M-116
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Implementation Method
---
# Summary

Derive navigation Projections from the CCE Claim

## Scope

navigation values derived from an Atom Claim.

## Claim

**to** derive navigation values from an Atom Claim, the Generator **must** derive the concise human-readable Summary **when** creating the Atom **and** derive requested Translations directly from the Claim, **without** adding authoritative meaning. choose wording under CA-M-294-CORE_META_MODEL-METHOD--use-simpler-words-without-losing-meaning. for an existing Atom identity, retain **and** check the Summary under CA-R-1273-CORE_META_MODEL-CORE-REQUIREMENT--keep-summary-source-faithful **and** CA-R-1464-CORE_META_MODEL-REQUIREMENT--keep-summary-fixed-for-atom-identity rather than regenerating it as an independent Projection.

## Details
