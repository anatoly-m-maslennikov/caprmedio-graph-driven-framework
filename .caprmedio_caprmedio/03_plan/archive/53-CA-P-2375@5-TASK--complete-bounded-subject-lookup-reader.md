---
atom_id: CA-P-2375@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 53
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 5
updated_at: 2026-10-24 06:12:26 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
tier: 3
---
# Summary

Complete bounded Subject lookup reader

## Objective

Reuse the existing Subject reader and matcher for exact, prefix, suffix and contains. Validate selected logical scope and source freshness without forcing unrelated C/A or missing-Type migration. Preserve the CLI and use existing bounded read utilities.

## Details

Prepare fixtures independently; production edits require the accepted CA-P-2374 rule packet, and final protocol execution requires the ready CA-P-2375@5/2376 implementation. These are stage-specific gates, not a whole-Task start BLOCKS relation or an Artifact depends_on relation.

Estimated own work: up to 15 minutes; split before exceeding this bound. Follow the independently reviewed lookup-exposure proposal. Root owns integration and Git. Preserve unrelated changes. Core Subject migration, ordinary content migration, broader connector rebuilding and live publication remain outside this Task.

### Acceptance — 2026-10-14

Independent reader review passed after correcting live and dangling selected role-directory symlinks: incomplete frontiers refuse, while excluded Analysis links remain excluded. All 71 ATOM_SEARCH tests passed on final code. A read-only local Core diagnostic returned 127 matches with full coverage and zero diagnostics in 17.85 seconds; all 906 Core sources plus Settings/Structure and control membership were unchanged. This diagnostic is not a connected-MCP call.

Implementation: commit `2a40cb4c8`. [Local completion receipt](../../../_projection/core-entity-review/stage2/tools-first/direct-subject-lookup-local-completion.md). No Core Subject migration or ordinary content update was performed.

### Definition of Done

Focused reader tests cover matching, real grammar pins, logical scope, selected-ID ambiguity, stale sources and unrelated malformed C/A. Independent review passes.

