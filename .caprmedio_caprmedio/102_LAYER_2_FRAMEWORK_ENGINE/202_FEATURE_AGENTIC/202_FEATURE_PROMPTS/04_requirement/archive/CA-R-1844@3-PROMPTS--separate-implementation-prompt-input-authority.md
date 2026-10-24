---
atom_id: CA-R-1844@3
content_role: Requirement
type: Requirement
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: 2026-10-24 01:18:03 +0400
subjects:
  governs: Subject/Engineering/Prompt Construction/Action Instructions
  depends_on:
  - Subject/Engineering/Prompt
  - Requirement
  - Delivery
  - Method
  - Evaluation
relations:
  relates_to:
  - CA-O-017
  - CA-O-018
  - CA-O-019
  - CA-O-020
tier: 3
---
# Summary

Separate implementation prompt input authority

## Scope

the admitted input packet passed to one current Implementation Workflow prompt.

## Claim

the Implementation **must** carry selected active R/D targets as what to implement, one verified complete active-M projection as how to implement, and applicable E atoms as separate checks, each with identity, revision, path, digest, and full required content.

## Details

The M projection is a derived Run input, sorted repeatably and retained downstream; membership does not establish applicability. Missing, stale, conflicting, unauthorized, or incomplete inputs return the source Step's blocked result.
