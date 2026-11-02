---
atom_id: CA-R-1999
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Rule.Default Value
  depends_on:
  - Entity/Graph Rule
  - Entity/Graph Rule.Condition
relations: {}
version: 1
updated_at: "2026-10-19 21:56:38 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1999-CORE_META_MODEL-CORE--define-entity-graph-rule-default-value.md
  source_atom_id: CA-R-1999
  source_atom_revision: 1
  source_sha256: 2de44f6236fb5fa54391431ac86f561e71e33ba2e02bb4e40720f452b2cd544e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Entity/Graph Rule.Default Value

## Scope

The optional fallback value associated with a Graph Rule.

## Claim

Graph Rule.Default Value **means** an optional fallback used when the corresponding value is absent, without replacing an explicit value and subject to the applicable constraints.

## Details

The property is optional. Selecting a default does not automatically write or materialize that value. This definition supplies no concrete default, cross-rule precedence, merge behavior, or override policy.
