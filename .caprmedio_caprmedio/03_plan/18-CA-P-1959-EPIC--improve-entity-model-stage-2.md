---
atom_id: CA-P-1959
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 18
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Term, Property, Carrier, Revision, Scope Unit, Projection, Plan, Tool, Journal, Operator]
version: 1
updated_at: "2026-10-10 22:32:47 +0400"
relations: {}
---
# Summary

Improve entity model — Stage 2

## Objective

The Core Meta-model has consistent Entity origins in RMEDO Subjects, then consistent Summary, Substance, Scope and Details, in that order.

## Details

### Order

1. Build and verify safe Subject lookup and sealed patch-preview Tools.
2. Map and migrate authoritative RMEDO Subjects, then rebuild and verify the graph.
3. Only after the complete Subject gate passes, update Summary, Substance, Substance Scope and Details.
4. Verify the final sources and reproducible graph.

The Operator approved safe Tool development first, while leaving authoritative Atoms unchanged. Creating this Epic creates planned work; it does not apply source changes.

### Source and model boundary

- Select Core Meta-model by itself, not Core plus Project Configuration or Extensions. The current declared authoring root is `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL`. Reopen `project_structure.toml` before execution and pin the actual current original sources. Delivered/installed/Applicable Methodology copies are not editable authority.
- Step 1 concerns R, M, E, D and O Subjects: `governs` and `depends_on`. Scope ownership and Substance applicability stay distinct. Atom incidence is not a native Entity or Term relation.
- The seven candidate roots are Artifact, Scope Unit, Actor, Relation, Revision, Carrier and Execution. Dependent Entities belong to their owner lifecycle. Candidate display paths, temporal display groups and pseudocode are not automatically native grammar.
- Keep the captured review frozen at commit `a971d0e00c33c779f485fc8cad63194894d440fb`. The [candidate](../_projection/core-entity-review/presentation/operator.entity-graph.candidate.json) and [consolidated review](../_projection/core-entity-review/consolidated/contract.md) guide decisions; they do not replace live source pins. Their 442 display proposals are not executable replacements, and 149 follow-ups must not be guessed or hidden.
- Latest Operator input wins. Use the existing 90% threshold: investigate missing evidence; ask only when a concrete unresolved decision remains below it.

### Tool audit and safe cutover

The current audit found that ATOM_SEARCH searches whole-carrier text; ATOM_UPDATE replaces complete frontmatter, and supplying only Subjects loses other metadata. Its standalone apply guard remains intact. The dedicated Subject migration planner is preview-only and currently preserves revision metadata. Recheck these findings as implementation changes.

Lookup must target exact Subject fields and return occurrence/source pins. Preview must use explicit replacements, preserve unrelated bytes and account for Version +1, updated_at, history and Journal effects. No full-frontmatter rewrite, guessed mapping, new unguarded writer or bypass of existing admission is allowed.

One exact decision remains before live migration: active grammar uses / for bearer qualification and treats . as ordinary text, while the chosen candidate uses / for narrowing and . for bearer qualification. CA-P-1964 asks whether the minimum governing grammar-body revisions may be included in Step 1. All other body work stays Step 2. This Epic does not answer or authorize that exception.

Live application needs a separately approved exact sealed packet, current pins and the existing admitted mutation boundary. Candidate approval and Tool approval are not that packet approval. Changed pins require a fresh preview. Preserve current Atom identities and history; do not delete entities, fabricate relations or rewrite archived history.

### Ownership and reuse

Own work: none. This Epic is completed through its direct decomposing Plans.

This Epic owns the Operator's new Subjects-first/content-second sequence. Reuse CA-P-1872's existing builders. CA-P-1909–1912 retain the sole accepted-graph, preview, application and reproduction route: CA-P-1967 prepares its candidate packet only after CA-P-1909 is Done; CA-P-1910 owns the one final approvable sealed preview; CA-P-1968 organizes batches executed only under CA-P-1911's authorized application; CA-P-1969 consumes CA-P-1912's one verification receipt and checks the content-update gate. No second preview approval, source execution or competing completion receipt is created. If this shared route is unavailable or its current gates conflict, stop before the affected stage. Creating this Epic does not close or rewrite those older Plans.

