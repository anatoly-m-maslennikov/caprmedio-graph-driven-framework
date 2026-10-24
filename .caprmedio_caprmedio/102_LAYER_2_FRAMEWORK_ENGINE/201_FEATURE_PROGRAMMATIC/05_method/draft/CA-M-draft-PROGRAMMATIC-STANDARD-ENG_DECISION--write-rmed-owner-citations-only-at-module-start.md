---
atom_id: CA-M-draft
content_role: Method
type: Eng Decision
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
tier: 3
status: Draft
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-23 19:11:00 +0400"
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

Resolve current applicable RMED authority and the actual owner first, then
write exactly one readable `# implementation of:` block at the beginning of
each owning module. Do not write ownership blocks before functions, classes,
methods, or other implementation units. Use canonical Atom IDs only, preserve
the Requirement/Method/Evaluation/Delivery role distinction, choose the
narrowest applicable leaf in each branch, and keep independent branches
separate. Many-to-many ownership remains valid when each relation is
materially real.

A shared policy provider cites the Method that it actually defines and
implements. A consumer that merely imports, calls or decorates that provider
does not cite the policy Method solely for reuse. Find such consumers
mechanically through code references; do not create a second manual
`applies` graph. A module with other substantive RMED claims still cites
those own claims. If another module independently implements the policy
behavior, it is also an owner and cites the policy Method without duplicating
citations for mere reuse.

A test module is an Evaluation owner only when it materially implements the
Evaluation check, fixture, or verification behavior. A test that merely
exercises another module is not an owner of that module's Requirement,
Method, or Evaluation. The policy still applies wherever applicable whether
or not a citation is present, and a comment never proves conformance,
completion, or observed outcome.

## Details

1. Resolve current active RMED source and identify the module that materially
   realizes each claim. Select the narrowest directly realized leaf for every
   relevant `child_of` or `parent_of` branch and do not duplicate
   ancestors already covered by that leaf. Cite independent branches
   separately. Preserve uncertainty for unresolved or dynamic definitions and
   references; do not invent an owner, parent, policy or proof.
2. Write this exact shape at the module beginning. These IDs are illustrative,
   not asserted source links:

   ```text
   # implementation of:
   # Requirement: CA-R-123, CA-R-456
   # Method: CA-M-789
   # Evaluation: CA-E-012
   # Delivery: CA-D-345
   ```

   Use only canonical Atom IDs. Omit empty roles. Do not include versions,
   paths, titles, draft markers or an `applies` block. Do not add a second
   authored block before a function, class, method or unit.
3. For an error-handling decorator, retry policy, logging policy or similar
   cross-cutting rule, cite the module where the policy is defined and
   implemented. Mere callers, importers and decorators are consumers, not
   Method owners solely because they reuse it. Inspect actual definitions and
   mechanics, not imports alone. If a consumer contains independent RMED
   behavior, cite that behavior's own canonical roles.
4. Derive consumer/call-site references mechanically for review. Do not turn
   those references into authored ownership edges or a second manual
   `applies` graph. Comments are trace metadata only; authoritative Atoms
   and observed implementation evidence remain required. Keep Requirements
   as what must be done and Methods as how the implementation and citation
   format are written; linked Evaluation carriers check the result and do not
   redefine this Method.

5. Apply the method only to the admitted current implementation boundary.
   Report out-of-boundary files for explicit disposition rather than
   mass-editing them. A missing or ambiguous current branch, an
   unidentifiable owner, or an invalid block is a traceability gap: preserve
   the source and report the gap.

## Adoption notes

This Draft proposes the module-only traceability and owner-localization
correction. Current CA-R-2117, CA-M-431, CA-E-653 and CA-M-411 remain active
authority until a reviewed role correction or replacement is accepted and
promoted. This Draft specifies how to achieve the companion Requirement's
traceability outcome; it does not silently supersede current Atoms and is not
an implementation or release gate.

Companion Requirement Draft: [trace RMED claims to canonical implementation owners](../../04_requirement/draft/CA-R-draft-PROGRAMMATIC-GENERAL-REQUIREMENT--trace-rmed-claims-to-canonical-module-owners.md).

Companion Evaluation Draft: [owner-only module citations and derived call-site traces](../../06_evaluation/draft/CA-E-draft-PROGRAMMATIC-STANDARD-QA_CASE--verify-owner-only-module-citations-and-derived-call-site-traces.md).
