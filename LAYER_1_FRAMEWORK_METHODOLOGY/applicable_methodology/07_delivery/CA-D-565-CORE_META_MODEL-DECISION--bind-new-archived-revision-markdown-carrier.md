---
atom_id: CA-D-565
ref_id: CA-D-565
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Status:Archived
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.Status
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
status: active
version: 23
updated_at: 2026-11-09 00:57:07 +0400
carrier_destination:
  file:
    name: CA-D-565-CORE_META_MODEL-DECISION--bind-new-archived-revision-markdown-carrier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-565-CORE_META_MODEL-DECISION--bind-new-archived-revision-markdown-carrier.md
  source_atom_id: CA-D-565
  source_atom_revision: 23
  source_sha256: 145c9175f8667a224754cff0c87a092770a86a355682addc9dcb8155cede7269
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Bind new archived Revision Markdown Carrier

## Claim

### Prose Claim


The single Markdown Archive Carrier created for an Atom Revision newly placed in Archived status.


**when** an Atom Revision newly attains its model-admitted `Archived` Status **and** no more-specific applicable Delivery mapping exists for its Artifact Type, its **`=1`** Markdown Archive Carrier **must** be classified as that Revision's Archive Carrier **and** be placed at `archive/<canonical-ID>@<version>[-<remaining-filename-components>].md`: the owning Content Role's existing `archive/` directory is retained, and the single `@<version>` marker occupies the Atom-ID segment under CA-D-283/CA-D-289. Preserve the archived Atom's numeric Version and prior Updated At; its new Archive Carrier carries logical Archived Status encoded as `archived` through the common named-value rule.

## Details

This is a binding of the existing generic Status-placement and Archive-basename rules, not a universal placement override. A more-specific admitted Delivery mapping takes precedence. It does not relocate existing historical carriers or require automatic normalization of legacy filenames.
