---
subjects:
  governs: "Canonical Signature Derivation"
  depends_on:
    ["Entity/Continuant/Object/Atom.Substance", "Atom Claim Canonical Signature", "CCE Operator"]
version: 11
updated_at: "2026-10-15 18:48:06 +0000"
relations:
  child_of:
    - CA-M-115
atom_id: "CA-M-240"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/05_method/CA-M-240-CORE_META_MODEL-METHOD--derive-restricted-cce-canonical-signatures-without-source-rewrite.md
  source_atom_id: CA-M-240
  source_atom_revision: 11
  source_sha256: 6638ed5e274fff2773930a589d8263350142167b5e50af7bc40ffdf49d9f3408
  original_relations_sha256: 8560a14f5d40024180f49119ad6216bc8babc0722610186fff08e9b20d081299
---
# Summary

Derive Restricted CCE Canonical Signatures **without** Source Rewrite

## Scope

derivation of Canonical Signatures from one selected Atom Carrier folder.

## Claim

**to** derive Canonical Signatures from one selected Atom Carrier folder, the Tool **must** inspect **only** active single-statement Atom Claims, identify **every** outermost parenthesized expression that **contains** the **and** Operator **or** the **or** Operator, derive a Canonical Signature **only** **if** the expression satisfies the Restricted Boolean Expression grammar, emit source-identity evidence **and** **every** exclusion diagnostic, **and** make no source-Carrier rewrite, lifecycle change, Claim merge, **or** authority decision.

## Details
