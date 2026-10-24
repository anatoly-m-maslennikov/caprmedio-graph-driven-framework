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
updated_at: "2026-10-23 19:01:35 +0400"
subjects:
  governs: Subject/Engineering/Source Unit Responsibility
  depends_on:
    - Subject/Engineering/Implementation Cohesion
    - Subject/Engineering/Behavior Ownership
relations:
  relates_to:
    - CA-M-403
    - CA-M-411
    - CA-M-419
---
# Summary

Localize engineering decisions and reuse shared policies

## Scope

Every new or changed PROGRAMMATIC implementation decision represented by an
implemented RMED Atom, across Requirements, Methods, Evaluations and Deliveries
and their descendant Scope Units.

## Claim

Localize each implemented RMED engineering decision in one owning module or
one cohesive package whenever practical. Many-to-many implementation relations
remain valid, but an unimplemented Atom receives no invented implementation
target. Split a decision across modules only for a genuine boundary and record
the concrete reason; do not hide dispersed behavior behind a facade. Apply
cross-cutting policies everywhere they are applicable through one shared
canonical implementation, such as a decorator or common boundary, rather than
duplicating the policy logic. A caller, adapter or router is not an
implementation owner unless it contains independent claim-specific logic.

## Details

- Treat an engineering decision from any implemented R, M, E or D Atom as an
  ownership obligation; this policy is not limited to Requirements and
  Deliveries.
- Prefer one owning module or one cohesive package for the decision's actual
  behavior, structure or evidence rule. Several RMED Atoms may share an owner,
  and one Atom may have several owners when the relation is genuinely
  many-to-many.
- Do not create a fake implementation relation for an Atom that is not
  implemented. A trace link, caller, dependency or facade alone is not
  claim-specific realization. A test does not own the behavior it merely
  exercises. A test module that materially implements an Evaluation Atom
  does own that Evaluation and cites its ID in the module header.
- Use a multi-module split only when a real responsibility, lifecycle, effect,
  interface, data or security boundary requires it. Name that reason and keep
  the resulting units cohesive; do not scatter logic merely to reduce a local
  size measurement.
- Implement a cross-cutting policy once at its canonical shared boundary and
  apply that implementation at every applicable owner. A decorator, shared
  helper or equivalent boundary may carry the policy. If copied policy logic
  exists, report its actual realizing modules and review the duplication;
  do not hide a real implementation site by labelling it a mere consumer.
- Callers, adapters, routers and orchestration layers remain consumers unless
  they contain independent logic that realizes part of the RMED Claim. Do not
  make them owners only because they invoke an owner.
- Cite implemented RMED Atoms only at actual owning source-module headers,
  including owning modules within a package. A package initializer or facade
  is not an implementation owner solely because it re-exports the behavior.
  Use the separate implementation-trace syntax decision, not a second format.

## Adoption notes

This is a Draft policy for review. It is not current authority, does not
supersede CA-M-403, CA-M-411 or CA-M-419, and must not be treated as an active
implementation gate until separately accepted and promoted.

Companion Draft: [module-start ownership citations](CA-M-draft-PROGRAMMATIC-STANDARD-ENG_DECISION--write-rmed-owner-citations-only-at-module-start.md).
