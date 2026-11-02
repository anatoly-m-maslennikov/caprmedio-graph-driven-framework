---
atom_id: CA-P-2418@2
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Atom
  - Scope Unit
  - Property
  - Tool
  - Workflow
relations:
  is_decomposition_of:
  - CA-P-2402
version: 2
updated_at: 2026-10-20 11:04:37 +0000
---
# Summary

Verify project attribution and immutable session input prefixes

## Objective

Complete one bounded evidence/safety prerequisite for the scoped five-day MCP audit without treating incomplete evidence as a completed operation.

## Details

Independently check actual session/turn Project or cwd metadata for the five-day frontier, rather than accepting any incidental mention of the repository. Inspect direct MCP event schemas and timestamp boundaries, distinguish invocation and completion time, and specify append-safe prefix byte/line cutoffs plus hashes so later log appends do not invalidate frozen evidence. Review the corrected direct-event release for omissions, ambiguous attribution and coverage overclaim. Read-only verification; no server, MCP, source or Git mutation.

Use a Luna worker and at most15minutes own work. Split any longer responsibility into a separately recorded bounded subtask before continuing. Historical analysis is MCP-call-only; this Task does not authorize implementation fixes, deployment or production tests. Manual permission covers planning records only, not Concern/source writes. All actual runtime reproductions require the verified disposable nonproduction harness.

### Definition of Done

The assigned evidence or fixture result has reproducible source references, exact observed outcomes and honest gaps; independent acceptance checks pass or blockers are recorded without effects being replayed. Production remains untouched. Planning checkpoint: Independent review accepts the bounded 384 native lifecycle rows for semantic analysis, not complete corpus/immutable session provenance. Every selected row has unique native identity, request/result, timestamps/status and exact project cwd proof; mixed-cwd rows have turn proof. Rejected claims: full-session immutable prefixes (4 KiB header only), complete-line prefix labels, and metadata saying outer-event window where payload-start is used. These limitations remain under CA-P-2416 and are explicitly carried into dependent Tasks. No source or runtime correction was performed.
