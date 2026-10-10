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
  governs: "Release Version/Step: deliver candidate sources"
  depends_on: [Workflow, Step, Action, Methodology Source, Delivery, Journal]
version: 4
updated_at: "2026-10-10 19:05:19 +0400"
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-166]
---
# Summary

Deliver the complete candidate Methodology sources

## Step

This Step invokes CA-O-166 once with phase `deliver_sources`, clearing replaceable product members and copying only the validated active Core Meta-Model, installed extension, and Project Configuration sources into `101_FRAMEWORK_METHODOLOGY/`.

## Details

It preserves protected product settings, does not broaden source membership, and does not compile, install, test, publish, or retry. A byte, identity, revision, digest, destination, or Journal mismatch stops the Workflow with actual evidence.
