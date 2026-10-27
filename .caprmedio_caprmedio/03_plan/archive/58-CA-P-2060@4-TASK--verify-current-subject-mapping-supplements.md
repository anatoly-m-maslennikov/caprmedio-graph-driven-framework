---
atom_id: CA-P-2060@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 58
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Entity
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject
  - Subject/Domain/Node/Continuant/Projection
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 4
updated_at: 2026-10-24 06:12:20 +0400
relations:
  is_decomposition_of:
  - CA-P-1966
tier: 3
---
# Summary

Verify current Subject mapping supplements

## Objective

Independently validate the mapping supplements before they can replace baseline candidate decisions.

## Details

Estimated own work: 15 minutes. Prepare a small read-only ad-hoc support/verify_subject_supplements.py and isolated tests; do not register a reusable Tool. Verify the eight research/correction outputs plus the Substance overlay against the frozen baseline, exact ownership IDs, input/source/evidence pins and span hashes, confidence/value invariants, candidate pointers, quarantine/origin preservation and executable=false. The checker is not semantic acceptance. Independent read-only peers inspect high-impact meanings. No Core, Plan, captured report, baseline ledger, MCP/FPF or runtime writes. Use .caprmedio_tmp for isolated fixtures and uv. Report failures rather than silently excluding incomplete or stale data. Root alone integrates and commits.

### Definition of Done

Not Done if required checks fail or are missing, source/evidence pins are stale, scope expands beyond the approved changes, unresolved work is hidden, actual effects are overstated, or own work exceeds 15 minutes without decomposition.

### Completion

Read-only checker independently reviewed by subject_review_005. Eight isolated tests passed under offline uv; the current full check passed for nine supplements and 2,163 occurrences. Receipt: `_projection/core-entity-review/stage2/task-2060.receipt.json`. This confirms structural pins, coverage and provenance only. Research and semantic acceptance remain open; no authoritative Atom or Subject was changed. Later grammar adoption makes its five old source pins historical and requires rebinding before migration.
