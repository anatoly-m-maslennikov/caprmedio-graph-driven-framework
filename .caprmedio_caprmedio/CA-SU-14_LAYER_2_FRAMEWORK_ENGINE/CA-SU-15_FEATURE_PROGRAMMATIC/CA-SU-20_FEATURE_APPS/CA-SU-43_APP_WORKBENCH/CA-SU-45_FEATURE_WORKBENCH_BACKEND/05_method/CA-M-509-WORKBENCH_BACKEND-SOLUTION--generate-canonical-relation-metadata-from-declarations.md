---
identity:
  ref_id: CA-M-509
  id: CA-M-509
context:
  container:
    scope_unit: CA-SU-45
  role: Method
  form: Solution
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Schema
    dependencies:
    - MODEL//CAPRMEDIO <+ CFEL <+ Relation
  tier: 3
state:
  status: Active
  version: 4
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-509-WORKBENCH_BACKEND-SOLUTION--generate-canonical-relation-metadata-from-declarations.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method
author: Anatoly Maslennikov
relations:
  method_for:
  - CA-R-2724
  IS_REPLACEMENT_FOR:
  - CA-D-705
---
## Summary

Generate canonical relation metadata from declarations

## Claim

### Prose Claim

Generate one rebuildable relation registry from Current Requirement relation Declarations for Workbench relation-name resolution and direct/derived materialization. Include canonical names, explicit inverse aliases, literal unqualified inverse bindings, and source IDs/versions. An inverse alias needs no separate Relation Declaration.

Normalize an explicit inverse by swapping endpoints once; preserve an unambiguous legacy named inverse through its declared counterpart without source edits or invented bindings. Derive container facts from effective Header.Container, including Context carrier layout, and resolve the Project root as `uppercase(Project prefix)-SU-00`. Build each inverse view once and refresh only affected rows/hashes on source change. Preserve exact model addresses: ambiguous/unsupported metadata is diagnosed and omitted, never guessed; prose, general CFEL and qualified derivation rules are not runtime facts.

Regenerate deterministic JSON metadata on every supported image rebuild, including local release, before image fingerprint/context assembly. Its fingerprint excludes a changing timestamp. A missing or failed asset prevents image/package acceptance rather than using handwritten/stale metadata. Relevant Current Declaration changes use the same compiler under existing owner synchronization; MCP tool discovery remains separate.
