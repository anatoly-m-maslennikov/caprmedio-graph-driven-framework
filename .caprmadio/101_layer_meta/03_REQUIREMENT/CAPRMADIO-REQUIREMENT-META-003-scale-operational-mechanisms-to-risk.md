---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-003
scope_path: layer:meta
subject_scope: scope-topology
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
---

# Requirement — Scale operational mechanisms to risk

## Primary claim

CAPRMADIO requires operational mechanisms to be proportional to explicit
failure risk and a declared authoritative-state boundary. It never mandates
one recovery or durability mechanism for every project.

## Rationale

Downstream profiles can select event sourcing, reconciliation, durable
execution, observed-progress checks, or simpler mechanisms according to
topology, write volume, concurrency, and recovery needs. Stateless services,
modest-write local tools, and concurrent durable systems should not inherit the
same mechanism merely because CAPRMADIO governs all three.
