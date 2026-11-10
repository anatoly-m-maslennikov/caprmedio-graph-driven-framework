---
atom_id: CA-C-463
ref_id: CA-C-463@2
container:
  scope_unit: CA-SU-16
role: Concern
form: Question
topics:
  main_subject: Subject/Engineering/Release Packaging/Payload Selection
  dependencies:
  - Subject/Engineering/Source Discovery/Transient and Secret Exclusion
relations:
  concern_about:
  - CA-P-1689
status: Archived
version: 2
updated_at: 2026-10-23 01:47:30 +0400
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
carrier_destination:
  file:
    name: CA-C-463@2-TOOLS-QUESTION--which-carriers-belong-in-a-complete-release-package.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/01_concern/archive
---
# Summary

Which carriers belong in a complete Release package

## Concern

The current Engine inventory includes .caprmedio_tmp test receipt files, treating transient state as distributable source. Choose all persistent declared Framework resources, excluding known ephemeral caches, temporary state and .DS_Store, and refusing secret-named carriers before any byte read. Alternatives were include every physical file or maintain a second hand-authored inventory. The selected shared classifier at89% confidence preserves complete source/package ownership without transient or credential delivery and avoids duplicate collectors. P1689 implements and verifies that choice; no secret file is read to test it.

## Evidences

Live Engine .caprmedio_tmp contains two disposable receipts; both current inventory collectors recursively select all regular files.

## Blast radius

Release inventory only, not canonical authoring authority or historical Journal relocation.
