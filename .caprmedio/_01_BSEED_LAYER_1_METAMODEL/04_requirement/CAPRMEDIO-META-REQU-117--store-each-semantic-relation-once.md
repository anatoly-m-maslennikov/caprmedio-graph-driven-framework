---
subject_scopes:
  - artifact-model
version: 2
updated_at: 2026-08-18 05:02:06
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-118--let-the-dependent-atom-own-the-relation
    - CAPRMEDIO-META-REQU-107--bind-traceability-to-exact-claims-and-revisions
    - CAPRMEDIO-META-REQU-128--separate-artifact-carrier-and-revision
    - CAPRMEDIO-META-REQU-643--assign-one-authoritative-owner-to-each-governed-claim
---
# Store each semantic relation once

CAPRMEDIO persists each semantic relation in exactly one artifact carrier. It must not store an inverse backlink, reciprocal copy, or second representation of the same relation in another carrier.

Tools and projections derive inverse navigation from the one persisted relation whenever readers need to traverse it in the opposite direction.

Every semantic relation has one persisted owner and any inverse view is derived.
