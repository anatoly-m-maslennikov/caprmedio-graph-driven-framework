---
atom_id: CA-P-2385@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 61
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Atom/Status
  - Subject/Domain/Node/Continuant/History/Journal
  - Workflow
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 5
updated_at: 2026-10-24 06:12:26 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
tier: 3
---
# Summary

Remove history and Journal gates from Atom Status operations

## Objective

MCP supports creation in any requested admitted Status and explicit update to any requested admitted Status without retained Draft-history or Journal admission checks. A Journal may be incomplete; that is not a blocker.

## Details

### Accepted completion — 2026-10-16

All bounded children, including the discovered native concurrency Task CA-P-2400, are Done after actual source alignment, implementation, independent review and isolated functional/connected checks. Source commit `dc6cfa1da` contains 23 source revisions, exact predecessors and 23 bounded LIAs; implementation commit `3d658ee7a` contains the accepted code/tests/fixture pins. CA-A-1215 binds exact final native hashes, image-specific checks and their limits. CA-C-524 is Resolved. CA-C-523 remains Active for independent host OS failures; no failed host run, full-suite, installed runtime activation, release or unrelated Plan completion is claimed.

### Operator decision — 2026-10-15

The Operator rejected the blocker that manually created Drafts cannot be promoted because MCP cannot find retained-history records. Drop this prerequisite rather than register retrospective history. MCP must permit Atom creation in any admitted Status and explicit Status updates. No Journal existence, completeness, continuity, baseline, receipt or prior-record check may gate these operations or their success. This latest decision supersedes conflicting earlier history/Journal-gate instructions for this task.

Journal append remains a separate attempt to record actual observations. Incomplete records or append failure do not invalidate a completed mutation and never authorize replay. Do not fabricate missing provenance or delete real history. Ordinary schema, identity, target/currentness and permission safeguards remain; no substitute history or Journal gate is introduced.

This task was opened as pending implementation; the accepted completion above records the bounded implemented and verified result. Related existing work is CA-P-2260 (creation), CA-P-2264/CA-P-2318 (Status), CA-P-2339 (promotion identity), and CA-P-2363/CA-P-2364 (local Draft bundles). Reconcile contradictory assumptions during implementation; do not silently mark these Plans Done or cascade Status changes.

### Ordered bounded work

- [CA-P-2386 — Align Atom Status and Journal contracts](61-CA-P-2385@5-TASK--remove-history-and-journal-gates-from-atom-status-operations/done/01-CA-P-2386-TASK--align-atom-status-and-journal-contracts.md)
- [CA-P-2387 — Remove retained Draft-history prerequisites](61-CA-P-2385@5-TASK--remove-history-and-journal-gates-from-atom-status-operations/done/02-CA-P-2387-TASK--remove-retained-draft-history-prerequisites.md)
- [CA-P-2388 — Allow requested Status on Atom create and update](61-CA-P-2385@5-TASK--remove-history-and-journal-gates-from-atom-status-operations/done/03-CA-P-2388-TASK--allow-requested-status-on-atom-create-and-update.md)
- [CA-P-2389 — Verify Status operations without history or Journal](61-CA-P-2385@5-TASK--remove-history-and-journal-gates-from-atom-status-operations/done/04-CA-P-2389-TASK--verify-status-operations-without-history-or-journal.md)
- [CA-P-2390 — Verify connected MCP Status behavior](61-CA-P-2385@5-TASK--remove-history-and-journal-gates-from-atom-status-operations/done/05-CA-P-2390-TASK--verify-connected-mcp-status-behavior.md)

Each leaf is one file and estimated at no more than 15 minutes; split further before execution if needed. This parent owns at most 15 minutes of coordination. After each child completes, review and update the next dependent child. Postpone blocked work with truthful issue records and continue independent ready work.

## Definition of Done

Contracts and actual implementation satisfy the decision, functional regressions cover manual Drafts and missing/incomplete Journals, and independent review plus actual connected checks are recorded separately. This Plan's creation does not complete its children, authorize an unrelated release, or establish a runtime change.
