---
subject_scopes:
  - artifact-model
version: 5
updated_at: 2026-08-20 18:43:06
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-098--scope-path-does-not-change-semantic-coordinates
    - CAPRMEDIO-META-REQU-128--separate-artifact-carrier-and-revision
---
# Separate immutable Atom ID from mutable scope

`atom_id` is the optional property whose value is a role-classified Atom's
stable identity. A role-classified draft omits `atom_id`; operator acceptance
assigns exactly one value with the semantic components
`<PREFIX>-<CONTENT_ROLE_LETTER>-<NUMBER>`. The sole roleless Intent Atom uses
its separately governed canonical identity instead of `atom_id`. Once assigned,
the property is immutable and independent of the Atom's mutable Carrier
filename, Structural scope, Tier, Summary, format, and Revision. A change to an
identity-bearing semantic fact does not mutate `atom_id`; it creates a
successor Atom with a new value.
