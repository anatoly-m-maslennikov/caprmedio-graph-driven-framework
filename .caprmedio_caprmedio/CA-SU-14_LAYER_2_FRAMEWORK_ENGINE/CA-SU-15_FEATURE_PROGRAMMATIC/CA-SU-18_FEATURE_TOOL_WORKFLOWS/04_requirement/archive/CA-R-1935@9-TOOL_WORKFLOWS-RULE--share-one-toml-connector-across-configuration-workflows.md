---
atom_id: CA-R-1935@9
content_role: Requirement
type: Rule
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
status: Archived
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-26 05:59:45 +0400
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Governing Configuration
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Continuant/Scope Unit
relations: {}
tier: 1
---
# Summary

Share one TOML connector across configuration Workflows

## Scope

Logical edits of TOML-backed Project configuration, including Project Structure and Project Settings.

## Claim

Configuration Workflows **must** use the same TOML storage connector while retaining a distinct Workflow for each configuration. The Workflow owns the configuration's meaning, explicit requested delta, applicable schema, authorization and result; the connector owns TOML access and private storage representation through CA-R-1936-CONNECTOR_TOOLS-RULE--use-one-coherent-connector-interface. Workflows supply logical targets, deltas, schema, source-view and authorization bindings; they do not encode backend paths, table names or storage query languages. Replacing the backend changes the connector binding or implementation, not the configuration Workflow's meaning or sequence. Do not create a separate connector merely because the TOML configuration differs.

Before a write, read the complete current configuration, bind its revision or source pin, validate the complete proposed configuration against that configuration's applicable schema and recheck currentness and permission. Missing or ambiguous schema authority, invalid values, stale source or missing permission **must** prevent the write. Apply only the explicit approved delta and preserve unrelated configuration. A verified unchanged configuration is a no-op without a write or fictitious revision or timestamp.

CreateScopeUnit is a logical Scope Unit operation whose declared Project Structure change uses this same connector; a filesystem folder alone does not declare a Scope Unit. This Requirement creates no new configuration schema. Its Workflow authority belongs to TOOL_WORKFLOWS; connector mechanics belong to the separately declared CONNECTOR_TOOLS Feature.

## Details

Required connector and Workflow behavior is a specification, not a current implementation or execution receipt. Existing publication concurrency/access deferrals remain in force.
