---
subject_scopes:
  - lifecycle-traceability
version: 3
updated_at: 2026-08-19 07:37:46
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
---
# Move replacement lineage to Journals

1. [x] Apply META-085, GOV-767, and GOV-768 as the current authority boundary: active RMAD represents current state, and historical replacement lineage belongs outside active Atom relations.
2. [ ] Register one append-only replacement Journal event that binds exact predecessor and successor Atom revisions and supports one-to-one, split, merge, and many-to-many replacement transitions.
3. [ ] Inventory every active, draft, done, and archived carrier that contains `replacement_of` before changing any carrier.
4. [ ] Backfill a replacement Journal event for every recoverable historical `replacement_of` declaration before removing that declaration from any mutable carrier.
5. [ ] Remove `replacement_of` from active and draft Atom frontmatter, relation schemas, writers, validators, and active-graph traversal. Preserve done and archived carriers unchanged and treat any embedded legacy declaration as non-authoritative history.
6. [ ] Make lifecycle-folder placement the authority for current lifecycle status and the Work Journal the authority for replacement transitions and successor mapping.
7. [ ] Generate `replaced_by`, inverse replacement views, transitive successor chains, and current-active-successor resolution from Journal events without writing those relations into Atoms.
8. [ ] Regenerate affected Projections and Project Settings from the updated authority and Journal frontier.
9. [ ] Verify that no active or draft Atom declares `replacement_of`, every migrated replacement resolves from the Journal, done and archived carriers remain unchanged, split and merge histories remain traversable, and active authority traversal ignores historical replacement edges.
