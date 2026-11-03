---
subjects:
  active: Aspects <+ Engineering <+ Data Handling <+ Data Transformation
  passive:
  - Aspects <+ Engineering <+ Authoring <+ Controlled English
  - 'Entity/Object/Continuant/Projection/Type: Canonical Scope Signature'
  - Carrier/File
version: 28
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-M-121
atom_id: CA-M-241
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Method
form: Implementation Method
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-241-CORE_META_MODEL-IMPLEMENTATION_METHOD--derive-canonical-scope-signatures-without-source-rewrite.md
  source_atom_id: CA-M-241
  source_atom_revision: 28
  source_sha256: 2730c0fcc70200c5307afe5c2a3f175b0a5e0929386af59a2e1ae42d0ca9b54d
  original_relations_sha256: 9c81d0cc7e058ef7249e0c55c89cc1a2f604371b94ce1e61069d033c3e36982f
---
## Summary

Derive Canonical Scope Signatures **without** Source Rewrite

## Claim scope

derivation of Canonical Scope Signatures from one caller-selected Atom Carrier folder.

## Claim

**to** derive Canonical Scope Signatures from one caller-selected Atom Carrier folder, the Tool **must** inspect **only** active Carriers with **`=1`** unwrapped Scope Expression **in** one `## Scope` section, resolve **every** atomic identity against active Atom IDs **in** that selected folder, derive a signature **only** **if** the Scope Expression satisfies the restricted Canonical Scope Signature grammar, emit source identity, source revision, source Carrier digest, source frontier digest, source expression, signature, **and** exclusion diagnostic, **and** make no source-Carrier rewrite, lifecycle change, Claim merge, authority decision, **or** dependency relation.
