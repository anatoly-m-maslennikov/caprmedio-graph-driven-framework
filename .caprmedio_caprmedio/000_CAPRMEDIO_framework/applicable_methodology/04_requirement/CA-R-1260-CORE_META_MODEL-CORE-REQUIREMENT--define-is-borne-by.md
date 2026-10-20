---
subjects:
  governs: "IS_BORNE_BY"
  depends_on:
    ["Entity", "Dependent Entity", "Entity/Node/Continuant/Projection/Type: Entities Graph", "Entity/Relation"]
version: 16
updated_at: "2026-10-20 04:50:22 +0400"
relations: {}
atom_id: "CA-R-1260"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1260-CORE_META_MODEL-CORE-REQUIREMENT--define-is-borne-by.md
  source_atom_id: CA-R-1260
  source_atom_revision: 16
  source_sha256: 1e94a17a3038f0725da761ea7cd9a03d12997ff885e9c26d1b2038a04a968222
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
