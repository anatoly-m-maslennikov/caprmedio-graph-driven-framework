---
atom_id: CA-E-509
ref_id: CA-E-509
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Validation
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Property
  - Subject/CAPRMEDIO/Carrier/File.YAML Frontmatter
tier: 2
relations:
  evaluation_for:
  - CA-D-478
  - CA-D-485
  - CA-R-1136
status: Active
version: 14
updated_at: 2026-10-27 19:59:36 +0400
carrier_destination:
  file:
    name: CA-E-509-TOOLS-EVAL_CASE--validate-required-defaults-and-optional-overrides.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/06_evaluation
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Summary

Validate required defaults and optional overrides

## Claim

the Carrier validation Tool **must** preserve the distinction between a required defaulted Atom value **and** an optional inherited-setting override under CA-D-485.

- accept a required internally carried value equal **to** its registered default; reject its omission rather than rejecting its presence as redundant.
- accept an unselected absent override **and** a selected explicit override that currently equals the inherited value; change the upstream setting **and** verify that **only** the unselected override follows inheritance.
- reject the same Property maintained independently **in** frontmatter **and** body.
- a CLI failure identifies the Property **and** violated encoding rule with a non-zero exit **without** rewriting source values.
