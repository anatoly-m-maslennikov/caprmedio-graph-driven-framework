---
atom_id: CA-M-377
ref_id: CA-M-377
container:
  scope_unit: CA-SU-17
role: Method
form: Eng Decision
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication"
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
tier: 3
relations:
  depends_on:
  - CA-M-376
  - CA-D-625
status: Active
version: 16
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-M-377-CONNECTOR_TOOLS-ENG_DECISION--construct-a-declared-scope-unit-query-adapter.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-17_FEATURE_CONNECTOR_TOOLS/05_method
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
author: Anatoly Maslennikov
---
# Summary

Construct a declared Scope Unit query adapter

## Scope

Construction of a replaceable backend adapter for the Scope Unit Query contract.

## Claim

**to** construct the Scope Unit Query adapter, the Implementer **must** refine CA-M-376-CONNECTOR_TOOLS-ENG_DECISION--execute-one-explicit-connector-operation **without** creating a hidden Workflow:

- bind CA-D-626-CONNECTOR_TOOLS-STANDARD-DELIVERY--deliver-declared-scope-unit-query-data to the common request/result roles **and** supported `query` operation. keep logical Project context, canonical Scope Unit identities **and** predicates separate from private backend locators.
- resolve Project Settings **and** Project Structure through their admitted source bindings **and** schema authority. build matching facts **only** from their declared values **and** structural relations; a directory **or** Projection is **not** a substitute.
- use explicit frontier traversal **and** conjunctive literal predicates. retain a deterministic canonical-name order **and** source attribution; reject duplicate identities, unresolved parents **or** cycles instead of repairing the declaration graph.
- preserve source-view **and** expected-state checking, including exact requested historical evidence **where** available. recheck required source evidence **before** reporting complete coverage; a drift **or** unresolved frontier produces the declared non-success error rather than silently refreshing the request.
- build a mutation-free adapter **and** an independently observable result verifier. verify declared coverage **and** matching facts separately from absence of exceptions; use CA-D-625-CONNECTOR_TOOLS-ENG_DECISION--deliver-coherent-connector-interface for actual error/effect evidence.

## Details

CA-R-1937-CONNECTOR_TOOLS-RULE--query-declared-scope-units owns the required result and CA-E-629-CONNECTOR_TOOLS-EVAL_CASE--verify-declared-scope-unit-queries owns acceptance cases. This Method selects no storage technology, new transport, implicit whole-Project query, retry/resume policy or runnable binding.
