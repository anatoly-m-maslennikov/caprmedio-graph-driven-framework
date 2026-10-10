---
atom_id: CA-P-1868
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
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

Specify the portable package **and** installation Tools

## Objective

the AI Agent establishes complete RMED for reusable package, initialization, isolated installation and retained-state migration capabilities.

## Details

1. Keep reusable compiler/installer, shared package/gate models/codecs, detached readers and generic O200 install/bootstrap/restore RMED and implementation currently in `RELEASE_VERSION` in `TOOLS`, allowing fresh arbitrary/non-Git targets without the project-development checkout.
2. Define release helper Tool RMED only in `PROJECT_TOOLS`: authoring sibling `205_FEATURE_PROJECT_TOOLS` of `TOOLS` under `PROGRAMMATIC`, delivered at root `PROJECT_TOOLS` outside the reusable Engine.
3. Exclude and relocate CAPRMEDIO-specific Local/Public release helper code from general Methodology/framework-package delivery. Register ProjectTools D declarations as excluded delivery-boundary content so the exporter frontier neither ships nor reports them as an outside-Engine error.
4. Validate its Project binding with the two release Operations, not a third Workflow, and preserve exact package/selector/source-catalog/lock/gate interfaces with non-live test inputs plus the Local full preflight before the first destructive product wipe.

### Definition of Done

the Plan is **not** Done **if** release helper RMED/code is in general `TOOLS` or the reusable package, reusable generic capabilities leave `TOOLS`, ProjectTools D declarations ship in or fault the generic exporter frontier, required relocation/exclusion is absent, or the Project-specific binding adds another Operator Workflow.
