---
artifact_type: assurance
artifact_subtype: qa_case
artifact_id: DSET-EVALUATION-CASE-GOV-036
scope_path: layer:gov
subject_scopes:
  - assurance
priority: medium
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - DSET-EVALUATION-CASE-GOV-028
  - type: check_of
    targets:
      - DSET-REQUIREMENT-GOV-098
      - DSET-REQUIREMENT-GOV-102
      - DSET-REQUIREMENT-GOV-112
---

# QA Case — Project-settings usability

## Claim checked

An operator unfamiliar with the repository can configure reporting mode,
artifact strictness, and one enabled artifact Type using only
`.dset/dset_settings.toml` and its in-file documentation.

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
