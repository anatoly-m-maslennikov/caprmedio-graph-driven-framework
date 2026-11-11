---
atom_id: CA-I-001
cce_version: cce_1
cce_form: implementation
subjects:
  governs:
    continuant:
    - Tool/DETECT_CLAIM_VALUE_SET_CANDIDATES/Implementation
  depends_on:
    continuant:
    - Claim Value Set Consolidation Candidate Detection
    - Tool/DETECT_CLAIM_VALUE_SET_CANDIDATES
    - Atom/Current Scope/Governed Subject Set
    - Entity Graph Projection
    - IS_ALLOWED_VALUE_OF
version: 2
updated_at: 2026-09-02 01:12:00 +0400
relations:
  implementation_for:
  - CA-M-238
status: Archived
ref_id: CA-I-001@2
carrier_destination:
  file:
    name: CA-I-001@2-DETECT_CLAIM_VALUE_SET_CANDIDATES-CORE-IMPLEMENTATION--implement-report-only-candidate-detection.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/DETECT_CLAIM_VALUE_SET_CANDIDATES/02_analysis/archive
---
# Implement Report-Only Candidate Detection

the `DETECT_CLAIM_VALUE_SET_CANDIDATES` Tool Implementation **must** deterministically derive Governed Subject Sets, Claim Scopes, **and** allowed-value evidence from the supplied Source frontier **and** Entity Graph Projection, emit a report, **and must not** rewrite, merge, archive, replace, compile, **or** change Source Atoms by another operation.
