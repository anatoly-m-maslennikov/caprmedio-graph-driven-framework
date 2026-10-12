---
atom_id: CA-O-170
content_role: Operations
type: Step
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: validate local inputs"
  depends_on: [Workflow, Step, Action, Methodology Source]
version: 3
updated_at: "2026-10-12 00:00:51 +0000"
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-165]
---
# Summary

Validate local release inputs

## Step

This Step invokes CA-O-165 once with phase `validate` to check current active Core Meta-Model, installed extension, Project Configuration sources, and delivery paths.

## Details

Missing, inactive, ambiguous, or mismatched inputs stop before tests or delivery effects and are reported for manual handling. This Step does not copy, compile, install, publish, or retry.
