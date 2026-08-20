---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-EVAL-014--verbose-project-settings-evaluation-case
  check_of:
    - CAPRMEDIO-GOV-REQU-294--interaction-reporting-mode-setting
    - CAPRMEDIO-GOV-REQU-385--resolve-artifact-routes-from-governed-authority-and-project-settings
    - CAPRMEDIO-GOV-REQU-302--atomic-admission-and-promotion-gate
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---

# Project-settings usability

## Claim checked

An operator unfamiliar with the repository can configure reporting mode,
artifact strictness, and one enabled artifact Type using only
`.caprmedio/caprmedio_project_settings.toml` and its in-file documentation.

## Applicable conditions

The operator has no undocumented framework knowledge and must not edit the
framework catalog.

## Acceptance criteria

Every intended change is made through project settings, and at least 90% of
classifications correctly distinguish project choices from methodology
definitions.

## Failure disposition

Record a Concern for every misleading or missing setting instruction and stop
settings-usability readiness until it is corrected.
