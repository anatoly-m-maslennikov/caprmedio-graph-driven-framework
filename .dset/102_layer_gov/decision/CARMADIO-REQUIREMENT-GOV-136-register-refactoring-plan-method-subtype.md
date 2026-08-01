---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-GOV-136
scope_path: layer:gov
subject_scopes:
  - artifact-catalog
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-086
      - CARMADIO-REQUIREMENT-META-088
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-GOV-138
---

# Requirement — Register Refactoring Plan as a Method subtype

GOV registers `refactoring_plan` as a direct subtype of the internal Method
Atom Type.

A Refactoring Plan selects one bounded, independently replaceable strategy for
changing an existing realization while preserving its declared behavior and
other applicable obligations. It identifies the target, preservation boundary,
intended structural transformation, applicable constraints, assurance needed,
and stop conditions. Independently replaceable transformations require sibling
Refactoring Plan Atoms rather than one compound plan.

A behavior or outcome change is governed by a separate Requirement Atom. A
Refactoring Plan may implement that Requirement, but it must not hide the
behavior change inside a refactoring claim.

## Primary claim

`refactoring_plan` is a direct internal Method subtype for one bounded
refactoring strategy.

## Rationale

Refactoring needs an accepted Method before implementation begins, while the
single-claim boundary prevents a broad plan from becoming an overlapping
container for unrelated transformations or hidden behavior changes.
