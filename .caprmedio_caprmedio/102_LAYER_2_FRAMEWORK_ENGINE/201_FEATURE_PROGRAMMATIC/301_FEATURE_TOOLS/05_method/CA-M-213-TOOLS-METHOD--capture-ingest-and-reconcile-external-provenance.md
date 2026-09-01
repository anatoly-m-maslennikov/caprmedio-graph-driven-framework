---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - artifact-operations
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  method_for:
    - CA-R-1144
    - CA-R-1145
    - CA-R-1146
  derived_from:
    - CA-A-058
---
# Capture ingest and reconcile external provenance

## Applicable when

Use this Method when external material must be captured, imported into bounded analysis, and reconciled with project provenance.

## Procedure

1. Capture the exact external page, post, video transcript, or text as an immutable source carrier with origin, retrieval time, attribution, digest, and reproducibility result.
2. Bind any imported analysis to that source identity, exact target frontier, source digest, and transformation session in a provenance envelope.
3. Keep imported claims non-authoritative until a separate operator adoption action creates or revises project authority.
4. Compare source, analysis draft, session, target revision, and digest provenance in read-only mode.
5. Report missing, conflicting, stale, unverifiable, and current links without making adoption decisions.

## Outcome

External material and derived analysis remain reproducible, bounded, and distinguishable from accepted project authority.

## Failure or stop

Stop ingestion when source identity or digest is unavailable; never invent provenance or promote imported claims implicitly.
