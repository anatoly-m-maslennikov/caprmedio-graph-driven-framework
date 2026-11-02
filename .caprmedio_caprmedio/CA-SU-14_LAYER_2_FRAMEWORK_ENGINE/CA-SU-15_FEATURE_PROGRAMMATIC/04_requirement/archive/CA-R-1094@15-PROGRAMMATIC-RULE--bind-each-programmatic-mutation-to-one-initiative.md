---
subjects:
  governs: Subject/Engineering/programmatic-mutation
  depends_on: []
version: 15
updated_at: 2026-10-24 11:58:20 +0400
atom_id: CA-R-1094@15
content_role: Requirement
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
relations: {}
tier: 3
type: Rule
---
# Summary

Bind each programmatic mutation to one Initiative

## Scope

## Claim

**every** accepted programmatic mutation **must** belong **to** **=1** sealed Initiative **and** one stable action identity. The Initiative **may** reference a persisted Plan **or** Task Atom **or** an ephemeral session task, **and** **must** retain a short summary derived from the human instruction plus sufficient structured context **to** identify that instruction **without** inventing a governed Plan Atom.

the sealed Initiative **and** action identity **must** survive asynchronous handoffs, retries, concurrent workers, Git commits, Journal records, **and** reconciliation. A worker **must not** replace them with a process, thread, adapter, **or** queue parent identity.

## Details
