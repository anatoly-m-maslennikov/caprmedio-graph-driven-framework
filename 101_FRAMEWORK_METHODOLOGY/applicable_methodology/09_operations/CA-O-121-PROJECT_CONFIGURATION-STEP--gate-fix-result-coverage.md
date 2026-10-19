---
atom_id: CA-O-121
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 5
updated_at: "2026-10-19 13:30:21 +0400"
subjects:
  governs: "RMED Atom Review Fix Coverage Gate Step"
  depends_on: ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Object/Atom", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/History/Journal"]
relations:
  relates_to: [CA-O-104, CA-O-118]
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-104-PROJECT_CONFIGURATION-WORKFLOW--review-and-repair-a-bounded-rmed-atom-batch/CA-O-110-PROJECT_CONFIGURATION-STEP--repair-the-evaluated-rmed-review-batch/CA-O-121-PROJECT_CONFIGURATION-STEP--gate-fix-result-coverage.md
  source_atom_id: CA-O-121
  source_atom_revision: 5
  source_sha256: 5b0c0bf6c93cc9e6218ed18f92d620283a5a164b7661c8d6a395fb879479f045
  original_relations_sha256: bf71386ada6c23487fc05e9498120de59784b00f41060c7bbc43ad9070f682e0
---
# Summary

Gate fix result coverage

## Operation

the fix Coverage Gate substep **must** invoke **`=1`** Action, CA-O-118, with stage=fix **after** the main fix Step **and** **before** continuation.

## Details

- inputs: frozen selection, saved Step results, required coverage obligations **and** shared Run evidence.
- covered permits continuation; ask_operator interrupts with the saved missing-work question.
- retain the existing Run ID **and** Journal; do **not** dispatch another Atom reviewer **or** replay completed effects.
