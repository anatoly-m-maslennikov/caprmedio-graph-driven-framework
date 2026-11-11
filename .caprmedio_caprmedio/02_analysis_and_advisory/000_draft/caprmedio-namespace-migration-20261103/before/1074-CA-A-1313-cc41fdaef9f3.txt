---
atom_id: CA-A-1313
status: Done
tier: 3
version: 9
updated_at: 2026-11-02 19:17:40 +0400
subjects:
  active: Scope Unit
relations: {}
form: Spec Proposal
role: Analysis & Advisory
---
## Summary

Keep Goals outside and define Scope Contracts inside each Scope Unit

## Proposal

Each Scope Unit has exactly one external Scope Unit Declaration and one or more separate external Goals. Its internal Tier-0 Atoms are Scope Contracts. A Scope Unit may have no local Scope Contracts; do not require every RMEDO Role.

The Declaration has Role Requirement and Form Scope Unit Declaration. Its active Subject identifies the specific Scope Unit. Its Claim declares ID where applicable, Name, optional Label, order.ordered, conditional order.number and direct containment. Scope Constraints are external and may be part of the Declaration. Do not copy Goal Claims into it or create another Definition Atom for each individual Scope Unit.

A Declaration may contain several statements forming one coherent declaration. Its Summary may name that topic. Other Forms keep their existing Claim and Summary rules.

“Outside” means outside the declared Scope Unit’s ownership. Non-root Declarations and Goals belong to its parent. The Project Declaration and Project Goal are externally Operator-owned. The Operator is an Actor, not a Scope Unit. The Project Goal keeps Tier −1.

Scope Unit Declarations replace project_structure.toml entirely. They are the sole structural source. Remove the old file, its governing rules, TOML readers and row writers. Keep the existing Scope Unit workflow definitions; remove their four TOML-specific executable bindings and implementation. Do not build replacement Scope Unit tools in this adoption.

## Ordering and identity

order groups the sibling Properties ordered and number. ordered has exactly one Boolean value. number has exactly one positive integer value when ordered is true, and no value otherwise. Scope Units have no Navigation Number. Step and Plan numbering remains separate.

Non-root Scope Unit IDs are stable CA-SU-<number> values through rename and move. The Project root is Unordered, has no Scope Unit ID or order.number, and is not moved or renamed through Scope Unit operations.

## Folders

The Project Authority Folder remains .caprmedio_<project name>; Delivery is the repository root. For non-root units:

| Unit | Authority Folder | Delivery Folder |
| --- | --- | --- |
| Ordered | <id>_<label>_<order>_<name> | <label>_<order>_<name> |
| Unordered | <id>_<label>_<name> | <label>_<name> |

Place each under its respective parent. Omit absent optional segments and their separators. Derive these names; do not independently author folder paths in each Declaration. Move existing Authority and Delivery folders to these names during adoption.

Applicable Methodology is a special Projection, not a separately declared Scope Unit. Preserve its Projection content.

## Writing

Keep the Operator’s wording as close as possible. Use simple grammar and coherent statements. Preserve terms and key concepts such as DRY and MECE; do not replace them with synonyms.
