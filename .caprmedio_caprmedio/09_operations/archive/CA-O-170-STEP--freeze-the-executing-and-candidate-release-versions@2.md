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
  governs: "Release Version/Step: freeze local boundary"
  depends_on: [Workflow, Step, Action, Version, Methodology Source, Journal]
version: 2
updated_at: "2026-10-10 19:05:19 +0400"
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-165]
---
# Summary

Freeze the executing and candidate release Versions

## Step

This Step invokes CA-O-165 once with phase `freeze`, binding the selected Version and active Core Meta-Model, installed extension, and Project Configuration source identities and digests. It returns that exact result unchanged.

## Details

Missing, mutable, stale, inactive, or unjournalable inputs stop before any test or delivery effect. This Step does not copy, compile, install, test, publish, or retry. Its Step Run and referenced Action Run retain their exact parent, input, and Journal evidence.
