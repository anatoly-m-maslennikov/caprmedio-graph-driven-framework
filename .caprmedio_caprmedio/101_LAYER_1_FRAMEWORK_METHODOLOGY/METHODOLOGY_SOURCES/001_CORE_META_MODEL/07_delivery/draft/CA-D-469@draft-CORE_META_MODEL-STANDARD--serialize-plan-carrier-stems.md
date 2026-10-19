---
subjects:
  governs: "Entity/Carrier/File Carrier.Filename"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Plan", "Entity/Node/Continuant/Atom/Content Role: Plan.Label", "Entity/Node/Continuant/Atom/Content Role: Plan.Work Sequence Number", "Entity/Node/Continuant/Atom.Summary", "Entity/Node/Continuant/Atom.ID", "Entity/Carrier"]
version: 9
updated_at: "2026-10-19 11:47:10 +0000"
relations: {"relates_to": ["CA-R-1576", "CA-R-991", "CA-D-381", "CA-D-282", "CA-D-284", "CA-D-460", "CA-R-997"]}
atom_id: "CA-D-469@draft"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
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
