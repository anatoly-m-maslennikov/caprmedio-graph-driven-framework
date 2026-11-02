---
version: 25
updated_at: 2026-10-26 17:47:19 +0400
relations:
  child_of:
  - CA-R-1489
  depends_on:
  - CA-M-279
subjects:
  governs: Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run.Implementation Retry Limit
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan/Type: Plan'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan/Type: Plan.implementation_retry_limit'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - Subject/Graph Node/Domain/Continuant/Governing Configuration
  - Subject/Graph Node/Engineering/Continuant/Carrier/File Carrier
atom_id: CA-M-295@25
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 5
type: Implementation Method
---
# Summary

Resolve implementation retry limits by source precedence

## Scope

an effective Implementation Retry Limit resolved from direct Operator input, a Plan, the nearest Hub, Framework Instance Settings, **or** Default Settings.

## Claim

**to** resolve an effective Implementation Retry Limit, select the first applicable explicit source **in** this precedence:

1. direct Operator input for the current execution context.
2. the current Plan's explicit Implementation Retry Limit.
3. the nearest Hub with an explicit limit, walking `IS_CONTAINED_BY` from nearest **to** farthest **and** reading its own current Plan File Carrier under CA-D-447-CORE_META_MODEL-DELIVERY--serialize-the-implementation-retry-limit-setting.
4. Framework Instance Settings, resolving an omitted instance parameter through Default Settings under CA-M-279-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-missing-framework-parameters-from-default-settings.

### resolution constraints

- an omitted optional retry override preserves inheritance; another explicit field does **not** stop this lookup. a missing mandatory Plan file is invalid, **not** an inherited-setting selection.
- determine presence, **not** truthiness: **`=0`** is an explicit limit.
- an invalid **or** ambiguous reached source requires Operator disposition **without** silent fallback; an absent effective value stops the affected retry decision.
- direct Operator input applies **only** within its stated context.
- do **not** copy inherited values **or** create separate Objective/settings files. retain explicit overrides even **when** equal **to** the inherited value.
- use the same Plan identity for a Hub's file **and** folder.
- resolution does **not** reset the consumed retry count governed by CA-O-024-CORE_META_MODEL-ACTION--control-implementation-retries.

## Details
