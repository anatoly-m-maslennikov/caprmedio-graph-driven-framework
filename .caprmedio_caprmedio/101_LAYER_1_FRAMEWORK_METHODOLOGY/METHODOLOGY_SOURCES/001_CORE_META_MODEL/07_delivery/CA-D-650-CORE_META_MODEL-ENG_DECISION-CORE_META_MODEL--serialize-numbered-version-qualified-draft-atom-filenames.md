---
subjects:
  governs: Subject/Graph Node/Carrier/File.Filename
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom.ID
  - Subject/Graph Node/Domain/Continuant/Atom.Version Number
version: 8
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-D-650
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
type: Eng Decision
tier: 3
---
# Summary

Serialize numbered version-qualified Draft Atom filenames

## Scope

Project-owned Draft Atom filename identity segments.

## Claim

A Draft Atom proposing a revision of an existing Atom **must** carry `atom_id: <canonical-ID>@<proposed-version>-draft`, where `<proposed-version>` is the proposed numeric Atom Version. Its filename **must** carry that exact marker once as the Atom-ID segment before the filename's mutable components under CA-D-283. Do **not** append another `@<version>` suffix to the basename. The Draft marker identifies the proposed revision; it does not replace or advance the Current Atom source before an admitted update.

New-Atom Draft markers continue to use the role-only form governed by CA-D-378; this rule does not add a version number to a new Atom's marker or change other filename components.

## Details

For an existing Atom, the proposed version follows the applicable revision rule, including the current-version-plus-one rule for an actual update. The owning role's `draft/` placement and remaining filename components continue to follow their applicable Delivery rules. Existing legacy Draft filenames are not normalized automatically.
