---
atom_id: CA-D-609
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Approved legacy cleanup"
  depends_on: [Tool, Runtime, Operator, Journal, Manifest]
relations:
  delivery_for: [CA-R-1916, CA-E-609, CA-M-364]
---
# Summary

Encode later approved legacy cleanup carrier

## Scope

One separately authorized post-migration cleanup of an exact retained legacy inventory.

## Claim

the INSTALL_TOOLS facade **must** admit legacy cleanup **only** from a later exact Operator-approved cleanup carrier, and **must not** couple cleanup to installation, migration or selector activation.

## Details

`.caprmedio_runtime/installation/migrations/<migration_id>/cleanup-approval.toml` contains `schema_version = 1`, migration ID, inventory SHA-256, target context SHA-256, exact ordered removable relative paths, approval reference and approval digest. It is valid only after a completed and reopened CA-D-606 switch plus retained CA-D-607 history; it never authorizes broad-root, glob or inferred-path deletion.

`cleanup-result.toml` records every pre-delete revalidation, actual removed path and terminal outcome. Changed inventory, active or uncertain owned process, missing approval, mismatched context, unresolved migration or unavailable terminal recording refuses without deletion. Historical migration and retained package evidence remain intact.
