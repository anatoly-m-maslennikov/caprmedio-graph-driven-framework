# Scope Unit Declaration source fields

This map records the old source and its proposed formal representation. The Current TOML is unchanged; these are Drafts, not a live source cutover.

| Source | Proposed formal representation |
| --- | --- |
| Project Settings name | `Project//caprmedio.Name`; Project classification comes from its model |
| No existing Scope Unit ID field | `Scope Unit//<name>.ID` for 43 non-root units; no ID for Project |
| scope_unit_name | `Scope Unit//<name>.Name` |
| scope_unit_label | `.Label`, preserving all 43 explicit labels |
| scope_unit_type | Boolean `.order.ordered`: Ordered → true, Unordered → false |
| local_order | `.order.number`; nine existing positive integers, exactly one for an Ordered unit; no value otherwise |
| parent | Direct `IS_CONTAINED_BY`; root parents resolve to `Project//caprmedio` |
| navigational_order_number | Omitted; Scope Units have no Navigation Number |
| authority_path / delivery_path | Historical evidence only. Folder paths are derived, not copied into Declarations |
| authority_mode | Retired by Operator decision; do not carry or formalize it |

The Project model supplies `Project//.order.ordered == false`, no `Project//.order.number`, and no `Project//.ID`. The individual root Declaration does not repeat these inherited constraints. A non-root Scope Unit has an ID that survives a move or rename; Project is not moved or renamed through Scope Unit operations.

Authority Folder names include `<id>_` only for non-root units. Delivery Folder names use the same suffix without that ID. `<order>_` appears only when ordered is true. The Project Authority Folder remains `.caprmedio_<project name>`.

Legacy owner data remains in the instance manifest for later correct external placement. Canonical Draft frontmatter contains no `current_scope_unit`, `claim_target_scope_unit` or Author. The root's external owner remains the Operator; no Operator Scope Unit is invented.

The original Goal and Tier-0 census remains [source acquisition evidence](goal-coverage.md). It is not silently regenerated into new Goals or a second structure authority.

Ordering property definitions: `Scope Unit.order.ordered: [bool]{:1}` and `Scope Unit.order.number: IF order.ordered = true THEN [int, 1+]{:1} ELSE []{:0}`. All nine existing Ordered units satisfy the positive-integer constraint.
