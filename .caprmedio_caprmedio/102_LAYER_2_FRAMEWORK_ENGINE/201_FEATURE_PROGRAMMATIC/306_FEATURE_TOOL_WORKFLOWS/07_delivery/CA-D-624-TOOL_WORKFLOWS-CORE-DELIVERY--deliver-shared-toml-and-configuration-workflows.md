---
atom_id: CA-D-624
content_role: Delivery
type: Eng Decision
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/Engineering/Configuration/Shared TOML Workflow Delivery
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Scope Unit//PROJECT_CONFIGURATION
  - Subject/Domain/Node/Continuant/Scope Unit
version: 7
updated_at: 2026-10-24 02:14:24 +0400
relations:
  delivery_for:
  - CA-R-1935
  relates_to:
  - CA-M-375
  - CA-O-204
  - CA-O-205
  - CA-O-206
  - CA-O-218
  - CA-D-631
  - CA-O-219
  - CA-O-220
tier: 2
---
# Summary

Deliver shared TOML and configuration workflows

## Scope

Workflow admission owns identity, Version/time, lifecycle and complete schema decisions. Connector calls use CA-D-625 only to verify the supplied request, source preconditions and permission and to perform the explicit mechanical operation. A connector does not choose those decisions.

The required shared TOML connector and configuration-specific workflow delivery contract under TOOL_WORKFLOWS. It establishes no additional configuration connector, storage backend or runtime path.

## Claim

one shared TOML connector under CONNECTOR_TOOLS supplies CA-O-218 complete Read under CA-D-631 **and** CA-O-204 Modify under CA-D-625 for admitted configuration sources. The Project Structure and Project Settings workflows each supply their own complete schema/domain validation and permission/currentness boundary.

## Details

Within the existing service envelope, a configuration workflow carries its explicit configuration kind, admitted logical source identity, exact expected source revision/digest, complete proposed TOML delta and applicable schema/validation evidence. The workflow parses and validates the complete proposed configuration before its effect; the connector verifies the supplied admission evidence and rechecks expected source state and permission without choosing the schema. No arbitrary filename or configuration kind can grant authority. Project Structure and Project Settings retain their configured authoritative TOML identities; their workflows reject generated/protected field edits and preserve unrelated values. Configuration-source bindings remain private adapter details, not new connector identities.

The TOML connector returns the exact bound state and proposed or observed result with source-state evidence. It does not choose a configuration schema, invent a Scope Unit or weaken the workflow's validation. Project Structure changes, including Scope Unit Create, follow its structural schema; Project Settings changes follow its settings schema. CA-O-205 uses CA-O-219 Read **before** CA-O-209 Modify; CA-O-206 uses CA-O-220 Read **before** CA-O-210 Modify. their read Steps call the same CA-O-218 Action. complete successful Read data **and** observed source-state evidence become explicit patch-Step inputs **before** proposal validation. their patch Steps call the same CA-O-204 Action. no Workflow reads storage itself **or** assumes that Modify implies Read support.

Return actual source revision/effect observations and explicit validation, stale, denied, failed, uncertain or no-op results through the existing shared result/recording contract. Physical TOML carrier names remain current adapter bindings. Preserve prior admitted configuration and accepted history within each action's claimed safety boundary; a serialization contract does not prove atomic publication.

### Delivery status

This is required future delivery, not implementation, installation, admitted MCP routing, DB support or stronger concurrency/publication proof. Configuration workflows do not multiply connectors. New workflow resume/retry and previously deferred publication/concurrency work remain deferred.
