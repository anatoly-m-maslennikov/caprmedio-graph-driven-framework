---
atom_id: CA-P-1833
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-08 23:56:13 +0400"
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
    - CA-P-1835
    - CA-P-1838
---
# Summary

Add Project **and** image launcher golden tests

## Objective

the AI Agent creates the test-first golden corpus for Project selection **and** image admission.

## Details

- input: the reviewed RMED **and** accepted selection/image cases; reuse the existing Docker runtime test infrastructure.
- output: deterministic fixtures **and** mocked tests for two repositories, two Projects **in** one repository, ambiguous selection, unsafe bindings, dropped selection during Gateway spawn, a valid source frontier bound **to** the wrong Project, absent images, compatible-image reuse, stale code, **and** build failure.
- verification: run the bounded tests **before** implementation; distinguish expected failures demonstrating missing behavior from invalid fixtures.
- effort: **`<=15`** minutes for **`=1`** AI Agent; the Epic's decomposition rule applies **before** execution **if** the estimate no longer holds.

### Definition of Done

the Plan is **not** Done **if** ((a listed selection **or** image case is absent) **or** (the fixtures depend on live Project secrets **or** mutable host state) **or** (the pre-implementation test result is missing)).
