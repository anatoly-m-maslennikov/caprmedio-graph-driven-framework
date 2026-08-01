---
artifact_type: assurance
artifact_subtype: qa_case
artifact_id: DSET-EVALUATION-CASE-GOV-040
scope_path: layer:gov
subject_scopes:
  - assurance
priority: medium
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - DSET-EVALUATION-CASE-GOV-039
  - type: check_of
    targets:
      - CARMADIO-REQUIREMENT-META-100
      - CARMADIO-REQUIREMENT-META-067
      - CARMADIO-REQUIREMENT-META-096
---

# QA Case — Current scope and layer distinction

## Claim checked

An operator can distinguish horizontal scope ownership, nested structural
scope, forward-only layer authority, and an invalid backward dependency.

## Applicable conditions

Representative structures include horizontal peer contracts, forward-only
ordered authority, nested Scope paths, and unavoidable backward dependencies.

## Acceptance criteria

At least 90% of classifications:

- classify horizontal ownership as peer scopes or features;
- classify ordered downstream authority as layers;
- preserve the current META → GOV → SPEC → PROFILES → IMPL → OPS direction;
  and
- treat irreducible backward dependency as a reason to stop claiming a clean
  layer model.

## Failure disposition

Record a Concern for every repeated ambiguity and stop topology-readiness until
the governing distinction or its presentation is corrected.
