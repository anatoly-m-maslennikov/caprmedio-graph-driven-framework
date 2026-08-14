---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-137
scope_path: layer:meta
subject_scope: lifecycle-traceability
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-130
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-080
      - CAPRMADIO-REQUIREMENT-META-131
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-113
---

# Requirement — Use Implementation Record as a Projection

An Implementation Record is an Implementation-role Projection of what the
current normative Atom frontier, native project targets, available provenance,
and any registered implementation lineage sources show as implemented.

It may report realization coverage, source-to-target bindings, relevant
commits, and unresolved implementation gaps. It is regenerated mechanically or
rebuilt through governed reasoning from its declared source frontier. It is
never an Atom and cannot replace normative Atoms, native implementation, Ops
evidence, or Verification.

The presence of this Projection does not require an internal Implementation
Atom. Storage, retention, and whether the Projection is committed or generated
at runtime remain governed separately.

## Primary claim

CAPRMADIO represents the current view of project realization through an
Implementation Record Projection rather than an Implementation Atom.
