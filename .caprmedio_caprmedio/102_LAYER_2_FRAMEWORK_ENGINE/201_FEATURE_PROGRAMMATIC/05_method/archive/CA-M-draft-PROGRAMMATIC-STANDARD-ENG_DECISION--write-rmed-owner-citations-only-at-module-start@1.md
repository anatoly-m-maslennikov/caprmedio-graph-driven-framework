---
atom_id: CA-M-draft
content_role: Method
type: Eng Decision
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
tier: 3
status: Draft
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-23 18:58:14 +0400"
subjects:
  governs: Subject/Engineering/Source Unit Responsibility
  depends_on:
    - Subject/Engineering/Implementation Cohesion
    - Subject/Engineering/Behavior Ownership
    - Subject/Engineering/Outcome Evidence
relations:
  relates_to:
    - CA-R-2117
    - CA-M-431
    - CA-E-653
    - CA-M-411
---
# Summary

Write RMED owner citations only at module start

## Scope

The method for materializing direct RMED-to-implementation traceability in
PROGRAMMATIC and descendant modules. It applies to actual implementation
owners, not to callers, facades, generated output, vendor code, frozen
fixtures, or legacy history unless those sources are explicitly admitted.

## Claim

Resolve the applicable active RMED authority and the actual owner first, then
write exactly one readable ownership block at the beginning of each owning
module. Do not write ownership blocks before functions, classes, methods, or
other implementation units. Use canonical Atom IDs only, preserve the
Requirement/Method/Evaluation/Delivery role distinction, choose the narrowest
applicable leaf in each branch, and keep independent branches separate.
Many-to-many ownership remains valid when each relation is materially real.

## Details

1. Resolve the current active RMED source and identify the module that
   materially realizes each claim. Preserve uncertainty for unresolved or
   dynamic definitions and references; do not make up an owner, parent,
   policy, or proof.
2. Write this shape at the module beginning. The IDs here are illustrative,
   not asserted source links:

   ```text
   # implementation of:
   # Requirement: CA-R-123, CA-R-456
   # Method: CA-M-789
   # Evaluation: CA-E-012
   # Delivery: CA-D-345
   ```

   Use only canonical Atom IDs. Omit empty roles. Do not include versions,
   paths, titles, draft markers, or an `applies` block.
3. Select the narrowest directly realized leaf for every relevant
   `child_of` or `parent_of` branch and do not duplicate ancestors already
   covered by that leaf. Cite independent branches separately. A module may
   cite several substantive RMED claims, and one claim may have several
   genuine module owners.
4. Locate a cross-cutting policy at the module where it is defined and
   implemented, such as the module containing an error-handling decorator.
   Consumers that only import, call, or decorate that policy are not policy
   owners solely because they reuse it. Find those consumers mechanically
   through code references rather than maintaining a second manual
   `applies` graph. If another module independently implements the same
   policy behavior, it is an owner and must cite the policy Method; avoid
   duplicate citations for mere reuse.
5. Apply every policy wherever it is applicable whether or not a citation is
   present. The block is direct trace metadata only; comments do not prove
   conformance, completion, or observed results. Keep Requirements as what
   must be done and Methods as how the implementation and citations are
   written.

## Adoption notes

This Draft proposes a coordinated future reconciliation of R2117, M431,
E653, and M411. Those current Atoms remain active authority until a reviewed
replacement is accepted and promoted. This Draft does not silently supersede
them and is not an implementation or release gate.

Companion Drafts: [ownership Requirement](../../04_requirement/draft/CA-R-draft-PROGRAMMATIC-GENERAL-REQUIREMENT--trace-rmed-claims-to-canonical-module-owners.md) and [traceability Evaluation](../../06_evaluation/draft/CA-E-draft-PROGRAMMATIC-STANDARD-QA_CASE--verify-owner-only-module-citations-and-derived-call-site-traces.md).
