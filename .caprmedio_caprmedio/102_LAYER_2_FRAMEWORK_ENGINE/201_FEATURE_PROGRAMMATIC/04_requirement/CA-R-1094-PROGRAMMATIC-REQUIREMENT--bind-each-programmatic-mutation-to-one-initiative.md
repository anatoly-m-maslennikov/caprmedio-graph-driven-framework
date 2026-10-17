---
subjects:
  governs: programmatic-mutation
  depends_on: []
version: 11
updated_at: "2026-10-18 03:44:50 +0400"
atom_id: CA-R-1094
content_role: Requirement
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
relations: {}
---
# Summary

Bind each programmatic mutation to one Initiative

## Scope

## Claim

**every** accepted programmatic mutation **must** belong **to** **=1** sealed Initiative **and** one stable action identity. The Initiative **may** reference a persisted Plan **or** Task Atom **or** an ephemeral session task, **and** **must** retain a short summary derived from the human instruction plus sufficient structured context **to** identify that instruction **without** inventing a governed Plan Atom.

the sealed Initiative **and** action identity **must** survive asynchronous handoffs, retries, concurrent workers, Git commits, Journal records, **and** reconciliation. A worker **must not** replace them with a process, thread, adapter, **or** queue parent identity.

## Details
