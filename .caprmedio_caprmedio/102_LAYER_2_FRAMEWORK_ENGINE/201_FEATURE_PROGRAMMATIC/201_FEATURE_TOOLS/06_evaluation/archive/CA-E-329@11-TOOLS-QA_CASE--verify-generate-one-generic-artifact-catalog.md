---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: artifact-catalog
  depends_on: []
version: 11
updated_at: 2026-10-24 00:28:02 +0400
relations:
  evaluation_for:
  - CA-M-211
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-329@11
status: Archived
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
