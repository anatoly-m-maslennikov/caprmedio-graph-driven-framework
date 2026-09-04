---
artifact_subtype: problem
subject_scopes:
  - artifact-catalog
priority: medium
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
---

# Problem — Active deltas and accepted truth reuse IDs inconsistently

The active 0.3 Change formerly retained pre-layer IDs whose accepted owners now used those IDs differently. The live delta, manifest, proof plans, solution landscape, and verification now reference the current accepted layer-owned IDs and retain only genuinely unaccepted deltas.

## Migrated context

- Original intake status: `resolved`
- Original owner Change: `CAPRMEDIO-CHANGE-SKILL-001`
- External references: https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/pull/9

This one-claim carrier replaces the former aggregate intake row. Current
status is derived from atomic lifecycle events.
