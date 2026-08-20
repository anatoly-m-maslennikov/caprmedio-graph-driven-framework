---
subject_scopes:
  - lifecycle-traceability
tier: core
version: 3
updated_at: 2026-08-20 06:09:50
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-M-001-PRINCIPLE-METHOD--mece-for-canonical-decompositions
---
# Define atom admission and lifecycle

CAPRMEDIO distinguishes these lifecycle meanings:

- `candidate` and `draft` name the same lifecycle meaning: an admitted Atom without stable identity that is not accepted as current authority;
- `accepted` means the operator approved the exact semantic contribution and assigns the stable Atom ID;
- `admitted` means the Atom satisfies the applicable entry rules for governed history without thereby gaining stable identity or current authority;
- `committed` means the exact carrier revision was mirrored in Git;
- `active` means an accepted and admitted Atom participates in current authority when its Content role is authoritative;
- `solved` means a Concern received its terminal disposition and no longer requires action;
- `done` means an Analysis product or a Plan's action points were completed; and
- `archived` means a preserved Atom no longer participates in current authority.

Acceptance, identity assignment, admission, commitment, activation, completion, and archival remain distinct. None implies another unless a governed rule explicitly requires the combination. Archival preserves any assigned Atom ID, revisions, relations, provenance, and historical dependents without preserving current authority.
