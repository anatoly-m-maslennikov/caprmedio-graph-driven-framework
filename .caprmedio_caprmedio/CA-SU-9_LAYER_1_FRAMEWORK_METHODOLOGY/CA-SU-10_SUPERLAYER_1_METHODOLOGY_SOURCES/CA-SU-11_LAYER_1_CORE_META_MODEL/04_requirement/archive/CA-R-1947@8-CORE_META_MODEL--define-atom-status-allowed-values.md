---
atom_id: CA-R-1947@8
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom.Status
relations:
  child_of:
  - CA-R-1174
version: 8
updated_at: 2026-10-25 17:32:27 +0400
tier: 2
type: Rule
---
# Summary

Define Atom.Status allowed values

## Scope

The base allowed values inherited by narrower Atom kinds.

## Claim

Atom.Status **must** admit (Draft, Active, Archived). Narrower Atom kinds inherit these values and **may** add allowed values under their applicable Content Role or Type. An inherited value does **not** require a separate declaration for every narrower kind.

## Details

CA-R-1412 requires exactly one Status but does not declare the base allowed values. CA-R-1309 declares Draft, Active and Archived only for Requirements; it must not be retargeted to all Atoms as a Subjects-only change.

Later content alignment is needed: CA-R-1539's exact Plan set excludes inherited Draft, CA-R-1875's Analysis set excludes inherited Active, and CA-R-1608 uses a different Concern spelling/domain. C/A content remains deferred. CA-R-1308 and CA-R-1313 also need alignment with additive inheritance. This draft does not change transition procedures, existing Status values or any active source.
