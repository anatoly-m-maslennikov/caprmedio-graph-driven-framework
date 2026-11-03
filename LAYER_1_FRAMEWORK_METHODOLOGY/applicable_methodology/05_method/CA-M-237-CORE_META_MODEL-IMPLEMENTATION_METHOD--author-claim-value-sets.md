---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Content
  passive:
  - CAPRMEDIO <+ MODEL <+ Actor
  - CAPRMEDIO <+ MODEL <+ Term//Property
  - CAPRMEDIO <+ MODEL <+ Entity
  - CAPRMEDIO <+ MODEL <+ CFEL<+Operator//AllowedValue
version: 33
updated_at: 2026-11-02 08:06:47 +0400
relations:
  child_of:
  - CA-M-443
atom_id: CA-M-237
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Method
form: Implementation Method
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-237-CORE_META_MODEL-IMPLEMENTATION_METHOD--author-claim-value-sets.md
  source_atom_id: CA-M-237
  source_atom_revision: 33
  source_sha256: 80a5fac14369d7a86063c866921af0a48f0fa10147cbebc4eca645dd09fbdfef
  original_relations_sha256: 41eea2b549fddac86f9ca945ab8fd8e81217096be0d79454a214399a75af697d
---
## Summary

Author Claim Value Sets

## Claim scope

Claim Value Set authoring.

## Claim

**to** author one Claim Value Set, the Author **must**:

1. identify **`=1`** Property X within **`=1`** Claim;
2. write its finite allowed-value set as `X: (A, B, C)`;
3. include **`>=1`** unique canonical values **and** treat their order as non-authoritative;
4. retain the complete set as **`=1`** Claim **only** **if** **all** values **must** be accepted, replaced, **and** retired together;
5. interpret `:` as Claim Value-Set syntax inside that Claim **and** as one allowed-value qualification inside a Subject Expression; neither use creates a graph Relation or assigns an instance value.
