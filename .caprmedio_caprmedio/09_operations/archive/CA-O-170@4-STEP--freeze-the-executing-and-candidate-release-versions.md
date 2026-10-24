---
atom_id: CA-O-170@4
content_role: Operations
type: Step
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Release Version/Step: validate local inputs'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Methodology Source
version: 4
updated_at: 2026-10-23 03:14:50 +0400
relations:
  part_of:
  - CA-O-164
  invokes:
  - CA-O-165
---
# Summary

Validate local release inputs

## Step

This Step invokes CA-O-165 once with phase `validate` to check current active Core Meta-Model, installed extension, Project Configuration sources, and delivery paths.

## Details

Missing, inactive, ambiguous, or mismatched inputs stop before tests or delivery effects and are reported for manual handling. This Step does not copy, compile, install, publish, or retry.
