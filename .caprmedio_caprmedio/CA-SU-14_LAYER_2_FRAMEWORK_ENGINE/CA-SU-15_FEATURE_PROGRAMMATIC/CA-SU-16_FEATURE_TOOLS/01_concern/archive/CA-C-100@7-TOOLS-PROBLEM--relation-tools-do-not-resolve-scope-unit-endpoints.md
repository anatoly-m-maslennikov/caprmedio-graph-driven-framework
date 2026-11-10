---
atom_id: CA-C-100
ref_id: CA-C-100@7
relations:
  concern_about:
  - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-529--patch-artifact-relations
  - CA-R-877-REQUIREMENT-BSEED_GOVERNANCE--validate-directional-relational-atoms
  - CA-R-883-REQUIREMENT-BSEED_GOVERNANCE--register-contract-endpoint-relations
status: Archived
version: 7
updated_at: 2026-10-23 03:17:34 +0400
subject_scopes:
- relation-tooling
priority: high
carrier_destination:
  file:
    name: CA-C-100@7-TOOLS-PROBLEM--relation-tools-do-not-resolve-scope-unit-endpoints.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/01_concern/archive
---
# Relation Tools do not resolve Scope Unit endpoints

The current executable relation registry and relation-processing code resolve active Markdown Artifact identities but do not resolve `.`, `./<FULL NAME>`, or `../<FULL NAME>` Scope Unit references as project-graph nodes relative to the source Atom's owner. They also do not parse or validate `relational_endpoints` descriptors and implement an earlier relation-metadata schema that lacks the registered relation family, ordering domain, target-position, and node-class fields required by the current Applicable Methodology.

Until the Tool realization is updated and evaluated, it cannot validate or patch the remaining Contract endpoint relations without producing false missing-target or incomplete-schema results.
