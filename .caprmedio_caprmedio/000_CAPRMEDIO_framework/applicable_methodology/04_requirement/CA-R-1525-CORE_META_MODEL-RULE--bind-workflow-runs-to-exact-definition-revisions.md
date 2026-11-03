---
subjects:
  active: Entity/Object/Occurrent/Execution/Workflow Run
  passive:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - Entity/Object/Occurrent/Execution/Step Run
  - Atom
  - Journal
  - Entity/Object/Continuant/Actor/Operator
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1525
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1525-CORE_META_MODEL-RULE--bind-workflow-runs-to-exact-definition-revisions.md
  source_atom_id: CA-R-1525
  source_atom_revision: 24
  source_sha256: 3fd24cdb5fb7b28a28bfdb699015a7ed9fb6c8ed041e3e727f1dc7e34f459464
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Bind Workflow Runs to exact definition Revisions

## Claim scope

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
