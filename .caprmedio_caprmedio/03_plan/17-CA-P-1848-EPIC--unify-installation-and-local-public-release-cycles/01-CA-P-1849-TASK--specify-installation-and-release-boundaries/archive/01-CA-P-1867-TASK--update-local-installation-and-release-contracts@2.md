---
atom_id: CA-P-1867
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-10 18:58:38 +0400"
subjects:
  governs: CAPRMEDIO Framework Instance
  depends_on: [Project, Plan, AI Agent, Operator, Framework Package, Methodology Source, Applicable Methodology, Project Structure, Requirement, Method, Evaluation, Delivery, Workflow, Step, Action, Tool, Journal, Version]
relations:
  is_decomposition_of: [CA-P-1849]
  blocks: [CA-P-1870]
---
# Summary

Update local installation **and** release contracts

## Objective

the AI Agent updates the authoritative Local release Operations contract to the approved beta-package, per-Project runtime and gated candidate boundaries.

## Details

1. Define the concrete Local release Operation only in the Project root `.caprmedio_caprmedio/09_operations`; it is not general Methodology or reusable Framework Package delivery.
2. Bind its release helper tools to Project-owned `PROJECT_TOOLS`; keep reusable compiler/installer capability, shared package/gate models/codecs, detached readers and generic O200 install/bootstrap/restore in `TOOLS`.
3. Include the Local full preflight before its first destructive product wipe, per-step scoped Git commits, protected-setting preservation and honest Journal evidence.
4. Plan code relocation/exclusion and exporter delivery-boundary registration without executing code, structure, runtime or Git changes here.

### Definition of Done

the Plan is **not** Done **if** Local release is defined outside Project Operations, its helpers are packaged generally, reusable capabilities leave `TOOLS`, ProjectTools D declarations are shipped or rejected by the generic exporter frontier, placement/relocation evidence is incomplete, or the gate/order contract is missing.
