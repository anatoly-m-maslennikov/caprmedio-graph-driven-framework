---
subject_scopes:
  - artifact-model
version: 2
updated_at: 2026-08-22 00:53:40
relations:
  concern_about:
    - CAPRMEDIO-META-REQU-084--relational-artifacts-declare-endpoints
    - CA-R-871-REQUIREMENT-BSEED_METAMODEL--distinguish-shared-authority-edges-and-relational-atoms
---
# Does Artifact semantic shape need an axis?

Solved: CAPRMEDIO admits `semantic_shape = standalone | relational` because an independently governed directional relationship requires validation, ownership, revision, and lifecycle behavior that ordinary graph connectivity does not imply.

Only directional relational Atoms are admitted. Shared descendant meaning uses an ordinary ancestor-scope RMEDO Atom, and a relationship without independently governed meaning remains a declared typed edge.
