---
atom_id: CA-P-2673@14
content_role: Plan
type: Plan
label: Epic
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject
version: 14
updated_at: 2026-10-27 22:47:33 +0400
relations: {}
tier: 3
---
# Summary

Subject refinement stage 3

## Objective

Prepare, review and adopt Candidate #10, migrate the selected Current RMEDO Subjects, then rebuild the primary Subject view without instances.

## Details

Candidate: [A1218 — Subject model Candidate #10](../02_analysis/CA-A-1218-SPECIFICATION_PROPOSAL--subject-model-candidate-10.md).

The Candidate belongs in an Analysis Atom of Type Specification Proposal. P Atoms hold tasks and progress. Each accepted review decision has its own A / Specification Proposal file; P Atoms link to it instead of copying decision text or the Candidate.

### Tasks

- [P2674 — Record Subject model Candidate #10](CA-P-2673-EPIC--subject-refinement-stage-3/done/01-CA-P-2674-TASK--record-subject-model-candidate-10.md).
- [P2675 — Draft main Subject definitions](CA-P-2673-EPIC--subject-refinement-stage-3/done/02-CA-P-2675-TASK--draft-main-subject-definitions.md).
- [P2676 — Review Subject model Candidate #10 with FPF](CA-P-2673-EPIC--subject-refinement-stage-3/done/03-CA-P-2676-TASK--review-subject-model-candidate-10-with-fpf.md).
- [P2677 — Resolve Candidate #10 review findings](CA-P-2673-EPIC--subject-refinement-stage-3/done/04-CA-P-2677-TASK--resolve-candidate-10-review-findings.md).

### Adoption and migration Tasks

- [P2678 — Map Candidate #10 Governs Subjects](CA-P-2673-EPIC--subject-refinement-stage-3/done/05-CA-P-2678-TASK--map-candidate-10-governs-subjects.md).
- [P2679 — Map Candidate #10 Depends On Subjects](CA-P-2673-EPIC--subject-refinement-stage-3/done/06-CA-P-2679-TASK--map-candidate-10-depends-on-subjects.md).
- [P2680 — Review Candidate #10 adoption batch](CA-P-2673-EPIC--subject-refinement-stage-3/done/07-CA-P-2680-TASK--review-candidate-10-adoption-batch.md).
- [P2681 — Adopt Candidate #10 and migrate Subjects](CA-P-2673-EPIC--subject-refinement-stage-3/done/08-CA-P-2681-TASK--adopt-candidate-10-and-migrate-subjects.md).
- [P2682 — Rebuild Candidate #10 Subject Graph](CA-P-2673-EPIC--subject-refinement-stage-3/done/09-CA-P-2682-TASK--rebuild-candidate-10-subject-graph.md).

### Scope

Completed preparation and review: main Subject structure and a defining R Atom for each primary entity or topic, without instances. The four completed Tasks remain Done.

Completed adoption/migration phase: inventory the selected Current RMEDO sources; map Governs first, then Depends On; review the prepared 42 definition/anchor Drafts and necessary mapped successors; apply only accepted changes; rebuild and check the primary Subject view from adopted Current sources.

The migration changes Subjects and adopts the already-prepared definition/anchor content. It does not include a general content migration, role/Type/Tier/ID/property-schema migration, governing-configuration rewrite, instance redesign, Terms Graph implementation, Scope Unit restructuring, code, Tools, runtime or release. Existing Archived sources and unrelated Drafts remain untouched; normal predecessor archives for actual selected updates are created.

### Review

The Candidate #10 FPF design challenge and independent validation are complete. The Operator resolved both findings in separate Specification Proposals. The concrete adoption/migration batch also passed independent exact-diff, namespace and rendering-scope reviews before publication. This did not introduce another FPF challenge or runtime gate.

### Decisions

Latest Operator statements override earlier candidates. Implementation is directly editable and is not a Projection. Projection changes belong in its sources and are rebuilt through its Workflow. Atom/Content Role is a classification-axis Subject, not a separate entity kind; Atom/Content Role: X identifies a narrower Atom kind. CAPRMEDIO and project-name namespaces qualify Subjects and do not mirror owning Scope Units.

## Definition of Done

The reviewed definition batch is adopted; selected Governs and Depends On Subjects match the accepted map; normal source history is preserved; and the rebuilt primary Subject view comes from those actual Current sources with defining R IDs. Prepared, reviewed, applied and rebuilt are reported as distinct outcomes, with no hidden gaps. No code or runtime work is included.


## Result

All nine child Tasks are Done. Governs was mapped first, then Depends On; the combined Draft batch passed review before promotion. Adopted 2,252 existing-source successors with predecessor archives and 15 new definitions. Publication checks pass. The fresh Current RMEDO source count is 2,273.

The primary view has 38 defining R references and no old Subject roots. Each accepted decision is saved separately in A1219–A1224. The single thin inventory in P2675 links actual Current carriers and marks applied rows.

The 17 pre-existing stale/non-next Draft records remain untouched. Terms Graph implementation, property/instance inventories, general content migration, Scope Unit restructuring, configuration changes, code, runtime and release remain outside this completed scope.

[Rebuilt main Subject view](../_projection/CA-PROJ-009-CAPRMEDIO--Subject-Graph--Current-RMEDO.md).

## Post-adoption review corrections

Accepted decisions A1225–A1229 are applied: 21 R successors are Current with 21 predecessor archives. The main structure is unchanged. The rebuilt Projection has 2,273 Current RMEDO sources, source_count 2,273 and 38 Current defining R references. Bounded Draft review and published-output checks pass; no repeat full FPF review, production-code or runtime change was performed.
