---
atom_id: CA-E-319
ref_id: CA-E-319
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Serialization"
tier: 3
relations:
  evaluation_for:
  - CA-M-201
status: Active
version: 20
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Verify normalize portable repository text bytes

## Claim checked

CA-M-201 produces one semantic-preserving **and** byte-idempotent representation of supported repository text.

## Applicable when

apply whenever the repository text-normalization policy **or** normalizer implementation changes.

## Test case

prepare equivalent supported text files with mixed line endings, optional byte-order marks, different final-newline states, **and** one undecodable file. normalize the supported files twice **and** compare decoded text **and** bytes.

## Acceptance criteria

**all** supported variants become byte-identical while decoded semantic text is preserved; the second pass changes no bytes; the undecodable file is rejected **and** remains byte-identical **to** its input.

## Failure disposition

reject the realization **and** preserve policy version, input **and** output digests, decoded comparisons, second-pass result, **and** rejected-file bytes.
