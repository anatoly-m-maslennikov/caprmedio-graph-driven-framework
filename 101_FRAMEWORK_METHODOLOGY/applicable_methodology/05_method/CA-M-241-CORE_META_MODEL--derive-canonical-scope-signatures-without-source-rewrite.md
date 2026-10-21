---
subjects:
  governs: "Canonical Scope Signature Derivation"
  depends_on:
    ["Scope Expression", "Entity/Node/Continuant/Projection/Type: Canonical Scope Signature", "Atom Carrier"]
version: 12
updated_at: "2026-10-19 15:54:44 +0400"
relations:
  child_of:
    - CA-M-121
atom_id: "CA-M-241"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/05_method/CA-M-241-CORE_META_MODEL--derive-canonical-scope-signatures-without-source-rewrite.md
  source_atom_id: CA-M-241
  source_atom_revision: 12
  source_sha256: 6e0c6711ff636167632d7bdad67dc23ced0041dbd48926285a738cff05830bf3
  original_relations_sha256: 6fc59a347195a35964bdd70772c15ed7cb8cb9aec1c3a511387f263fc6569134
---
# Summary

Derive Canonical Scope Signatures **without** Source Rewrite

## Scope

derivation of Canonical Scope Signatures from one caller-selected Atom Carrier folder.

## Claim

**to** derive Canonical Scope Signatures from one caller-selected Atom Carrier folder, the Tool **must** inspect **only** active Carriers with **`=1`** unwrapped Scope Expression **in** one `## Scope` section, resolve **every** atomic identity against active Atom IDs **in** that selected folder, derive a signature **only** **if** the Scope Expression satisfies the restricted Canonical Scope Signature grammar, emit source identity, source revision, source Carrier digest, source frontier digest, source expression, signature, **and** exclusion diagnostic, **and** make no source-Carrier rewrite, lifecycle change, Claim merge, authority decision, **or** dependency relation.

## Details
