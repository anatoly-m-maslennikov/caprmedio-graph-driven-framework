---
subjects:
  governs: Subject/Engineering/Carrier/File Carrier.Filename
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan.Label'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan.Work Sequence Number'
  - Subject/Domain/Node/Continuant/Atom.Summary
  - Subject/Domain/Node/Continuant/Atom.ID
  - Subject/Engineering/Carrier
version: 13
updated_at: 2026-10-24 00:51:05 +0400
relations:
  relates_to:
  - CA-R-1576
  - CA-R-991
  - CA-D-381
  - CA-D-282
  - CA-D-284
  - CA-D-460
  - CA-R-997
atom_id: CA-D-469@13
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Serialize Plan Carrier stems

## Scope

identified Plan Carrier stems.

## Claim

**every** identified Plan Carrier stem **must** use `[<WORK_SEQUENCE_NUMBER>-]<ATOM_ID>[-<LABEL>]--<SUMMARY_SLUG>`, with `.md` **only** on its File Carrier.

- the optional Label is a navigation token, **not** an Atom Type token; normalize it under CA-D-284.
- render the Summary under CA-D-282.
- **by default**, direct Plans decomposing the same Hub use unique leading Work Sequence Numbers **before** their Atom IDs, under CA-D-381 **and** CA-R-997.
- a same-bundle Directory Carrier **and** File Carrier use the same stem; number **or** Label changes preserve Atom identity **and** do **not** declare `BLOCKS`.

## Details
