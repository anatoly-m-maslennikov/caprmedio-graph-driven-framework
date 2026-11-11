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
status: Active
version: 5
updated_at: "2026-11-07 18:02:00 +0400"
carrier_destination:
  file:
    name: CA-P-2711-EPIC--adopt-the-medo-role-and-form-model.md
    path: .caprmedio_caprmedio/03_plan
---

## Summary

Adopt the MEDO Role and Form model

## Objective

Adopt the reviewed MEDO Role meanings and contribution Forms, define P Work Report and I Atoms, then reconcile affected Current and Draft Atoms and their consumers.

## Scope

MEDO Role Semantics; Solution, Direct Policy, Approach Policy and Decision; the Scope Delegation and Tier rules needed for their adoption; optional CONTRIBUTES_TO traceability.

Extend the model with P Work Report and I Atoms. Their model definitions, identities and lifecycles are planned in the child Tasks below.

The Requirement Semantics Draft is a prerequisite: required outcomes and constraints apply across Aspects. Specification remains in RMEDO. This Epic tracks adoption work.

## Inputs

- [Specification proposal CA-A-1328@1-draft](../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/02_analysis/draft/CA-A-1328@1-draft-CORE_META_MODEL-SPECIFICATION_PROPOSAL--introduce-scope-delegation-and-policy-forms.md).
- [Model adoption record](CA-P-2711-EPIC--adopt-the-medo-role-and-form-model/model-adoption-20261107/README.md).

The selected MODEL sources have been reviewed and promoted manually. This establishes source adoption; instance migration and consumer verification remain separate stages.

[I / Code Synopsis model adoption](CA-P-2711-EPIC--adopt-the-medo-role-and-form-model/done/02-CA-P-2713-TASK--define-implementation-atoms/implementation-model-20261107/README.md) is complete. P / Work Report and consumer implementation remain open.

## Work

- [x] Review the proposal and Role Drafts against Current authorities; settle the adoption choices listed in the proposal.
- [x] Complete the required Declarations and RMED for Forms, Scope Delegation, Tier rules and CONTRIBUTES_TO; review and repair the packet.
- [x] Adopt the reviewed packet with valid identities, Versions and preserved history.
- [ ] [CA-P-2712 — Define Work Report Atoms](CA-P-2711-EPIC--adopt-the-medo-role-and-form-model/001_backlog/01-CA-P-2712-TASK--define-work-report-atoms.md).
- [x] [CA-P-2713 — Define Implementation Atoms](CA-P-2711-EPIC--adopt-the-medo-role-and-form-model/done/02-CA-P-2713-TASK--define-implementation-atoms.md).
- [ ] Map affected Current and Draft MEDO Atoms by Claim and scope; report ambiguous cases for resolution.
- [ ] Preview and review the migration, then apply the accepted mapping.
- [ ] Identify affected validators, authoring operations and projections; hand off required implementation work to their owners and verify compatibility.
- [ ] Regenerate affected projections and check them against the adopted sources.
- [ ] Review coverage and record acceptance evidence and any remaining exceptions.

## Acceptance

- Current Declarations and governing rules express the reviewed model consistently.
- P Work Report and I are defined by reviewed Current model Atoms, including identity, lifecycle and their separate purposes.
- Every selected migration candidate is accounted for, with its identity and history preserved.
- Forms and Tiers follow the adopted rules; optional CONTRIBUTES_TO links remain optional.
- Affected consumers and projections are verified against the same adopted source set.
- Completion records distinguish source adoption, migration and implementation verification.

## Boundaries

The Project Package rename, unrelated Header migrations and unrelated Workbench/runtime changes belong to their own work. Archived Atoms and frozen evidence retain their historical meaning.

The model stage is adopted. The Epic remains open for instance mapping, migration, implementation compatibility and projections.
