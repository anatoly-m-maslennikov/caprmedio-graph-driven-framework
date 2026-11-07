---
atom_id: CA-E-801
ref_id: CA-E-801
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Code Synopsis)
tier: 3
status: Active
version: 2
updated_at: "2026-11-07 17:10:31 +0400"
carrier_destination:
  file:
    name: CA-E-801-CORE_META_MODEL-EVAL_CASE--verify-code-synopsis-accuracy.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-801-CORE_META_MODEL-EVAL_CASE--verify-code-synopsis-accuracy.md
  source_atom_id: CA-E-801
  source_atom_revision: 2
  source_sha256: d46bc29f663c173143e9cc552ff1ace9a16b0fa19d920e4a04e297082f09ee5c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Verify Code Synopsis accuracy

## Claim

### Prose Claim

For a selected Code Synopsis:

1. Resolve its code locations in the stated Project context.
2. Compare its descriptive claims with the referenced code.
3. Check that documented rationale and inferred explanations are distinguishable.
4. Check an optional specification comparison against the cited specification.
5. Check the inherited Atom rules and declared Claim structure.

Use these cases:

- Legacy code without a specification: accept an accurate Synopsis.
- A supported code/specification difference: accept the neutral observation without requiring a Concern.
- An ambiguous or missing code location: report failed verification.
- A claim contradicted by the referenced code: report failed verification.
- Inferred rationale presented as a supported fact: report failed verification.

Record the result and evidence. Verification does not change code or create a Concern.
