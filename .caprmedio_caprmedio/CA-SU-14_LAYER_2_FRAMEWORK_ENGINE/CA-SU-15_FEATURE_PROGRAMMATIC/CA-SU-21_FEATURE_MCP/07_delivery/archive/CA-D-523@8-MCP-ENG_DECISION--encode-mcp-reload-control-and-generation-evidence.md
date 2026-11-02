---
atom_id: CA-D-523@8
content_role: Delivery
current_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-26 00:46:35 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Architecture/Communication
  depends_on:
  - Subject/Graph Node/Engineering/MCP
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/Project
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Continuant/Atom
type: Eng Decision
tier: 3
---
# Summary

Encode MCP reload control and generation evidence

## Scope

server-side hot reload for the Project-local MCP gateway.

## Claim

the MCP gateway **must** carry reload requests **and** generation evidence through the following explicit interfaces.

## Details

- implementation belongs to 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP; preserve the existing --project-root binding **and** stdio transport.
- reload_mcp_implementation accepts **only** operation reload **and** a caller-chosen request_id. its Tool annotations declare read_only_hint=false, destructive_hint=false, idempotent_hint=true **and** open_world_hint=false.
- get_mcp_reload_status accepts an empty request **and** declares read_only_hint=true, destructive_hint=false, idempotent_hint=true **and** open_world_hint=false. it observes generation state without preparing, publishing **or** persisting a reload.
- arbitrary filesystem paths, shell commands **and** alternate Project roots are rejected. server annotations describe behavior; they do **not** override the client's permission policy.
- reload evidence carries request_id, outcome, previous_generation, active_generation, implementation_fingerprint, registry_fingerprint, registry_changed, notification_status, client_refresh_status **and** diagnostics.
- reload outcomes: reloaded, unchanged, rejected **or** failed. status reports the serving generation **and** in-flight counts without initiating reload.
- notification_status distinguishes sent, unsupported **and** failed; client_refresh_status defaults to unconfirmed.
- local operational generation receipts belong to .caprmedio_install/mcp_hot_reload/. they are execution evidence, **not** Atom authority.
- dependency isolation uses the declared Project runtime; reload does **not** install packages implicitly.
- the persistent gateway reloads registered implementations, **not** its own code **or** protocol runtime. gateway changes require explicit reconnect.
