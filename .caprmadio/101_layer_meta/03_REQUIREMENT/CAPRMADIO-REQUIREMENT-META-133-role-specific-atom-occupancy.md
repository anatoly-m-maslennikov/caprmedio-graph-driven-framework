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

# Requirement — Admit Atoms only where a role has an atomic claim

An internal Content role receives an internal Atom Type only when the role has
an independently governed claim that benefits from atomic admission and
replacement. CAPRMADIO does not create placeholder Atom Types merely to fill
every semantic coordinate.

For an admitted internal Atom route, the canonical `artifact_type` equals its
`content_role`. A direct subtype may refine that Type without introducing
another top-level Type for the same route.

Plan admits the internal `plan` Atom Type. Implementation does not require an
internal Atom Type: the native project outside `.caprmadio/` is the actual
Implementation, while Journals and Projections about that realization retain
their own Artifact forms. External or relational Implementation routes may be
admitted independently when they carry a materially distinct governed claim.

## Primary claim

Internal Atom Type equality applies only to admitted atomic routes; CAPRMADIO
permits empty Atom coordinates and does not require an internal Implementation
Atom.

## Rationale

Artifact-form occupancy should follow semantic need. Forcing an Atom into every
role confuses the realized project with a record about it and creates artificial
types solely for matrix completeness.
