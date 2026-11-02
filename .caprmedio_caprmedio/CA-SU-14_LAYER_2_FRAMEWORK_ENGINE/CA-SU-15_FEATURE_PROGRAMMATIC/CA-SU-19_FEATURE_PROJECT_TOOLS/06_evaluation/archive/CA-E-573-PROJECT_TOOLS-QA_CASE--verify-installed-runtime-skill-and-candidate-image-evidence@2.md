---
atom_id: CA-E-573
content_role: Evaluation
type: QA Case
current_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-12 00:00:00 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Installed-delivery QA"
  depends_on: [Tool, Runtime, Skill, Image]
relations:
  evaluation_for: [CA-R-1877, CA-R-1878, CA-M-332]
---
# Summary

Verify direct installed delivery

## Scope

The installed project runtime and `ca` Skill after a direct Local release.

## Claim

The QA case verifies the installed package/runtime and project-local `ca` Skill, then runs the intended Docker/MCP smoke behavior. A failed check stops the release and is reported for manual handling.

## Details

This case does not require a sealed manifest, candidate identity, full-suite aggregation, or promotion state.
