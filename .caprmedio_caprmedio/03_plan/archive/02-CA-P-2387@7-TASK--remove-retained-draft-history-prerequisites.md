---
atom_id: CA-P-2387@7
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
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Atom/Status
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Engineering/Workflow
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 7
updated_at: 2026-10-24 08:22:45 +0400
relations:
  is_decomposition_of:
  - CA-P-2385
tier: 3
---
# Summary

Remove retained Draft-history prerequisites

## Objective

The ordinary affected execution path accepts manual Draft promotion without a retained-history directory or records. Existing retained records are optional evidence, not permission; actual failures and partial effects remain truthful.

## Details

### Accepted completion — 2026-10-16

The native path now accepts valid manual ID-free Drafts without retained-history/head/lineage/successor prerequisites. Every ordinary ID-free promotion uses a fresh unused ID; exact actual history and collision/source/permission safeguards remain. CA-P-2400 closed the independently found native publication race and descriptor-cleanup correction after independent review and exact post-cleanup Linux checks. CA-C-524 is Resolved; the unrelated host restriction remains Active in CA-C-523. Implementation commit `3d658ee7a` and CA-A-1215 record the bounded acceptance.

- [CA-P-2400 — Exclude concurrent native identity publication](02-CA-P-2387@7-TASK--remove-retained-draft-history-prerequisites/done/01-CA-P-2400-TASK--exclude-concurrent-native-identity-publication.md)

Remove trusted-head, never-identified/demotion lineage and consuming-successor prerequisites from the affected lifecycle and MCP/Workflow adapters. A valid manually authored Draft with no retained-history records must be promotable through the ordinary interface. Reuse existing identity/collision and source-write safety behavior; do not require retrospective registration, invent provenance or delete real history.

Estimated own work: at most 15 minutes; split further before execution if needed. After completion, review/update the next dependent task. A blocked leaf is postponed with a truthful Problem/Question Concern as appropriate; independent ready work continues.

## Definition of Done

The ordinary affected execution path accepts manual Draft promotion without a retained-history directory or records. Existing retained records are optional evidence, not permission; actual failures and partial effects remain truthful.
