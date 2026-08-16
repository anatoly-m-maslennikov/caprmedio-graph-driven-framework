---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-159
scope_path: layer:meta
subject_scopes:
  - lifecycle-traceability
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
    - CAPRMADIO-REQUIREMENT-116-preserve-strict-semantic-distinctions
---

# Define Atom admission and lifecycle

CAPRMADIO separates lifecycle conditions from lifecycle events:

- a `candidate` is exploratory material without governed Artifact identity;
- a `draft` is an admitted Atom with stable identity in `drafts/`, governed but
  not accepted as current authority;
- `accepted` means the operator approved the exact semantic claim;
- `admitted` means the carrier has stable identity and satisfies the applicable
  governance rules for entry into governed history;
- `committed` means an exact carrier revision was persisted in Git;
- `active` means an accepted, admitted Atom has its current carrier in the
  active location and participates in current authority when applicable;
- `done` is the terminal placement of a fully executed Plan; and
- `archived` means the Artifact is preserved in `archive/` but no longer
  participates in current authority.

Acceptance, admission, commitment, and activation are distinct events or
conditions. A committed draft is not active authority. An accepted claim that
has not been admitted and committed is not yet durable current authority.
Archiving an Atom makes its identity dead for current authority without erasing
its revisions, relations, provenance, or historical dependents. `done` applies
only to Plans and records successful execution rather than rejection or
replacement.

Lifecycle conditions are derived from governed history, canonical placement,
and explicit relations rather than duplicated status properties. GOV owns the
valid transition procedure and carrier operations.

CAPRMADIO distinguishes candidate, draft, accepted, admitted, committed,
active, done, and archived semantics so that operator approval, governance,
Git persistence, and current authority cannot be conflated.
