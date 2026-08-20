---
subject_scopes:
  - lifecycle-traceability
tier: core
version: 7
updated_at: 2026-08-20 20:02:11
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-M-001-PRINCIPLE-METHOD--mece_mutually-exclusive-collectively-exhaustive
---
# Define atom admission and lifecycle

CAPRMEDIO distinguishes these lifecycle meanings:

- `candidate` and `draft` name the same lifecycle meaning: an admitted Atom that omits `atom_id` and is not accepted as current authority;
- `accepted` means the operator approved the exact semantic contribution and, for a role-classified Atom, assigned the stable `atom_id` property;
- `admitted` means the Atom satisfies the applicable entry rules for governed history without thereby gaining stable identity or current authority;
- `committed` means the exact carrier revision was mirrored in Git;
- `active` means an accepted and admitted Atom participates in current authority when its Content role is authoritative;
- `solved` means a Concern received its terminal disposition and no longer requires action;
- `done` means an Analysis product or a Plan's action points were completed; and
- `archived` means a preserved Atom no longer participates in current authority.

Admission, acceptance, commitment, activation, completion, and archival remain
distinct transitions. Admission alone does not assign identity. Operator
acceptance of a role-classified draft assigns `atom_id` by definition; the other
transitions do not imply one another unless a governed rule explicitly requires
the combination. Archival preserves any assigned `atom_id`, Revisions,
relations, provenance, and historical dependents without preserving current
authority.
