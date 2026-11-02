---
atom_id: CA-R-1899@12
content_role: Requirement
current_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Storage
  depends_on:
  - Subject/Graph Node/Engineering/Data Handling/Data Validation
  - Subject/Graph Node/Domain/Continuant/Projection
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Occurrent/Execution
  - Subject/Graph Node/Engineering/Data Handling/Serialization
  - Subject/Graph Node/Carrier/File
relations: {}
tier: 3
type: Rule
---
# Summary

Admit exact acceptance-carrier relocations

## Scope

the one registered relocation of three acceptance carriers under the current Epic.

## Claim

the selected binding Projection **must** admit only the three exact registered acceptance-carrier path relocations in CA-D-592-MCP-ENG_DECISION--register-exact-acceptance-carrier-relocations while preserving their bytes, identities, versions, pins, route structure, graph and registry.

## Details

- the registration is authority for exactly CA-P-1618@1, CA-P-1535@2 and CA-P-1622@4; every prior and current path, digest and canonical input digest is exact.
- preserve the existing fixed-path selected-source refresh. this admission creates no alias, raw-manifest edit, general relocation capability or changed source pin.
- derive the candidate, seal it under the existing typed Operator publisher, retain its lock and pending intent, revalidate currentness before publication, then require strict readback and a real Work Journal receipt.
- unknown, duplicate, stale, mismatched or extra relocation evidence refuses before effects. a pending publication or recording remains recoverable through the existing lifecycle.
