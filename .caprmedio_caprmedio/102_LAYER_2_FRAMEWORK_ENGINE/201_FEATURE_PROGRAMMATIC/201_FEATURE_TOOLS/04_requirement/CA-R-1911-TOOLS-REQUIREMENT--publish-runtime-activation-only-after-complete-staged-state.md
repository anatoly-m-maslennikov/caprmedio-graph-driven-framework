---
atom_id: CA-R-1911
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-09 17:01:07 +0400"
subjects:
  governs: "Framework Installation contribution/Activation order"
  depends_on: [Tool, Runtime, Skill, Projection, State]
relations:
  relates_to: [CA-D-599, CA-D-601, CA-D-603]
---
# Summary

Publish runtime activation only after complete staged state

## Scope

the publication order for one isolated target runtime.

## Claim

the INSTALL_TOOLS facade **must** publish a target runtime selector **only after** its complete Skill, wrappers, projection and state generation reopen successfully, and **must not** expose staged state as active.

## Details

The target selector is the sole activation point. Its shared lock is held through staged verification and atomic replacement. A failed Skill, wrapper, projection or state publication before replacement retains actual evidence and keeps the prior selection authoritative. Default mutable configuration is created only if `.caprmedio_runtime/config.toml` is absent; existing configuration bytes are retained across activation, upgrade, rollback and recovery. A Journal failure after selector replacement retains and reopens the actual new selected bytes as `recording_pending`; it does not claim that state non-active, roll it back, replay activation or start another Run. Recovery records only the missing terminal Event after original selector, package, context and started-Run evidence agree.
