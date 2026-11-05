---
atom_id: CA-A-1319
ref_id: CA-A-1319@1-draft
version: 1
status: Draft
role: Analysis
form: Specification Proposal
tier: 3
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header
updated_at: 2026-11-05 13:01:22 +0400
carrier_destination:
  file:
    name: CA-A-1319@1-draft-SPECIFICATION_PROPOSAL--move-atom-containment-into-header-container.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/02_analysis/draft
container:
  scope_unit: CA-SU-11
---
## Summary

Move Atom containment into Header.Container

## Decisions

- Header.Container is one mapping with exactly one key.
- `scope_unit` stores the containing Scope Unit ID.
- `atom` stores the containing Atom's base ID; it selects Current by default.
- Names, name suffixes and paths are resolved from the ID.
- The CAPRMEDIO Project Scope Unit has ID `CA-SU-00`.
- `CA-SU--1` is the predefined Scope Unit named `world`, without a Declaration.
- The root Project Declaration Atom uses `scope_unit: CA-SU--1`. If omitted, that mapping is its effective default.
- The Project Scope Unit itself stays unordered, without order.number or a formal parent.
- Header.Relations is optional and carries no duplicate containment fact.
- D264 and D266 remain. The declared Container and placement readback identify the same fact.
- Runs use formal containment Relations. Run Properties remain deferred.

## Rationale

IDs preserve references through Scope Unit renames and moves. The Project and its Declaration Atom are different objects. Predefined world supplies the Declaration Atom's bootstrap Container without another Declaration or a scalar exception.

## Source changes

1. Require stable IDs on declared Scope Units; assign the root ID in its specific Declaration.
2. Exempt predefined world from Declaration coverage and the ordinary non-Project parent requirement.
3. Declare the Container mapping and its two ID-valued leaf Properties.
4. Reconcile Header, Relation serialization, placement and validation consumers.
5. Adopt the reviewed source/schema packet with compatible readers, then migrate carriers and refresh the seven MODEL views.

## Drafts

Root/bootstrap Drafts created or rebased in `application/project-root-id-drafts-20261105`:

- CA-R-2523@4-draft: Scope Unit parent exception.
- CA-R-2524@4-draft: Project ID allowance.
- CA-R-2526@5-draft: stable Scope Unit IDs and reserved bootstrap ID.
- CA-R-2640@2-draft: CAPRMEDIO Project ID `CA-SU-00`.
- CA-R-2688@3-draft: Declaration coverage with the world exception.
- CA-M-461@3-draft: Declaration authoring.
- CA-E-670@2-draft: ID, coverage and reserved-ID checks.
- CA-D-442@27-draft: Declaration delivery.
- CA-R-2779@1-draft: Container mapping and bootstrap default.
- CA-R-2508@7-draft: one effective containment link per Atom.

Other existing Drafts remain part of coordinated integration:

- CA-R-2783@1-draft: Container.atom ID value.
- CA-R-2784@1-draft: Container.scope_unit ID value.
- CA-R-2719@2-draft: Header members.
- CA-R-2709@2-draft: optional Relations.
- CA-R-2712@3-draft: sequence uniqueness by Container.
- CA-R-2511@6-draft: Plan containment permissions.
- CA-E-240@50-draft: Container validation.
- CA-D-264@30-draft, CA-D-266@30-draft and CA-D-268@31-draft: containment readback and serialization.
- CA-D-467@29-draft and CA-E-500@29-draft: recursive Step placement agreement.

CA-R-2530@3-draft is a separate Path proposal, not a Container prerequisite. Current Path authority stays unchanged.

## Adoption gates

The root/bootstrap choices are settled. The current reader rejects a root ID; compatible reader/model/validator and bootstrap adapter changes belong to CA #3 and are recorded in P2707. Finish consumer and syntax integration before promotion and carrier migration. No Current root update, reader admission or carrier migration is claimed by these Draft writes.
