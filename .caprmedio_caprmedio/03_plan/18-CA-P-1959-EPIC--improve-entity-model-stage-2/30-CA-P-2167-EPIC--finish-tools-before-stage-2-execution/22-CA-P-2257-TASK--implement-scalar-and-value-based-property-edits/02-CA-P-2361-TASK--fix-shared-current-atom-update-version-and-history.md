---
atom_id: CA-P-2361
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
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Revision, Journal, Tool, Plan]
version: 1
updated_at: "2026-10-13 23:14:39 +0400"
relations:
  is_decomposition_of: [CA-P-2257]
---
# Summary

Fix shared current Atom Update Version and history

## Objective

Fix the existing shared lifecycle_intents Update branch so every real admitted identified same-ID non-Draft current Atom update increments Version by exactly 1 and preserves the exact predecessor, while an exact no-op remains unchanged. Draft updates and legacy migration remain outside this correction.

## Details

Own only lifecycle_intents.py's existing current identified Atom Update branch and focused author tests. Reopen current CA-R-1432 v11 and retain its exact source pin (SHA-256 `91f4b7c5600e775ae357230792fafe2e5e64433714dec1839a73553361a41202`) together with applicable existing classification, authorization, currentness and rollback contracts. Apply the same Version +1 and exact prior-byte preservation to admitted carrier_only, equivalent_refinement and semantic_revision changes; keep existing semantic Revision and lineage-review requirements intact. Fix the existing shared writer and history/rollback path needed by Property and Section integration, not another writer. Preserve an exact no-op's bytes, Version and Updated At with no new history or changed effect. Refuse stale, denied or unresolved changes before mutation and retain truthful rollback/partial diagnostics.

Implementation owner: settings_rules, with exclusive lifecycle_intents.py and focused author-test scope; independent settings_reader_checks owns separate tests. You are not alone: preserve others' edits and coordinate shared boundaries. Own work is bounded to 15 minutes; split before exceeding it. Root owns Plans and Git. Draft promotion/identity and Draft-history policy, legacy migration, renderer redesign, new public routes and live effects are excluded. If current Draft or legacy behavior contradicts selected authority, report the exact evidence and seek separate direction rather than infer policy.

### Definition of Done

Actual admitted current-Atom carrier_only, refinement and semantic_revision cases prove Version +1 exactly once, refreshed Updated At, retained ID and exact predecessor bytes including prior Version, Status and Updated At. Exact no-ops preserve bytes and metadata without creating another history entry. Focused shared-path Property and Section checks, stale/denied/unresolved refusal and failure/rollback checks pass without unrelated regressions or unauthorized effects. Pin final code/source/test evidence for P2362; preparation alone is not acceptance. Existing classification, authorization, lineage and recovery boundaries remain intact. This child does not close parent receiving/publication/runtime gates.
