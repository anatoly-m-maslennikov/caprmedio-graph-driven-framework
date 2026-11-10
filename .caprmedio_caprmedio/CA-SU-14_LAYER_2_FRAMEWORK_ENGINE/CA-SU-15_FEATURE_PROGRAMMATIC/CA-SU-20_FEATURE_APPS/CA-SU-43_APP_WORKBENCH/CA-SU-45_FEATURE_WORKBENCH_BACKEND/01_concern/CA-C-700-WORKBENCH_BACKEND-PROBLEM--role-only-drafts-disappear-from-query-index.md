---
atom_id: CA-C-700
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Resolved
version: 2
author: Anatoly Maslennikov
role: Concern
form: Problem
tier: 3
priority: medium
relations:
  concern_about:
  - CA-M-465
  - CA-R-2725
carrier_destination:
  file:
    name: CA-C-700-WORKBENCH_BACKEND-PROBLEM--role-only-drafts-disappear-from-query-index.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/01_concern
updated_at: 2026-11-10 20:47:54 +0400
ref_id: CA-C-700
container:
  scope_unit: CA-SU-45
topics:
  main_subject: MODEL//CAPRMEDIO <+ Projection
---

## Summary

Role-only Drafts disappear from the query index.

## Concern

The six lifecycle Drafts that carried the role-only technical reference
`CA-O-draft` shared one reference and were excluded from the derived source
inventory. A source-reader identity based only on the Atom ID could not retain
all of those carriers.

## Resolution

The SourceReader now preserves the `CA-O-draft` Atom ID and derives its
technical `ref` from the project-relative carrier path. The six real lifecycle
Drafts are verified, and one full-repository verification capture contained 4,908 Atoms,
47 Scopes, 30 role-only operation Drafts, and 30 unique references.
`tests/test_source_reader.py` passes 20 tests. This resolves the source defect;
runtime adoption and deployment remain separate tracking concerns.
