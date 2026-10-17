---
atom_id: CA-O-120
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-15 18:54:08 +0000"
subjects:
  governs: "RMED Atom Review Check Coverage Gate Step"
  depends_on: ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Object/Atom", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/History/Journal"]
relations:
  relates_to: [CA-O-104, CA-O-118]
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/09_operations/CA-O-104-CORE_META_MODEL-WORKFLOW--review-and-repair-a-bounded-rmed-atom-batch/CA-O-109-CORE_META_MODEL-STEP--evaluate-the-selected-rmed-review-batch/CA-O-120-CORE_META_MODEL-STEP--gate-check-result-coverage.md
  source_atom_id: CA-O-120
  source_atom_revision: 4
  source_sha256: 495c9205a5c13165fe09632e6d2ffb62116a70860fea8dd2e3e8609e5cee4128
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
