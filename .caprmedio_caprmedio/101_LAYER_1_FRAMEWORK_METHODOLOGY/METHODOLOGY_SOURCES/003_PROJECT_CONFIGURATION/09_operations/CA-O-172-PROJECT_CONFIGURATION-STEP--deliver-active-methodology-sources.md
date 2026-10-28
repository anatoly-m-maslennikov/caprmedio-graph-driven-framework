---
atom_id: CA-O-172
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/caprmedio/Step//Release Version/Step: deliver active sources'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Release.ID
version: 13
updated_at: 2026-10-27 19:59:47 +0400
relations:
  part_of:
  - CA-O-164
  invokes:
  - CA-O-166
tier: 3
---
# Summary

Deliver active Methodology sources

## Step

This Step invokes CA-O-166 once with phase `deliver_sources`, clearing replaceable product members and copying only the current active Core Meta-Model, installed extension, and Project Configuration sources into `101_FRAMEWORK_METHODOLOGY/`.

## Details

It preserves protected product settings, does not broaden source membership, and does not compile, install, test, publish, or retry. A source or destination mismatch stops and is reported for manual handling.
