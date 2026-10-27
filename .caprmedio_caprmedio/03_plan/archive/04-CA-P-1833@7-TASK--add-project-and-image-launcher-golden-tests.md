---
atom_id: CA-P-1833@7
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
version: 7
updated_at: 2026-10-24 09:20:34 +0400
subjects:
  governs: CAPRMEDIO Framework Instance
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - Subject/Domain/Node/Continuant/Project.Settings
  - Subject/Domain/Node/Continuant/Project.Structure
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Subject/Engineering/Tool
  - Subject/Engineering/Action
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Engineering/Carrier
  - Subject/Engineering/Evaluation Implementation
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
relations:
  is_decomposition_of:
  - CA-P-1829
  blocks:
  - CA-P-1835
  - CA-P-1838
tier: 3
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

- completion evidence: selection **and** image executable golden fixtures; expected missing-module test-first failures saved **in** `.caprmedio_tmp/launcher-epic-1829/pre-implementation-selection-images.md`; source-change, immutable default-build reinspection **and** foreign-context cases added following review.

the Plan is **not** Done **if** ((a listed selection **or** image case is absent) **or** (the fixtures depend on live Project secrets **or** mutable host state) **or** (the pre-implementation test result is missing)).
