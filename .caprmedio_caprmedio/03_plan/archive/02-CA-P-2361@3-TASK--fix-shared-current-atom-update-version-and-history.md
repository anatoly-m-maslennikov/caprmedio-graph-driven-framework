---
atom_id: CA-P-2361@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Atom
  - Revision
  - Journal
  - Tool
  - Plan
version: 3
updated_at: 2026-10-24 06:04:19 +0400
relations:
  is_decomposition_of:
  - CA-P-2257
tier: 3
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

### Completion checkpoint

Committed shared fix `bced47e49` implements the existing non-Draft identified current-Atom Update boundary without adding a writer. Current R1432 v11 remains pinned at SHA-256 `91f4b7c5600e775ae357230792fafe2e5e64433714dec1839a73553361a41202`. Final production SHA-256: `73f169c6497213c2a4fc4eecc299ac4956fb20c1a1a543c2f44dfabb6c218ad0`; author test: `092b0f20a73248487b9e0e4c2376d39e0c059c75806a9e20357b831a576f3628`; independent test: `cec7ed23909fd54f2b1d07a15c9ddffc65c647e10f0dcb5ef0a3d86afe90689c`.

Author regression evidence reports 125 checks PASS; independent actual shared-Update verification reports 9 methods/14 subtests PASS, and a separate independent scoped correctness review reports 41 checks PASS. The closure audit freshly reproduced the 9 independent tests in 1.676 seconds on unchanged final pins. Admitted carrier_only, equivalent_refinement and semantic_revision cases retain ID, increment Version exactly once, refresh Updated At and preserve exact prior bytes/metadata (including CRLF); exact no-op adds no history or changed effect. Actual Property preparation and Section edits feed the same admitted Update path; denied/stale/unresolved, rollback and failed-history-cleanup checks preserve authorization and truthful recovery evidence without unrelated fixture changes.

Acceptance is limited to this shared metadata/history correction and its independent checks. Generic Property/Section receiving integration, raw renderer work and parent P2257's wider gates remain open. Draft/legacy behavior is not changed or accepted; the 9 excluded Draft golden tests fail in setup against an old removed authority root and are reported as a separate fixture limitation, not a successful check or new policy. No live effects, public route, source-policy or runtime change is claimed.
