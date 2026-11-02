---
atom_id: CA-P-2692@1
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Formal Model
version: 1
updated_at: 2026-10-28 20:00:14 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2683
tier: 4
---
# Summary

Retire superseded contracts after preserving their meanings

## Objective

Retire superseded contracts after preserving their meanings.

## Details

After CA-P-2691.

Identify obsolete separate Graph Rule entity/Type/carrier/authoring declarations and other contracts superseded by the adopted model. Transfer any still-needed structure, constraints and meanings into the relevant Definition Claims before archiving the obsolete source. Do not archive a source merely because its name is old.

Find and repair in-scope typed consumers before retirement. A Current relation must not silently become a link to an archived-only target. Keep a concrete retirement unresolved if required Engine consumers cannot be repaired within scope; coordinate that dependency with P2637 rather than expanding this Epic. Existing historical versions remain history and are not normalized.

Mark the earlier superseded Draft packet as non-promotable and prevent a later accidental adoption of the old Graph Rule population or separate Claim arrangement.

## Definition of Done

Each retired source has a meaning-preservation disposition and safe Current consumers; no unresolved retirement or lost constraint is hidden behind an archive operation.

## Progress

Not started. Prior analysis and Drafts are inputs, not completion evidence.
