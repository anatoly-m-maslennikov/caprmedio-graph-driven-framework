---
subjects:
  governs: "Claim Value Set Authoring"
  depends_on:
    ["Entity/Continuant/Object/Atom.Substance", "Author", "Claim Value Set", "Property", "Subject Expression", "IS_ALLOWED_VALUE_OF"]
version: 12
updated_at: "2026-10-15 18:48:04 +0000"
relations:
  child_of:
    - CA-M-115
atom_id: "CA-M-237"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/05_method/CA-M-237-CORE_META_MODEL--author-claim-value-sets.md
  source_atom_id: CA-M-237
  source_atom_revision: 12
  source_sha256: f17db364ce1c6d2efb448ff5a23182d2a921c0fe4b366421ba4120bd83b8e6b9
  original_relations_sha256: 8560a14f5d40024180f49119ad6216bc8babc0722610186fff08e9b20d081299
---
# Summary

Author Claim Value Sets

## Scope

Claim Value Set authoring.

## Claim

**to** author one Claim Value Set, the Author **must**:

1. identify **`=1`** Property X within **`=1`** Claim;
2. write its finite allowed-value set as `X: (A, B, C)`;
3. include **`>=1`** unique canonical values **and** treat their order as non-authoritative;
4. retain the complete set as **`=1`** Claim **only** **if** **all** values **must** be accepted, replaced, **and** retired together;
5. interpret `:` as Claim Value-Set syntax inside that Claim **and** as **`=1`** IS_ALLOWED_VALUE_OF relation **only** inside a Subject Expression.

## Details
