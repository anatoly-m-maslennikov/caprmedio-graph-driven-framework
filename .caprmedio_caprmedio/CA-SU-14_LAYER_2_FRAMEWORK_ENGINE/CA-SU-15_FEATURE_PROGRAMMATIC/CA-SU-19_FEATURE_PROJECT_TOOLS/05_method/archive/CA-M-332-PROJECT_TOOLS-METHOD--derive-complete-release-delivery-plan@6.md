---
atom_id: CA-M-332
content_role: Method
current_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 6
updated_at: "2026-10-12 00:00:00 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Direct delivery"
  depends_on: [Tool, Methodology, Runtime, Skill, Image]
relations:
  method_for: [CA-R-1877, CA-R-1878]
---
# Summary

Deliver one selected release directly

## Scope

The direct Local release path from active Methodology source through compilation, package installation, runtime/Skill verification, and Docker/MCP smoke.

## Claim

The Tool copies the selected active source, compiles it, prepares the package, installs the selected project runtime and `ca` Skill, and runs the intended Docker/MCP smoke checks. It stops and reports a failed step; it does not seal a candidate, aggregate a gate, or recover a prior attempt.

## Details

Before each Local release step and at completion, inspect Git state. Preserve the project's runtime configuration and do not modify authoritative sources during delivery. Use only project-owned Docker images for cleanup, retaining any image that is in use or cannot be identified as owned by the project.
