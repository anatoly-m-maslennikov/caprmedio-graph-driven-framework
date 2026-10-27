---
atom_id: CA-P-2334
content_role: Plan
type: Plan
label: Task
work_sequence_number: 9
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Tool
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Relation
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
version: 6
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-2307
tier: 3
---
# Summary

Deduplicate relation lookup targets

## Objective

One target used by different Relation Kinds is resolved once without changing authored Relations.

## Details

Estimated own work: up to 15 minutes. Independent relation-order testing found that a target used once in evaluation_for and once in depends_on is rejected as a duplicate lookup ID before graph validation. Confirm the existing lookup and per-kind relation contracts, then deduplicate only the internal lookup request. Keep original lists unchanged and retain duplicate-within-kind, endpoint, currentness and Relation Kind checks.

Verify the real complete-carrier failure before the fix, successful cross-kind reuse after it, and refusal for duplicate targets within one kind. Independent review is required. No public API, source policy, live mutation or new relation kind is included.

### Definition of Done

The Plan is not Done if valid cross-kind reuse still fails, authored Relations are rewritten, within-kind duplicates pass, or actual regression evidence and independent review are absent.

### Accepted outcome

The one-line fix deduplicates internal lookup IDs only. Author tests: three new regressions plus 18 reference-scope tests passed. Independent tests: three passed after a verified failing baseline, covering both default and scoped validation, unchanged metadata/bytes, within-kind duplicate refusal, and missing or duplicate actual-carrier refusal. Broader admission and publication remain separate. See cross-kind-relation-lookup-acceptance.md in the tools-first evidence directory.
