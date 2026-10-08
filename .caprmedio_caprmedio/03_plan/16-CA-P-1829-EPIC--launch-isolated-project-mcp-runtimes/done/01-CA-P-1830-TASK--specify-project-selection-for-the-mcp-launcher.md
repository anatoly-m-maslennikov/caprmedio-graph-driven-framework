---
atom_id: CA-P-1830
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Done
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-09 00:27:59 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on:
    - "Project"
    - "Project Settings"
    - "Project Structure"
    - "Framework Instance Settings"
    - "Tool"
    - "Action"
    - "Workflow Run"
    - "Carrier"
    - "Evaluation"
    - "AI Agent"
    - "Operator"
relations:
  is_decomposition_of:
    - CA-P-1829
  blocks:
    - CA-P-1831
---
# Summary

Specify Project selection for the MCP launcher

## Objective

the AI Agent defines the Project-selection contract for the Python launcher so the selected CAPRMEDIO Framework Instance is unambiguous **before** runtime effects.

## Details

- input: the approved launcher design, Project Settings, Project Structure, **and** existing authority **in** `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/203_FEATURE_APPS/WORKFLOW_ORCHESTRATOR` **and** `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/204_FEATURE_MCP`.
- output: reviewed source RMED for the explicit Project root path **and** its directly contained `.caprmedio_<project>` settings/control folder, canonical instance identity, permitted mounts, **and** per-Project runtime state, including MCP reload receipts, pending work, **and** caches. separate Project roots can share a repository; image build sources are independent. reuse existing authority rather than duplicate it.
- verification: compare the contract with separate-repository **and** same-repository Project examples; reject ambiguous selection **without** choosing another Project.
- effort: **`<=15`** minutes for **`=1`** AI Agent; the Epic's decomposition rule applies **before** execution **if** the estimate no longer holds.

### Definition of Done

- completion evidence: R1900, M355, E599, D593 source contract; independent launcher_security review passed the explicit Project-root, no-Git-precondition, selected-mount, identity, ambiguity, authority **and** state boundaries.

the Plan is **not** Done **if** ((the selected Project cannot be resolved uniquely from the specified inputs) **or** (same-repository instance identity **and** state boundaries are unspecified) **or** (the source contract has no recorded independent review)).
