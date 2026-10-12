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
  depends_on: [Workflow, Step, Action, Methodology, Implementation, Skill, Permission]
version: 5
updated_at: "2026-10-12 00:00:51 +0000"
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-169]
---
# Summary

Install the runtime and project-local ca Skill

## Step

This Step invokes CA-O-169 once with phase `install` to copy compiled `101_FRAMEWORK_METHODOLOGY/`, preserve protected configuration and Project state, install Engine `.install` into the Project runtime package, and install the `ca` payload.

## Details

Only this Step clears replaceable installed Framework members, copies the product as-is, installs `ca`, and restarts or reuses Project MCP for Docker/MCP smoke. It preserves settings and Project state, does not alter authoring, push, create a PR, or retry an uncertain effect.
