---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Content.Summary
  - CAPRMEDIO_MODEL <+ Atom.Header.Topics.Main Subject
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_BLOCKED_BY
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_CONTAINED_BY
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Carrier/File
version: 34
updated_at: 2026-11-04 16:52:59 +0400
relations:
  depends_on:
  - CA-R-1588
atom_id: CA-M-306
ref_id: CA-M-306
status: Active
tier: 2
role: Method
form: Implementation Method
carrier_destination:
  file:
    name: CA-M-306-IMPLEMENTATION_METHOD--author-plan-atoms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
container:
  scope_unit: CA-SU-11
---
## Summary

Author Plan Atoms

## Claim

### Prose Claim

To author a Plan Atom, apply the common Plan rules independently of Label:

1. State the intended work or outcome and provide own work, direct Plan decomposition, or both under CA-R-1575. Apply the executable leaf-work bound under CA-R-1589.
2. Resolve the active Subject and its target Scope under CA-R-1588. Apply the applicable completion and verification rules, including CA-R-1599, and use Labels only under their governing rules. For a containing Plan whose Status is Done or Canceled, require every directly contained Plan to be Done or Canceled; mixed terminal statuses are allowed, and containment does not force a child Status to match the parent.
3. Express required start dependencies as direct `IS_BLOCKED_BY` Relations on the dependent Plan and derive `BLOCKS`. For Plan containment, declare `IS_CONTAINED_BY` on the child and derive `CONTAINS`. Do not infer dependencies from numbers or folder placement.
4. Resolve confidence from its applicable sources and store only an explicitly selected confidence override under its admitted encoding.
5. Review the finalized intended contribution against its supporting content and completion criteria, then derive Summary under CA-R-1418 and CA-R-2499. Preserve Summary across Revisions; a changed Summary requires the applicable replacement identity under CA-R-1464.
