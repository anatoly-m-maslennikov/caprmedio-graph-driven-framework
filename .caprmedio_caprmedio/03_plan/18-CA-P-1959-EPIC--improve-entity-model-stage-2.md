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
version: 13
updated_at: "2026-10-11 03:59:01 +0400"
relations: {}
---
# Summary

Improve entity model — Stage 2

## Objective

The Core Meta-model has consistent Entity origins in RMEDO Subjects, then consistent Summary, Substance, Scope and Details, in that order.

## Details

### Order

1. Review and update RMEDO for the Subject Tools; independently verify it.
2. Compile the reviewed Tool contracts, then build and verify the safe lookup and patch-preview Tools.
3. Map and migrate authoritative Core RMEDO Subjects, then rebuild and verify the graph.
4. Only after the complete Subject gate passes, update Core Summary, Substance, Substance Scope and Details.
5. Verify the final sources and reproducible graph.

The Operator added CA-P-1978 as the first Task: review and update the Tools' Requirements, Methods, Evaluations, Delivery and Operations before implementation. This exception covers only Tool-governing RMEDO in their declared Engine Scope Units. Core entity-model Subjects, grammar and ordinary content stay behind their existing gates. Creating or updating this Epic records work; it does not execute the repair or migration.

### Source and model boundary

- Select Core Meta-model by itself, not Core plus Project Configuration or Extensions. The current declared authoring root is `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL`. Reopen `project_structure.toml` before execution and pin the actual current original sources. Delivered/installed/Applicable Methodology copies are not editable authority.
- Step 1 concerns R, M, E, D and O Subjects: `governs` and `depends_on`. Scope ownership and Substance applicability stay distinct. Atom incidence is not a native Entity or Term relation.

- For the later Core Subject migration, the allowed roles are exactly Requirement, Method, Evaluation, Delivery and Operations. Report Concern, Analysis, Plan and other roles as excluded. Check both the declared Core source path and `current_scope_unit: CORE_META_MODEL`; a mismatch is a finding, not a silent inclusion or exclusion. CA-P-1978 and its children instead select the declared Engine Tool Scope Units and their actual owning scope; the Core filter does not apply to that Tool-RMEDO repair.
- The seven candidate roots are Artifact, Scope Unit, Actor, Relation, Revision, Carrier and Execution. Dependent Entities belong to their owner lifecycle. Candidate display paths, temporal display groups and pseudocode are not automatically native grammar.
- Keep the captured review frozen at commit `a971d0e00c33c779f485fc8cad63194894d440fb`. The [candidate](../_projection/core-entity-review/presentation/operator.entity-graph.candidate.json) and [consolidated review](../_projection/core-entity-review/consolidated/contract.md) guide decisions; they do not replace live source pins. Their 442 display proposals are not executable replacements, and 149 follow-ups must not be guessed or hidden.
- Latest Operator input wins. Use the existing 90% threshold: investigate missing evidence; ask only when a concrete unresolved decision remains below it.

The Operator clarified: Atom.Substance is the shared field; Claim, Question and Issue are labels, not separate dependent Entities or allowed values. Preserve the owning Atom's Content Role. Exact Atom/Claim can map to Atom.Substance where it refers to primary content; compound paths retain their separate owner/domain checks. CA-P-2047 records the actual answer as an additional pinned decision, without rewriting the frozen review inputs. Rename body labels later, in Step 2.

### Simple execution boundary

The Operator approved the five-definition grammar exception during Step 1. CA-P-1977 records the actual answer; CA-P-2059 adopts only those exact grammar definitions and their replacement/history effects. All other ordinary content stays in Step 2. Native slash admission and live Subject migration remain separate.

- [CA-P-2059 — Adopt the approved Subject grammar definitions](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/15-CA-P-2059-TASK--adopt-the-approved-subject-grammar-definitions.md)

