---
atom_id: CA-P-1849
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
    - "Framework Package"
    - "Methodology Source"
    - "Applicable Methodology"
    - "Project Structure"
    - "Requirement"
    - "Method"
    - "Delivery"
    - "Workflow"
    - "Action"
    - "Journal"
relations:
  is_decomposition_of:
    - CA-P-1848
  blocks:
    - CA-P-1850
    - CA-P-1851
    - CA-P-1852
    - CA-P-1853
    - CA-P-1854
---
# Summary

Specify installation **and** release boundaries

## Objective

the AI Agent establishes the RMED **and** Operations contract that separates a reusable beta Framework Package **from** a selected Project runtime **and** defines the local **and** public release cycles.

## Details

- scope: the installation/release contribution of the CAPRMEDIO Framework Instance delivered by the caprmedio Project.
- input: the Operator's approved layout **and** the current installer, release, Methodology, startup **and** duplicate-copy findings.
- output: update the relevant Requirement, Method, Evaluation **and** Delivery Atoms **before** implementation; define the Workflow, Actions **and** Steps separately **in** Operations. keep generic model semantics **in** CORE_META_MODEL, concrete caprmedio bindings **in** PROJECT_CONFIGURATION, **and** Engine implementation specifications **in** their owning Scope Units.
- the reusable beta Framework Package belongs **in** `.caprmedio_install`; runtime state, environments **and** execution for the selected Project belong **in** that Project's `.caprmedio_runtime`. introduce **=1** package schema **and** selected release identity rather than competing Tool-only **and** full-Engine installations.
- declare Project root, package root, `.caprmedio_<project>` selection, Methodology source authority, installed projection, version/lock manifests, migration/state boundaries **and** supported host platforms. installation into another Project **must not** require the development checkout **or** the caprmedio Project's personal settings.
- declare explicit Operator invocation, source freshness, capability discovery, parameter/output contracts, Journal recording for Workflow **and** Action Runs, idempotent reinstallation, failure recovery **and** the full-suite gates for both cycles. no release **or** merge is performed by authoring these definitions.
- effort: own work for **=1** AI Agent **must** fit **<=15** minutes. **if** this Plan needs larger own work, decompose it **before** execution **and** preserve its Objective **and** acceptance.
- control: use applicable Operator input **and** inherited Framework Instance Settings for permission, confidence **and** retry gates. creation is planned work **only**, **not** permission to execute the local/public cycle immediately.

### Definition of Done

the Plan is **not** Done **if** a package/runtime boundary, supported-Project contract, Workflow binding, source authority, full-suite gate **or** failure/recovery contract remains unspecified.
