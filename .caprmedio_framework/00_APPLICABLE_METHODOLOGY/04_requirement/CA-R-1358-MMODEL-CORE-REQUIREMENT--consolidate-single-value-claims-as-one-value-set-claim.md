---
atom_id: CA-R-1358
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Atom/Claim
  depends_on:
    continuant:
      - Atom/Current Scope
      - Atom/Claim Scope
      - IS_ALLOWED_VALUE_OF
version: 1
updated_at: 2026-09-01 01:06:56 +0400
relations:
  child_of:
    - CA-R-918
    - CA-R-919
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1358-MMODEL-CORE-REQUIREMENT--consolidate-single-value-claims-as-one-value-set-claim.md
---
# Consolidate Single-Value Claims as One Value-Set Claim

multiple Claims with the same Current Scope, Claim Scope, **and** X **must** be consolidated as **`=1`** Claim in the form `X: (A, B, C)` **if** they differ **only** by one allowed value of X.
