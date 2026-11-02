---
atom_id: CA-R-1935
content_role: Requirement
type: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-12 23:13:45 +0400"
subjects:
  governs: "Tool"
  depends_on: ["Workflow", "Property", "Scope Unit"]
relations:
  relates_to: [CA-R-1829, CA-M-375, CA-O-204, CA-O-205, CA-O-206]
---
# Summary

Share one TOML connector across configuration Workflows

## Scope

Logical edits of TOML-backed Project configuration, including Project Structure and Project Settings.

## Claim

Configuration Workflows **must** use the same TOML storage connector while retaining a distinct Workflow for each configuration. The Workflow owns the configuration's meaning, explicit requested delta, applicable schema, authorization and result; the connector owns TOML access and storage representation. Do not create a separate connector merely because the TOML configuration differs.

Before a write, read the complete current configuration, bind its revision or source pin, validate the complete proposed configuration against that configuration's applicable schema and recheck currentness and permission. Missing or ambiguous schema authority, invalid values, stale source or missing permission **must** prevent the write. Apply only the explicit approved delta and preserve unrelated configuration. A verified unchanged configuration is a no-op without a write or fictitious revision or timestamp.

CreateScopeUnit is a logical Scope Unit operation whose declared Project Structure change uses this same connector; a filesystem folder alone does not declare a Scope Unit. This Requirement creates no new configuration schema or Scope Unit.

## Details

Required connector and Workflow behavior is a specification, not a current implementation or execution receipt. Existing publication concurrency/access deferrals remain in force.
