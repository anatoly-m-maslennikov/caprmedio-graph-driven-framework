---
cce_version: cce_1
cce_form: method
subjects:
  governs: provenance
  depends_on:
  - Subject/Engineering/Journal Operations
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Project
  - 'Subject/Domain/Node/Continuant/Projection/Type: Applicable Methodology'
version: 30
updated_at: 2026-10-24 02:14:24 +0400
relations:
  relates_to:
  - CA-R-1491
  method_for:
  - CA-R-803
  - CA-R-804
  - CA-R-805
  - CA-R-812
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-M-087@30
status: Archived
content_role: Method
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eng Decision
tier: 2
---
# Process one project-path action

use this composite Method for **`=1`** sealed project-path action. its subject is **`=1`** file **or** **`=1`** non-empty folder; a folder action has **`=1`** frozen ordered entry set **and** remains **`=1`** action.

1. COMMIT_TRIGGER atomically accepts **`=1`** immutable source event into the Runtime inbox **and** returns. it performs no repository scan, context gathering, Journal append, staging, Git mutation, retry, **or** worker spawn.
2. the independently supervised COMMIT_AUTOMATION service reconciles inbox events with the current Git-admitted repository frontier. its pure manager defines the fixed action graph **and** its mechanical Scheduler persists **and** advances **only** declared transitions. new events remain durable **and** mark the repository pending while another Git-mutating action is active.
3. a COMMIT_CONTEXT worker produces provisional deterministic context with the Initiative, expected frontier, resolved atomic target **or** frozen folder entry set, **and** provenance facts. Project **or** Git mutation consumers revalidate their mutation preconditions at their effect boundary. Journal append/read preserves supplied actual observations under CA-R-1491 without Journal validation, prior-history, chain, receipt, deduplication, retry or recovery gates; it does not require the observed Project state to remain unchanged.
4. from sealed context, advance two independent branches. an APPEND_CHANGE_RECORDS worker appends supplied actual observations through the shared plain append/read library, without suppressing repeated data or creating a reconciliation gate. preserve intact historical observations **without** silently rebinding them **to** later Project state. independently, a real-change item becomes eligible for the Git gate **without** waiting for the Journal branch.
5. a COMMIT_CHANGE_SET worker alone owns the repository-scoped fenced Git lease. it revalidates the sealed Initiative, action state, expected Git base, target frontier, **and** complete staged target set immediately **before** commit creation. it creates **`=1`** real-change commit containing **all** **and** **only** the action targets **or** **`=1`** separate Journal-only batch commit containing **only** selected Journal Carriers. it never imports **or** invokes its peer Tools **and** rejects **every** non-commit Git operation.
6. persist the Git action's transitions through queued, reconciling, context_sealed, real_change_pending **or** real_change_committed, **and** completed **or** no_change, with explicit retry_wait, paused, blocked **and** dead_letter outcomes. resume that Git work from its last safe persisted phase **and** reconcile uncertain commit outcomes **before** replay. Journal append/read is not a prerequisite, proof, retry branch **or** reconciliation state for this action; preserve truthful append I/O failure **without** automatic recording retry **or** source-effect replay.
7. reconcile at low frequency while enabled so missed Hook delivery **and** external Project edits do **not** make a host callback the correctness boundary.

return the common Tool result envelope. dry run predicts **only** context, queue **and** gate eligibility, message Projection, **and** the supplied Journal observations without writing. this Method never edits governed subject content, infers Atom meaning beyond the admitted action, **or** performs branch, upstream, remote, synchronization, push, tag, **or** release operations.

Plain Project Journal append/read may also be requested independently of this composite Git Method. It neither performs the recorded source effect nor requires this inbox, scheduler, Git lease or commit pipeline.
