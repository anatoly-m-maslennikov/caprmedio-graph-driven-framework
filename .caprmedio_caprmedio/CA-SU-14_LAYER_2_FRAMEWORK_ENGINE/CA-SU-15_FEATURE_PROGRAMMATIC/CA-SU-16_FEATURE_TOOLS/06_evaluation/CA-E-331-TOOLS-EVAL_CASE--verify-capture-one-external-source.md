---
atom_id: CA-E-331
ref_id: CA-E-331
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Retrieval
tier: 3
relations:
  evaluation_for:
  - CA-M-213
status: Active
version: 21
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Verify capture one external source

## Claim checked

CA-M-213 captures one immutable external source carrier with complete provenance **and** an explicit reproducibility result.

## Applicable when

apply whenever external-source capture **or** provenance-carrier mechanics change.

## Test case

capture one supplied external text with origin, retrieval time, attribution, **and** content digest. attempt a second capture lacking attribution **and** inspect both outcomes.

## Acceptance criteria

the valid capture creates one immutable carrier whose bytes match its digest **and** records the required provenance **and** reproducibility outcome. the incomplete capture produces no carrier **and** no invented provenance.

## Failure disposition

reject the source-capture method **and** preserve both capture inputs, carrier bytes, digest comparison, recorded provenance, reproducibility result, **and** rejection evidence.
