---
atom_id: CA-M-495
ref_id: CA-M-495@1
container:
  scope_unit: CA-SU-15
role: Method
form: Direct Policy
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Component Structure
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Traceability
tier: 1
status: archived
version: 1
updated_at: 2026-11-10 20:47:54 +0400
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
destination:
  file:
    name: CA-M-495@1-PROGRAMMATIC-CORE-DIRECT_POLICY--localize-engineering-decisions-and-reuse-shared-policies.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method/099_archived
---
## Summary

Localize engineering decisions and reuse shared policies

## Claim scope

Every new or changed PROGRAMMATIC implementation decision represented by an
implemented RMED Atom, across Requirements, Methods, Evaluations and Deliveries
and their descendant Scope Units.

## Claim

### Prose Claim

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

Treat every implemented R, M, E, or D engineering decision as an ownership obligation. Prefer one cohesive module or package for its actual behavior, structure, or evidence; many-to-many realization remains valid, but do not invent an owner from a trace link, caller, dependency, facade, or test invocation. A test owns an Evaluation only when it materially implements its check, fixture, or verification behavior, and its module cites that Atom's ID and Version in the module header.

Split a decision only at a real responsibility, lifecycle, effect, interface, data, or security boundary, record that reason, and do not scatter logic to reduce a size measure. Implement each cross-cutting policy once at its canonical shared boundary and apply it wherever applicable; copied logic remains a real implementation site for review. Callers, adapters, routers, and orchestration layers are consumers unless they contain independent claim-specific logic. Put required citations on actual owning module headers, including package members; a package initializer or facade is not an owner merely by re-exporting behavior. Use the admitted implementation-trace policy for citation scope and syntax.
