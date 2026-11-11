---
atom_id: CA-R-1918
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/First runtime boundary"
  depends_on: [Tool, Runtime, Project, Framework Package, Skill]
relations:
  relates_to: [CA-R-1881, CA-D-598, CA-D-599]
---
# Summary

Keep first runtime initialization empty and package-bound

## Scope

the relationship between a preexisting reusable package and first target runtime activation.

## Claim

the INSTALL_TOOLS facade **must** permit an admitted preexisting package selector while requiring an empty target runtime boundary for first activation, and **must not** reinterpret adoption as upgrade of an active runtime.

## Details

Adoption may validate existing Project metadata only. An existing target selector, retained runtime release, nonempty runtime state or public `ca` Skill blocks first activation under CA-R-1881. Upgrade and idempotency of an active target runtime require a distinct later contribution and cannot be inferred from package selection.
