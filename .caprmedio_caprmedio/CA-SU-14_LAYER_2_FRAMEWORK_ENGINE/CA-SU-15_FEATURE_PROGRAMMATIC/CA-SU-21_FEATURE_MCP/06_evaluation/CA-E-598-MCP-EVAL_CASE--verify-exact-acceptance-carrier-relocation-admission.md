---
atom_id: CA-E-598
ref_id: CA-E-598
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Storage
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling
    <+ Data Validation
  - MODEL//CAPRMEDIO <+ Projection
  - MODEL//CAPRMEDIO <+ Actor/Operator
  - MODEL//CAPRMEDIO <+ Execution
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling
    <+ Serialization
  - MODEL//CAPRMEDIO <+ Carrier/File
tier: 3
status: Active
version: 14
updated_at: 2026-11-10 20:47:54 +0400
carrier_destination:
  file:
    name: CA-E-598-MCP-EVAL_CASE--verify-exact-acceptance-carrier-relocation-admission.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/06_evaluation
current_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

Verify exact acceptance-carrier relocation admission

## Claim

### Prose Claim

the exact acceptance-carrier relocation admission **must** pass its declared unchanged-bytes and no-broadened-authority checks.

## Details

### Relocation admission checks

- Exactly one candidate replaces exactly the three registered prior source paths with their registered current paths; carrier bytes, identities, versions, and digests remain unchanged.
- Malformed, duplicate, missing, unknown, unsafe, stale, or mismatched registration fields, input hashes, or path occurrences refuse before effects.
- Routes, graph edges, registry identity, source digests, and fixed-path refresh behavior remain unchanged. Only the three registered path occurrences, canonical serialization, and derived canonical_manifest_sha256 may differ; route-identical selected_binding_digest remains unchanged. Aliases, raw-manifest edits, and general relocation requests refuse.
- Publication uses trusted Operator context, lock, pending intent, exact readback, and a real Work Journal receipt. An interrupted pre-effect attempt may retry the same candidate once only when exact original input, sealed intent, and current sources match; once it exists recovery is recording-only without rewrite. Ambiguous bytes refuse.
