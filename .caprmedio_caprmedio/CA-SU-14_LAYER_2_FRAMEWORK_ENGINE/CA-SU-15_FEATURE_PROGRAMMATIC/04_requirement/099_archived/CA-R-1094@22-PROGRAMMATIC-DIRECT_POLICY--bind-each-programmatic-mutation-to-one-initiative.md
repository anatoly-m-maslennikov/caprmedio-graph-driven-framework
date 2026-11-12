---
identity:
  atom_id: CA-R-1094
  ref_id: CA-R-1094@22
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Traceability
  tier: 3
state:
  status: Archived
  version: 22
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-1094@22-PROGRAMMATIC-DIRECT_POLICY--bind-each-programmatic-mutation-to-one-initiative.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/099_archived
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
## Summary

Bind each programmatic mutation to one Initiative

## Claim

### Prose Claim

**every** accepted programmatic mutation **must** belong **to** **=1** sealed Initiative **and** one stable action identity. The Initiative **may** reference a persisted Plan **or** Task Atom **or** an ephemeral session task, **and** **must** retain a short summary derived from the human instruction plus sufficient structured context **to** identify that instruction **without** inventing a governed Plan Atom.

the sealed Initiative **and** action identity **must** survive asynchronous handoffs, retries, concurrent workers, Git commits, Journal records, **and** reconciliation. A worker **must not** replace them with a process, thread, adapter, **or** queue parent identity.

