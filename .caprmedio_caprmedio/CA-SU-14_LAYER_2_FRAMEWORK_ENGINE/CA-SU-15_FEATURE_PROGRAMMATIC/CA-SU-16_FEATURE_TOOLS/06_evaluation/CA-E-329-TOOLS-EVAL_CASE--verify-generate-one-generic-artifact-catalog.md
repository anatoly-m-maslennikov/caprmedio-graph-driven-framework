---
cce_version: cce_1
cce_form: evaluation
topics:
  main_subject: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Catalog'
version: 19
updated_at: 2026-11-02 19:44:26 +0400
relations:
  evaluation_for:
  - CA-M-211
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-329
ref_id: CA-E-329
status: Active
role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
form: Eval Case
tier: 3
container:
  scope_unit: CA-SU-16
---
# Verify generate one generic Artifact catalog

## Claim checked

CA-M-211 materializes a deterministic non-authoritative catalog from exactly its declared authority frontier.

## Applicable when

apply whenever a catalog definition, source contribution, **or** generator changes.

## Test case

build one catalog twice from a known declared authority frontier, **then** attempt generation with a source contribution whose required ordering value is unresolved.

## Acceptance criteria

the two valid builds are byte-identical, contain **every** **and** **only** declared source contribution **in** stable order, **and** identify the source frontier **and** generator. the unresolved-ordering case produces no catalog.

## Failure disposition

reject the catalog method **and** preserve definition, source frontier, both derived outputs, unresolved-ordering finding, **and** source-to-output comparison.
