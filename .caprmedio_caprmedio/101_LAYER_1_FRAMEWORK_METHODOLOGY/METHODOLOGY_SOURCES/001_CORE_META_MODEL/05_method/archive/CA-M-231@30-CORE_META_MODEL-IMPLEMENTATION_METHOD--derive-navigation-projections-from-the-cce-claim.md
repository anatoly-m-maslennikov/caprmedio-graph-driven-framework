---
subjects:
  governs: Entity/Object/Continuant/Projection
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity/Object/Continuant/Governing Objects/Atom.Content.Summary
version: 30
updated_at: 2026-10-29 07:17:22 +0400
relations: {}
atom_id: CA-M-231@30
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Implementation Method
---
# Summary

Derive Navigation Projections from the CCE Claim

## Scope

derivation of an Atom's navigation values from its authoritative content.

## Claim

**to** derive an Atom's navigation values, derive them from authoritative content rather than another navigation value:

- derive a new Atom's Summary from its finalized primary contribution within its applicability under CA-R-1465 **and** CA-M-111. for RMED, use Claim read within Scope, **not** Scope alone.
- derive **every** requested Projection from its applicable complete source content, including relevant textual applicability restrictions, **not** from the Summary.
- for an existing Atom identity, retain its Summary **and** check source faithfulness. a needed Summary change follows CA-R-1464 **and** **must not** be applied as a same-identity refresh.

## Details
