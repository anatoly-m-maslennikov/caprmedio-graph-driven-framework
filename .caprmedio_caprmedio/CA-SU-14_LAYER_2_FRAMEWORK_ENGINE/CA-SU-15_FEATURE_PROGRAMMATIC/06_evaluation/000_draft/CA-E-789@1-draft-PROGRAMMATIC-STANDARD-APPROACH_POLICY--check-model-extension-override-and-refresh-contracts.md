---
atom_id: CA-E-789
ref_id: CA-E-789@1-draft
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Approach Policy
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data
    Handling <+ State Synchronization
  dependencies:
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+
    Schema
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+
    Source Retrieval
status: Draft
version: 1
updated_at: 2026-10-20 02:51:38 +0400
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
destination:
  file:
    name: CA-E-789@1-draft-PROGRAMMATIC-STANDARD-APPROACH_POLICY--check-model-extension-override-and-refresh-contracts.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/000_draft
---
## Summary

Check model extension, override and refresh contracts

## Claim scope

Evaluation design for the declared model mechanism and selected override/refresh policy; no evaluation is executed by this Draft.

## Claim

### Prose Claim

Demonstrate an admitted Type addition, an explicitly permitted Relation Type/Graph Rule override and a Project-specific effective value, each traceable to exact provider/configuration evidence. Demonstrate that a protected base rewrite, inactive Extension, missing source/reference, schema-valid but unrelated or wrong-Project configuration, incompatible schema, undeclared precedence and out-of-permission override cannot produce a selected partial model. Current Core permission and any future authorized delta shall be distinguishable in the evidence.

## Details

Use at least two Projects with different effective definitions, including the same local declaration name where permitted, and verify that model/provenance reuse never substitutes the wrong Project identity or source frontier. Verify that each delivered generation resolves to the exact input bytes it validated; change an input between observation and selection and confirm that no torn generation is selected. Check valid refresh, invalid refresh, cold load without a usable generation and an operation overlapping a generation switch. The expected result shall follow the chosen continue-with-prior or pause policy and retain an attributable diagnostic. Verify supported file changes against the claimed code-edit/image-rebuild boundary; parser support for JSON is evaluated only if JSON is selected. Preserve the full-entity versus named Relation Type/concrete Graph Rule declaration-view boundary and do not treat graph projection output or rule evaluation results as definition authority. Record failures and untested cases; a passing schema check alone is not semantic or release evidence.
