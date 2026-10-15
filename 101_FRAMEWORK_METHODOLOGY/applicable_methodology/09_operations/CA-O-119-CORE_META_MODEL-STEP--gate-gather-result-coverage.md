---
atom_id: CA-O-119
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
  governs: "RMED Atom Review Workflow/coverage/Step: 119"
  depends_on: [Workflow, Step, Action, Atom, Operator, Journal]
relations:
  relates_to: [CA-O-104, CA-O-118]
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/09_operations/CA-O-104-CORE_META_MODEL-WORKFLOW--review-and-repair-a-bounded-rmed-atom-batch/CA-O-108-CORE_META_MODEL-STEP--select-the-rmed-review-batch/CA-O-119-CORE_META_MODEL-STEP--gate-gather-result-coverage.md
  source_atom_id: CA-O-119
  source_atom_revision: 2
  source_sha256: 1eb8a85a0bba4cf96f9509f5f423224f9022c06ed8bab56758ae6600499716c6
  original_relations_sha256: bf71386ada6c23487fc05e9498120de59784b00f41060c7bbc43ad9070f682e0
---
# Summary

Gate gather result coverage

## Operation

the gather Coverage Gate substep **must** invoke **`=1`** Action, CA-O-118, with stage=gather **after** the main gather Step **and** **before** continuation.

## Details

- inputs: frozen selection, saved Step results, required coverage obligations **and** shared Run evidence.
- covered permits continuation; ask_operator interrupts with the saved missing-work question.
- retain the existing Run ID **and** Journal; do **not** dispatch another Atom reviewer **or** replay completed effects.
