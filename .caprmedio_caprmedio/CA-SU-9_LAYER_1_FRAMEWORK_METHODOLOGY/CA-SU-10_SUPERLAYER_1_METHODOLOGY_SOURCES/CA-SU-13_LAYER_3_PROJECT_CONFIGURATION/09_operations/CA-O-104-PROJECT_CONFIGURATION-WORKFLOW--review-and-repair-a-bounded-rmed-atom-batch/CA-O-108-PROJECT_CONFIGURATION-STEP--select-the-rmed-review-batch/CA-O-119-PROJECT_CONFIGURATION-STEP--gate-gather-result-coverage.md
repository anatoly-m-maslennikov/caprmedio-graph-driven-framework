---
atom_id: CA-O-119
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-27 19:59:46 +0400
subjects:
  governs: Subject/caprmedio/Step//RMED Atom Review Gather Coverage Gate Step
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
relations: {}
tier: 3
---
# Summary

Gate gather result coverage

## Operation

the gather Coverage Gate substep **must** invoke **`=1`** Action, CA-O-118, with stage=gather **after** the main gather Step **and** **before** continuation.

## Details

- inputs: frozen selection, saved Step results, required coverage obligations **and** shared Run evidence.
- covered permits continuation; ask_operator interrupts with the saved missing-work question.
- retain the existing Run ID **and** Journal; do **not** dispatch another Atom reviewer **or** replay completed effects.
