---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-097
scope_path: layer:meta
subject_scope: assurance
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-078
  child_of:
    - CAPRMADIO-REQUIREMENT-META-091-authority-assurance-and-ops-remain-distinct
    - CAPRMADIO-REQUIREMENT-META-121-bind-traceability-to-exact-claims-and-revisions
---

# Requirement — Keep provenance separate from evidence

Provenance establishes the origin, carrier identity, revision, sequence, and transformation history of a governed claim or Implementation. It does not by itself establish that the claim is correct, accepted, current, applicable, or sufficiently assured.

Git history is canonical provenance for persisted repository state. A commit, author identity, session identifier, signature, hash, or intact carrier proves only the bounded historical fact it records. None of those facts becomes evidence for the carrier's semantic claim without a separate, explicit claim-bound Evidence relation.

Evidence used for reliance must identify the claim it supports, the relevant carrier or Ops record, the producing or interpreting work or Method when material, and the applicable scope and time boundary. Verification remains a separate Assurance conclusion. A claim, its carrier, and the work that created it must not silently evidence themselves.

## Primary claim

Provenance makes governed history recoverable but never substitutes for claim-bound Evidence or Verification.
