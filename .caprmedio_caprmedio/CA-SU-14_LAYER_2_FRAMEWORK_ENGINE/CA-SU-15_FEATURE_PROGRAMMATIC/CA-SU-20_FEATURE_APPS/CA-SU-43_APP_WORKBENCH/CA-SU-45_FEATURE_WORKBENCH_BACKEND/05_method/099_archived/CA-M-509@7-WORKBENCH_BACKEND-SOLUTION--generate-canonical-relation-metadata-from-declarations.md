---
identity:
  ref_id: CA-M-509@7
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
  status: archived
  version: 7
  updated_at: '2026-11-12T13:30:43.732876+00:00'
destination:
  file:
    name: CA-M-509@7-WORKBENCH_BACKEND-SOLUTION--generate-canonical-relation-metadata-from-declarations.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method/099_archived
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

In refresh mode, generate deterministic JSON metadata before image fingerprint and context assembly. In existing mode, use the checkout registry unchanged. Its fingerprint excludes a changing timestamp. A missing or invalid asset or a failed refresh prevents image or package acceptance. Load the delivered registry at startup. Source changes refresh relation facts under that registry. Apply relation declaration changes by refreshing the registry and rebuilding the image. MCP tool discovery remains separate.


Generate declaration-derived model facts only from CFEL-labelled code blocks in `Content.Claim.Formal Claim`. Ignore `#` comments outside quoted strings, including section markers such as `# model`; comments are not declarations or parsing gates. Prose Claim, Semantics, Details, examples and Header Topics do not supply model facts. Source identity, lifecycle and provenance metadata may select and bind inputs. Register Relation names, inverse bindings and aliases from their formal declarations, not from Header Topics.
