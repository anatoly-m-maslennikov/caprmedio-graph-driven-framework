---
subject_scopes:
  - provenance
version: 1
updated_at: 2026-08-17 19:42:05
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-181-represent-accepted-meaning-faithfully
  method_for:
    - CAPRMADIO-REQUIREMENT-GOV-190-bind-proof-records-to-dependency-frontiers
    - CAPRMADIO-REQUIREMENT-GOV-191-generate-proof-currentness-catalog
---
# Encode proof frontiers as typed reference lists

CAPRMADIO must encode a proof carrier's machine-readable dependency frontier as `proof_frontier_refs`, a YAML list whose entries use `atom:<atom-name>@<version>,<updated_at>` for exact Atom revisions or `<kind>:<repository-relative-locator>@sha256:<digest>` for `file`, `configuration`, `evaluator`, and `input` dependencies; an `environment` dependency uses `environment:<name>@sha256:<fingerprint>`, and prose `invalidation_conditions` make currentness `unknown` until a governed checker resolves them.
