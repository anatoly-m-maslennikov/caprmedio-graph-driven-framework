---
atom_id: CA-E-275
ref_id: CA-E-275
container:
  scope_unit: CA-SU-21
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
tier: 3
relations:
  evaluation_for:
  - CA-M-169
  derived_from:
  - CA-A-057
status: Active
version: 18
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
---
# Reject one incomplete Tool invocation contract

## Claim checked

MCP exposes **only** a complete coherent canonical descriptor with `schema_version: 1`.

## Test case

Validate one Tool descriptor missing a required CA-D-621 field beside one complete Tool descriptor. Repeat with a handwritten duplicate input schema, an unresolved callable entrypoint, and a missing Action binding.

## Acceptance criteria

The defective Tool returns a field-level unavailable diagnostic and produces no eligible projection. The independent complete Tool remains eligible. The harness proves models are imported from canonical symbols and that validation never invokes or applies either Tool.

## Failure disposition

Stop exposure of the affected descriptor **until** its contract is complete, canonical-model-derived, **and** unambiguous.
