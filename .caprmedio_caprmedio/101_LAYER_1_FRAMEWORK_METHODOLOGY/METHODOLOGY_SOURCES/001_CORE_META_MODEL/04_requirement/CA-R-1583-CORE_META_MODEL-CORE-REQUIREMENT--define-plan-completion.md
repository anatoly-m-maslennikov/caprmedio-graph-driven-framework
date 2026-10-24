---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan.Status: Done'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan.Definition of Done'
  - Subject/Engineering/Carrier/File Carrier
version: 15
updated_at: 2026-10-24 01:37:42 +0400
relations:
  relates_to:
  - CA-R-1575
  - CA-R-1579
  - CA-R-1599
  - CA-R-1539
atom_id: CA-R-1583
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define Plan completion

## Scope

Plan completion.

## Claim

Plan Status Done **means** that **all** applicable completion conditions hold:

- the Plan satisfies CA-R-1575; absence of work **and** decomposition **must not** count as completion.
- its own work, **if** present, is complete.
- **every** directly decomposed Plan is Done.
- its Definition of Done falsifying Condition Expression evaluates **to** false.

a Hub requires its own Definition of Done **and** completion of its decomposed Plans; Canceled **or** Archived work does **not** satisfy Done.

## Details
