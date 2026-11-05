---
atom_id: CA-E-324
ref_id: CA-E-324
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
tier: 3
relations:
  evaluation_for:
  - CA-M-206
status: Active
version: 19
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Verify project bounded work journal ndjson to toon

## Claim checked

CA-M-206 produces a reproducible lossless TOON Projection of one unchanged bounded Journal frontier.

## Applicable when

apply whenever the Journal-to-TOON encoder, frontier grammar, **or** Projection metadata changes.

## Test case

select a known ordered NDJSON event range, project its unchanged sealed frontier twice, **and** compare decoded values, identities, order, source frontier, encoder provenance, **and** output bytes. **then** change one selected source line between sealing **and** publication.

## Acceptance criteria

both unchanged runs are byte-identical **and** decode **to** **every** original event field **in** original order; metadata identifies the exact source frontier **and** encoder; the changed-frontier run produces no accepted Projection.

## Failure disposition

reject the Projection method **and** preserve source **and** output digests, decoded comparisons, provenance metadata, **and** changed-frontier handling.
