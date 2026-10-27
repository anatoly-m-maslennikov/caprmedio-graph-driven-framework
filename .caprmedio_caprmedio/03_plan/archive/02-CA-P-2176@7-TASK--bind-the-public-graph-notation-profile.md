---
atom_id: CA-P-2176@7
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
  - Subject
  - Subject/Domain/Node/Continuant/Projection
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 7
updated_at: 2026-10-24 08:22:45 +0400
relations:
  is_decomposition_of:
  - CA-P-2172
  blocks:
  - CA-P-2174
tier: 3
---
# Summary

Bind the public graph notation profile

## Objective

The existing public graph entry point uses an explicit approved profile under the accepted contracts.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Required prerequisites: CA-P-2169 and its actual current public graph contract packet independently accepted under CA-P-2171. Other contract packets need not be complete. Reopen public graph callers/exports/fixtures and bind the affected entry-point files. Own public profile forwarding/validation and its focused tests; reuse the internal reviewed parser and coordinate shared files with integration.

Apply the smallest change that carries and validates the selected approved profile through the existing path. Check approved compact/selector forms, `Atom`/`atom` case, unsupported/absent explicit selection, legacy/default behavior, pins and provenance. Do not add native Relations or infer meanings from candidate display paths. Deliver code/test pins and actual results to CA-P-2174. Split larger work before execution. No production graph or Core source change occurs.

### Completion receipt

The actual public graph contract packet passed [independent contract acceptance](../../../../_projection/core-entity-review/stage2/tools-first/contract-acceptance.md) before implementation. Commit `a8da9b50b` implements the explicit approved profile in the existing request/entry-point/source path and adds its focused public-profile checks. `tools_first_verifier` independently accepted the bounded implementation. Root ran 245 graph checks and four MCP descriptor checks; all passed. Legacy/default behavior, case distinctions, grammar/source pins and publication/no-op safeguards remain covered; parsing grants no native fact admission or selector resolution.

This completes CA-P-2176@7 only. Preview-fix acceptance, the combined CA-P-2174 Tool receipt, admitted application implementation and live migration gates remain separate. No Core source or runtime publication effect is claimed.

### Definition of Done

The Plan is **not** Done if contract acceptance is missing/stale, a caller silently uses the wrong profile, legacy/case/source semantics regress, native admission is inferred, focused checks fail, or own work exceeds 15 minutes without decomposition.
