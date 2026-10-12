---
atom_id: CA-O-172
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: deliver candidate sources"
  depends_on: [Workflow, Step, Action, Methodology Source, Delivery, Journal]
version: 3
updated_at: 2026-10-09 16:36:54 +0400
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-166]
---
# Summary

Deliver the complete candidate Methodology sources

## Step

This Step invokes CA-O-166 once with phase `deliver_sources`, binding the validated N+1 complete active-source manifest and the sealed private `.caprmedio_tmp/release_candidates/<run_id>/methodology/` export with its logical root `methodology/` mapping. It returns the delivery manifest or truthful failure unchanged.

## Details

It does not broaden source membership, repair a path, compile, install, test, build, promote or retire; in particular, it does not write live root `methodology/`. A byte, identity, revision, digest, destination or Journal mismatch stops the Workflow with actual evidence.
