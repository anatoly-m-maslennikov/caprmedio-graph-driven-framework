---
atom_id: CA-E-598
ref_id: CA-E-598
role: Evaluation
form: Eval Case
current_scope_unit: MCP
status: Active
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-27 19:59:38 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Validation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Serialization
  - Subject/CAPRMEDIO/Carrier/File
tier: 3
container:
  scope_unit: CA-SU-21
carrier_destination:
  file:
    name: CA-E-598-MCP-EVAL_CASE--verify-exact-acceptance-carrier-relocation-admission.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
---
# Summary

Verify exact acceptance-carrier relocation admission

## Scope

the one registered relocation of three acceptance carriers under the current Epic.

## Claim

the exact acceptance-carrier relocation admission **must** pass its declared unchanged-bytes and no-broadened-authority checks.

## Details

- exactly one candidate replaces exactly the three registered prior source paths with their registered current paths; the listed carrier bytes, identities, versions and digests remain unchanged.
- malformed, duplicate, missing, unknown, unsafe, stale or mismatched registration fields, input hashes or path occurrences refuse before effects.
- every route, graph edge, registry identity, source digest and fixed-path refresh behavior remains unchanged. only the three registered source-path occurrences, resulting canonical serialization and derived `canonical_manifest_sha256` may differ; the route-identical `selected_binding_digest` remains unchanged. aliases, raw-manifest edits and general relocation requests refuse.
- publication requires the existing trusted Operator context, lock, pending intent and exact readback; its Work Journal receipt is real. an interrupted pre-effect attempt may retry the same candidate once only when the exact registered original input, sealed intent and current sources still match. after an exact candidate exists, recovery is recording-only without rewrite; ambiguous bytes refuse.
