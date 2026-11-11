---
atom_id: CA-P-2711
ref_id: CA-P-2711
container:
  scope_unit: CA-SU-00
role: Plan
form: Plan
label: Epic
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit
tier: 3
status: Backlog
version: 1
updated_at: "2026-11-07 13:26:13 +0400"
carrier_destination:
  file:
    name: CA-P-2711-EPIC--adopt-the-medo-role-and-form-model.md
    path: .caprmedio_caprmedio/03_plan
---

## Summary

Adopt the MEDO Role and Form model

## Objective

Adopt the reviewed MEDO Role meanings and contribution Forms, then reconcile affected Current and Draft Atoms and their consumers.

## Scope

MEDO Role Semantics; Solution, Direct Policy, Approach Policy and Decision; the Scope Delegation and Tier rules needed for their adoption; optional CONTRIBUTES_TO traceability.

The Requirement Semantics Draft is a prerequisite: required outcomes and constraints apply across Aspects. Specification remains in RMEDO. This Epic tracks adoption work.

## Inputs

- [CA-A-1328@1-draft — specification proposal](../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/02_analysis/draft/CA-A-1328@1-draft-CORE_META_MODEL-SPECIFICATION_PROPOSAL--introduce-scope-delegation-and-policy-forms.md).
- [CA-R-2512@3-draft — Requirement Declaration](../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/CA-R-2512@3-draft-CORE_META_MODEL-DECLARATION--declare-requirement.md).
- [CA-R-2513@3-draft — Method Declaration](../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/CA-R-2513@3-draft-CORE_META_MODEL-DECLARATION--declare-method.md).
- [CA-R-2514@3-draft — Evaluation Declaration](../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/CA-R-2514@3-draft-CORE_META_MODEL-DECLARATION--declare-evaluation.md).
- [CA-R-2515@3-draft — Delivery Declaration](../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/CA-R-2515@3-draft-CORE_META_MODEL-DECLARATION--declare-delivery.md).
- [CA-R-2463@3-draft — Operations Declaration](../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/CA-R-2463@3-draft-CORE_META_MODEL-DECLARATION--declare-operations.md).
- [Role Semantics review](../02_analysis/draft/role-semantics-20261107/README.md).

These inputs are Drafts. Their preparation and bounded review do not establish adoption.

## Work

- [ ] Review the proposal and Role Drafts against Current authorities; settle the adoption choices listed in the proposal.
- [ ] Complete the required Declarations and RMED for Forms, Scope Delegation, Tier rules and CONTRIBUTES_TO; review and repair the packet.
- [ ] Adopt the reviewed packet with valid identities, Versions and preserved history.
- [ ] Map affected Current and Draft MEDO Atoms by Claim and scope; report ambiguous cases for resolution.
- [ ] Preview and review the migration, then apply the accepted mapping.
- [ ] Identify affected validators, authoring operations and projections; hand off required implementation work to their owners and verify compatibility.
- [ ] Regenerate affected projections and check them against the adopted sources.
- [ ] Review coverage and record acceptance evidence and any remaining exceptions.

## Acceptance

- Current Declarations and governing rules express the reviewed model consistently.
- Every selected migration candidate is accounted for, with its identity and history preserved.
- Forms and Tiers follow the adopted rules; optional CONTRIBUTES_TO links remain optional.
- Affected consumers and projections are verified against the same adopted source set.
- Completion records distinguish source adoption, migration and implementation verification.

## Boundaries

The Project Package rename, unrelated Header migrations and unrelated Workbench/runtime changes belong to their own work. Archived Atoms and frozen evidence retain their historical meaning.

Creating this Epic starts no promotion, migration or implementation.
