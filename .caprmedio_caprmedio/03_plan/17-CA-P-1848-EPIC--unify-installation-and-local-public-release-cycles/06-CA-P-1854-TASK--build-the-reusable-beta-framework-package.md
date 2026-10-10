---
atom_id: CA-P-1854
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-10 18:58:38 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on: [Project, Plan, AI Agent, Operator, Framework Instance Settings, Framework Package, Methodology Source, Applicable Methodology, Tool, Carrier, Version, Journal]
relations:
  is_decomposition_of: [CA-P-1848]
  blocks: [CA-P-1855]
---
# Summary

Build the reusable beta Framework package

## Objective

the AI Agent implements a portable beta Framework Package under `.caprmedio_install` that can be installed into another Project.

## Details

1. Deliver reusable Engine, Methodology, Skill/default-settings payload and compiler/installer capabilities from `TOOLS` in the Framework Package.
2. Exclude CAPRMEDIO-specific Local/Public Release Operations and release helper Tool implementations/RMED from the reusable Engine/package and from general Methodology delivery.
3. Relocate those concrete project features to Project-owned delivery: Operations under `.caprmedio_caprmedio/09_operations`; helper tools under delivery root `PROJECT_TOOLS`, outside the reusable Engine. Preserve package/source identities and fail closed for an excluded or misplaced release feature.
4. Seal and test the package candidate through the Local non-live preflight before the first product wipe; do not execute this Plan as a package build or installation.

### Definition of Done

the Plan is **not** Done **if** a reusable compiler/installer capability leaves `TOOLS`, a project-specific release Operation/helper is packaged as general framework/Methodology content, package identity is incomplete, or portability requires the development checkout.
