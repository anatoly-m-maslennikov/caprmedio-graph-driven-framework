---
atom_id: CA-M-377
content_role: Method
type: Method
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-13 02:01:49 +0400"
subjects:
  governs: "Tool"
  depends_on: ["Scope Unit", "Project", "Project Structure", "Project Settings"]
relations:
  relates_to: [CA-R-1937, CA-E-629, CA-D-626, CA-O-211, CA-R-1936, CA-M-376, CA-E-628, CA-D-625, CA-R-1484, CA-D-442]
---
# Summary

Construct a declared Scope Unit query adapter

## Scope

Construction of a replaceable backend adapter for the Scope Unit Query contract.

## Claim

**to** construct the Scope Unit Query adapter, the Implementer **must** refine CA-M-376-CONNECTOR_TOOLS-CORE-METHOD--execute-one-explicit-connector-operation **without** creating a hidden Workflow:

- bind CA-D-626-CONNECTOR_TOOLS-STANDARD-DELIVERY--deliver-declared-scope-unit-query-data to the common request/result roles **and** supported `query` operation. keep logical Project context, canonical Scope Unit identities **and** predicates separate from private backend locators.
- resolve Project Settings **and** Project Structure through their admitted source bindings **and** schema authority. build matching facts **only** from their declared values **and** structural relations; a directory **or** Projection is **not** a substitute.
- use explicit frontier traversal **and** conjunctive literal predicates. retain a deterministic canonical-name order **and** source attribution; reject duplicate identities, unresolved parents **or** cycles instead of repairing the declaration graph.
- preserve source-view **and** expected-state checking, including exact requested historical evidence **where** available. recheck required source evidence **before** reporting complete coverage; a drift **or** unresolved frontier produces the declared non-success error rather than silently refreshing the request.
- build a mutation-free adapter **and** an independently observable result verifier. verify declared coverage **and** matching facts separately from absence of exceptions; use CA-D-625-CONNECTOR_TOOLS-CORE-DELIVERY--deliver-coherent-connector-interface for actual error/effect evidence.

## Details

CA-R-1937-CONNECTOR_TOOLS-STANDARD-REQUIREMENT--query-declared-scope-units owns the required result and CA-E-629-CONNECTOR_TOOLS-STANDARD-QA_CASE--verify-declared-scope-unit-queries owns acceptance cases. This Method selects no storage technology, new transport, implicit whole-Project query, retry/resume policy or runnable binding.
