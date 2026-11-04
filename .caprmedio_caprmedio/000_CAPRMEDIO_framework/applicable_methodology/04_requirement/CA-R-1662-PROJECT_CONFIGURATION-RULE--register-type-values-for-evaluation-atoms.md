---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation).Header.Form'
version: 39
updated_at: 2026-11-02 19:44:26 +0400
relations:
  depends_on:
  - CA-R-1506
atom_id: CA-R-1662
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1662-PROJECT_CONFIGURATION-RULE--register-type-values-for-evaluation-atoms.md
  source_atom_id: CA-R-1662
  source_atom_revision: 39
  source_sha256: 241b6adfa8c873d14168a65ae4beef281551ef8d80b83a93a2467eef79929cfe
  original_relations_sha256: 7c0fb333f30aaaf7bab5ef0cca0a81542ac7fe43fe5784a738aed1c0c0f79d4a
---
## Summary

Register Type Values for Evaluation Atoms

## Claim

### Prose Claim


internal values of `Atom/(.Header.Role := Evaluation).Header.Form`.


Policy, Eval Case, QA Case, **and** Evaluation Control **must** be registered as internal values of `Atom/(.Header.Role := Evaluation).Header.Form`.

## Details

Eval Case is defined by CA-R-2116@9. QA Case remains registered for existing Atoms pending individually evidenced migration; this registration does not require bulk reclassification. Evaluation Control remains a distinct specific Type.
