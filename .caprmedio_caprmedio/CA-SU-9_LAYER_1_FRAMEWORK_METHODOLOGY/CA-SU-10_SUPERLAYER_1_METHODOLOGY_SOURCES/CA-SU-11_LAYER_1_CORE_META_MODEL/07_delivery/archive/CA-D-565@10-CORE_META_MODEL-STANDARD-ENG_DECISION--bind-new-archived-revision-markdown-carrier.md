---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom.Status: Archived'
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Status
  - 'Subject/Domain/Node/Continuant/Atom.Status: Archived'
  - Subject/Engineering/Carrier.Canonical Address
version: 10
updated_at: 2026-10-24 09:42:52 +0400
relations:
  relates_to:
  - CA-D-289
  - CA-D-466
atom_id: CA-D-565@10
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
type: Eng Decision
author: Anatoly Maslennikov
tier: 3
---
# Summary

Bind new archived Revision Markdown Carrier

## Scope

The single Markdown Archive Carrier created for an Atom Revision newly placed in Archived status.

## Claim

**when** an Atom Revision newly attains its model-admitted `Archived` Status **and** no more-specific applicable Delivery mapping exists for its Artifact Type, its **`=1`** Markdown Archive Carrier **must** be classified as that Revision's Archive Carrier **and** be placed at `archive/<canonical-ID>@<version>[-<remaining-filename-components>].md`: the owning Content Role's existing `archive/` directory is retained, and the single `@<version>` marker occupies the Atom-ID segment under CA-D-283/CA-D-289. Preserve the archived Atom's numeric Version and prior Updated At; its new Archive Carrier carries `status: Archived`.

## Details

This is a binding of the existing generic Status-placement and Archive-basename rules, not a universal placement override. A more-specific admitted Delivery mapping takes precedence. It does not relocate existing historical carriers or require automatic normalization of legacy filenames.
