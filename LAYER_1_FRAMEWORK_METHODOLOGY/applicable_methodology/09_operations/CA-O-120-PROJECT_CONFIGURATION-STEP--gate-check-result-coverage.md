---
atom_id: CA-O-120
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 6
updated_at: "2026-10-19 15:56:55 +0400"
subjects:
  governs: "RMED Atom Review Check Coverage Gate Step"
  depends_on: ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Workflow", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/Atom", "Entity/Node/Continuant/Actor/Type: Operator", "Entity/Node/Continuant/History/Journal"]
relations:
  relates_to: [CA-O-104, CA-O-118]
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-104-PROJECT_CONFIGURATION-WORKFLOW--review-and-repair-a-bounded-rmed-atom-batch/CA-O-109-PROJECT_CONFIGURATION-STEP--evaluate-the-selected-rmed-review-batch/CA-O-120-PROJECT_CONFIGURATION-STEP--gate-check-result-coverage.md
  source_atom_id: CA-O-120
  source_atom_revision: 6
  source_sha256: f61eb76893c132992fdc48e831fdf6514173d0735301dcbb147d7a2e2443d75b
  original_relations_sha256: bf71386ada6c23487fc05e9498120de59784b00f41060c7bbc43ad9070f682e0
---
# Summary

Gate check result coverage

## Operation

the check Coverage Gate substep **must** invoke **`=1`** Action, CA-O-118, with stage=check **after** the main check Step **and** **before** continuation.

## Details

- inputs: frozen selection, saved Step results, required coverage obligations **and** shared Run evidence.
- covered permits continuation; ask_operator interrupts with the saved missing-work question.
- retain the existing Run ID **and** Journal; do **not** dispatch another Atom reviewer **or** replay completed effects.
