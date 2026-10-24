---
atom_id: CA-O-173@9
content_role: Operations
type: Step
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Release Version/Step: compile applicable Methodology'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Projection/Type: Applicable Methodology'
  - Compiler
  - Delivery
version: 9
updated_at: 2026-10-24 00:38:25 +0400
relations:
  part_of:
  - CA-O-164
  invokes:
  - CA-O-166
tier: 3
---
# Summary

Compile applicable Methodology

## Step

This Step invokes CA-O-166 once with phase `compile` for `101_FRAMEWORK_METHODOLOGY/` and the canonical compiler. Its output remains in that derived product; it does not write the installed Framework.

## Details

This is not another compiler graph. An incomplete product, unavailable Tool/layout, or output mismatch stops before installation and is reported for manual handling.
