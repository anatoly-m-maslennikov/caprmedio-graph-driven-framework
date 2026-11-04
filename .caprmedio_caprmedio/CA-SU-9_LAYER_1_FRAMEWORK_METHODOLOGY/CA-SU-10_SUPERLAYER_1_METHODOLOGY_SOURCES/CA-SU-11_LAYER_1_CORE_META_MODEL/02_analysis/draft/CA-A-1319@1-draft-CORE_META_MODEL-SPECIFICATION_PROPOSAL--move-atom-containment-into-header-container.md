---
atom_id: CA-A-1319
version: 1
status: Draft
role: Analysis
form: Specification Proposal
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
updated_at: 2026-11-04 23:09:24 +0400
carrier_destination:
  file:
    name: CA-A-1319@1-draft-CORE_META_MODEL-SPECIFICATION_PROPOSAL--move-atom-containment-into-header-container.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/02_analysis/draft
---
## Summary

Move Atom containment into Header.Container

## Decisions

- Store one immediate Container in Atom.Header.Container.
- Its value is a full Scope Unit path or a base Atom ID.
- A base Atom ID selects Current by default.
- Header.Relations is optional. It stores other authored Relations.
- Keep IS_CONTAINED_BY, CONTAINS and +>/<+ in Formal Claims and the MODEL.
- Scope Unit containment remains in its Declaration Claim: one Container per non-Project Scope Unit; none for Project.
- Each Declaration Atom separately has its own Header.Container.

## Rationale

One stored Property supplies an Atom's Container. Formal containment expressions keep their established meaning. A Declaration Atom and the Scope Unit it declares are separate hosts.

## Source changes

1. Declare Header.Container and add it to Header.
2. Make Header.Relations optional.
3. Retire the old typed Header.Relations.IS_CONTAINED_BY wrapper and its atom/scope_unit children after consumer repair.
4. Update Atom, Plan lookup, sequence-number and Delivery constraints.
5. Review and push the source checkpoint before the mechanical data migration.
6. Verify migrated sources and refresh the seven MODEL views. Implementation and test gates remain with CA #3; Workbench and Workflow owners keep their files.

## Open decisions

- Canonical encoding of the full Scope Unit path: one string or an ordered chain.
- An external Project Declaration Atom still needs a valid Atom Container, although its declared Project has none.

## Prepared evidence

The Header, consumer, Delivery and planning previews are listed in the Epic packet at `.caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/coverage/container-header-change/`. They are previews, not created Declaration Drafts.
