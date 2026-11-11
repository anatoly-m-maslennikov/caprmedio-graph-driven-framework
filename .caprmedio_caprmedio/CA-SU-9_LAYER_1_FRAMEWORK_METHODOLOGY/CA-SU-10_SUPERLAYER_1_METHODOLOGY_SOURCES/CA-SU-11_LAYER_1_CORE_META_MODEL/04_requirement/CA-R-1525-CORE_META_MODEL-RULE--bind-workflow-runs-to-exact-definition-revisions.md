---
atom_id: CA-R-1525
ref_id: CA-R-1525
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Workflow)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Workflow) >{1+} Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Step)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Action)'
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Step Run
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
tier: 2
status: Active
version: 25
updated_at: 2026-11-03 23:17:14 +0400
carrier_destination:
  file:
    name: CA-R-1525-CORE_META_MODEL-RULE--bind-workflow-runs-to-exact-definition-revisions.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Bind Workflow Runs to exact definition Revisions

## Claim

### Prose Claim


Business Workflow Runs and their exact definition Revisions admitted for execution. Technical read-only queries and maintenance of rebuildable query indexes are runtime activities, not Workflow Runs under this Rule.


**every** business Workflow Run **must** retain the exact Workflow graph Revision, referenced Step Atom Revisions, **and** referenced Action definition Revisions admitted for its execution.

## Details

- technical read-only queries and maintenance of rebuildable query indexes report normal output through runtime stdout and failures through runtime stderr. these activities create no Project Journal observation or definition-binding obligation under this Rule.
- record references **to** those source Revisions **and** the actual binding used by **every** Step Run as actual observations **in** the Project Journal, without prior-record, chain, validation, receipt, deduplication, retry or recovery prerequisites. a leaf Step Run records its exact Action binding; a containing Step Run records its Step binding and has no own Action binding; its nested Step Runs remain distinct under existing Run parentage **and** lineage. do **not** create independently maintained copies of the definitions as another authority.
- **before** dispatch **and** on recovery, check whether a bound definition has changed, been withdrawn, **or** become unavailable. a detected change pauses further dispatch for revalidation; the executor **must not** silently substitute the newest Revision **or** assume the old binding remains authorized.
- revalidation **must** identify the exact definitions admitted for the remaining work, check their compatibility with completed effects **and** remaining inputs, **and** satisfy the applicable approval conditions. resume **only** **after** that decision is actually made and retained in the Run's admitted execution evidence; unresolved compatibility **or** authority keeps execution blocked. Journal recording is an observation, not proof or a resume gate.
- completed Step Runs retain their original definition bindings **and** outcomes. revalidation **must not** rewrite history, reset retry allowances, **or** automatically replay completed effects.
- an Action already running follows its admitted interruption policy; a definition change alone does **not** authorize forced termination **or** blind replay. retain its actual result under the binding used **and** revalidate **before** further dispatch.
- definition binding does **not** freeze permissions **or** mutable target state. current authorization, required Operator decisions, **and** input freshness still apply **before** effects.
- a successor Workflow Run obtains its own admitted definition bindings rather than silently inheriting the predecessor's bindings for another Workflow.
