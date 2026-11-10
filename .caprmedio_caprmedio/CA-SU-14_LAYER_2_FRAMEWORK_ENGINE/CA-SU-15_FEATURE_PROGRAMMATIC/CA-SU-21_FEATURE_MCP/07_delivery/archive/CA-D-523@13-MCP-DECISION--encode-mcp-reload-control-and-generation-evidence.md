---
atom_id: CA-D-523
ref_id: CA-D-523@13
container:
  scope_unit: CA-SU-21
role: Delivery
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
tier: 3
status: Archived
version: 13
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-D-523@13-MCP-DECISION--encode-mcp-reload-control-and-generation-evidence.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/07_delivery/archive
current_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

Encode MCP reload control and generation evidence

## Claim

### Prose Claim

the MCP gateway **must** carry reload requests **and** generation evidence through the following explicit interfaces.

## Details

### Scope

server-side hot reload for the Project-local MCP gateway, only when explicitly enabled.

Use `CAPRMEDIO_HOT_RELOAD=1` for explicit startup opt-in; an absent or other value leaves hot reload disabled. Default startup uses one MCP process and omits reload-only control tools. Restart the process/container to apply code changes in default mode. Forward this switch explicitly through Docker service environments, defaulting to disabled.

- implementation belongs to LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP; preserve the existing --project-root binding **and** stdio transport.
- reload_mcp_implementation accepts **only** operation reload **and** a caller-chosen request_id. its Tool annotations declare read_only_hint=false, destructive_hint=false, idempotent_hint=true **and** open_world_hint=false.
- get_mcp_reload_status accepts an empty request **and** declares read_only_hint=true, destructive_hint=false, idempotent_hint=true **and** open_world_hint=false. it observes generation state without preparing, publishing **or** persisting a reload.
- arbitrary filesystem paths, shell commands **and** alternate Project roots are rejected. server annotations describe behavior; they do **not** override the client's permission policy.
- reload evidence carries request_id, outcome, previous_generation, active_generation, implementation_fingerprint, registry_fingerprint, registry_changed, notification_status, client_refresh_status **and** diagnostics.
- reload outcomes: reloaded, unchanged, rejected **or** failed. status reports the serving generation **and** in-flight counts without initiating reload.
- notification_status distinguishes sent, unsupported **and** failed; client_refresh_status defaults to unconfirmed.
- local operational generation receipts belong to .caprmedio_install/mcp_hot_reload/. they are execution evidence, **not** Atom authority.
- dependency isolation uses the declared Project runtime; reload does **not** install packages implicitly.
- the persistent gateway reloads registered implementations, **not** its own code **or** protocol runtime. gateway changes require explicit reconnect.
