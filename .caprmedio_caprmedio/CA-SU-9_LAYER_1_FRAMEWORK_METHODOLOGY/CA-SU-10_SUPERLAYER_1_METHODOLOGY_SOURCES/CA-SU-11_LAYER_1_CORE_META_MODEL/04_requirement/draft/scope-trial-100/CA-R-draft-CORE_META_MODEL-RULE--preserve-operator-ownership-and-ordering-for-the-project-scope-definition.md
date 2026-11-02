---
atom_id: CA-R-draft
content_role: Requirement
type: Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
tier: 1
version: 1
updated_at: 2026-10-29 20:32:25 +0400
author: Anatoly Maslennikov
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Scope Definition'
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - Entity/Object/Continuant/Actor/Operator
relations: {}
---
## Summary

Preserve Operator ownership and ordering for the Project Scope Definition

## Claim scope

Scope Definition Requirements targeting the Project.

## Claim

For the proposed Scope Definition targeting the Project, the Operator Actor is the actual owner, and the Operator is not a Scope Unit. Storage at Project level alone does not establish this identity. For governing order, use the Target Project as the derived ordering context while retaining the Operator Actor as actual owner. This is a proposed migration of the current Project Goal exception, not an already admitted exception for the proposed Type.

## Details

The predecessor defined a distinct Project Goal Type with one desired result, and distinguished ordinary Scope Unit ownership. Current CA-R-2132 specifies Project Goal Tier admission, and CA-R-2149 specifies its ordering context. Review and migrate these rules, CA-R-655 and all other Goal identity, ownership, Tier and ordering consumers together; existing Project Goal rules do not automatically admit Scope Definition. Preserve specific outcome constraints separately as appropriate. The paired general Type proposal is replacement-ca-r-925.
