---
atom_id: CA-E-421
ref_id: CA-E-421
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
tier: 3
relations:
  evaluation_for:
  - CA-M-255
status: Active
version: 21
updated_at: 2026-11-02 19:46:47 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Verify rebuild affected Projections

## Claim checked

CA-M-255 derives **every** affected Projection, materializes **only** approved outputs **in** dependency order, **and** verifies currentness **and** idempotence.

## Applicable when

apply whenever affected-Projection derivation, dependency ordering, preview approval, currentness, **or** idempotence handling changes.

## Test case

inspect the registered `PROJECTION_REBUILD` unit, **then** use changed source frontiers that affect one upstream Projection **and** one dependent Projection. preview, approve, **and** rebuild them, **then** rebuild against the unchanged frontier **and** compare outputs; repeat with the dependent Projection omitted from the affected set.

## Acceptance criteria

`PROJECTION_REBUILD` has prefix `PROJECTION_REBUILD`, immediate `TOOLS` owner, `unordered_unit` kind, Structural level `4`, address `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/PROJECTION_REBUILD`, **and** realization path `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/PROJECTION_REBUILD/`. the valid case previews **and** materializes both affected outputs **in** dependency order with source-frontier provenance; the repeated build is identical **and** current. the incomplete affected set produces no accepted publication.

## Failure disposition

reject the realization **and** preserve changed frontiers, dependency graph, preview, approvals, output provenance, repeated-output comparison, **and** incomplete-set finding.
