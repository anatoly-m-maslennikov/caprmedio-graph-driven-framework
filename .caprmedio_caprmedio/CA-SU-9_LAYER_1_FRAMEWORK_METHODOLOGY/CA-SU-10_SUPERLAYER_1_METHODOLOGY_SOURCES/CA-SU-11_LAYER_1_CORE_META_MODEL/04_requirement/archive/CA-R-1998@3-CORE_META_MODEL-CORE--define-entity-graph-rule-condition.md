---
atom_id: CA-R-1998@3
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Rule.Condition
  depends_on:
  - Entity/Graph Rule.Type
  - Entity/Graph Rule.Applies To
  - Subject/Graph/Relation
relations: {}
version: 3
updated_at: 2026-10-23 03:06:32 +0400
---
# Summary

Define Entity/Graph Rule.Condition

## Scope

The operative condition of a Graph Rule in the Entity model.

## Claim

Graph Rule.Condition **means** the structured operative constraint on the applicable cases, expressed under the schema selected by the one Graph Rule Type.

## Details

For a whitelist, Condition has separate source and target lists of Subject paths, and both endpoints must match their corresponding list. A narrower kind inherits membership from a listed broader kind. These lists express permission, not a requirement that a Relation exist. For cardinality, minimum and maximum bound the count per node for the matching Relation Type, direction and endpoint filters, not a total for the whole graph. A minimum of 1 makes a matching connection mandatory; a minimum of 0 permits absence and does not ban a connection. Equal minimum and maximum express an exact count. For example, a Plan can have zero or one outgoing IS_CONTAINED_BY connection to another Plan, without counting its other target kinds. A separate mandatory Boolean is unnecessary. CA-D-637 defines Cardinality's explicit nonnegative integer minimum and maximum, with null maximum meaning unbounded, and opposite-endpoint kind filters. Count distinct matching Relations per applicable node, including zero-edge cases; repeated filter matches and derived inverse navigation do not multiply the count. A constraint does not create a Relation or assign a default. This definition does not establish complete expression languages or schemas for the remaining Types.
