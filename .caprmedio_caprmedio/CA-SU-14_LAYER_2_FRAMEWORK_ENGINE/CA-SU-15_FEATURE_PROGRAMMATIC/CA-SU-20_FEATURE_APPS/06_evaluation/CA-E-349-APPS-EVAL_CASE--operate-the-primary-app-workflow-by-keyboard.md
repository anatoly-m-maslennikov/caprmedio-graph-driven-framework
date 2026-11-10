---
atom_id: CA-E-349
ref_id: CA-E-349
container:
  scope_unit: CA-SU-20
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Interaction <+ Accessibility
tier: 1
status: Active
version: 17
updated_at: "2026-11-11 00:07:48 +0400"
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: APPS
carrier_destination:
  file:
    name: CA-E-349-APPS-EVAL_CASE--operate-the-primary-app-workflow-by-keyboard.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/06_evaluation
---
## Summary

Operate the primary App workflow by keyboard

## Claim

### Prose Claim

#### Claim checked

the primary App workflow remains operable **without** specialist craft work **or** a
pointer-only interaction.

#### Test case

Complete the primary Operator workflow using **only** a keyboard. Record the
browser **and** assistive-technology boundary used; automated checks **may** support
but cannot replace this interaction case.

#### Acceptance criteria

Focus is visible, control names **and** roles are meaningful, traversal order is
predictable, status changes are announced, error recovery is reachable, **and** no
required action is pointer-only.

#### Failure disposition

Reject the App workflow **when** **any** required action, status, **or** recovery path is
unavailable **or** ambiguous through keyboard operation.

#### Sources

- [Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/)
- [Understanding WCAG 2.2](https://www.w3.org/WAI/WCAG22/understanding/)
