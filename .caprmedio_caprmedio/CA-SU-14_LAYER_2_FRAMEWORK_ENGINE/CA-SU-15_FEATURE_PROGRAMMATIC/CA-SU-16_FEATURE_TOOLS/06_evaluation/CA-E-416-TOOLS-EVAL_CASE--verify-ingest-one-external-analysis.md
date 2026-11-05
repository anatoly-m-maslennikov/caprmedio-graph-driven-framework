---
atom_id: CA-E-416
ref_id: CA-E-416
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Retrieval
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Artifact
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Analysis & Advisory'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Carrier
tier: 2
relations:
  evaluation_for:
  - CA-R-1145
  - CA-O-035
status: Active
version: 23
updated_at: 2026-11-02 15:49:28 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Verify ingest one external Analysis

## Claim checked

CA-O-035 creates an attributable bounded external-Analysis provenance envelope **without** creating **or** revising accepted project authority.

## Applicable when

apply whenever external-Analysis ingestion, provenance-envelope composition, **or** adoption-boundary handling changes.

## Test case

supply one external Analysis with source identity, source digest, transformation session, **and** exact target frontier. ingest it **without** an adoption decision **and** compare accepted project authority **before** **and** **after**; repeat with the target frontier absent.

## Acceptance criteria

the complete case produces one envelope with **every** supplied provenance value **and** marks imported claims non-authoritative. the incomplete case produces no envelope. neither case creates **or** revises accepted project authority.

## Failure disposition

reject the realization **and** preserve source **and** frontier inputs, envelope contents, authority comparison, **and** incomplete-provenance result.
