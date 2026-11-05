---
atom_id: CA-P-2707
ref_id: CA-P-2707
role: Plan
form: Plan
label: Task
status: Active
version: 10
updated_at: 2026-11-05 18:04:53 +0400
tier: 4
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
carrier_destination:
  file:
    name: 12-CA-P-2707-TASK--verify-declaration-source-cutover.md
    path: .caprmedio_caprmedio/03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing
container:
  atom: CA-P-2694
---
## Summary

Verify the Declaration source cutover

## Objective

Verify the final Current Declaration sources and their source consumers. Reconcile source-side authority and identity before carrier admission. CA #3 owns engine implementation/runtime changes, fixtures, regression work and execution of carrier-admission, complete-suite, launcher, Docker and lifecycle checks. Those remain required external dependencies before P2707 or the Epic can be Done.

## Recorded evidence

- Earlier cutover evidence reported 44 Scope Unit Declarations, 43 non-root IDs and nine Ordered units. The 2026-11-05 source snapshot has 46 Current Declarations, 45 unique non-root IDs and nine Ordered units: one old Declaration is archived and three Workbench Declarations were added. All 43 surviving originals have source-backed namespace/wrapping-only differences. Recheck the final stable candidate; this source snapshot does not close runtime gates.
- The live project_structure.toml was retired. Recheck production, bindings, fixtures and documentation for executable dependencies.
- Current D657 replaces retired D274 as live carrier-encoding authority. Its reviewed Claim digest, registry closure and 588 validator tests are recorded in the completion packet.
- The latest reader passed 426 graph tests. Seven MODEL views use Project root ownership and Form + Scope Unit identity.
- Connector and moved-default fixture corrections passed 48 focused tests.
- Earlier whole-suite runs contained concurrent edits and failures. They do not establish a final pass.

## Concrete writer defect — CA #3

The release copy phase reads Authority paths, drops each declared Delivery path, and builds the target from `source.name`. It would recreate the three ID-prefixed directories after the verified physical rename.

Required behavior:

1. Read source bytes from the declared Authority paths.
2. Write each copied subtree to its declared Delivery path, using the existing layout resolver where applicable.
3. Preserve copied file bytes and canonical Authority sources.
4. Verify that the next copy produces `LAYER_1_CORE_META_MODEL`, `LAYER_2_INSTALLED_EXTENSIONS` and `LAYER_3_PROJECT_CONFIGURATION`, without recreating their ID-prefixed siblings.

The static trace is in `coverage/folder-derivation-live-check-20261105/writer-static-audit.json` in the completion packet. CA #3 owns the implementation and focused writer verification, followed by the existing final integration gates. The source lane has made no implementation change.

## Root ID and bootstrap cutover — CA #3

The accepted Project root ID is `CA-SU-00`. `CA-SU--1` identifies the predefined Scope Unit named `world`, without a Declaration. The root Declaration Atom uses `container.scope_unit: CA-SU--1`; the Project Scope Unit itself keeps no formal parent.

The current reader accepts only the root Name statement and identifies the root by an absent ID. Its model/validator rejects a root ID. Before promotion:

1. Accept the root Declaration's ID and preserve both zeroes in `CA-SU-00` as text. Root identity follows the Project kind, not an absent ID. Shared rules support other Project ID namespaces.
2. Resolve `CA-SU--1` to predefined world without requiring or creating a World Declaration, Carrier or folder. Reject a supplied Declaration reusing that reserved ID.
3. Include the Project root in declared-ID uniqueness checks. Keep world separate from the Declaration count: the current baseline is 46 Declarations plus predefined world.
4. Read the one-key `Header.Container` mapping. Resolve base Atom IDs to Current and Scope Unit IDs to the declared or predefined Scope Unit. Apply the omitted-root-Declaration default mapping to world. Store no duplicate containment fact in Relations.
5. Preserve unordered/no-number/no-parent Project behavior and `.caprmedio_<project name>` root naming. Verify the bootstrap Declaration's adapter admission and placement before carrier migration.
6. Keep the source Current until the compatible reader, model, validator and adapter are ready. Verify the coordinated candidate through the existing admission and integration gates below.

