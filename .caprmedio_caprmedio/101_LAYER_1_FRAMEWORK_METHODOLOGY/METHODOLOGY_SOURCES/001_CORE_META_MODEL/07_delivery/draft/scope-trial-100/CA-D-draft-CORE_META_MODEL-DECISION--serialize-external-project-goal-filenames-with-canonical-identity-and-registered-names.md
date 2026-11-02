---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Project Goal'
  depends_on:
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings.Project Name
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
version: 1
updated_at: 2026-10-29 20:32:25 +0400
relations: {}
atom_id: CA-D-draft
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
tier: 3
type: Decision
---
## Summary

Serialize external Project Goal filenames with canonical identity and registered names

## Claim scope

external Project Goal filenames.

## Claim

**every** external Project Goal filename **must** begin with the unqualified canonical Atom ID prefix `<CANONICAL_ATOM_ID>-` for a Current Project Goal or the once-qualified canonical Atom ID prefix `<CANONICAL_ATOM_ID>@<VERSION>-` for an Archived Project Goal, followed by `<OPERATOR_NAMES>-DEFINES_GOAL_FOR-<PROJECT_SCOPE>--<SUMMARY_SLUG>.<EXT>`.

The `<OPERATOR_NAMES>` filename token **must** identify the registered Operator; `<PROJECT_SCOPE>` **must** preserve the exact registered Project Name. The canonical current ID or once-qualified archived ID is the identity prefix; no additional Project prefix, Content Role letter or unrelated number may be inserted into the preserved segment.
