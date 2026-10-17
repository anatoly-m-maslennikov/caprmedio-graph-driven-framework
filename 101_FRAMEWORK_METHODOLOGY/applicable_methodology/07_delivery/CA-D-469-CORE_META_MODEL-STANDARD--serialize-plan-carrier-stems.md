---
subjects:
  governs: "Entity/Carrier/File Carrier.Filename"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Plan", "Entity/Continuant/Object/Atom/Content Role: Plan.Label", "Entity/Continuant/Object/Atom/Content Role: Plan.Work Sequence Number", "Entity/Continuant/Object/Atom.Summary", "Entity/Continuant/Object/Atom.ID", "Entity/Carrier"]
version: 7
updated_at: "2026-10-16 12:09:33 +0000"
relations: {"relates_to": ["CA-R-1576", "CA-R-991", "CA-D-381", "CA-D-282", "CA-D-284", "CA-D-460", "CA-R-997"]}
atom_id: "CA-D-469"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-469-CORE_META_MODEL-STANDARD--serialize-plan-carrier-stems.md
  source_atom_id: CA-D-469
  source_atom_revision: 7
  source_sha256: a09a83dd339eadf0258e9f57b8643ebf1be5d7bb9035f0446e9650bceab38449
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
