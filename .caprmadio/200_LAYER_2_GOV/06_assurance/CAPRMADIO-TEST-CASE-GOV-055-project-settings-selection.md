---
artifact_type: assurance
artifact_subtype: qa_case
artifact_id: CAPRMADIO-TEST-CASE-GOV-055
scope_path: layer:gov
subject_scopes:
  - assurance
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-TEST-CASE-GOV-039
  - type: check_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-098
      - CAPRMADIO-REQUIREMENT-GOV-102
      - CAPRMADIO-REQUIREMENT-GOV-112
---

# Canonical project-settings selection

## Claim checked

Project settings accept exactly the registered values, resolve deterministically,
and fail closed on invalid or unknown selections.

## Applicable conditions

1. Load `.caprmadio/caprmadio_settings.toml` with documented defaults.
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
