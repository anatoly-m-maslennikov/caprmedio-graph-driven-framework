---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-103
scope_path: layer:meta
subject_scopes:
  - artifact-model
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-REQUIREMENT-META-074
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-080
      - CARMADIO-REQUIREMENT-META-086
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-101
---

# Requirement — Give every Atom one independently replaceable claim

One Atom owns exactly one independently replaceable claim. “One” describes a lifecycle and replacement unit, not a sentence, paragraph, or file length.

A candidate contains more than one claim and must be split when any part can:

- be implemented independently;
- be checked or evidenced independently;
- be resolved independently;
- change without changing the rest; or
- be replaced while the rest remains valid.

Supporting rationale, examples, acceptance criteria, and relation references may remain in the same carrier only when they explain or bound the one primary claim rather than establish another independently replaceable claim.

This invariant applies to every Atom Type. For example:

- a Requirement Atom establishes one obligation, boundary, or desired outcome;
- a Concern Atom establishes one matter requiring disposition;
- an Assurance Atom establishes one check or proof obligation;
- a Delivery Atom establishes one delivery rule;
- a Method Atom establishes one realization approach;
- an Analysis Atom establishes one primary conclusion; and
- an Ops Atom establishes one enacted or observed fact.

Atomic identity liveness is binary:

- `active` means the artifact ID has a current carrier revision; and
- `dead` means the carrier is archived and the artifact ID is no longer current.

These conditions are derived from placement and relations, not stored as frontmatter status. Partial absorption, partial replacement, and partially active artifact identities are forbidden. Earlier committed revisions remain immutable Git history and may retain revision-bound dependents.

A multi-claim candidate must be split before admission. If an admitted historical artifact contains several independently replaceable claims, one governed replacement creates the complete set of single-claim successors and replaces the predecessor in full. The predecessor moves unchanged to `archive/` only after no part of its claim set remains current solely through that predecessor.

## Primary claim

Every Atom is one independently replaceable claim and is either fully active or fully dead; CARMADIO has no partial absorption state.

## Rationale

Single-claim Atoms align implementation, assurance, replacement, and archive boundaries without forcing one sentence or one file-length limit.
