---
atom_id: CA-M-241
ref_id: CA-M-241
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Data Handling <+ Data Transformation
  dependencies:
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Authoring <+ Controlled English
  - 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/Type: Canonical Scope Signature'
  - CAPRMEDIO_MODEL <+ Carrier/File
tier: 4
relations:
  child_of:
  - CA-M-121
status: Active
version: 28
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-M-241-CORE_META_MODEL-IMPLEMENTATION_METHOD--derive-canonical-scope-signatures-without-source-rewrite.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Derive Canonical Scope Signatures **without** Source Rewrite

## Claim

### Prose Claim


derivation of Canonical Scope Signatures from one caller-selected Atom Carrier folder.


**to** derive Canonical Scope Signatures from one caller-selected Atom Carrier folder, the Tool **must** inspect **only** active Carriers with **`=1`** unwrapped Scope Expression **in** one `## Scope` section, resolve **every** atomic identity against active Atom IDs **in** that selected folder, derive a signature **only** **if** the Scope Expression satisfies the restricted Canonical Scope Signature grammar, emit source identity, source revision, source Carrier digest, source frontier digest, source expression, signature, **and** exclusion diagnostic, **and** make no source-Carrier rewrite, lifecycle change, Claim merge, authority decision, **or** dependency relation.
