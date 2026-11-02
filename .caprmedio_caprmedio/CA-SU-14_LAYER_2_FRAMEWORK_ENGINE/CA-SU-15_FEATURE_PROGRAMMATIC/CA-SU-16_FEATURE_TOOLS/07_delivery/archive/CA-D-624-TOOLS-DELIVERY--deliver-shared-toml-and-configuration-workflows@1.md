---
atom_id: CA-D-624
content_role: Delivery
type: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool"
  depends_on: ["Workflow","Project Configuration","Scope Unit"]
version: 1
updated_at: "2026-10-12 23:13:13 +0400"
relations:
  delivery_for: ["CA-R-1935"]
  relates_to: ["CA-M-375","CA-O-204","CA-O-205","CA-O-206"]
---
# Summary

Deliver shared TOML and configuration workflows

## Scope

The required shared TOML connector and configuration-specific workflow delivery contract under TOOLS. It establishes no additional configuration connector, storage backend or runtime path.

## Claim

One TOML connector carries the mechanical read/proposed-write boundary for admitted configuration sources. The Project Structure and Project Settings workflows each supply their own complete schema/domain validation and permission/currentness boundary.

## Details

Within the existing service envelope, a configuration workflow carries its explicit configuration kind, admitted logical source identity, exact expected source revision/digest, complete proposed TOML delta and applicable schema/validation evidence. Parse and validate the complete proposed configuration before its effect, then recheck expected source state and permission. No arbitrary filename or configuration kind can grant authority. Project Structure and Project Settings retain their configured authoritative TOML identities; their workflows reject generated/protected field edits and preserve unrelated values. Configuration-source bindings remain private adapter details, not new connector identities.

The TOML connector returns the exact bound state and proposed or observed result with source-state evidence. It does not choose a configuration schema, invent a Scope Unit or weaken the workflow's validation. Project Structure changes, including Scope Unit Create, follow its structural schema; Project Settings changes follow its settings schema. O205/O206 remain distinct workflows using the same O204 connector action.

Return actual source revision/effect observations and explicit validation, stale, denied, failed, uncertain or no-op results through the existing shared result/recording contract. Physical TOML carrier names remain current adapter bindings. Preserve prior admitted configuration and accepted history within each action's claimed safety boundary; a serialization contract does not prove atomic publication.

### Delivery status

This is required future delivery, not implementation, installation, admitted MCP routing, DB support or stronger concurrency/publication proof. Configuration workflows do not multiply connectors. New workflow resume/retry and previously deferred publication/concurrency work remain deferred.
