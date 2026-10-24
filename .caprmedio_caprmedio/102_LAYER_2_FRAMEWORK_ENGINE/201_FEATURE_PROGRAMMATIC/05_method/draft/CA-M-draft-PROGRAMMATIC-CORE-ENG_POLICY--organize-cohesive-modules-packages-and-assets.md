---
atom_id: CA-M-draft
content_role: Method
type: Eng Policy
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
tier: 1
status: Draft
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-23 19:11:00 +0400"
subjects:
  governs: Subject/Engineering/Implementation Cohesion
  depends_on:
    - Subject/Engineering/Source Unit Responsibility
    - Subject/Engineering/Behavior Ownership
    - Subject/Engineering/Outcome Evidence
relations:
  relates_to:
    - CA-M-403
    - CA-M-411
    - CA-M-419
    - CA-E-364
    - CA-E-539
---
# Summary

Organize cohesive modules, packages and assets

## Scope

New or materially changed hand-authored PROGRAMMATIC implementation,
including code modules, packages, tests and owned non-code source assets
throughout descendant Scope Units. This Method owns the source-size,
cohesion, package-organization and source-asset rules; linked Evaluation
carriers measure and check them but do not own the policy.

## Claim

Organize implementation around cohesive responsibilities and the following
non-optional source boundaries:

- Every executable function and method has a 25-line soft limit and a
  40-line hard limit. Crossing the soft limit requires a cohesion review and
  written justification. More than 40 logical executable lines is a failure
  with no exception.
- Every module has a 200-line soft limit and a 300-line hard limit. Crossing
  200 physical lines requires a cohesion review and written justification.
  More than 300 physical lines is a failure with no exception.
- Logical executable function LOC excludes comments, docstrings and blank
  lines. Module physical LOC includes all text under the current counting
  convention.
- Each class has one cohesive responsibility and has no arbitrary numeric
  class-size cap. Every method defined on a class remains governed by the
  function and method limits.
- A helper is meaningful only when it expresses a reusable responsibility or
  boundary. Do not add helpers, wrappers, indirection, line compression or
  formatting changes merely to game a threshold.
- Growing implementation is split into cohesive packages or subfolders with
  visible ownership, not a sprawling flat file set or meaningless nesting.
- Descriptive, sufficiently verbose filenames identify module responsibility.
  Platform-required names and locations are preserved when genuinely
  required.
- JSON, YAML, TOML and other owned source assets belong in the owning
  module's local `assets/` folder unless a platform requires another name or
  location. Governed Atom carriers, Journals and Runtime outputs are not
  implementation source assets.

Under this proposal, size and cohesion rules are Method policy. The companion
Evaluation Draft specifies measurement, checker and linter paths; it does not
create, weaken or waive these rules. Existing CA-E-364 and CA-E-539 content
requires coordinated reconciliation at adoption, not reinterpretation now.

## Details

1. Count each standalone, nested, asynchronous and class-defined executable
   function or method by logical executable lines, excluding comments,
   docstrings and blanks. Count module physical lines as all text under the
   current convention. Exactly 25/40 and 200/300 remain within their
   respective limits; crossing a soft boundary requires a written cohesion
   review, while exceeding a hard boundary fails without exception.
2. Review the class responsibility separately from numeric size. Do not split
   a cohesive class merely to satisfy a number, and do not use a class-size
   argument to excuse an oversized or incohesive method.
3. Extract a helper only for a meaningful reusable responsibility or real
   boundary. Keep dependency direction visible and use cohesive packages or
   subfolders when a module grows. Avoid flat helper sprawl and arbitrary
   nesting.
4. Keep source assets beside their owning module under `assets/`, subject to
   genuine platform-required names or locations. Never reclassify governed
   Carriers, Journal records or Runtime outputs as local source assets.
5. Apply the policy to new or materially changed hand-authored source. Do not
   silently migrate vendor code, generated output, frozen fixtures or legacy
   history. A linked Evaluation result can be pass, fail or unresolved, but
   it is evidence about this Method rather than a second policy owner.

## Adoption notes

This Draft proposes Method ownership of the listed size, cohesion,
organization and asset decisions. It is not current authority and does not
silently supersede CA-M-403, CA-M-411, CA-M-419, CA-E-364 or CA-E-539.
Those active Atoms remain unchanged until coordinated adoption reconciles
their existing rules. The proposed Evaluation checks this Method rather than
owning a second set of rules.

Companion Evaluation Draft: [source-size and organization Evaluation](../../06_evaluation/draft/CA-E-draft-PROGRAMMATIC-GENERAL-EVALUATION_APPROACH--evaluate-source-size-cohesion-and-package-organization.md).