The pinned static evidence is `coverage/project-root-id-20261105/static-impact/report.json` in the completion packet. Source Draft writes are not reader acceptance or runtime evidence.

## CFEL and single-person source cutover — CA #3

The reviewed candidate is `coverage/value-relations-20261105/final-live-cohort.json` in the completion packet. Its 49 Drafts are not Current syntax. The Operator requires source-first sequencing: complete and review CFEL, migrate Current and Draft Atoms in place, check that migration, then send CA #3 the implementation handoff. After that handoff, the required compatibility work is:

1. Distinguish HAS_ALLOWED_VALUE (`:=`, OR across applicable and inherited admissions) from HAS_VALUE_CONSTRAINT (`::`, AND across applicable and inherited constraints). With no admissions, omit that group. Preserve qualified-Subject `:=` and `{::n}` allowed cardinalities.
2. Support the accepted typed logical participants, `//` narrowing, `/` containment, scoped IF/THEN and FOR EACH groups, explicit bindings, and `# model` / `# instances`. Remove modeled CFEL Operator descriptor dependencies while preserving Actor/Operator.
3. Implement the final reviewed canonical-Relation and inverse-alias contract. Preserve model references such as Relation//CONTAINS and the declared IS_INVERSE_ALIAS_FOR binding. Keep literal/constraint endpoint domains and zero-default bounds; do not restore separate inverse facts or infer reverse permissions.
4. Implement Atom-owned storage: Header.Relations is the default for outgoing canonical facts about the Atom; IS_CONTAINED_BY uses Header.Container. Header.Relations is optional and stores no inverse alias or duplicate containment. Coordinate the single-person schema/registry changes. Current R1559@28 and E440@38 already govern threshold-and-permission approval; the other attribution and root-ID changes remain staged. Preserve accepted historical records.
5. Use the existing Project-global identity boundary for allocation and application. The repaired value Relation IDs are R2826–R2829; retained history and all statuses reserve IDs. Keep other owners' Workbench sources intact.
6. Record semantic/parser/admission and integration results on one stable candidate through the five checks below. Source receipts and refreshed projections alone do not satisfy them.

## Remaining checks

1. The source lane verifies final Declaration counts, identities, derived paths and source hashes. Explain every digest change from preserved source evidence. CA #3 fixes and verifies the concrete Delivery writer defect above before the final stable-candidate checks.
2. Reconcile the legacy scope-field disposition from Current authority and identify a valid Current execution binding for every required operation. CA #3 owns matching implementation, registry/fixture changes and tests; a retired or archived carrier is not a Current replacement. The missing actual CA-O-104 Review Workflow remains a distinct source-authority issue and cannot be filled by a projection or installed copy.
3. CA #3 verifies live Project admission and fresh Docker query/status and lifecycle checks, including the W10 result/timestamp comparison, on the stable candidate.
4. CA #3 runs the complete current-source suite and launcher on that same stable candidate. Record exact implementation, source and image identities, results and cleanup. These checks remain pending until an actual terminal result is recorded; focused or mixed-state runs do not satisfy them.
5. Preserve the explicit O016 expected-failure disposition under P2708. It does not waive unrelated failures. Actual Workflow-instance migration remains separately deferred; do not conflate it with the missing CA-O-104 source or with the settled Occurrent kind decisions.

## Status

Active. Focused tests and source adoption receipts do not close this gate. No release is required.

## Evidence

- [Current Scope Declaration source census](../../02_analysis/draft/epic-completion-20261104/coverage/scope-declaration-check-20261105/REPORT.md).
- [Integration packet](../../02_analysis/draft/epic-completion-20261104/integration/REPORT.md).
- [Full acceptance matrix](../../02_analysis/draft/epic-completion-20261104/acceptance/matrix.json).
- [Earlier cutover verification](scope-unit-governance-20261031/verification/final-cutover-verification.json).
