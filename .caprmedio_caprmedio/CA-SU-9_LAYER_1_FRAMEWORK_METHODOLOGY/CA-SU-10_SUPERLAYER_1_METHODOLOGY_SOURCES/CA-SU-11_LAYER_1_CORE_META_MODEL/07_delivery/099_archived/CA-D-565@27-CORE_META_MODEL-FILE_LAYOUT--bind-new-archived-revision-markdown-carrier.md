---
atom_id: CA-D-565
ref_id: CA-D-565@27
container:
  scope_unit: CA-SU-11
role: Delivery
form: file_layout
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom.Header.State.Status >| Status Group := Archived'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.State.Status
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
status: archived
version: 27
updated_at: '2026-11-11T19:06:04+04:00'
carrier_destination:
  file:
    name: CA-D-565@27-CORE_META_MODEL-FILE_LAYOUT--bind-new-archived-revision-markdown-carrier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Bind new archived Revision Markdown Carrier

## Claim

### Prose Claim


The single Markdown Archive Carrier created for an Atom Revision newly placed in Archived status.


Place Archived Atom Markdown Carriers in the shared `<owning scope unit>/<role folder>/099_archived/` directory. The Atom's owning Scope Unit and Role determine this directory.

When an Atom Revision attains Archived Status, classify its single Markdown Archive Carrier as that Revision's Archive Carrier. Its filename is `<canonical-ID>@<version>[-<remaining-filename-components>].md`. The single `@<version>` marker occupies the Atom-ID segment under CA-D-283/CA-D-289. Preserve the archived Atom's numeric Version and prior Updated At; its new Archive Carrier carries logical Archived Status encoded as `archived` through the common named-value rule.

### Formal Claim

```CFEL
# model
Atom/(.Header.State.Status := Archived).Header.Destination.File.Path == PATH_TEMPLATE("<owning scope unit>/<role folder>/099_archived");
```

## Details

This rule applies to newly archived Revisions. It does not relocate existing historical carriers or authorize independent legacy moves, rewrites, or automatic normalization of legacy filenames.
