# Workbench Header readiness — 2026-11-06

**Live source-cutover verdict: NOT READY.** This is an implementation/report artifact, not source migration, native Workflow admission or deployment approval. UI work is not a Header cutover gate.

## Confirmed implementation

- Nested and historical flat Headers use the shared semantic read view for typed ID, Version, Status, Role, Form and Tier. The actual raw Header mapping stays intact for SQL projection.
- Nested Topics and Container produce direct and derived graph facts. Declaration-directory moves invalidate cached structure; symlink replacements evict old cached source rows; watcher paths reject traversal outside the selected root.
- Focused reader, relation and watcher regressions pass. The new nested-reader module has five passing cases; existing reader/relation/watcher modules have 23/10/7 passing cases.
- Header SQL columns derive from all observed value-bearing raw Header paths. Flat atom_id becomes header_atom_id; nested identity.atom_id becomes header_identity_atom_id. No short aliases are retained. One header_relations JSON column remains materialized from native graph facts.
- Content SQL columns derive from Current model Declarations, with dots between levels and snake_case segments: content.claim.formal_claim. No handwritten property list remains. The compiler is limited to admitted literal Content declarations/applicability, not arbitrary CFEL evaluation.
- Runtime schema assets live beside the Workbench projection database. New populated or globally empty Header columns and actual Content schema/rule changes trigger full capture/replacement; ordinary value edits remain incremental. Declaration provenance-only changes update the asset without replacing tables. Header/Content and QueryStore/Service focused checks pass; combined checks are ongoing.
- Eight owned RMED Drafts are indexed in .caprmedio_tmp/workbench/header-sql-column-names/drafts.json. Independent Draft review passed. Current RMED, native MODEL, live Headers, Journals and the deferred standalone-chat bridge were not changed by this lane.

## Concrete blockers for live cutover

1. **Shared Scope Unit reader creates false Subject ambiguity.** Current root CA-R-2640 has only topics.main_subject, and no physical subjects key. carrier_read_view adds equal legacy subjects.active/governs aliases; scope_declaration_parse._metadata mistakes their presence for conflicting authored values. Do not repair valid source data. The proposed one-line fix accepts equal aliases while rejecting unequal values. Tested only in memory, it loads the Project and all 46 declared child Scope Units. Shared code is unchanged pending Operator approval. Evidence and prepared patch: .caprmedio_tmp/workbench/live-canary/{reader-ambiguity-proof.json,scope-alias-fix-proof.json,scope-alias-fix.patch}.
2. **Installed runtime is still the old image.** Docker inspect confirmed the running MCP image is sha256:86fe6c76e0f3abb8679dd37c9cf68e8035f86a8cfe268e3b9f85c9d7a18a719b. The new reader/schema implementation has not been installed. Do not infer live readiness from working-tree tests.
3. Complete the combined backend/query verification after cached Content validation integration. Browser UI refinements do not gate native source grouping.

## Separate follow-up evidence

- The live-project canary is implemented as an explicit opt-in test. Its dry preflight stopped at the shared-reader bug before writing any source. No temporary live Scope Unit or Atom was created.
- Current literal model Declarations compile five Content columns: summary, claim.formal_claim, claim.prose_claim, semantics and details. TLDR and the older Analysis/Plan fields lack current literal declarations; their source-model additions are outside this Workbench implementation. No implicit fallback columns were invented.
- Compact UI, independent Interface/Content text zoom, source-newline display and muted type labels are implemented. Frontend workspace tests and build pass; browser E2E is running against a disposable fixture endpoint.
- No full-repository green result, release, deployment, commit, push or live Header cutover is claimed.
