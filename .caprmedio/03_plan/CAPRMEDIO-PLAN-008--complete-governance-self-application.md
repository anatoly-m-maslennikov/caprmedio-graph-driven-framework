---
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 1
updated_at: 2026-08-17 07:51:33
---
# Complete governance self-application

1. Backfill every existing Atom with frontmatter `version` and `updated_at` values while preserving stable filenames; complete when every Atom conforms to GOV-194.
2. Update Atom creation and mutation mechanisms to write `version` and `updated_at` and to increment them under GOV-194; complete when newly created and revised Atoms conform without manual repair.
3. Rebuild every existing Projection with `updated_at` through the journal-backed rebuild flow; complete when every Projection conforms to GOV-199 and every rebuild is recorded under META-211 and GOV-206.
4. Preserve existing `technical_decision` Method Atoms until the operator activates their deferred migration, then migrate them to the current Method subtype model without changing accepted meaning.
5. Implement proof-currentness derivation and generate its Catalog; complete when governed proof dependency frontiers deterministically produce `current`, `stale`, or `unknown` results under GOV-190 and GOV-191.
