---
subjects:
  governs: "IS_BORNE_BY"
  depends_on:
    ["Entity", "Dependent Entity", "Entity/Node/Continuant/Projection/Type: Entities Graph", "Entity/Relation"]
version: 16
updated_at: "2026-10-20 04:50:22 +0400"
relations: {}
atom_id: CA-R-1260@16
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Define IS_BORNE_BY

## Scope

an IS_BORNE_BY Relation from Entity A **to** Entity B **in** the Entities Graph.

## Claim

an IS_BORNE_BY Relation from Entity A **to** Entity B **in** the Entities Graph **means** that A is a Dependent Entity whose identity requires B as its immediate bearer.

## Semantics

Primary means that identity does not require another Entity occurrence as bearer. Dependent means that identity requires an immediate bearer, as expressed by IS_BORNE_BY. These describe bearer dependence, not additional taxonomy branches. An absent edge in an incomplete view does not establish independence.

## Details

### relation admission

- Status: the IS_BORNE_BY Relation Kind is Active.
