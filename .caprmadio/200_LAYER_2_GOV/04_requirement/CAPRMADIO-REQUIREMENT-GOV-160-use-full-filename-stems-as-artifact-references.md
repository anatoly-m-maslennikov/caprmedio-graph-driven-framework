---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-160
scope_path: layer:gov
subject_scopes:
  - relation-model
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-181-simple-outside-necessarily-complex-inside
    - CAPRMADIO-REQUIREMENT-META-139-use-canonical-carrier-address-as-authority
    - CAPRMADIO-REQUIREMENT-META-149-keep-an-atom-summary-immutable
    - CAPRMADIO-REQUIREMENT-META-165-economical-readable-yaml-frontmatter
    - CAPRMADIO-REQUIREMENT-GOV-159-encode-relations-as-relation-kind-maps
---

# Use full filename stems as Artifact references

Every relation target in a Markdown Atom must be the target Artifact's complete
filename without its extension. The Artifact reference therefore includes the
Artifact ID and immutable summary while omitting the redundant `.md` suffix.

The resolver must extract and validate the Artifact ID, find exactly one
carrier with the referenced filename stem under `.caprmadio`, and reject an
ID-only, ambiguous, missing, or stem-mismatched reference. Directory location
is not part of the Artifact reference, so moving a carrier among its active,
`drafts`, `done`, and `archive` locations preserves incoming relations.
