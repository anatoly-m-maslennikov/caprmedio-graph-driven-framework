---
subject_scopes:
  - settings
version: 3
updated_at: 2026-08-18 07:53:29
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-646--govern-project-settings-projection-through-framework-methodology
    - CAPRMEDIO-META-REQU-166--projections-have-updated-at
    - CAPRMEDIO-META-REQU-627--bind-every-projected-setting-to-exact-source-authority
---
# Encode Project Settings source frontier in TOML

The Project Settings TOML carrier must encode `updated_at`, generator identity and digest, Framework Settings identity and digest, Project Settings Map path, `updated_at`, and digest, source-frontier digest, and exact source Atom references in `[projection]`; it must encode each effective leaf setting key's exact source Atom references in `[projection.bindings]`; and it must keep effective settings in their ordinary TOML tables without a separate manifest or third settings carrier.
