---
atom_id: CA-E-384
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Claim-Boundary Evaluation
  depends_on:
    continuant:
      - Claim
      - Claim Scope
version: 3
updated_at: 2026-08-29 02:40:41 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-384-GOVERN-CORE-EVALUATION--validate-composite-claims-and-derived-summaries.md
---
# Validate Composite Claims and Derived Summaries

the Evaluation **must** reject an Atom **if** it has zero **or** multiple Claims, zero **or** multiple Claim Scopes, an independently replaceable component inside one Claim, ambiguous composite grouping, a non-deterministic Scope Expression, **or** a Summary that is **not** reproducibly source-faithful to the complete Claim **and** Claim Scope.
