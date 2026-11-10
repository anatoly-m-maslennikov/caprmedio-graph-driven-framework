---
atom_id: CA-E-351
ref_id: CA-E-351@17
container:
  scope_unit: CA-SU-20
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Output
    Publication
tier: 2
relations:
  evaluation_for:
  - CA-M-222
status: Archived
version: 17
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: APPS
carrier_destination:
  file:
    name: CA-E-351@17-APPS-EVAL_CASE--render-untrusted-project-content-only-as-data.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/06_evaluation/archive
---
## Summary

Render untrusted project content only as data

## Claim

### Prose Claim

#### Claim checked

An App interface renders untrusted project content safely **without** turning data
into executable authority **or** capability.

#### Test case

Render **every** supported App view with project text containing HTML, script,
URL, style, **and** bidirectional-control payloads.

#### Acceptance criteria

Each value is encoded for its exact output context, executes no active content,
gains no additional capability, **and** remains inspectable as project data.

#### Failure disposition

Reject the rendering boundary **when** **any** payload executes, escapes its output
context, gains capability, **or** becomes unavailable for inspection as data.

#### Sources

- [OWASP Cross Site Scripting Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/02-checklist/05-checklist)
