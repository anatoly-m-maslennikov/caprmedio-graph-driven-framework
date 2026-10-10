---
atom_id: CA-O-185
content_role: Operations
type: Step
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: run closed candidate Unit gate"
  depends_on: [Workflow, Step, Action, Test, Methodology, Journal]
version: 4
updated_at: "2026-10-10 19:05:19 +0400"
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-168]
---
# Summary

Run the closed candidate Unit gate

## Step

This Step invokes CA-O-168 once with phase `closed_unit_gate`, binding CA-O-175's exact private compiled candidate, frozen active-source boundary, and declared Unit/source partition.

## Details

Every declared Unit/source testcase must terminal-pass for the frozen candidate; skipped, excluded, missing, focused, cached, or historical results are non-pass. Host-capable Candidate E2E remains CA-O-182, and CA-O-184 alone aggregates the complete Release Gate. This Step does not clear, copy, compile, install, publish, or retry.
