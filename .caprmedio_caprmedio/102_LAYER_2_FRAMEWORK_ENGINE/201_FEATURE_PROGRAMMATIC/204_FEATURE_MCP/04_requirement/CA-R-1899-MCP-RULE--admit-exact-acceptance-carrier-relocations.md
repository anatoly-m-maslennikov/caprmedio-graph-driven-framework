---
atom_id: CA-R-1899
content_role: Requirement
current_scope_unit: MCP
status: Active
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-27 20:00:05 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Validation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Serialization
  - Subject/CAPRMEDIO/Carrier/File
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
