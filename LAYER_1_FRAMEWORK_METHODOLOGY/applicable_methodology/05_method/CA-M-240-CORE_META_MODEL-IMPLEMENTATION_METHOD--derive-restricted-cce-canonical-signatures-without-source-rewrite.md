---
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Data Handling <+ Data Transformation
  passive:
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Data Handling <+ Data Transformation
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Data Handling <+ Parsing
version: 30
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-M-443
atom_id: CA-M-240
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Method
form: Implementation Method
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-240-CORE_META_MODEL-IMPLEMENTATION_METHOD--derive-restricted-cce-canonical-signatures-without-source-rewrite.md
  source_atom_id: CA-M-240
  source_atom_revision: 30
  source_sha256: 7ffa0ed50b2d8eb7fdab33bab40cf3409a6d954cbd888532f35d0c0a8e252afd
  original_relations_sha256: 41eea2b549fddac86f9ca945ab8fd8e81217096be0d79454a214399a75af697d
---
## Summary

Derive Restricted CCE Canonical Signatures **without** Source Rewrite

## Claim

### Prose Claim


derivation of Canonical Signatures from one selected Atom Carrier folder.


**to** derive Canonical Signatures from one selected Atom Carrier folder, the Tool **must** inspect **only** active single-statement Atom Claims, identify **every** outermost parenthesized expression that **contains** the **and** Operator **or** the **or** Operator, derive a Canonical Signature **only** **if** the expression satisfies the Restricted Boolean Expression grammar, emit source-identity evidence **and** **every** exclusion diagnostic, **and** make no source-Carrier rewrite, lifecycle change, Claim merge, **or** authority decision.
