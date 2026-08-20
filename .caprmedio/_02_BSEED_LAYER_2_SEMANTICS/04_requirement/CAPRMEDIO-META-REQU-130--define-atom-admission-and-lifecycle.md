---
subject_scopes:
  - lifecycle-traceability
tier: core
version: 2
updated_at: 2026-08-20 05:48:13
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-M-001-METHOD-PRINCIPLE--mece-for-canonical-decompositions
---
# Define atom admission and lifecycle

CAPRMEDIO distinguishes these lifecycle meanings:

- `candidate` and `draft` name the same lifecycle meaning: an admitted Atom with stable identity that is not accepted as current authority;
- `accepted` means the operator approved the exact semantic contribution;
- `admitted` means the Atom has stable identity and satisfies the applicable entry rules for governed history;
- `committed` means the exact carrier revision was mirrored in Git;
- `active` means an accepted and admitted Atom participates in current authority when its Content role is authoritative;
- `solved` means a Concern received its terminal disposition and no longer requires action;
- `done` means an Analysis product or a Plan's action points were completed; and
- `archived` means a preserved Atom no longer participates in current authority.

Acceptance, admission, commitment, activation, completion, and archival remain distinct. None implies another unless a governed rule explicitly requires the combination. Archival preserves identity, revisions, relations, provenance, and historical dependents without preserving current authority.
