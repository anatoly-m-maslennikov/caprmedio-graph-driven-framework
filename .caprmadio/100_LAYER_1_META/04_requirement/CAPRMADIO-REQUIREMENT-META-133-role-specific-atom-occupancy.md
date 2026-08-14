---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-133
scope_path: layer:meta
subject_scope: artifact-model
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-088
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-080
      - CAPRMADIO-REQUIREMENT-META-131
  - type: relates_to
    targets:
      - CAPRMADIO-ANALYSIS-META-003
      - CAPRMADIO-REQUIREMENT-META-098
---

# Requirement — Admit Atoms only where a role has an atomic unit

An internal Content role receives an internal Atom Type only when the role has
an independently governed unit under its role-specific atomicity model that
benefits from stable identity, admission, and whole-unit lifecycle. CAPRMADIO
does not create placeholder Atom Types merely to fill every semantic coordinate.

For an admitted internal Atom route, the canonical `artifact_type` equals its
`content_role`. An Artifact Type is the registered top-level semantic class for
an admitted route. An optional direct subtype narrows that Type's governed
meaning without creating another top-level Type. Sub-subtypes are forbidden.

Plan admits the internal `plan` Atom Type. A Plan is a short-lived Atom whose
atomic unit is one bounded execution package containing one or more action
points. This does not create separate semantic kinds called “Plan” and “Plan
Atom”; the artifact is simply a Plan. Implementation does not require an
internal Atom Type: the native project outside `.caprmadio/` is the actual
Implementation, while Journals and Projections about that realization retain
their own Artifact forms. Whether external or relation Governance-locus
Implementation routes qualify as Atoms, and what atomicity model they use, is
deferred to CAPRMADIO-QUESTION-META-006.

## Primary claim

Internal Atom Type equality applies only to admitted atomic routes. Plan is a
short-lived atomic route, and CAPRMADIO does not require an internal
Implementation Atom.
