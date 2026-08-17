---
artifact_type: evaluation_plan
artifact_id: CAPRMADIO-EVALUATION-CASE-GOV-028
scope_path: layer:gov
subject_scopes:
  - assurance
priority: medium
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: check_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-037
  - type: replacement_of
    targets:
      - CAPRMADIO-EVALUATION-CASE-GOV-027
---

# Evaluation Case — Judge settings discoverability

Without implementation knowledge, cold readers must find every active setting,
accepted value, default, effect, and practical example in
`caprmadio_settings.toml`. They must correctly predict where to change an operator
preference and where to inspect project identity, topology, contracts, release
targets, or verification commands.

At least 90% of representative questions must be answered correctly, with no
authority-source error, no assumption that omitted settings are unavailable,
and no treatment of legacy `dset.toml` compatibility as a writable second
source.

This emitted Evaluation definition is immutable. Execution and evidence are
separate.

## Primary claim

Cold readers can configure DSET from caprmadio_settings.toml and correctly distinguish selectable behavior from project truth and governing definitions.
