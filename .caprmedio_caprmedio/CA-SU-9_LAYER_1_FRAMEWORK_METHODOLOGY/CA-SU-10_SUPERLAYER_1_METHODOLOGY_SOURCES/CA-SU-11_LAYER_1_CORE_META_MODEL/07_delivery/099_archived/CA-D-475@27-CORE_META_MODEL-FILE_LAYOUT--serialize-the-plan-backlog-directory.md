---
atom_id: CA-D-475
ref_id: CA-D-475@27
container:
  scope_unit: CA-SU-11
role: Delivery
form: file_layout
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.State.Status >| Status Group := Backlog'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.Context.Label'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.State.Status'
  - CAPRMEDIO_MODEL <+ Carrier/Directory
tier: 3
status: Archived
version: 27
updated_at: '2026-11-11T19:06:04+04:00'
carrier_destination:
  file:
    name: CA-D-475@27-CORE_META_MODEL-FILE_LAYOUT--serialize-the-plan-backlog-directory.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Serialize the Plan Backlog directory

## Claim

### Prose Claim

The Plan Backlog directory is `<owning scope unit>/<Plan Role folder>/001_backlog/`. It is a shared placement folder.

- Place a Backlog Plan directly in that folder when its direct Container is a Scope Unit or a Plan outside the Backlog group.
- When the direct Container is a Backlog Plan, place the file in that Plan's matching directory. Apply the same rule recursively.
- A Backlog Plan with contained Plans retains its matching directory and applicable descendant layout. Version labels use the ordinary Plan filename rule.
- Preserve the logical Container when placement uses the shared folder. Resolve containment from the Atom's Container.

The Formal Claim supplies the shared base directory. The direct Backlog Container rule supplies the more specific containing directory.

### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role := Plan)/(.Header.State.Status := Backlog).Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/<role folder>/001_backlog");
```
