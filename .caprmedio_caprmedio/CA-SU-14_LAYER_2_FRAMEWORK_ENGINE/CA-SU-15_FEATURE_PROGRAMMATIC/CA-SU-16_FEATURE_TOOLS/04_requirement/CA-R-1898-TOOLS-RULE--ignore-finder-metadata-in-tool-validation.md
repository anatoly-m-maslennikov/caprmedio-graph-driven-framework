---
atom_id: CA-R-1898
ref_id: CA-R-1898
container:
  scope_unit: CA-SU-16
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Validation
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
tier: 3
status: Active
version: 13
updated_at: 2026-10-27 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-1898-TOOLS-RULE--ignore-finder-metadata-in-tool-validation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/04_requirement
current_scope_unit: TOOLS
author: Anatoly Maslennikov
---
# Summary

Ignore Finder metadata in Tool validation

## Scope

Tool selection, persistent inventories, digests, package and Projection checks, and runtime control-directory checks at any depth.

## Claim

Tool validation **must** ignore files named `.DS_Store` so their presence, absence **or** contents do **not** change validation results.

## Details

Finder metadata is not an admitted source, package member, generated output, Skill resource, Journal event or runtime message. Exclude it before reading file contents or comparing persistent inventories; neither deleting it nor preventing Finder from creating it is a prerequisite.

This exclusion is for the exact basename `.DS_Store`. All other files retain their existing admission, ownership, missing-file, digest, mode and safety checks. Historical evidence remains unchanged; an earlier metadata-related failure retains its actual recorded outcome.
