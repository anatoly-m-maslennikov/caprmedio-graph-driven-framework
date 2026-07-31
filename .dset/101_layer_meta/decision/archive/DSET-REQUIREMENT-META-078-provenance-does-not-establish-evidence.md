---
artifact_type: requirement
artifact_id: DSET-REQUIREMENT-META-078
scope_path: layer:meta
subject_scopes:
  - assurance
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - DSET-REQUIREMENT-META-076
  - type: relates_to
    targets:
      - DSET-REQUIREMENT-META-028
      - DSET-REQUIREMENT-META-073
---

# Requirement — Keep provenance separate from evidence

Provenance establishes the origin, carrier identity, revision, sequence, and
transformation history of a governed claim or implementation. It does not by
itself establish that the claim is correct, accepted, current, applicable, or
sufficiently assured.

Git history is canonical provenance for persisted repository state. A commit,
author identity, session identifier, signature, hash, or intact carrier proves
only the bounded historical fact it records. None of those facts becomes
evidence for the carrier's semantic claim without a separate, explicit
claim-bound evidence relation.

Evidence used for reliance must identify the claim it supports, the relevant
carrier or observation, the producing or interpreting work or method when
material, and the applicable scope and time boundary. Verification remains a
separate assurance conclusion. A claim, its carrier, and the work that created
it must not silently evidence themselves.

## Primary claim

Provenance makes governed history recoverable but never substitutes for
claim-bound evidence or Verification.

## Rationale

Separating historical authenticity from semantic support prevents Git history,
session metadata, generated reports, or signatures from becoming
self-justifying truth while retaining their full audit value.
