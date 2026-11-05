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
updated_at: 2026-11-05 06:18:20 +0400
carrier_destination:
  file:
    name: CA-A-1319@1-draft-CORE_META_MODEL-SPECIFICATION_PROPOSAL--move-atom-containment-into-header-container.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/02_analysis/draft
---
## Summary

Move Atom containment into Header.Container

## Decisions

- Header.Container is one mapping with exactly one key.
- `scope_unit` stores a stable Scope Unit ID, for example `CA-SU-11`.
- `atom` stores an Atom ID, for example `CA-P-123`.
- Store no Scope Unit name, name suffix or path in the reference.
- Resolve current names and physical destinations from the ID.
- The referenced container determines placement. D264 reads back that same containment fact from the nearest eligible Directory Carrier.
- Header.Relations is optional and stores no duplicate containment fact.
- D264 and D266 remain. Earlier retirement and dependent-link-removal previews are superseded.
- Runs have no Properties in this version. Their parentage uses formal Relations only.
- The Current Project root has no Scope Unit ID. Its future ID/reference case remains pending.
- Preserve the settled world bootstrap meaning: no World entity or graph link. Reconcile its encoding with the one-key mapping before admission.

## Rationale

An ID keeps the reference stable when a Scope Unit is renamed or moved. The same declared identity governs physical placement and the derived containment view. A Scope Unit Declaration Atom and the unit it declares remain distinct.

## Source changes

1. Rebase the Container group and declare its two alternative leaf Properties.
2. Transfer the old typed containment wrapper contracts from Header.Relations.
3. Keep explicit direct and inverse permissions; update Atom and Plan consumers.
4. Align D264, D266, D268 and affected placement Rules with the same containment fact.
5. Review and push the source checkpoint before mechanical migration.
6. Verify migrated carriers and the seven MODEL views. CA #3 owns implementation and tests; Workflow and Workbench owners retain their sources.

## Existing Drafts

- CA-R-2779@1-draft: Container group; its earlier scalar schema needs rebasing.
- CA-R-2783@1-draft: Container.atom ID value.
- CA-R-2784@1-draft: Container.scope_unit stable ID value.
- CA-R-2508@7-draft: Atom containment; scalar-world comparisons need rebasing.
- CA-R-2719@2-draft: Header members.
- CA-R-2709@2-draft: optional Relations.
- CA-R-2712@3-draft: sequence uniqueness by Container.
- CA-R-2511@6-draft: Plan containment permissions.
- CA-E-240@50-draft: Container validation.
- CA-D-264@30-draft: placement readback of the same declared containment fact.
- CA-D-266@30-draft: derived containment protection; placement agreement rebased.
- CA-D-268@31-draft: direct-only serialization; placement agreement rebased.
- CA-D-467@29-draft: recursive Step placement aligned with declared containment.
- CA-E-500@29-draft: placement agreement checks aligned.

These five Draft writes passed pinned source-helper readback in `application/container-placement-drafts-20261105`. Their Current predecessors remain unchanged.

CA-R-2530@3-draft is a separate scalar Path proposal, not a prerequisite for ID-based Container references. Current Path authority remains unchanged.

## Adoption gates

Resolve the Project root and bootstrap encoding. Finish the group/leaf and consumer rebases, then review and promote the coordinated packet. No Current Container schema or carrier-data migration is claimed here.
