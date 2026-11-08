---
identity:
  id: CA-I-5
  ref_id: CA-I-5@1-draft
context:
  container:
    scope_unit: CA-SU-45
  role: Implementation
  form: Code Synopsis
  tier: 8
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom.Header
state:
  status: Draft
  version: 1
  updated_at: 2026-11-09 00:07:21 +0400
destination:
  file:
    name: CA-I-5@1-draft-WORKBENCH_BACKEND-CODE_SYNOPSIS--workbench-has-observed-header-schemas-with-underscore-names.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/08_implementation/draft/engine-refinement-20261108
author: Anatoly Maslennikov
---

## Summary

Workbench has observed Header schemas with underscore names

## Claim

### Prose Claim

At the pinned code state, Workbench derives public Header columns from observed source Headers. It joins Header path segments with underscores, while declared Content columns use dots. There is no cold-start choice that limits Header columns to model-declared Properties. The reader already compiles declared Content and reuses source contributions for incremental updates.

The running 0.4.4.39 query_schema response confirms the underscore Header names. This does not satisfy the newly adopted dotted-path and two-mode specifications. Those specifications remain the intended behavior; the implementation is being corrected.

## Details

Code snapshot: `b8da4472e53a99370a27fae54f8cde8e08e2ad3d`. These hashes describe that snapshot, not subsequent edits or a test result.

| Code location | SHA-256 |
| --- | --- |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/header_columns.py` | `7c0b8d3989c447a7c0679c0270365c76a0606916d4b83c25e049dd484a729dcf` |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/content_schema.py` | `ef22f33af29b86ca364ca029879b7b92eb3f23a335cf101f3c02f1dafa53d788` |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/query_store.py` | `1425de3f7bc3a500a3da81c9262da585607a3fbef4f4d6489c30d1394505046a` |
| `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/runtime_settings.py` | `475bee7b2fe4cd1f28864feedf03f8fd74214849131ed80f3675c8c2355a8f3d` |
