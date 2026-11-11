---
atom_id: CA-D-666
form: Policy
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Scope Unit
  passive:
  - CAPRMEDIO <+ MODEL <+ Carrier
version: 1
relations: {}
tier: 3
updated_at: 2026-11-02 19:17:40 +0400
role: Delivery
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-666-CORE_META_MODEL-POLICY--carry-scope-unit-declarations-as-governing-atoms.md
  source_atom_id: CA-D-666
  source_atom_revision: 1
  source_sha256: 69b3e609510c3848583b4e62ca05d464a00a40969434ac1c185b1f576011e0a0
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Carry Scope Unit Declarations as Governing Atoms

## Claim

Carry a Scope Unit Declaration in a Markdown Atom file. The file is its Carrier; the Declaration is the governing source.

Frontmatter carries its Role, Form and active Subject. Claim carries its operative prose, CFEL expressions, or both. `project_structure.toml` is not a governing source.
