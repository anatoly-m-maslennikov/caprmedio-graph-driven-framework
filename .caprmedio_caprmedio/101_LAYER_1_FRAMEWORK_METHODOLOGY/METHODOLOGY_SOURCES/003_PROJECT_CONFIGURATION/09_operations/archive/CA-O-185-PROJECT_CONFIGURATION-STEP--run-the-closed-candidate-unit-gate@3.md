---
atom_id: CA-O-185
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: run complete local test preflight"
  depends_on: [Workflow, Step, Action, Test, Methodology, Journal]
version: 3
updated_at: "2026-10-10 18:44:09 +0400"
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-168]
---
# Summary

Run the closed candidate Unit gate

## Step

This Step invokes CA-O-168 once with phase `complete_local_suite`, binding CA-O-170's frozen active source boundary and the declared complete local suite before either product or installed Framework is cleared.

## Details

Every declared test must terminal-pass for the frozen boundary; skipped, excluded, missing, focused, cached, host-only, or historical results are non-pass. This Step does not clear, copy, compile, install, publish, or retry.