Reusable Tools operate correct files only: structural Subject lookup and exact pinned Subject-only preview/update. Repair broken carriers and migrate notation with small ad-hoc scripts. Do not build a reusable repair/migration framework. This latest Operator direction narrows the older Tool work below; it does not waive source pins, exact approval or the existing live-write guard. Commit after each completed Task.

### Tool audit and safe cutover

The current audit found that ATOM_SEARCH searches whole-carrier text; ATOM_UPDATE replaces complete frontmatter, and supplying only Subjects loses other metadata. Its standalone apply guard remains intact. The dedicated Subject migration planner is preview-only and currently preserves revision metadata. Recheck these findings as implementation changes.

Lookup must target exact Subject fields and return occurrence/source pins. Preview must use explicit replacements, preserve unrelated bytes and account for Version +1, updated_at, history and Journal effects. No full-frontmatter rewrite, guessed mapping, new unguarded writer or bypass of existing admission is allowed.

Tests must preserve every unrelated frontmatter field and body byte, not just named sections. Use a separately authored expected occurrence/edge ledger; the verifier must not call the producer's graph builder. A deliberate wrong output must fail the check. After grammar support changes, CA-P-1975 rechecks the exact implementation before any final migration preview.

The five-definition grammar exception is approved and adopted by CA-P-2059: / is broader-to-narrower, . is bearer-to-dependent, : remains Property-to-allowed-value, and @ is outside Subject syntax. Current original Subjects remain unchanged. CA-P-1965 must implement the approved profile before the final migration preview. All other body work stays Step 2; native slash admission and selector grammar are not authorized by this exception.

Live application needs a separately approved exact sealed packet, current pins and the existing admitted mutation boundary. Candidate approval and Tool approval are not that packet approval. Changed pins require a fresh preview. Preserve current Atom identities and history; do not delete entities, fabricate relations or rewrite archived history.

For each current Atom update: keep its ID, set Version to exactly old Version +1, use the actual Project-time effect timestamp, keep the new current revision Active and classify the prior revision as Archived history. The sealed packet must define how execution-time metadata is bound and hashed; an illustrative preview timestamp is not an execution receipt. Preserve exact prior contents/versions through Git. An archive Carrier is a historical location, not a second editable source. Journal records identify actual effects/Atom IDs, not duplicate contents; missing required recording prevents success.

### Ownership and reuse

Own work: none. This Epic is completed through its direct decomposing Plans.

Preparation Tasks do not complete a mapping, application or content-update group. Their bounded work children must exist and finish, and the group's real output/effect checks must pass. Waiting for an Operator decision is a gate, not 15 minutes of assigned work.

This Epic owns the Operator's new Subjects-first/content-second sequence. Reuse CA-P-1872's existing builders. CA-P-1909–1912 retain the sole accepted-graph, preview, application and reproduction route: CA-P-1967 prepares its candidate packet only after CA-P-1909 is Done; CA-P-1910 owns the one final approvable sealed preview; CA-P-1968 organizes batches executed only under CA-P-1911's authorized application; CA-P-1969 consumes CA-P-1912's one verification receipt and checks the content-update gate. No second preview approval, source execution or competing completion receipt is created. If this shared route is unavailable or its current gates conflict, stop before the affected stage. Creating this Epic does not close or rewrite those older Plans.

Use MCP only when its advertised, admitted execution capability supports the exact operation. If MCP does not support it, do not use MCP or invent a binding. Use an already admitted, authorized local method if one exists; otherwise report the unsupported operation. Local work must not bypass an MCP-required sealed envelope, approval, source pin or write guard.

Keep the separate Terms graph, MCP delivery, Apps/viewers, native fact admission, release/install/runtime activation and unrelated source/structure work out of scope. Direct authoring and isolated preparation remain without MCP/FPF under the retained Operator instruction. Live writes still require the admitted mutation route and exact approval; if that route is unavailable, stop. No raw internal call, fabricated authorization or Run/Journal receipt is allowed.

