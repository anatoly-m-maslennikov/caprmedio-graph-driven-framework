---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-143
scope_path: layer:gov
subject_scopes:
  - artifact-catalog
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-078
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-107
      - CAPRMADIO-REQUIREMENT-GOV-138
---

# Register Release Record as an Ops subtype

GOV registers `release_record` as a direct subtype of the internal Ops Atom
Type.

A Release Record is emitted only by the project's configured successful release
event. It identifies the released version and binds an exact manifest of the
applicable normative Atom revisions, realized Implementation and Delivery
revisions, Assurance and Ops records used for readiness, release identifier,
and canonical Git commit or tag.

Planning allocation, release-candidate naming, pull-request creation, or
implementation completion cannot emit a Release Record. A correction after
release requires another governed Atom; the released historical fact is not
rewritten.

## Rationale

The subtype gives the factual release boundary a precise carrier without
conflating mutable delivery planning, readiness judgment, or publication
mechanisms with the event that actually froze the version.
