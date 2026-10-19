---
atom_id: "CA-O-120@draft"
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: "Draft"
author: Anatoly Maslennikov
version: 6
updated_at: "2026-10-19 11:49:48 +0000"
subjects:
  governs: "RMED Atom Review Check Coverage Gate Step"
  depends_on: ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Workflow", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/Atom", "Entity/Node/Continuant/Actor/Type: Operator", "Entity/Node/Continuant/History/Journal"]
relations:
  relates_to: [CA-O-104, CA-O-118]
---
# Summary

Gate check result coverage

## Operation

the check Coverage Gate substep **must** invoke **`=1`** Action, CA-O-118, with stage=check **after** the main check Step **and** **before** continuation.

## Details

- inputs: frozen selection, saved Step results, required coverage obligations **and** shared Run evidence.
- covered permits continuation; ask_operator interrupts with the saved missing-work question.
- retain the existing Run ID **and** Journal; do **not** dispatch another Atom reviewer **or** replay completed effects.
