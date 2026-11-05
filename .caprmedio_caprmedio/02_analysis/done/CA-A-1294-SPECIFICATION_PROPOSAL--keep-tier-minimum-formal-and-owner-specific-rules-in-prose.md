---
atom_id: CA-A-1294
ref_id: CA-A-1294
role: Analysis & Advisory
form: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Done
author: Anatoly Maslennikov
topics:
  main_subject: Model::CAPRMEDIO::Graph Syntax
version: 3
tier: 3
updated_at: 2026-11-02 15:49:28 +0400
container:
  scope_unit: CA-SU-00
---
# Summary

Keep the Tier minimum formal and owner-specific rules in prose

## Decision

Use the simple formal part:

```text
atom.tier[int, >=-1]
```

Express the remaining Tier conditions in prose. This does not change the established policy: Project Goals have Tier -1 and Operator ownership; ordinary Project-local Atoms have Tier >=0; other ordinary Atoms have Tier >=1. The general lower bound is not permission to use -1 for every Project-local Atom.

Do not introduce an owning-Scope lookup function or conditional expression merely to restate this case. A1292 and A1293 preserve the exploratory alternatives, which are deferred. The previous policy-versus-syntax question is resolved by retaining the existing policy and using prose for the owner-specific conditions.

## State

A next-version Tier Definition Draft and the base-property/Model Draft annotations use the simple bound. No Current Tier value or policy is migrated; runtime is unchanged.
