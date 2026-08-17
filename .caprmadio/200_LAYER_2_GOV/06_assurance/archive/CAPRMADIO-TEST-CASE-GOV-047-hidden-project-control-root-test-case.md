---
artifact_type: test_plan
artifact_id: CAPRMADIO-TEST-CASE-GOV-047
scope_path: layer:gov
subject_scopes:
  - assurance
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: check_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-042
  - type: replacement_of
    targets:
      - CAPRMADIO-TEST-CASE-GOV-046
---

# Test Case — Verify the hidden project control root

Run layout, settings, bootstrap, governance, carrier-transition, runtime,
link, classification, traceability, and full repository tests. Prove that:

1. current discovery selects only `.caprmadio/caprmadio_settings.toml` and schema 1.3;
2. persisted canonical paths resolve from the repository root;
3. fixed layer roots are direct children of `.caprmadio/`;
4. project-wide and Version artifacts resolve through `project/` and
   `versions/`;
5. replaceable operational state is written under ignored `.caprmadio/runtime/`;
6. initialization emits that layout and passes repository validation without a
   follow-up migration;
7. competing current/legacy configuration carriers fail closed; and
8. every immutable relocation remains byte-, semantic-, and
   Git-source-verifiable through the complete registered transition chain.

This Test atom is immutable. Later correction requires a successor Test and an
append-only lifecycle event.

## Primary claim

Deterministic tests prove hidden-root discovery, repository-root-relative canonical paths, runtime-state isolation, direct ownership roots, initialization, migration integrity, and rejection of competing legacy carriers.
