---
atom_id: CA-P-2400@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
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
  - Workflow
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 5
updated_at: 2026-10-24 08:10:13 +0400
relations:
  is_decomposition_of:
  - CA-P-2387
tier: 3
---
# Summary

Exclude concurrent native identity publication

## Objective

Keep fresh Atom ID allocation and publication collision-safe when native lifecycle calls run concurrently, without retained-history, Journal or pending-reservation admission prerequisites.

## Details

### Accepted completion — 2026-10-16

The native owner implemented one runtime-backed cross-process identity guard across fresh allocation and publication, including ordinary/direct/native Create/Promote and CLI fresh-ID paths. Independent review accepted reentrancy, release, symlink refusal and the interrupted-acquisition descriptor cleanup. The exact post-cleanup Linux image passed all four concurrency/interruption tests; no retained-history or Journal prerequisite was restored. CA-C-524 is Resolved. Code commit `3d658ee7a` and CA-A-1215 bind the observed final hashes and checks.

A threaded native review observed two ID-free Draft promotions both apply the same fresh CA-R-1876 to different carriers (created9901 and created9902). This is a native-path safety defect; the present connected MCP DBOS queue has concurrency one, so this observation does not establish a concurrent MCP exploit. CA-C-524 is now Resolved after the actual repair and independent checks; no prior Concern revision is invented.

Use project runtime identity exclusion for the actual allocation/publication interval and verify simultaneous native callers cannot publish one ID twice. Preserve source/currentness/permission/schema checks, fresh unused IDs, exact actual predecessor history and truthful partial failures. Do not reintroduce removed Draft-history/head/lineage or Journal gates, fabricate past records, add a second identity authority or replay effects.

Estimated own work: at most 15 minutes. Root owns integration; the native implementation owner and independent reviewer have distinct responsibilities. After the result, review the pending CA-P-2389/2390 verification inputs before continuing. The actual concurrency regression and independent acceptance are now complete, as recorded above.

## Definition of Done

The final native identity path has observed positive/negative concurrency regression results and independent acceptance at exact code pins. Any OS restriction or remaining failure is recorded separately. Focused tests alone do not establish installed runtime activation, connected MCP concurrency, a full suite or parent completion.