One integration owner controls shared-state changes and Git. Parallel workers may own disjoint source reviews, implementation modules or tests. Own-work Tasks fit at most 15 minutes; groups have no own implementation work and must gain bounded child Tasks before execution. BLOCKS records Plan prerequisites; actual Operator decisions/approval, current pins and the admitted route are additional gates. Navigation numbers and Active Status grant no readiness. Scratch/cache files belong in `.caprmedio_tmp`.

Step 2 must classify proposed edits before writing. Current authority requires a new Atom ID when Summary changes; preserve replacement lineage rather than treating that as a same-ID revision. Substance/Scope/Details edits follow their applicable change class. No schema/key rename or waiver of the Summary identity rule is implied by this Epic.

### Decomposing Plans

- [CA-P-1978 — Review and update RMEDO for Subject Tools](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/01-CA-P-1978-TASK--review-and-update-rmedo-for-subject-tools.md)
- [CA-P-1960 — Define safe Subject Tool contracts](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/02-CA-P-1960-TASK--define-safe-subject-tool-contracts.md)
- [CA-P-1961 — Implement field-aware Subject lookup](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/03-CA-P-1961-TASK--implement-field-aware-subject-lookup.md)
- [CA-P-1962 — Implement sealed Subject patch previews](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/04-CA-P-1962-TASK--implement-sealed-subject-patch-preview.md)
- [CA-P-1963 — Verify Subject Tools on isolated fixtures](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/05-CA-P-1963-TASK--verify-subject-tools-on-isolated-fixtures.md)
- [CA-P-1964 — Resolve the Subject grammar cutover boundary](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/06-CA-P-1964-TASK--resolve-the-subject-grammar-cutover-boundary.md)
- [CA-P-1965 — Support the approved Subject grammar in Tools](18-CA-P-1959-EPIC--improve-entity-model-stage-2/07-CA-P-1965-TASK--support-the-approved-subject-grammar-in-tools.md)
- [CA-P-1975 — Verify grammar-aware Subject Tool readiness](18-CA-P-1959-EPIC--improve-entity-model-stage-2/14-CA-P-1975-TASK--verify-grammar-aware-subject-tool-readiness.md)
- [CA-P-1966 — Map current Core Subject origins](18-CA-P-1959-EPIC--improve-entity-model-stage-2/08-CA-P-1966-EPIC--map-current-core-subject-origins.md)
- [CA-P-1967 — Seal the exact Subject migration preview](18-CA-P-1959-EPIC--improve-entity-model-stage-2/09-CA-P-1967-TASK--seal-the-exact-subject-migration-preview.md)
- [CA-P-1968 — Apply approved Subject migration batches](18-CA-P-1959-EPIC--improve-entity-model-stage-2/10-CA-P-1968-EPIC--apply-approved-subject-migration-batches.md)
- [CA-P-1969 — Verify Subjects before content updates](18-CA-P-1959-EPIC--improve-entity-model-stage-2/11-CA-P-1969-TASK--verify-subject-migration-before-content-updates.md)
- [CA-P-1970 — Align Atom content after Subject migration](18-CA-P-1959-EPIC--improve-entity-model-stage-2/12-CA-P-1970-EPIC--align-atom-content-after-subject-migration.md)
- [CA-P-1971 — Verify the Stage 2 entity model](18-CA-P-1959-EPIC--improve-entity-model-stage-2/13-CA-P-1971-TASK--verify-the-stage-2-entity-model.md)

### Definition of Done

The Epic is **not** Done if any decomposing Plan is not Done; Tool implementation began before CA-P-1978's RMEDO repair and independent verification passed; Subject origins remain unaccounted for; a source effect lacks exact approval or current pins; Step 2 began before complete Step-1 verification; ordinary Core entity-model content changed during Step 1 or grammar-body changes exceeded the exact approved exception; required history/records are missing; validation or graph reproduction fails; or completion claims exceed the actual evidence.
