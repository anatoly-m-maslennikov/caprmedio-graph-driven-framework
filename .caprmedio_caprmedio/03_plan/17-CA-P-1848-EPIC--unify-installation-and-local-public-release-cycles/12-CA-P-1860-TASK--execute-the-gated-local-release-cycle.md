---
atom_id: CA-P-1860
content_role: Plan
type: Plan
label: Task
work_sequence_number: 12
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-09 12:12:13 +0000"
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
    - "Version"
    - "Tool"
    - "Workflow"
    - "Action"
    - "Workflow Run"
    - "Journal"
    - "Projection"
relations:
  is_decomposition_of:
    - CA-P-1848
  blocks:
    - CA-P-1861
---
# Summary

Execute the gated local release cycle

## Objective

the AI Agent executes the approved local release Workflow to install the validated N+1 package/runtime for this Project.

## Details

- scope: the installation/release contribution of the CAPRMEDIO Framework Instance delivered by the caprmedio Project.
- input: the passing local full-suite receipt, exact sealed Version/source/configuration/catalog/lock/package/image byte identities, current N installation **and** explicit Operator authorization for the selected Project.
- flow **after** the gate passes:
  1. quiesce the selected Project's affected runtime, preserve the admitted N recovery inventory, **and** migrate operational state **from** `.caprmedio_install` into the selected Project's `.caprmedio_runtime` **before** beta-package promotion.
  2. execute the reviewed authoring-source/Project Structure path cutover **before** installing a projection into the old source-containing Framework Instance target. verify the pre-approved path mapping, unchanged intended source contents, fresh source pins **and** recoverability; stop **if** the tested closure has drifted.
  3. promote the already sealed selected active-source export to root `methodology/`, then install its admitted source copy **and** the sealed compiled Methodology projection under `.caprmedio_caprmedio/000_CAPRMEDIO_framework`; do **not** re-export **or** recompile **after** the gate.
  4. promote the same sealed reusable beta package bytes into `.caprmedio_install`, then install/bind this Project's `.caprmedio_runtime`; do **not** rebuild package **or** image **after** the gate. live package promotion may **not** precede state migration.
- install ca for the Project, admit the matching already sealed Docker image, start/reuse this Project's container on an available loopback port, **and** return its MCP URL **with** the installation-lock **and** running-generation proof.
- the executing N handles promotion/admission of N+1; preserve the previous selection **and** recovery path **until** N+1 passes live verification. record the reusable Workflow, each bound Step **and** Action Run **in** the shared Journal **with** parentage, exact input/output/evidence identities **and** terminal outcomes.
- refuse stale gate/pins **before** effects. failures preserve evidence **and** do **not** automatically replay uncertain mutations **or** publish partial success; invoke the documented recovery path under existing authorization.
- effort: own work for **=1** AI Agent **must** fit **<=15** minutes. **if** this Plan needs larger own work, decompose it **before** execution **and** preserve its Objective **and** acceptance.
- control: use applicable Operator input **and** inherited Framework Instance Settings for permission, confidence **and** retry gates. creation is planned work **only**, **not** permission to execute the local/public cycle immediately.

### Definition of Done

the Plan is **not** Done **if** any required local phase lacks a successful terminal receipt, N+1 is **not** selected/installed, promotion rebuilt **or** differs **from** the gated candidate bytes, package/Methodology/image/lock identities disagree, **or** N recovery/state isolation was lost.
