---
artifact_type: evaluation_plan
artifact_id: CARMADIO-EVALUATION-CASE-GOV-029
scope_path: layer:gov
subject_scopes:
  - assurance
priority: medium
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: check_of
    targets:
      - CARMADIO-DECISION-GOV-019
      - CARMADIO-DECISION-OPS-007
  - type: replacement_of
    targets:
      - CARMADIO-EVALUATION-CASE-GOV-019
      - CARMADIO-EVALUATION-CASE-OPS-010
---

# Evaluation Case — Interpret the Version artifact Type

Give independent reviewers the current artifact catalog, filenames, and short
artifact examples without explaining the former name. Pass only when every
reviewer identifies Version as the release-lifecycle Type; assigns Roadmap,
Version Scope, Change, Release Plan, Readiness Record, and Release Record as
flat direct subtypes; preserves their distinct roles; and does not confuse the
Type with product-version strings, source-control versions, deployment state,
or semantic Decision Types.

Record ambiguity and rival interpretations. A majority vote does not conceal
one materially different classification; reconcile it or keep the Evaluation
inconclusive.

This emitted Evaluation atom is immutable. Later correction requires a
successor Evaluation and append-only lifecycle event.

## Primary claim

Independent reviewers can correctly interpret Version and assign all six release-lifecycle artifacts without needing an additional explanation of the primary Type name.


## Historical frontmatter metadata

```yaml
promotion:
  affected_children:
    - "gov"
    - "ops"
  applies_unchanged: false
  local_context_required: true
  parent_scope:
    kind: "project"
    id: "dset-specs-loops-framework"
```
