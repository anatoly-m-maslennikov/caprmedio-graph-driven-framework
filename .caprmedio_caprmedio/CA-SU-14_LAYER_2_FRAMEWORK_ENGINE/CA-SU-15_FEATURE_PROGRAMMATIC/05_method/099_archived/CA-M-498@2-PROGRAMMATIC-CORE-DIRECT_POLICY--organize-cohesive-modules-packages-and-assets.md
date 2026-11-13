---
atom_id: CA-M-498
ref_id: CA-M-498@2
container:
  scope_unit: CA-SU-15
role: Method
form: Direct Policy
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Authoring <+ Code Authoring
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture
    <+ Component Structure
tier: 1
status: archived
version: 2
updated_at: 2026-11-10 20:47:54 +0400
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
destination:
  file:
    name: CA-M-498@2-PROGRAMMATIC-CORE-DIRECT_POLICY--organize-cohesive-modules-packages-and-assets.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method/099_archived
---

## Summary

Organize cohesive modules, packages and assets

## Claim scope

New or materially changed hand-authored PROGRAMMATIC implementation, including code modules, packages, tests and owned non-code source assets throughout descendant Scope Units. This Method owns shared cohesion, package organization and source-asset rules. Applicable language-specific source-size rules keep their own authority.

## Claim

### Prose Claim

Organize implementation around cohesive responsibilities:

- Each class, function and module has one cohesive responsibility. Review responsibility separately from numeric size.
- A helper is meaningful only when it expresses a reusable responsibility or boundary. Do not add helpers, wrappers, indirection, line compression or formatting changes merely to game a threshold.
- Growing implementation is split into cohesive packages or subfolders with visible ownership, not a sprawling flat file set or meaningless nesting.
- Descriptive, sufficiently verbose filenames identify module responsibility. Preserve platform-required names and locations.
- JSON, YAML, TOML and other owned source assets belong in the owning module's local `assets/` folder unless a platform requires another name or location. Governed Atom carriers, Journals and Runtime outputs are not implementation source assets.

Apply the relevant source-size and measurement rules to their declared language and source boundary. Do not turn Python limits into limits for every language or weaken the separate frontend limits. An unresolved policy conflict remains unresolved; do not invent a shared number.

## Details

Apply this Method to new or materially changed hand-authored source. Vendor code, generated output, frozen fixtures and legacy history remain outside automatic migration.

Preserve dependency direction and testability when extracting helpers or splitting packages. Do not split a cohesive class merely to satisfy a count, or use class size to excuse an oversized or incohesive method under its applicable policy. Source assets stay with their owner; governed Carriers, Journal records and Runtime outputs keep their existing boundaries.
