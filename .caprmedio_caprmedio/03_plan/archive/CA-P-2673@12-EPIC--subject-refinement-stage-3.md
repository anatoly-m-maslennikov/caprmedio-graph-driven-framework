---
atom_id: CA-P-2673@12
content_role: Plan
type: Plan
label: Epic
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject
version: 12
updated_at: 2026-10-27 20:01:31 +0400
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
- [P2682 — Rebuild Candidate #10 Subject Graph](CA-P-2673-EPIC--subject-refinement-stage-3/09-CA-P-2682-TASK--rebuild-candidate-10-subject-graph.md).

### Scope

Completed preparation and review: main Subject structure and a defining R Atom for each primary entity or topic, without instances. The four completed Tasks remain Done.

New adoption/migration phase: inventory the selected Current RMEDO sources; map Governs first, then Depends On; review the prepared 42 definition/anchor Drafts and necessary mapped successors; apply only accepted changes; rebuild and check the primary Subject view from adopted Current sources.

The migration changes Subjects and adopts the already-prepared definition/anchor content. It does not include a general content migration, role/Type/Tier/ID/property-schema migration, governing-configuration rewrite, instance redesign, Terms Graph implementation, Scope Unit restructuring, code, Tools, runtime or release. Existing Archived sources and unrelated Drafts remain untouched; normal predecessor archives for actual selected updates are created.

### Review

The Candidate #10 FPF design challenge and independent validation are complete. The Operator resolved both findings in separate Specification Proposals. The next review checks the concrete adoption/migration batch against those accepted decisions; it is not another full FPF challenge or a new runtime gate.

### Decisions

Latest Operator statements override earlier candidates. Implementation is directly editable and is not a Projection. Projection changes belong in its sources and are rebuilt through its Workflow. Atom/Content Role is a classification-axis Subject, not a separate entity kind; Atom/Content Role: X identifies a narrower Atom kind. CAPRMEDIO and project-name namespaces qualify Subjects and do not mirror owning Scope Units.

## Definition of Done

The reviewed definition batch is adopted; selected Governs and Depends On Subjects match the accepted map; normal source history is preserved; and the rebuilt primary Subject view comes from those actual Current sources with defining R IDs. Prepared, reviewed, applied and rebuilt are reported as distinct outcomes, with no hidden gaps. No code or runtime work is included.


### Preparation state

A1218 contains the main tree and definitions; 42 R/MED anchor and Definition Drafts are prepared. P2674 and P2675 are Done. The FPF design challenge is complete and independently validated. P2676 is Done; P2677 is Done. Both findings have Operator decisions recorded separately in A1219 and A1220; the three affected Definition Drafts and Candidate #10 are refined. Adoption has not occurred.


### Preparation/review completion

Candidate #10 contains the main Subject structure, defining R Atom IDs and definitions without instances.42Drafts are prepared; the FPF design challenge and independent validation are complete. The two review findings have separately saved Operator decisions and matching Draft refinements. The four original child Tasks are Done. This was the completed preparation/review phase. The Operator has now reopened and expanded the same Epic with adoption, migration and rebuild work; those new Tasks are queued and have not run.


### Execution order and current state

P2678 → P2679 → P2680 → P2681 → P2682. Reuse the existing thin inventory in P2675 rather than creating competing maps. Each accepted decision stays in one A / Specification Proposal; P Atoms hold work and progress with links. The initial definition set is 42 Drafts; the fresh mapping inventory determines additional Subject-only successors. This edit expands the Plan only: Governs mapping has started;803changes are Drafted.CurrentRMEDO promotion,migration andgraphrebuild have not started.

## Governs staging result

P2678 is Done: 2,240 existing-source successors and 15 new definitions are Drafted. All 2,258 Current RMEDO source bytes remain unchanged. P2679 is Active for dependency mapping; review, publication and rebuild have not run.

## Combined Draft batch

Governs and Depends On mappings are complete in Drafts (P2678/P2679 Done). P2680 reviews 2,252 source successors and 15 new definitions. All 2,258 Current RMEDO originals remain unchanged pending adoption.

## Adoption gate

P2680 is Done with independent PASS reviews. P2681 is Active to promote the accepted Drafts and archive predecessors. No runtime or tool code changes are included.

## Applied source result

P2681 is Done: 2,252 existing sources updated, their predecessors archived, and 15 new definitions Current. P2682 is Active for the main-Subject view from the actual 2,273 Current sources.
