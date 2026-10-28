---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
version: 21
updated_at: 2026-10-27 19:59:57 +0400
relations: {}
atom_id: CA-R-1525
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Bind Workflow Runs to exact definition Revisions

## Scope

Workflow Runs **and** their exact definition Revisions admitted for execution.

## Claim

**every** Workflow Run **must** retain the exact Workflow graph Revision, referenced Step Atom Revisions, **and** referenced Action definition Revisions admitted for its execution.

## Details

- record references **to** those source Revisions **and** the actual binding used by **every** Step Run as actual observations **in** the Project Journal, without prior-record, chain, validation, receipt, deduplication, retry or recovery prerequisites. a leaf Step Run records its exact Action binding; a containing Step Run records its Step binding and has no own Action binding; its nested Step Runs remain distinct under existing Run parentage **and** lineage. do **not** create independently maintained copies of the definitions as another authority.
- **before** dispatch **and** on recovery, check whether a bound definition has changed, been withdrawn, **or** become unavailable. a detected change pauses further dispatch for revalidation; the executor **must not** silently substitute the newest Revision **or** assume the old binding remains authorized.
- revalidation **must** identify the exact definitions admitted for the remaining work, check their compatibility with completed effects **and** remaining inputs, **and** satisfy the applicable approval conditions. resume **only** **after** that decision is actually made and retained in the Run's admitted execution evidence; unresolved compatibility **or** authority keeps execution blocked. Journal recording is an observation, not proof or a resume gate.
- completed Step Runs retain their original definition bindings **and** outcomes. revalidation **must not** rewrite history, reset retry allowances, **or** automatically replay completed effects.
- an Action already running follows its admitted interruption policy; a definition change alone does **not** authorize forced termination **or** blind replay. retain its actual result under the binding used **and** revalidate **before** further dispatch.
- definition binding does **not** freeze permissions **or** mutable target state. current authorization, required Operator decisions, **and** input freshness still apply **before** effects.
- a successor Workflow Run obtains its own admitted definition bindings rather than silently inheriting the predecessor's bindings for another Workflow.