Keep the separate Terms graph, MCP delivery, Apps/viewers, native fact admission, release/install/runtime activation and unrelated source/structure work out of scope. Work is direct without MCP/FPF under the retained Operator instruction; that does not weaken governed live-write gates or claim a Run/Journal receipt.

One integration owner controls shared-state changes and Git. Parallel workers may own disjoint source reviews, implementation modules or tests. Own-work Tasks fit at most 15 minutes; group Epics have no own implementation work and must gain bounded child Tasks before execution. The BLOCKS Relations, not navigation numbers or Active Status, determine readiness. Scratch/cache files belong in `.caprmedio_tmp`.

### Decomposing Plans

- [CA-P-1960 — Define safe Subject Tool contracts](18-CA-P-1959-EPIC--improve-entity-model-stage-2/01-CA-P-1960-TASK--define-safe-subject-tool-contracts.md)
- [CA-P-1961 — Implement field-aware Subject lookup](18-CA-P-1959-EPIC--improve-entity-model-stage-2/02-CA-P-1961-TASK--implement-field-aware-subject-lookup.md)
- [CA-P-1962 — Implement sealed Subject patch previews](18-CA-P-1959-EPIC--improve-entity-model-stage-2/03-CA-P-1962-TASK--implement-sealed-subject-patch-preview.md)
- [CA-P-1963 — Verify Subject Tools on isolated fixtures](18-CA-P-1959-EPIC--improve-entity-model-stage-2/04-CA-P-1963-TASK--verify-subject-tools-on-isolated-fixtures.md)
- [CA-P-1964 — Resolve the Subject grammar cutover boundary](18-CA-P-1959-EPIC--improve-entity-model-stage-2/05-CA-P-1964-TASK--resolve-the-subject-grammar-cutover-boundary.md)
- [CA-P-1965 — Support the approved Subject grammar in Tools](18-CA-P-1959-EPIC--improve-entity-model-stage-2/06-CA-P-1965-TASK--support-the-approved-subject-grammar-in-tools.md)
- [CA-P-1966 — Map current Core Subject origins](18-CA-P-1959-EPIC--improve-entity-model-stage-2/07-CA-P-1966-EPIC--map-current-core-subject-origins.md)
- [CA-P-1967 — Seal the exact Subject migration preview](18-CA-P-1959-EPIC--improve-entity-model-stage-2/08-CA-P-1967-TASK--seal-the-exact-subject-migration-preview.md)
- [CA-P-1968 — Apply approved Subject migration batches](18-CA-P-1959-EPIC--improve-entity-model-stage-2/09-CA-P-1968-EPIC--apply-approved-subject-migration-batches.md)
- [CA-P-1969 — Verify Subjects before content updates](18-CA-P-1959-EPIC--improve-entity-model-stage-2/10-CA-P-1969-TASK--verify-subject-migration-before-content-updates.md)
- [CA-P-1970 — Align Atom content after Subject migration](18-CA-P-1959-EPIC--improve-entity-model-stage-2/11-CA-P-1970-EPIC--align-atom-content-after-subject-migration.md)
- [CA-P-1971 — Verify the Stage 2 entity model](18-CA-P-1959-EPIC--improve-entity-model-stage-2/12-CA-P-1971-TASK--verify-the-stage-2-entity-model.md)

### Definition of Done

The Epic is **not** Done if any decomposing Plan is not Done, Subject origins remain unaccounted for, a source effect lacks exact approval or current pins, Step 2 began before complete Step-1 verification, ordinary content changed during the Subject cutover without the approved minimum grammar exception, required history/records are missing, validation or graph reproduction fails, or completion claims exceed the actual evidence.
