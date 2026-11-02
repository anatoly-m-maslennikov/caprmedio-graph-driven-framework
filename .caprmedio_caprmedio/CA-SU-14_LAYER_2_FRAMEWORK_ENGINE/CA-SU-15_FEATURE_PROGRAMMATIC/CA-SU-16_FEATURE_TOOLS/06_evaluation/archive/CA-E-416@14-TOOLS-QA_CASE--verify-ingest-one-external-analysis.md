---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Ingest External Analysis
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Continuant/Term//Artifact
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Analysis'
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Artifact/Revision
version: 14
updated_at: 2026-10-24 05:56:25 +0400
relations:
  evaluation_for:
  - CA-R-1145
  - CA-O-035
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-416@14
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
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
