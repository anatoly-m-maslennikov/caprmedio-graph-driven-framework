---
subjects:
  governs: Subject/Graph Node/Carrier/File.Filename
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Label'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Work Sequence Number'
  - Subject/Graph Node/Domain/Continuant/Atom.Summary
  - Subject/Graph Node/Domain/Continuant/Atom.ID
  - Subject/Graph Node/Carrier
version: 19
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-D-469@19
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
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
