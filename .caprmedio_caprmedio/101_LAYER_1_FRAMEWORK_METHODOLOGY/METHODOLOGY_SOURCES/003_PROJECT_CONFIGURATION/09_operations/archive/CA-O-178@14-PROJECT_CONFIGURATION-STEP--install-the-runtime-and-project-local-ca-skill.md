---
atom_id: CA-O-178@14
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step//Release Version/Step: install product and refresh Project MCP'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Applicable Methodology'
  - Subject/Graph Node/Engineering/Delivery
  - Subject/Graph Node/UX/CAPRMEDIO Skill and MCP Entry Interface
  - Subject/Graph Node/Engineering/Execution Control/Effect Authorization
version: 14
updated_at: 2026-10-27 06:04:45 +0400
relations:
  part_of:
  - CA-O-164
  invokes:
  - CA-O-169
tier: 3
---
# Summary

Install the runtime and project-local ca Skill

## Step

This Step invokes CA-O-169 once with phase `install` to copy compiled `101_FRAMEWORK_METHODOLOGY/`, preserve protected configuration and Project state, install Engine `.install` into the Project runtime package, and install the `ca` payload.

## Details

Only this Step clears replaceable installed Framework members, copies the product as-is, installs `ca`, and restarts or reuses Project MCP for Docker/MCP smoke. It preserves settings and Project state, does not alter authoring, push, create a PR, or retry an uncertain effect.

Reuse canonical image preparation only after the Workflow's full suite is green. This occurrence also owns CA-O-169's post-smoke selected-Project retention: keep the exact admitted current-Version candidate, remove only proven owned unused noncandidate images, preserve all container references and other Projects' images, and report pending cleanup. Same fingerprint alone does not preserve an older rebuild. No additional retirement Step is inserted into CA-O-164.
