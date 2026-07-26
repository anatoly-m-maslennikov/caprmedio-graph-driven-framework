---
artifact_type: requirement
artifact_id: DSET-REQUIREMENT-META-074
scope_path: layer:meta
subject_scopes:
  - artifact-model
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - DSET-REQUIREMENT-META-073
  - type: relates_to
    targets:
      - DSET-REQUIREMENT-META-055
      - DSET-REQUIREMENT-META-072
---

# Requirement — Give every Atomic Artifact one independently replaceable claim

One Atomic Artifact owns exactly one independently replaceable claim. “One”
describes a lifecycle and replacement unit, not a sentence, paragraph, or file
length.

A candidate contains more than one claim and must be split when any part can:

- be implemented independently;
- be checked or evidenced independently;
- be resolved independently;
- change without changing the rest; or
- be replaced while the rest remains valid.

Supporting rationale, examples, acceptance criteria, and relation references
may remain in the same carrier only when they explain or bound the one primary
claim rather than establish another independently replaceable claim.

This invariant applies to every Atomic Artifact Type. In particular:

- a Definition atom establishes one obligation, boundary, or desired outcome;
- a Problem atom establishes one observed discrepancy;
- an Assurance atom establishes one check; and
- an Analysis atom establishes one primary conclusion.

Atomic semantic liveness is binary:

- `active` means the claim remains current; and
- `dead` means the carrier is archived and the claim is no longer current.

These conditions are derived from placement and relations, not stored as a
frontmatter status. Partial absorption, partial replacement, and partially
active atoms are forbidden.

An unbound multi-claim atom must be split before it freezes. If a frozen
historical atom contains several claims, one governed transaction creates the
complete set of single-claim successors and replaces the predecessor in full.
The predecessor moves unchanged to `archive/` only after no part of its claim
set remains current solely through that predecessor.

## Primary claim

Every Atomic Artifact is one independently replaceable claim and is either
fully active or fully dead; DSET has no partial absorption state.

## Rationale

Single-claim atoms align implementation, assurance, replacement, and archive
boundaries. A claim can then be superseded without silently killing unrelated
authority or leaving an ambiguous partially active predecessor.
