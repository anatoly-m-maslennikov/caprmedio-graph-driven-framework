---
atom_id: CA-E-598@7
content_role: Evaluation
type: Eval Case
current_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 7
updated_at: 2026-10-24 11:58:20 +0400
subjects:
  governs: Subject/Engineering/Carrier
  depends_on:
  - Subject/Engineering/MCP
  - Subject/Domain/Node/Continuant/Projection
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Occurrent/Execution
  - Subject/Engineering/Carrier/Journal Serialization
  - Subject/Engineering/Carrier/File Carrier
relations:
  relates_to:
  - CA-P-1117
  - CA-D-592
tier: 3
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
