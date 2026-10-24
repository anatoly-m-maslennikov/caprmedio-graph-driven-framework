---
atom_id: CA-P-1959@135
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 18
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject
  depends_on: [Subject/Domain/Node/Continuant/Atom, Subject/Domain/Node/Continuant/Scope Unit, Subject/Domain/Node/Continuant/Projection, Subject/Graph/Relation, Subject/Graph/Rule]
version: 135
updated_at: 2026-10-23 01:52:23 +0400
relations: {}
---
# Summary

Improve entity model — Stage 2

## Objective

Complete Candidate #7's methodology migration: Subjects, defining rules, Types, global properties and Atom IDs. Rebuild the affected Subject projections from the actual migrated sources. Keep general content migration separate.

## Details

### Current authority and scope

Use [Candidate #7](../_projection/core-entity-review/presentation/operator.model.candidate-7.md) and the latest Operator decisions. The [application plan](../_projection/core-entity-review/presentation/candidate-7.methodology-application.md) describes the boundary. The [applied increment](../_projection/core-entity-review/presentation/candidate-7.methodology-increment-2026-10-22.md) records actual source changes, not full completion.

This Epic changes methodology source files and Plans only. Direct file edits are authorized for this continuation. Tool implementation, code, implementation schemas, tests, MCP, Settings values, runtime, releases and commits are outside this work. Do not repair a missing tool route to proceed.

Subject is the root. Domain and Engineering are the current topic branches; Graph/Relation and Graph/Rule apply across them. Preserve full paths, classifier values, named instances and inherited properties. UX/Design and exact new Type-to-tier restrictions remain deferred.

Core stays abstract and reusable. Project-specific procedures and choices belong to Project Configuration. Source Atoms, not derived views or delivered copies, hold authority. Keep the PROGRAMMATIC chat's changes intact.

### 2026-10-23 — bounded bare-Tool source cleanup

The Operator authorized source-specific review of 207 bare-Tool owners, including replacement/splitting, tier and Scope Unit changes where justified. Check whether the real Subject is an existing Domain entity; do not introduce a new Domain entity without asking the Operator. This bounded permission does not turn the rest of this Epic into general content migration.

[Applied result](../_projection/core-entity-review/presentation/candidate-7.tool-atom-cleanup-2026-10-23.md): 205 same-ID updates, 153 Type corrections, six ownership/carrier moves and one duplicate retirement, with 206 predecessor archives. Governing Subjects use 91 existing Domain bearers and 114 Engineering topics; no new Domain entity, Summary or Substance was introduced. E567 remains unchanged under PROGRAMMATIC ownership. Independent post-write checks passed.

This is not full completion. Keep the wider legacy dependency mapping, property/ID and filename work, graph rebuild and final verification in the queue. Review O160's concrete-Step ownership separately; it was outside the 207-owner frontier. Do not reuse the earlier worklist's changed source pins as if still current.

### Remaining execution order

1. Refresh current-source mapping worklists and resolve the remaining exact Subjects. Keep source-specific uncertainty and malformed legacy carriers visible. Do not guess from a folder, Content Role or prefix alone.
2. Apply supported Candidate #7 increments: Subjects; required property/ID data; Type classification; needed R/D rule alignment; and filename-token alignment. Review defining-R coverage and add only genuine missing definitions. General Substance rewrites stay outside this Epic.
3. Verify actual effects and rebuild the affected Core, Project Configuration and Engine Subject views from the resulting sources. Preserve unresolved cases in the output; do not hide them to produce a clean-looking tree.
4. Before closing this Epic, re-home the unfinished CA-P-2167 Plan bundle outside this Epic's containment tree. Preserve its IDs, statuses, child bundles and history; update its containment/decomposition reference and affected current links. This is Plan administration, not Tool implementation or a requirement to finish the Tools backlog. The parent's Done cascade must not cancel that independent work.

Mapping, source application and final verification are separate responsibilities. The current mapping worklist is a source-derived planning aid, not a new authority or proof that every canonical-looking path is semantically correct.

### Current task groups

- [CA-P-1966 — Map current Core Subject origins](18-CA-P-1959-EPIC--improve-entity-model-stage-2/08-CA-P-1966-EPIC--map-current-core-subject-origins.md): maintain the current mapping frontier and integrate exact dispositions.
- [CA-P-1968 — Apply approved Subject migration batches](18-CA-P-1959-EPIC--improve-entity-model-stage-2/10-CA-P-1968-EPIC--apply-approved-subject-migration-batches.md): organize the remaining Candidate #7 methodology-source increments, including the approved property, ID and Type work.
- [CA-P-1969 — Verify Subjects before content updates](18-CA-P-1959-EPIC--improve-entity-model-stage-2/11-CA-P-1969-TASK--verify-subject-migration-before-content-updates.md): verify the actual Candidate #7 effects and rebuilt views, not the earlier Candidate #4 batch.
- [CA-P-2167 — Finish Tools before Stage 2 execution](18-CA-P-1959-EPIC--improve-entity-model-stage-2/30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution.md): independent Tools backlog retained for later work. Its historical title does not make it a prerequisite for this direct methodology migration.

General content review/update belongs to CA-P-1970, outside this Epic's completion criteria. No Tools, release, runtime or general content work must be completed merely to close this methodology migration.

### Worklists and evidence

The [remaining Subject worklist](../_projection/core-entity-review/presentation/candidate-7.remaining-subject-worklist.json) and its [reading note](../_projection/core-entity-review/presentation/candidate-7.remaining-subject-worklist.md) replace the old fixed-count research assignments. Read their source boundary and exclusions. A lexical routing lane is not a proposed target Subject. Refresh changed source records before use; do not require unchanged historical rule fingerprints or a fixed global frontier for every independent edit.

The seven mapping lanes are history_actor, content_roles_types, operations, relations_subjects, carrier_storage, methodology_configuration and other. Each remaining occurrence has one routing lane. Canonical-form occurrences and excluded carriers remain separately reported.

Plans are excluded from that bounded specification worklist. This Plan repair updates the retained execution instructions, not every historical Plan's Subjects or mandatory metadata. Include remaining Current Plan metadata and Draft-ID cases in CA-P-1968's separate identity/property worklist before claiming full migration completion.

Record actual changed paths, Versions, predecessor archives and unresolved items. Scratch records and derived views are not Journal events, executed Workflows, commits or runtime acceptance.

### Update and archive rules

Every real Current-Atom update advances Version by one and updates Updated At. Preserve the base ID unless the identity rules require a successor; changing Summary creates a new Atom identity. This one-time migration may correct Type under the same ID when Summary and Substance are unchanged.

Archive the predecessor with Archived Status and its old Version qualifier in its carried ID and filename. Keep the archived numeric Version, Updated At and unrelated content unchanged. Exact-old-bytes preservation is not the archive contract. Git retains the pre-change file history.

Current includes Active, Done, Canceled and Backlog, but excludes Draft and Archived. Current IDs remain unique. Draft and Archived IDs follow Candidate #7's group-qualified forms. Default Atom relations address unsuffixed Current IDs.

Stop the affected increment on failure or uncertainty. Preserve completed effects and the untouched remainder. Do not invent receipts or automatically reset, replay or roll back a batch.

### Completed and canceled work

The first Candidate #7 source increment is applied and checked; its result report lists the actual changes and remaining gaps. It is not full migration completion.

The Operator canceled the outdated Candidate #3/#4 review-packet, sealed-preview and staging chain: 58 Plans, including the CA-P-2193 subtree and CA-P-1967/1973/2188/2189/2190/2191. Their predecessor archives preserve prior results. Canceled tasks do not have to become Done and must not block the retained migration.

Old 611-Atom and 746-Atom migration results remain historical evidence for their own frontiers. They are not Candidate #7 verification. Old Candidate #3/#4 pins, separate sealed-packet approvals, deep per-Atom review packets and Tools-first gates are not current execution prerequisites.

The full former Epic, including historical checkpoints and prior task indexes, is preserved in [CA-P-1959@132](archive/CA-P-1959@132-EPIC--improve-entity-model-stage-2.md). Read it as history, not as another set of current instructions.

## Definition of Done

- All in-scope Candidate #7 Subject, Type, property, ID and defining-rule work has an actual source disposition: applied, unchanged with evidence, or explicitly deferred by the Operator. An unresolved required case prevents completion; do not silently omit it.
- Current identities, group-qualified Draft/Archived identities, mandatory properties, applicable Types, labels and filename rules have been checked against the settled model. Specialized Graph Rule and incomplete-Draft exceptions remain valid.
- Applied updates have the expected Version/time effects and predecessor archives. Intended statuses, ownership and unrelated content are preserved unless the approved increment explicitly changes them.
- The affected Subject projections have been rebuilt from the final actual source frontier, with source Versions and visible limitations. Older saved graphs, mapping candidates and bounded PROGRAMMATIC policy bundles are not substitutes.
- Current mapping/application/verification tasks have their actual outcomes recorded. Canceled tasks and independent Tools backlog are not completion gates.
- Unfinished independent Tools Plans have been re-homed outside this Epic before its Done transition. Do not close this Epic while its containment cascade would cancel them.

Keep this Epic Active until these conditions are met. General content migration, Tools implementation, runtime tests, deployment and release remain separate.
