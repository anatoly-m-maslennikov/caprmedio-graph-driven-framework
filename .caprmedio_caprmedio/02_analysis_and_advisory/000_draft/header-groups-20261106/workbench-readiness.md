# Workbench Header readiness — 2026-11-06

**Prior packet (`identity.atom_id`): nested Header implementation verified. Latest target (`identity.id`): HOLD pending the rebased handoff and shared-reader compatibility review. Installed runtime: still old; no live cutover is ready.** This is an implementation/report artifact, not source migration, native Workflow admission or deployment approval. UI work is not a Header cutover gate.

## Confirmed implementation

- Nested and historical flat Headers use the shared semantic read view for typed ID, Version, Status, Role, Form and Tier. The actual raw Header mapping stays intact for SQL projection.
- Nested Topics and Container produce direct and derived graph facts. Declaration-directory moves invalidate cached structure; symlink replacements evict old cached source rows; watcher paths reject traversal outside the selected root.
- Focused reader, relation and watcher regressions pass. The new nested-reader module has five passing cases; existing reader/relation/watcher modules have 23/10/7 passing cases.
- Header SQL columns derive from all observed value-bearing raw Header paths. Flat atom_id becomes header_atom_id; nested identity.atom_id becomes header_identity_atom_id. No short aliases are retained. One header_relations JSON column remains materialized from native graph facts.
- Content SQL columns derive from Current model Declarations, with dots between levels and snake_case segments: content.claim.formal_claim. No handwritten property list remains. The compiler is limited to admitted literal Content declarations/applicability, not arbitrary CFEL evaluation.
- Runtime schema assets live beside the Workbench projection database. New populated or globally empty Header columns and actual Content schema/rule changes trigger full capture/replacement; ordinary value edits remain incremental. Declaration provenance-only changes update the asset without replacing tables. Header/Content and QueryStore/Service focused checks pass; combined checks are ongoing.
- Eight owned RMED Drafts are indexed in .caprmedio_tmp/workbench/header-sql-column-names/drafts.json. Independent Draft review passed. Current RMED, native MODEL, live Headers, Journals and the deferred standalone-chat bridge were not changed by this lane.

## Narrow Header cutover verdict

The following verification applies to the prior nested Header packet using `identity.atom_id`:

- Typed nested identity/state/Tier and flat-history compatibility pass.
- Nested Topics/Container direct-and-derived graph extraction passes.
- Generated Header/Content SQL and native query checks pass.
- The compiler supports both legacy Header.Role/Form and grouped Header.Context.Role/Form selectors. An in-memory test of the real prepared migration transform preserves the exact Content schema shape.
- The Operator-approved shared-reader alias correction is applied. All 24 shared Scope Unit tests pass; the actual Project plus 46 child Scope Units load without source edits.
- A read-only full-current-project verification passes: 4,969 indexed Atoms, 47 Scope Units, 46 Header columns, and the five declaration-derived Content columns. Capture took 13.742 seconds; capture/materialization/native database load/query proof took 25.310 seconds. Evidence: .caprmedio_tmp/workbench/header-sql-column-names/current-source-proof.json.
- The two blockers found by that proof are fixed: cold inventory no longer repeatedly scans 77k archived Markdown paths against every role root, and case-colliding native Relation labels warn and omit all ambiguous types under the existing policy rather than crashing DuckPGQ. Sources are unchanged; raw Header facts remain private and intact.

**The remaining live-cutover prerequisite is the installed runtime.** Docker inspect confirmed the running MCP still uses sha256:86fe6c76e0f3abb8679dd37c9cf68e8035f86a8cfe268e3b9f85c9d7a18a719b. Working-tree code checks do not update that image. Do not group live Headers while that old Workbench indexer continues reading them. UI tests, compact layout and unrelated release checks are not Header source-code gates.

Workbench host checks pass (138 tests; the live canary stays opt-in), and native MCP/HTTP Workspace E2E passes (7 tests). This report does not claim full-repository green, deployment or native Workflow admission.

## Separate follow-up evidence

- The live-project canary is implemented as an explicit opt-in test. Its initial dry preflight exposed the shared-reader bug before writing any source; that bug is now fixed. Expanded all-operation canary rehearsal remains separate. No temporary live Scope Unit or Atom was created.
- Current literal model Declarations compile five Content columns: summary, claim.formal_claim, claim.prose_claim, semantics and details. TLDR and the older Analysis/Plan fields lack current literal declarations; their source-model additions are outside this Workbench implementation. No implicit fallback columns were invented.
- Compact UI, independent Interface/Content text zoom, source-newline display and muted type labels are implemented. Frontend workspace tests and build pass; browser E2E is running against a disposable fixture endpoint and is not a Header migration gate.
- No full-repository green result, release, deployment, commit, push or live Header cutover is claimed.

## New source-lane identity decision

CA #5 reports a newer direct Operator decision: serialized nested identity must use `identity.id`, alongside `identity.ref_id`, rather than `identity.atom_id`. Its previous migration packet is not eligible for live application until rebased. Header SQL generation naturally follows raw paths (`header_identity_id`), but the shared semantic identity reader and typed consumers must be reviewed/tested against that new key. No new implementation was requested in that heads-up; this lane has not silently changed shared identity mappings. The earlier READY code result must not be read as approval of the new target.
