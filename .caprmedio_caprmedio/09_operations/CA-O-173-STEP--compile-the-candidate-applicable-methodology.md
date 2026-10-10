---
atom_id: CA-O-173
content_role: Operations
type: Step
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: compile candidate Methodology"
  depends_on: [Workflow, Step, Action, Applicable Methodology, Compiler, Delivery, Journal]
version: 6
updated_at: "2026-10-10 19:05:19 +0400"
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-166]
---
# Summary

Compile the candidate Applicable Methodology

## Step

This Step invokes CA-O-166 once with phase `compile`, binding the verified `101_FRAMEWORK_METHODOLOGY/` source product and canonical compiler. Its output remains in that derived product; it does not write the installed Framework.

## Details

This is not another compiler graph. A changed frontier, incomplete product, unbound Tool/layout, output mismatch, or source mutation stops before installation. Compilation does not require a repeated full suite.
