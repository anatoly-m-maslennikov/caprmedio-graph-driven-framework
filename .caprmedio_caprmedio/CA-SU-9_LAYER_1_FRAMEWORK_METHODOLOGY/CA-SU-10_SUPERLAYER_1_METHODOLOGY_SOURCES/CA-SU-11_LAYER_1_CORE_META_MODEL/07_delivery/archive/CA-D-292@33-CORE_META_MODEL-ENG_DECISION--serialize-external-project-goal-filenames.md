---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Requirement)/(.Type: Project Goal)'
  depends_on:
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings.Name
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
version: 33
updated_at: 2026-10-30 17:22:58 +0400
relations: {}
atom_id: CA-D-292@33
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Decision
---
## Summary

Serialize External Project Goal Filenames

## Claim scope

external Project Goal filenames.

## Claim

**every** external Project Goal filename **must** begin with the unqualified canonical Atom ID prefix `<CANONICAL_ATOM_ID>-` for a Current Project Goal or the once-qualified canonical Atom ID prefix `<CANONICAL_ATOM_ID>@<VERSION>-` for an Archived Project Goal, followed by `<OPERATOR_NAMES>-DEFINES_GOAL_FOR-<PROJECT_SCOPE>--<SUMMARY_SLUG>.<EXT>`.

The `<OPERATOR_NAMES>` filename token **must** identify the registered Operator; `<PROJECT_SCOPE>` **must** preserve the exact registered Project Settings Name. The canonical current ID or once-qualified archived ID is the identity prefix; no additional Project Prefix, Content Role letter or unrelated number may be inserted into the preserved segment.

### Current source pin

Proposed N+1 successor of `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/CA-D-292-CORE_META_MODEL-ENG_DECISION--serialize-external-project-goal-filenames.md`, CA-D-292@32, SHA-256 `244cc4f2eca9145cf1e314263f31c9e1cc3d4031a0059f1204d5de1f098c00ed`. Current bytes remain unchanged; this Draft performs no promotion or filename migration.
