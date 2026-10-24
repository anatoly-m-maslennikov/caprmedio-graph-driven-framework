---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: plugin-packaging
  depends_on: []
version: 8
updated_at: 2026-10-24 00:51:05 +0400
relations:
  evaluation_for:
  - CA-M-151
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-289@8
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: APPS
---
# Reject one invalid Codex plugin package

## Claim checked

A Codex plugin package **contains** a coherent manifest, contained relative references, **and** matching marketplace entry.

## Test case

Build one package whose manifest names a missing packaged capability.

## Acceptance criteria

Package validation rejects it **before** marketplace publication **or** installation.

## Failure disposition

Stop packaging **and** report the missing **or** inconsistent carrier.
