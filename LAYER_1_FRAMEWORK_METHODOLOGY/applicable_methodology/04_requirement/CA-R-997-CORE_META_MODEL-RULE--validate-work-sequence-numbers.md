---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan).Work Sequence Number
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan)
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan).Work Sequence Number
version: 34
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-2520
  - CA-R-992
atom_id: CA-R-997
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-997-CORE_META_MODEL-RULE--validate-work-sequence-numbers.md
  source_atom_id: CA-R-997
  source_atom_revision: 34
  source_sha256: 8e343aee198fc0941887be2b31b29f78bc9aa519b08d3ea42f49a3d38c9e6fbd
  original_relations_sha256: e3cb7ba04df44e248817a6642b01424b625d1bb053399bc02906c615371e6b65
---
## Summary

Validate Work Sequence Numbers

## Claim scope

supplied Work Sequence Numbers for Plans directly contained by the same Plan or sharing the same top-level Plan container.

## Claim

**every** supplied Work Sequence Number **must** be a unique positive ordinal among Plans directly contained by the same Plan **or** sharing the same top-level Plan container.
