---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-107
scope_path: layer:meta
subject_scope: development-flow
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-135-preserve-content-role-boundaries-through-caprmadio-loop
---
# Requirement — Freeze a version only at release

A target version remains mutable until its configured release event succeeds.
The event may be, for example, acceptance of a release pull request into the
main branch, but each project declares its exact boundary.

Release creates one factual Ops Atom called the Release Record, whose primary
claim is that the identified version was released with an exact manifest. The manifest binds the normative
Atom revisions, realized implementation and delivery revisions, applicable
assurance and evidence, release identifier, and canonical Git commit or tag.

META owns the Release Record's freeze semantics. GOV owns its concrete
Type/subtype registration and carrier rules.

Planning allocation, implementation completion, pull-request creation, or
release-candidate naming does not freeze the version before that event.

## Primary claim

A version freezes only when its configured release event creates an immutable,
revision-bound Release Record with the Ops Content role and exact released
manifest.
