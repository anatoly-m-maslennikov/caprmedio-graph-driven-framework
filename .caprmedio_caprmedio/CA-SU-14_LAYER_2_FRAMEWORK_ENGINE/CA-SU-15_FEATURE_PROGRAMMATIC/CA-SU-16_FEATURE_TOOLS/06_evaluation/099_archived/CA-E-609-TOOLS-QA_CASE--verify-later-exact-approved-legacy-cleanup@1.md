---
atom_id: CA-E-609
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Cleanup acceptance"
  depends_on: [Tool, Runtime, Operator, Manifest, Journal]
relations:
  evaluation_for: [CA-R-1916, CA-R-1919, CA-M-364, CA-D-609]
---
# Summary

Verify later exact approved legacy cleanup

## Scope

the post-migration cleanup and refusal boundary.

## Claim

the QA case **must** permit cleanup **only** after separate exact approval and revalidation of the retained inventory, and **must not** delete on installation, migration, wildcard or stale approval.

## Details

The positive fixture has a completed migration, inactive proven-owned processes and an approval listing exact relative paths. Negative fixtures omit approval, alter context/inventory, add a path, retain active/uncertain process or terminal failure; no path is removed. Goldens preserve prior N/history, package and Journal evidence after every case.
