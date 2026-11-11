---
atom_id: CA-D-565
ref_id: CA-D-565@24
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.State.Status:Archived
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.State.Status
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
status: archived
version: 24
updated_at: '2026-11-11 15:27:11 +0400'
carrier_destination:
  file:
    name: CA-D-565@24-CORE_META_MODEL-DECISION--bind-new-archived-revision-markdown-carrier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Bind new archived Revision Markdown Carrier

## Claim

### Prose Claim


The single Markdown Archive Carrier created for an Atom Revision newly placed in Archived status.


**when** an Atom Revision newly attains its model-admitted `Archived` Status, its **`=1`** Markdown Archive Carrier **must** be classified as that Revision's Archive Carrier **and** be placed directly in the owning Scope Unit's shared Content Role `archived` directory, regardless of its logical container, as `archived/<canonical-ID>@<version>[-<remaining-filename-components>].md`. The single `@<version>` marker occupies the Atom-ID segment under CA-D-283/CA-D-289. Preserve the archived Atom's numeric Version and prior Updated At; its new Archive Carrier carries logical Archived Status encoded as `archived` through the common named-value rule.

## Details

This rule applies to newly archived Revisions. It does not relocate existing historical carriers or authorize independent legacy moves, rewrites, or automatic normalization of legacy filenames.
