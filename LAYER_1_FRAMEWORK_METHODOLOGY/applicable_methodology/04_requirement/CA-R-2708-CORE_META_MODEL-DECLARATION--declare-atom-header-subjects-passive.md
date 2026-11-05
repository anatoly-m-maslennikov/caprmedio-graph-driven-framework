---
atom_id: CA-R-2708
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Subjects.Passive
version: 1
relations: {}
tier: 3
updated_at: 2026-11-03 20:00:05 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2708-CORE_META_MODEL-DECLARATION--declare-atom-header-subjects-passive.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2708-CORE_META_MODEL-DECLARATION--declare-atom-header-subjects-passive.md
  source_atom_id: CA-R-2708
  source_atom_revision: 1
  source_sha256: 2b525cc7e96e8f348248a8e8fbfb591114c434d847e7c9e4cf7d3a8f8ceb9351
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Header.Subjects.Passive

## Claim

### Prose Claim

Passive Subjects identify direct contextual dependencies.

### Formal Claim

```CFEL
# model
Atom.Header.Subjects.Passive{:0..1}: [string]{:0+};

Atom.Header.Subjects.Passive.*[]{:0};

# instances
Atom//$atom;

COUNT($atom.Header.Subjects.Passive: $) = COUNT(DISTINCT $atom.Header.Subjects.Passive: $)
```
