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
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-10 18:08:27 +0400"
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

the AI Agent executes the approved local release Workflow to destructively replace the selected installed package/runtime with the validated package for this Project.

## Details

- scope: the installation/release contribution of the CAPRMEDIO Framework Instance delivered by the caprmedio Project.
- input: the passing local full-suite receipt, exact sealed Version/source/configuration/catalog/lock/package/image byte identities, current N installation **and** explicit Operator authorization for the selected Project.
- flow **after** the gate passes:
  1. quiesce the selected Project's affected runtime, preserve migration inventory and Project-owned evidence, and migrate operational state from `.caprmedio_install` into the selected Project's `.caprmedio_runtime` before destructive replacement.
  2. execute the reviewed authoring-source/Project Structure path cutover **before** installing a projection into the old source-containing Framework Instance target. verify the pre-approved path mapping, unchanged intended source contents, fresh source pins **and** recoverability; stop **if** the tested closure has drifted.
  3. promote the already sealed selected active-source export to root `methodology/`, then install its admitted source copy **and** the sealed compiled Methodology projection under `.caprmedio_caprmedio/000_CAPRMEDIO_framework`; do **not** re-export **or** recompile **after** the gate.
  4. after staging and revalidation, remove the selected installed package tree, install the same sealed reusable beta package bytes, then publish package and target selectors last; do not rebuild package or image after the gate. Live destructive replacement may not precede state migration. A failure after removal is unavailable and preserves configuration, Project authority, Journal and transaction evidence without restoring a removed package.
- install ca for the Project, admit the matching already sealed Docker image, start/reuse this Project's container on an available loopback port, **and** return its MCP URL **with** the installation-lock **and** running-generation proof.
- verify this Project's existing `.caprmedio_runtime/config.toml` remains byte-identical across installation. create admitted defaults **only if** absent; require explicit configuration migration **or** stop **if** the new runtime cannot use the existing configuration.
- record the reusable Workflow, each bound Step and Action Run in the shared Journal with parentage, exact input/output/evidence identities and terminal outcomes. The replacement selector is published only after the new package exists; no old installed package or selector is retained as a fallback after destructive removal.
- refuse stale gate/pins **before** effects. failures preserve evidence **and** do **not** automatically replay uncertain mutations **or** publish partial success; invoke the documented recovery path under existing authorization.
- effort: own work for **=1** AI Agent **must** fit **<=15** minutes. **if** this Plan needs larger own work, decompose it **before** execution **and** preserve its Objective **and** acceptance.
- control: use applicable Operator input **and** inherited Framework Instance Settings for permission, confidence **and** retry gates. creation is planned work **only**, **not** permission to execute the local/public cycle immediately.

### Definition of Done

the Plan is **not** Done **if** any required local phase lacks a successful terminal receipt, the replacement is not selected/installed, promotion rebuilt or differs from the gated candidate bytes, package/Methodology/image/lock identities disagree, or configuration/Project-owned state isolation was lost.
