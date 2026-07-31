---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-107
scope_path: layer:meta
subject_scopes:
  - release-finalization
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-080
      - CARMADIO-REQUIREMENT-META-086
      - CARMADIO-REQUIREMENT-META-105
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-004
      - CARMADIO-REQUIREMENT-META-076
      - CARMADIO-REQUIREMENT-META-091
      - CARMADIO-REQUIREMENT-META-097
---

# Requirement — Freeze a version only at release

A target version remains mutable until its configured release event succeeds.
The event may be, for example, acceptance of a release pull request into the
main branch, but each project declares its exact boundary.

Release creates one factual Ops Atom whose primary claim is that the identified
version was released with an exact manifest. The manifest binds the normative
Atom revisions, realized implementation and delivery revisions, applicable
assurance and evidence, release identifier, and canonical Git commit or tag.

Planning allocation, implementation completion, pull-request creation, or
release-candidate naming does not freeze the version before that event.

## Primary claim

A version freezes only when its configured release event creates an immutable,
revision-bound Ops Atom recording the exact released manifest.

## Rationale

One factual release boundary preserves planning flexibility while making the
delivered version replayable from exact authority, implementation, assurance,
delivery, and Git history.
