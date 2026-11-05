---
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Requirement)/(.Header.Form: Project Goal)'
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Project.Settings.Name
  - CAPRMEDIO_MODEL <+ Project
version: 35
updated_at: 2026-11-02 19:46:47 +0400
atom_id: CA-D-292
ref_id: CA-D-292
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-D-292-CORE_META_MODEL-DECISION--serialize-external-project-goal-filenames.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
---
## Summary

Serialize External Project Goal Filenames

## Claim

### Prose Claim


external Project Goal filenames.


**every** external Project Goal filename **must** begin with the unqualified canonical Atom ID prefix `<CANONICAL_ATOM_ID>-` for a Current Project Goal or the once-qualified canonical Atom ID prefix `<CANONICAL_ATOM_ID>@<VERSION>-` for an Archived Project Goal, followed by `<OPERATOR_NAMES>-DEFINES_GOAL_FOR-<PROJECT_SCOPE>--<SUMMARY_SLUG>.<EXT>`.

The `<OPERATOR_NAMES>` filename token **must** identify the registered Operator; `<PROJECT_SCOPE>` **must** preserve the exact registered Project Settings Name. The canonical current ID or once-qualified archived ID is the identity prefix; no additional Project Prefix, Content Role letter or unrelated number may be inserted into the preserved segment.

### Current source pin

Proposed N+1 successor of `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-292-CORE_META_MODEL-ENG_DECISION--serialize-external-project-goal-filenames.md`, CA-D-292@32, SHA-256 `244cc4f2eca9145cf1e314263f31c9e1cc3d4031a0059f1204d5de1f098c00ed`. Current bytes remain unchanged; this Draft performs no promotion or filename migration.
