---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Status:Archived
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom.Status
  - CAPRMEDIO <+ MODEL <+ Atom.Status:Archived
  - CAPRMEDIO <+ MODEL <+ Carrier.Canonical Address
version: 20
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-D-565
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-565-CORE_META_MODEL-DECISION--bind-new-archived-revision-markdown-carrier.md
  source_atom_id: CA-D-565
  source_atom_revision: 20
  source_sha256: 6dad83a70b49b2d9a9a9f80bea7de8b8927ac06d5e8ec9b748f55a569ca6c5db
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Bind new archived Revision Markdown Carrier

## Claim scope

The single Markdown Archive Carrier created for an Atom Revision newly placed in Archived status.

## Claim

**when** an Atom Revision newly attains its model-admitted `Archived` Status **and** no more-specific applicable Delivery mapping exists for its Artifact Type, its **`=1`** Markdown Archive Carrier **must** be classified as that Revision's Archive Carrier **and** be placed at `archive/<canonical-ID>@<version>[-<remaining-filename-components>].md`: the owning Content Role's existing `archive/` directory is retained, and the single `@<version>` marker occupies the Atom-ID segment under CA-D-283/CA-D-289. Preserve the archived Atom's numeric Version and prior Updated At; its new Archive Carrier carries `status: Archived`.

## Details

This is a binding of the existing generic Status-placement and Archive-basename rules, not a universal placement override. A more-specific admitted Delivery mapping takes precedence. It does not relocate existing historical carriers or require automatic normalization of legacy filenames.
