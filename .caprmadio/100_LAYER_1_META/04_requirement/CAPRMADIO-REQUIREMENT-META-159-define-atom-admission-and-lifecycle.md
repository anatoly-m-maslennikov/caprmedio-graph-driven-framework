---
subject_scopes:
  - lifecycle-traceability
tier: core
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
---
# Define atom admission and lifecycle

CAPRMADIO distinguishes these lifecycle meanings:

- `candidate` is exploratory material without governed Atom identity;
- `draft` is an admitted Atom with stable identity that is not accepted as current authority;
- `accepted` means the operator approved the exact semantic contribution;
- `admitted` means the Atom has stable identity and satisfies the applicable entry rules for governed history;
- `committed` means the exact carrier revision was mirrored in Git;
- `active` means an accepted and admitted Atom participates in current authority when its Content role is authoritative;
- `solved` means a Concern received its terminal disposition and no longer requires action;
- `done` means an Analysis product or a Plan's action points were completed; and
- `archived` means a preserved Atom no longer participates in current authority.

Acceptance, admission, commitment, activation, completion, and archival remain distinct. None implies another unless a governed rule explicitly requires the combination. Archival preserves identity, revisions, relations, provenance, and historical dependents without preserving current authority.
