---
atom_id: CA-O-178
content_role: Operations
type: Step
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: install product and refresh Project MCP"
  depends_on: [Workflow, Step, Action, Version, Methodology, Implementation, Skill, Permission, Journal]
version: 4
updated_at: "2026-10-10 19:05:19 +0400"
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-169]
---
# Summary

Promote the candidate runtime and project-local ca Skill

## Step

This Step invokes CA-O-169 once with phase `install`, binding the passing full-suite preflight, exact compiled `101_FRAMEWORK_METHODOLOGY/` product, protected configuration and Project state, Engine/package/runtime inputs, and the bound `ca` payload.

## Details

Only this Step clears replaceable installed Framework members, copies the product as-is, installs `ca`, and restarts or reuses Project MCP for smoke. It preserves settings and Project state, does not alter authoring, push, create a PR, or retry an uncertain effect.
