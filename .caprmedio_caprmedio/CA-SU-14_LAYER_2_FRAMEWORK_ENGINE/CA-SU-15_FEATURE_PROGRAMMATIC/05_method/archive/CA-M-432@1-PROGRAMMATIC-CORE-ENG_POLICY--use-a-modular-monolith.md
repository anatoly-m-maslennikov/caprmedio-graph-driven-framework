---
atom_id: CA-M-432@1
content_role: Method
type: Eng Policy
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Core
global_tier: 6
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: 2026-10-23 17:46:12 +0400
subjects:
  governs: Subject/Engineering/Runtime Architecture
  depends_on: []
---
# Summary

Use a modular monolith

## Scope

New or changed PROGRAMMATIC runtime implementation, including all descendant
Scope Units that contribute to that runtime.

## Claim

Implement the PROGRAMMATIC runtime as one modular application with shared queue
and run state. Keep clear module boundaries aligned with Scope Unit
responsibilities. Do not introduce separate services or internal network APIs
merely to separate Scope Units.

## Details

Adapters, Single Actions, schedulers, Workflows, the Action Engine and MCP retain
distinct responsibilities within the shared runtime. Scope Units define
responsibility and ownership, not deployment boundaries.
