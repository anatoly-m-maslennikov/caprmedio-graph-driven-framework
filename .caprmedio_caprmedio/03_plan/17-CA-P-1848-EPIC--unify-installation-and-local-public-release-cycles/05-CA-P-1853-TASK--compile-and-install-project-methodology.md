---
atom_id: CA-P-1853
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 15:41:25 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on:
    - "Project"
    - "Plan"
    - "AI Agent"
    - "Operator"
    - "Framework Instance Settings"
    - "Applicable Methodology"
    - "Methodology Source"
    - "Projection"
    - "Atom"
    - "Project Settings"
    - "Workflow"
    - "Evaluation"
relations:
  is_decomposition_of:
    - CA-P-1848
  blocks:
    - CA-P-1855
---
# Summary

Compile **and** install Project Methodology

## Objective

the AI Agent implements a traceable per-Project Applicable Methodology projection **from** the delivered Methodology sources.

## Details

- scope: the installation/release contribution of the CAPRMEDIO Framework Instance delivered by the caprmedio Project.
- input: root `methodology/`, the selected Project's installed extensions **and** Project configuration, **and** the reviewed compiler contract.
- output: compile, validate **and** install the selected Project's Methodology under `.caprmedio_<project>/000_CAPRMEDIO_framework`; for this Project the target is `.caprmedio_caprmedio/000_CAPRMEDIO_framework`. leave authoring sources outside this installation target.
- preserve each projected Atom's relation to its original source Atom. select active sources mechanically, report conflicts **and** gaps, **and** obtain the applicable Operator approval **before** source corrections; derived output is **not** edited independently.
- repair the observed stale/missing CA-O-187 delivery/compiled coverage **and** canonical compiler-currentness path-set mismatch through correct upstream selection **and** regeneration.
- test different Project configurations, source/target completeness, conflict diagnostics, approved correction/recompile, provenance, currentness, installation failure **and** recovery. live publication waits for the local full-suite gate.
- effort: own work for **=1** AI Agent **must** fit **<=15** minutes. **if** this Plan needs larger own work, decompose it **before** execution **and** preserve its Objective **and** acceptance.
- control: use applicable Operator input **and** inherited Framework Instance Settings for permission, confidence **and** retry gates. creation is planned work **only**, **not** permission to execute the local/public cycle immediately.

### Definition of Done

the Plan is **not** Done **if** installed Methodology is untraceable, differs **from** the selected source/configuration without a recorded disposition, has unresolved currentness gaps, **or** is treated as editable source authority.
