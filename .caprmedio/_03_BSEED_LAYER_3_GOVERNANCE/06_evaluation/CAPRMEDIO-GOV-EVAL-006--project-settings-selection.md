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
    - CAPRMEDIO-GOV-EVAL-027--canonical-settings-selections-test-case
  check_of:
    - CAPRMEDIO-GOV-REQU-294--interaction-reporting-mode-setting
    - CAPRMEDIO-GOV-REQU-385--resolve-artifact-routes-from-governed-authority-and-project-settings
    - CAPRMEDIO-GOV-REQU-302--atomic-admission-and-promotion-gate
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---

# Canonical project-settings selection

## Claim checked

Project settings accept exactly the registered values, resolve deterministically,
and fail closed on invalid or unknown selections.

## Applicable conditions

1. Load `.caprmedio/caprmedio_project_settings.toml` with documented defaults.
2. Accept only enabled catalog types, subtypes, and Governance loci.
3. Accept only `medium` or `high` artifact creation strictness.
4. Accept only `silent` or `verbose` interaction reporting.
5. Reject unknown keys when the governing schema marks their table closed.
6. Confirm a second parse produces identical effective settings.

## Acceptance criteria

Every valid selection resolves deterministically and every invalid selection
fails closed with the exact key and allowed values.

## Failure disposition

Record a Concern naming the accepted invalid value, rejected valid value, or
non-deterministic result and stop settings-schema readiness.
