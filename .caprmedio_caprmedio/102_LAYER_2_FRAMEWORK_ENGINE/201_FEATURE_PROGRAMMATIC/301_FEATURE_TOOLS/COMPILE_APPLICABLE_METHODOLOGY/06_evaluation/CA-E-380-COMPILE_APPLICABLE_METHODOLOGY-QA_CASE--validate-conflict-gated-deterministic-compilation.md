---
atom_id: CA-E-380
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Applicable Methodology Compilation Validation
  depends_on:
    continuant:
      - Tool/COMPILE_APPLICABLE_METHODOLOGY
      - Applicable Methodology/Compilation Output
version: 1
updated_at: 2026-08-27 21:37:28 +0400
relations:
  evaluation_for:
    - CA-R-1240
    - CA-M-226
---
# Validate Conflict-Gated Deterministic Compilation

the `COMPILE_APPLICABLE_METHODOLOGY` Evaluation **must not pass** if (dry-run mutates a Source or Output Carrier **or** dry-run omits a duplicate selected Atom identity, unresolved replacement, incompatible retained Candidate, unresolved priority, or output-path collision **or** apply accepts a stale, partial, missing, ambiguous, or mismatched Local Configuration approval **or** apply emits a non-RMEDO, Draft, archived, monolithic, or persistent-index Carrier **or** a projected Carrier changes source frontmatter or Claim content beyond `projection.source_carrier_path` **or** a transaction failure leaves partial output **or** identical resolved Source Frontiers produce different output **or** removing generated output Carriers prevents complete regeneration).
