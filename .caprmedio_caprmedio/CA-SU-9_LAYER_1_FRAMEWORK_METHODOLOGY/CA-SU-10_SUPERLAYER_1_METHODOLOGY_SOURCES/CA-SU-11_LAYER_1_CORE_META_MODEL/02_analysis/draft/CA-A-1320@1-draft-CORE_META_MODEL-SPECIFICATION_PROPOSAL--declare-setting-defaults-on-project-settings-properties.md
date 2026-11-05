---
atom_id: CA-A-1320
ref_id: CA-A-1320@1-draft
container:
  scope_unit: CA-SU-11
role: Analysis
form: Specification Proposal
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings
tier: 3
status: Draft
version: 1
updated_at: 2026-11-04 23:09:29 +0400
carrier_destination:
  file:
    name: CA-A-1320@1-draft-SPECIFICATION_PROPOSAL--declare-setting-defaults-on-project-settings-properties.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/02_analysis/draft
---
## Summary

Declare setting defaults on Project Settings Properties

## Decisions

- Declare defaults on the corresponding Project.Settings Property with ?==.
- Preserve explicitly supplied valid values, including zero and false where their formats allow them.
- Validate values against each Property's declared format and cardinality.
- Keep Project initialization inputs distinct from declared defaults.
- Keep MODEL rules separate from Carrier serialization.

## Rationale

Each Property owns its format, cardinality and default. The separate Default Settings Artifact duplicates that schema. Moving defaults preserves one governing definition per Property.

## Existing values

- AI Agent Confidence Threshold: 90, already declared in the integer domain 0..100.
- Implementation Retry Limit: 3, read from the current D407-governed `caprmedio_framework_default_settings.toml`, SHA-256 `f8fda1107671ad6c3fd02653ada4f16ffe01ce0a3f57b4a732d7eac39d4e3851`.

The retry value is prepared for R2635. Other defaults need their own source-backed mapping.

## Source changes

1. Reconcile R1441/R1429 and their validation/resolution consumers.
2. Preserve defaults, validation, presence, isolation and writeback constraints that remain applicable.
3. Retire D407/D408 only after their Current consumers have a replacement or an explicit disposition.
4. Keep the earlier removal of the Plan Retry Limit. Workflow execution remains with its owner.
5. Leave runtime files and implementation changes to their owners.

## Prepared evidence

The source previews, default-file pin and consumer dispositions are in `.caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/coverage/remaining-disposition/governing-configuration-repair/property-defaults/`. These are previews; no dependent source retirement is claimed.
