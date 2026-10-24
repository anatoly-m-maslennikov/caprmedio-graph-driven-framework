---
atom_id: CA-M-draft
content_role: Method
type: Eng Policy
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
tier: 1
status: Draft
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-23 18:58:14 +0400"
subjects:
  governs: Subject/Engineering/Implementation Cohesion
  depends_on:
    - Subject/Engineering/Source Unit Responsibility
    - Subject/Engineering/Behavior Ownership
relations:
  relates_to:
    - CA-M-403
    - CA-M-411
    - CA-M-419
---
# Summary

Organize cohesive modules, packages and assets

## Scope

New or changed PROGRAMMATIC implementation, including its code modules,
packages, tests and non-code source assets.

## Claim

Organize implementation around cohesive responsibilities: keep functions,
methods and classes meaningful; split growing modules into coherent packages or
subfolders; use descriptive filenames; and place non-code source assets in the
owning module's local `assets/` subfolder. A class has one coherent
responsibility without an arbitrary numeric class-size cap, while every method
and function remains subject to its applicable Evaluation policies. Preserve
platform-required names and paths, and do not treat governed Carriers, Journal
records or Runtime outputs as source assets. Numeric size thresholds and
acceptance decisions belong to the companion Evaluation, not this Method.

## Details

- Keep each class responsibility coherent without splitting classes merely to
  satisfy an invented numeric metric. Apply the applicable E policy to every
  function and method, including methods defined on a class.
- Extract a helper when it expresses a meaningful reusable responsibility or
  boundary; do not add helpers, wrappers or indirection only to game a size
  metric.
- When a module grows, split it into coherent packages or subfolders with
  visible ownership. Avoid a huge flat collection of helper files and avoid
  arbitrary nesting that hides responsibility.
- Use descriptive, sufficiently verbose filenames so a module's responsibility
  is understandable from its path. Preserve names and paths required by a
  platform, framework, protocol or tool when they are genuinely required.
- Store JSON, YAML, TOML and other non-code source assets in the owning
  module's local `assets/` subfolder unless a platform requires another
  location. Governed Atom carriers, Journals and Runtime outputs are not local
  source assets and remain under their own authorities.
- Use the applicable E policies for function and module size measurements;
  this Method does not create alternative limits, waivers or exceptions.

## Adoption notes

This is a Draft policy for review. It is not current authority, does not
supersede CA-M-403, CA-M-411 or CA-M-419, and must not be treated as an active
implementation gate until separately accepted and promoted.

Companion Draft: [source-size and organization Evaluation](../../06_evaluation/draft/CA-E-draft-PROGRAMMATIC-GENERAL-EVALUATION_APPROACH--evaluate-source-size-cohesion-and-package-organization.md).
