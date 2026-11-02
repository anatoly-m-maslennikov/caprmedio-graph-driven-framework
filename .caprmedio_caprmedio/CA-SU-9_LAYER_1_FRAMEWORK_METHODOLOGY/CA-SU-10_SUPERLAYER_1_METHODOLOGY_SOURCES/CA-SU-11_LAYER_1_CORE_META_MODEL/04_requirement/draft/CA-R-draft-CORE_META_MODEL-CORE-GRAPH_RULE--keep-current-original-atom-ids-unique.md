---
content_role: Requirement
type: Graph Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: Entity/Node/Continuant/Atom.ID
  depends_on:
  - Entity/Node/Continuant/Atom.Version Number
  - Entity/Node/Continuant/Atom.Status
relations: {}
version: 1
updated_at: "2026-10-22T01:39:08+04:00"
---
# Summary

Require unique canonical IDs among Current original Atoms

```yaml
graph_rule_type: value_constraint
applies_to:
  node: "Entity/Node/Continuant/Selection//Current Original Atoms"
  property: "Entity/Node/Continuant/Atom.ID"
condition:
  unique: true
```

## Details

The `value_constraint` mapping is proposed only. [CA-D-637@5](../../07_delivery/CA-D-637-CORE_META_MODEL-CORE--carry-a-formal-graph-rule-as-yaml-with-a-readable-summary.md) names the type but does not yet admit its schema or a Selection resolver.

The named Selection means all Current original logical Atoms in the selected source of truth. Exclude Drafts, archived originals and projection copies. Include Current statuses such as Done and Canceled, not only Active. Classify archival membership from the authoritative lifecycle/placement rules, not preserved historical Status bytes alone. Count logical Atoms, not file/folder representations or repeated source references. An unknown or incomplete population is unresolved, not a passing empty set.

The uniqueness key is canonical Atom.ID alone, never ID plus Version. Archived versions can reuse a canonical ID at different Versions without joining this population.

Sources: [CA-D-446@17](../../07_delivery/CA-D-446-CORE_META_MODEL-CORE--give-every-non-draft-atom-revision-one-identifier.md), [CA-D-378@16](../../07_delivery/CA-D-378-CORE_META_MODEL--serialize-assigned-atom-identities.md) and [CA-D-570@12](../../07_delivery/CA-D-570-CORE_META_MODEL-DELIVERY--serialize-draft-revision-lineage.md). [Project Configuration CA-D-305@16](../../../003_PROJECT_CONFIGURATION/07_delivery/CA-D-305-PROJECT_CONFIGURATION-CORE--carry-projected-atoms-without-new-identity.md) is a concrete example of projected members retaining source identity, not an extra universal Core authority.
