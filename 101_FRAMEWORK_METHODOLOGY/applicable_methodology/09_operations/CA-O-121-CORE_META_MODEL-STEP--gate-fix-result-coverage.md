---
atom_id: CA-O-121
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-14 13:44:47 +0400"
subjects:
  governs: "RMED Atom Review Workflow/coverage/Step: 121"
  depends_on: [Workflow, Step, Action, Atom, Operator, Journal]
relations:
  relates_to: [CA-O-104, CA-O-118]
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/09_operations/CA-O-104-CORE_META_MODEL-WORKFLOW--review-and-repair-a-bounded-rmed-atom-batch/CA-O-110-CORE_META_MODEL-STEP--repair-the-evaluated-rmed-review-batch/CA-O-121-CORE_META_MODEL-STEP--gate-fix-result-coverage.md
  source_atom_id: CA-O-121
  source_atom_revision: 2
  source_sha256: b2bece2d48e968e8856a3bfbba222f65038e62b95bc99f13c3d23e637f77f8d2
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
