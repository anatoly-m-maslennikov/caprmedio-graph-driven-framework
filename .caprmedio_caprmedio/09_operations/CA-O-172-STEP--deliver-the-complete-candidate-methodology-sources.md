---
atom_id: CA-O-172
content_role: Operations
type: Step
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: deliver active sources"
  depends_on: [Workflow, Step, Action, Methodology Source, Delivery]
version: 5
updated_at: "2026-10-12 00:00:51 +0000"
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-166]
---
# Summary

Deliver active Methodology sources

## Step

This Step invokes CA-O-166 once with phase `deliver_sources`, clearing replaceable product members and copying only the current active Core Meta-Model, installed extension, and Project Configuration sources into `101_FRAMEWORK_METHODOLOGY/`.

## Details

It preserves protected product settings, does not broaden source membership, and does not compile, install, test, publish, or retry. A source or destination mismatch stops and is reported for manual handling.
