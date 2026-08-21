---
subject_scopes:
  - artifact-model
version: 1
updated_at: 2026-08-21 20:51:16
relations:
  concern_about:
    - CAPRMEDIO-META-REQU-084--relational-artifacts-declare-endpoints
    - CAPRMEDIO-META-REQU-127--define-three-governance-loci
---
# Does Artifact semantic shape need an axis?

Does CAPRMEDIO need an independently governed Artifact axis such as
`semantic_shape = standalone | relational`, or can Artifact Type, governed
content, and typed frontmatter relations express every required distinction?

The axis should be admitted only if it changes non-derivable routing,
validation, applicability, or Runtime behavior. Graph connectivity alone is not
sufficient justification because every graph node may participate in typed
relations.
