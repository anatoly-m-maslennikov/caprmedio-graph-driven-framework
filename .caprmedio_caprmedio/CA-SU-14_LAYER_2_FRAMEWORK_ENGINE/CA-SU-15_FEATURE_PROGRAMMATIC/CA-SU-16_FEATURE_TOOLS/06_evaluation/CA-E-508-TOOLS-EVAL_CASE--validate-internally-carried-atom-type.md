---
cce_version: cce_1
cce_form: evaluation
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Type
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Type
  - Subject/CAPRMEDIO/Carrier
version: 14
updated_at: 2026-10-27 19:59:36 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-D-478
  - CA-D-480
  - CA-R-1136
atom_id: CA-E-508
ref_id: CA-E-508
status: Active
role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
form: Eval Case
tier: 2
container:
  scope_unit: CA-SU-16
carrier_destination:
  file:
    name: CA-E-508-TOOLS-EVAL_CASE--validate-internally-carried-atom-type.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/06_evaluation
---
# Summary

Validate internally carried Atom Type

## Claim

the Carrier validation Tool **must** accept a valid Atom Type carried inside its Markdown file under the applicable Delivery schema **and** reject missing required **or** contradictory representations.

- parse the carried Type without using a filename Type token as its source; a matching token is a valid representation, **not** prohibited duplication.
- remove the required internal value while leaving a valid filename token: reject the Atom.
- alter the token so that it disagrees with the carried Type: reject the mismatch **without** silently selecting the address value.
- a CLI failure reports the affected Property **and** Carrier with a non-zero exit; the Tool **must not** repair the source as part of validation.
