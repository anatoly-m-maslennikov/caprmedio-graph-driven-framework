---
atom_id: CA-P-1855
content_role: Plan
type: Plan
label: Task
work_sequence_number: 7
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
    - "Project Settings"
    - "Tool"
    - "Workflow Run"
    - "Journal"
    - "Carrier"
relations:
  is_decomposition_of:
    - CA-P-1848
  blocks:
    - CA-P-1856
---
# Summary

Install an isolated runtime for a selected Project

## Objective

the AI Agent implements installation of the selected beta Framework Package into a runtime isolated to the requested Project.

## Details

- scope: the installation/release contribution of the CAPRMEDIO Framework Instance delivered by the caprmedio Project.
- input: an explicit package root/release **and** Project root containing its directly nested `.caprmedio_<project>` settings/control folder.
- output: this Project's `.caprmedio_runtime`, selected package execution binding, uv-managed isolated environment, configured Methodology installation, installed ca Skill **and** attributable initialization result.
- support relocation, Git **and** non-Git Projects, separate repositories **and** multiple Project root folders **in** one repository. package inputs can be reusable; runtime databases, locks, Runs, dependency environments **and** endpoint selection remain per-Project.
- bootstrap dependencies through uv **and** the lockfile. installed execution **must not** silently fall back to system Python, system libraries, another Project **or** the development checkout. distinguish an explicit development mode **from** normal installed execution.
- integrate the reviewed legacy-state migration without deleting historical evidence. test first install, same-version reinstall, upgrade, missing uv/input, interruption, recovery **and** rollback; real cutover occurs **only** after the local full-suite gate.
- effort: own work for **=1** AI Agent **must** fit **<=15** minutes. **if** this Plan needs larger own work, decompose it **before** execution **and** preserve its Objective **and** acceptance.
- control: use applicable Operator input **and** inherited Framework Instance Settings for permission, confidence **and** retry gates. creation is planned work **only**, **not** permission to execute the local/public cycle immediately.

### Definition of Done

the Plan is **not** Done **if** a fresh Project cannot install without the checkout, a runtime uses another Project's state/configuration, dependencies escape uv isolation, **or** installation cannot recover without losing evidence.
