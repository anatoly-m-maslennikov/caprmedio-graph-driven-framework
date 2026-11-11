---
atom_id: CA-D-461
ref_id: CA-D-461
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.State.Status'
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.State.Status'
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)
tier: 1
status: Active
version: 33
updated_at: '2026-11-11T19:06:04+04:00'
carrier_destination:
  file:
    name: CA-D-461-CORE_META_MODEL-DECISION--place-plan-carriers-by-status.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Place Plan Carriers by Status

## Claim

### Prose Claim


Current Plan Carrier Bundle placement by carried Status.


Apply CA-D-466 for Current Plan placement.

Status folders are Carrier directories. Validate folder nesting against the child's direct `IS_CONTAINED_BY` declaration.

read Status from the Plan's own Markdown file under CA-D-483 **and** check its local placement; a parent **or** folder name **must not** supply a descendant's Status at read time. **every** admitted parent Status change requires the containment cascade under CA-R-1521: separate single-Atom Actions write the Status prescribed by CA-R-1521 to each selected latest descendant under its own model, without an optional descendant mode. For a containing Plan Atom whose requested Status is Done **or** Canceled, preserve every selected latest contained Plan already Done **or** Canceled and request Canceled for every other selected latest contained Plan. After the cascade, every selected latest contained Plan must be Done **or** Canceled; mixed terminal statuses are allowed, and no contained Plan is forced to match the parent's requested Status merely because the parent is Done **or** Canceled. For other admitted parent Statuses, preserve the applicable cascade. Archive selects the latest Atoms in the logical Container chain. Other references and older archived Revisions are excluded. Apply the Current layout to Current descendants. Apply CA-D-475 to Backlog descendants. Resolve descendants through logical Container, including Backlog Plans placed in the shared Backlog folder.

## Details

- Preserve exact older version bytes **without** rewriting their Version **or** Status. Retained-history subtrees and non-Atom assets may move byte-for-byte with an authorized matching Directory Carrier move; they are not independent Status targets. This does **not** authorize independent legacy-tree migration.
