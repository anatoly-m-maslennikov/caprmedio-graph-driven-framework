---
atom_id: CA-M-206
ref_id: CA-M-206
container:
  scope_unit: CA-SU-16
role: Method
form: Eng Policy
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
tier: 2
relations:
  method_for:
  - CA-R-1128
  derived_from:
  - CA-A-058
status: Active
version: 18
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Project bounded Work Journal NDJSON to TOON

## Applicable when

use this Method **when** a bounded Work Journal frontier **must** be represented as a compact TOON Projection.

## Procedure

1. resolve an exact Journal file, event range, **or** sealed event frontier **and** record its ordered source identities **and** digests.
2. parse **every** NDJSON line strictly **and** reject malformed, duplicate, **or** changed input **before** projection.
3. encode the same ordered event values into TOON **without** adding authority, interpretation, **or** omitted fields.
4. attach the source frontier, encoder identity **and** version, **and** output digest **to** the Projection metadata.
5. decode **or** independently compare the result **to** prove lossless identity, value, **and** order preservation.

## Outcome

one reproducible non-authoritative TOON Projection represents the exact bounded Journal frontier losslessly.

## Failure or stop

produce no Projection **when** the frontier changes during generation, **any** line is malformed, **or** the result cannot be proven lossless.
