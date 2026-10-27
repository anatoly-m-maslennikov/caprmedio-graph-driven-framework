---
atom_id: CA-P-2185@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Atom
  - Subject
  - Carrier
  - Projection
  - Plan
  - Operator
version: 3
updated_at: 2026-10-23 23:03:23 +0400
relations:
  is_decomposition_of:
  - CA-P-2183
  blocks:
  - CA-P-2186
---
# Summary

Implement opt-in Subject preview staging

## Objective

The existing local Tool can write and revalidate temporary proposed carriers through an explicit staging option.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Required prerequisite: CA-P-2184's actual updated accepted RMEDO; independent candidate review alone is insufficient. Reopen CLI callers before edits. Own only a small `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_subject_stage.py` adapter, required staging integration in `atom_operations.py`, and its `ATOM_UPDATE/atom_update.py` wrapper if needed. Keep pure `atom_subject_patch.py` unchanged. CA-P-2186 owns the dedicated fixture file; coordinate shared files with one integration owner and preserve other workers' edits.

Add opt-in local `ATOM_UPDATE run --stage-preview`. Reuse existing preview/`proposed_carrier` bytes; create a fresh generated `.caprmedio_tmp/subject-preview/<id>/`, preserve original identity/provenance and re-read/validate staged files. Reject destination escape, reused/unsafe output, stale source pins and invalid proposed bytes. Keep staged files outside current-original source selection and preserve existing default behavior.

No original, history, Journal or publication writes; no new source effect-time materialization or bypass of the deferred live guard. Check valid staging, non-Active Status/byte preservation, stale/invalid input, unsafe destination and default behavior on isolated fixtures. Deliver code/output/check pins to CA-P-2186; split a concrete overrun before execution. No mapping/re-pin, migration or release occurs.

### Completion receipt

Implementation followed [actual contract acceptance](../../../../_projection/core-entity-review/stage2/tools-first/staged-preview-contract-acceptance.md) at `15d2373db`. [independent staging verification](../../../../_projection/core-entity-review/stage2/tools-first/staged-preview-verification.md) at `ef39bf1fd` records independent code acceptance of staging `9e5c6007` and shared integration `a78f3dea`; the pure planner remains unchanged. Root's full UPDATE suite passed 80 checks, including the 14 independent staging cases; SEARCH 49, generic lifecycle 30 and selected-Subject eight also passed. The explicit local staging path creates and revalidates only temporary candidates; original/history/Journal/publication effects and live capability remain unclaimed.

### Definition of Done

The Plan is **not** Done if contracts are unaccepted/stale, staging is implicit, proposed bytes or provenance drift, re-read validation is absent, a destination escapes/reuses unsafe state, authority/history/Journal/publication changes, focused checks fail, or own work exceeds 15 minutes without decomposition.
