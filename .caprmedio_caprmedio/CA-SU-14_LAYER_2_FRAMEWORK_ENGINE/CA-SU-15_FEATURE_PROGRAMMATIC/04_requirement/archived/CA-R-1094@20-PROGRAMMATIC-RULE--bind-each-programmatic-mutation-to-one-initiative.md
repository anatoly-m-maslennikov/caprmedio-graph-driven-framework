---
atom_id: CA-R-1094
ref_id: CA-R-1094@20
container:
  scope_unit: CA-SU-15
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect
    Authorization
tier: 3
status: Archived
version: 20
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1094@20-PROGRAMMATIC-RULE--bind-each-programmatic-mutation-to-one-initiative.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/archived
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Bind each programmatic mutation to one Initiative

## Scope

## Claim

**every** accepted programmatic mutation **must** belong **to** **=1** sealed Initiative **and** one stable action identity. The Initiative **may** reference a persisted Plan **or** Task Atom **or** an ephemeral session task, **and** **must** retain a short summary derived from the human instruction plus sufficient structured context **to** identify that instruction **without** inventing a governed Plan Atom.

the sealed Initiative **and** action identity **must** survive asynchronous handoffs, retries, concurrent workers, Git commits, Journal records, **and** reconciliation. A worker **must not** replace them with a process, thread, adapter, **or** queue parent identity.

## Details
