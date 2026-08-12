---
artifact_type: evaluation_plan
artifact_id: CARMADIO-EVALUATION-CASE-GOV-032
scope_path: layer:gov
subject_scopes:
  - assurance
priority: medium
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: check_of
    targets:
      - CARMADIO-REQUIREMENT-GOV-043
  - type: replacement_of
    targets:
      - CARMADIO-EVALUATION-CASE-GOV-031
---

# Evaluation Case — Interpret the three state boundaries

Give independent reviewers a repository tree including hidden entries and the
governing description. Pass when they consistently identify:

- `.carmadio/` as committed project control truth;
- `.carmadio_runtime/` as ignored but resumable project-local operational state;
- `/tmp` on POSIX, or the native Windows temporary root, as disposable process
  scratch; and
- same-directory atomic swap state as a bounded publication mechanism rather
  than durable runtime or governance.

Record ambiguity instead of resolving it by majority vote. This Evaluation
atom is immutable; later correction requires a successor Evaluation and an
append-only lifecycle event.

## Primary claim

A reviewer can distinguish committed DSET control truth, ignored resumable runtime state, and disposable process scratch from the repository tree and governing text.
