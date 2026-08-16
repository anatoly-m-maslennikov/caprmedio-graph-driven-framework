---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-057
scope_path: layer:meta
subject_scope: framework-boundary
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-031
  child_of:
    - CAPRMADIO-REQUIREMENT-META-066-meta-eligibility-rule
    - CAPRMADIO-REQUIREMENT-META-118-keep-meta-and-gov-implementation-neutral
---

# Requirement — Bound recursive self-hosting

## Primary claim

CAPRMADIO applies the same layer constitution and governance semantics to its own
repository while keeping reusable framework source, installed methodology, and
applied project truth under distinct owners.

The recursion terminates at a declared fixed point: the repository-local
applied authority selects a materialized methodology version, and that
methodology resolves without following a live reference back to its reusable
source or creating another governance owner.
