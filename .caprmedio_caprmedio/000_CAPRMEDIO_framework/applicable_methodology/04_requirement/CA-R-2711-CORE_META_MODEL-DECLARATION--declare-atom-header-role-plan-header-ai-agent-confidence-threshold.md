---
atom_id: CA-R-2711
ref_id: CA-R-2711
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.AI Agent Confidence Threshold
tier: 3
status: Active
version: 6
updated_at: 2026-11-04 21:11:03 +0400
carrier_destination:
  file:
    name: CA-R-2711-DECLARATION--declare-atom-header-role-plan-header-ai-agent-confidence-threshold.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2711-CORE_META_MODEL-DECLARATION--declare-atom-header-role-plan-header-ai-agent-confidence-threshold.md
  source_atom_id: CA-R-2711
  source_atom_revision: 6
  source_sha256: fbf494e6d6543b9b9f235d8bb330a9017b8fd1bba377192873705e2638b6d1cb
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom/(.Header.Role := Plan).Header.AI Agent Confidence Threshold

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role: Plan).Header.AI Agent Confidence Threshold:: [int, 0..100]{::0..1};

Atom/(.Header.Role: Plan).Header.AI Agent Confidence Threshold.*[]{::0};

# instances
Atom/(.Header.Role: Plan)//$plan;
Scope Unit/Project//$project{::1};

$plan.Header.AI Agent Confidence Threshold
  ?== LOOKUP(Relation//IS_CONTAINED_BY, Atom/(.Header.Role: Plan).Header.AI Agent Confidence Threshold)
  ?== $project.Settings.AI Agent Confidence Threshold
```
