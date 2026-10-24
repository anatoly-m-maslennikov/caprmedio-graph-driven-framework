---
atom_id: CA-O-173@7
content_role: Operations
type: Step
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: "Release Version/Step: compile applicable Methodology"
  depends_on: [Workflow, Step, Action, Applicable Methodology, Compiler, Delivery]
version: 7
updated_at: "2026-10-12 00:00:51 +0000"
relations:
  part_of: [CA-O-164]
  invokes: [CA-O-166]
---
# Summary

Compile applicable Methodology

## Step

This Step invokes CA-O-166 once with phase `compile` for `101_FRAMEWORK_METHODOLOGY/` and the canonical compiler. Its output remains in that derived product; it does not write the installed Framework.

## Details

This is not another compiler graph. An incomplete product, unavailable Tool/layout, or output mismatch stops before installation and is reported for manual handling.
