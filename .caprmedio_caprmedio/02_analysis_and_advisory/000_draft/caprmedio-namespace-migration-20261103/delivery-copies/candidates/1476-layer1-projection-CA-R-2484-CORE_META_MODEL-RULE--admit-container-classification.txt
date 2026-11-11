---
atom_id: CA-R-2484
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Node >| Container
version: 2
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2484-CORE_META_MODEL-RULE--admit-container-classification.md
  source_atom_id: CA-R-2484
  source_atom_revision: 2
  source_sha256: 6072c421bfa8f40d978f1aa729ac79f7897260407e3cc25661b05ee198b603b8
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Classify permission to have parts as Container

## Claim

Container is a classification whose admitted value cases are yes and no:

```CFEL
Node >| Container: yes;
Node >| Container: no
```

The yes case permits the Node to be the whole endpoint of CONTAINS, subject to its effective Relation whitelist and cardinalities. It does not by itself require a part. The no case forbids that endpoint role. Whether a part may belong to a whole is distinct from whether that part may itself have parts.

Use `Node// >| Container = yes` when selecting eligible whole instances. Container is not a required Boolean Property authored on every instance. This Draft does not assign an implicit default or require a classification annotation for every Node.

## Details

The Operator chose IS_CONTAINED_BY / CONTAINS and Container: yes/no. Current CA-R-1945@13 distinguishes permission from a requirement to have children; retain that distinction while replacing the old Atom.Enabled Relations.Contains Property representation. Its default-False mechanism is not silently imported into the new general classification. Explicit CONTAINS cardinalities can require parts for a particular Node, such as Workflow.
