---
atom_id: CA-R-1904
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Target context and generation"
  depends_on: [Tool, Runtime, Project, State, Manifest]
relations:
  relates_to: [CA-D-599, CA-D-600, CA-D-604]
---
# Summary

Bind each runtime to target context and state generation

## Scope

the active installation identity for one target Project.

## Claim

the INSTALL_TOOLS facade **must** bind each activated runtime to **=1** reopened target-project context and monotonic state generation, and **must not** identify it by package or PID alone.

## Details

The activation selector carries the package manifest SHA-256, target context SHA-256, state generation, installation lock generation and image digest. The context binds explicit root/control child, bootstrap-or-adopt mode and verified settings, Structure and registry digests. A changed target input, generation, selector, package or image refuses activation.
