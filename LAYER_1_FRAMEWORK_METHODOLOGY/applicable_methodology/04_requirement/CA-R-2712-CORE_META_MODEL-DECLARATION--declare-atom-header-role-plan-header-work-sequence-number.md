---
atom_id: CA-R-2712
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Work Sequence Number
version: 2
relations: {}
tier: 3
updated_at: 2026-11-04 05:21:15 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2712-CORE_META_MODEL-DECLARATION--declare-atom-header-role-plan-header-work-sequence-number.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2712-CORE_META_MODEL-DECLARATION--declare-atom-header-role-plan-header-work-sequence-number.md
  source_atom_id: CA-R-2712
  source_atom_revision: 2
  source_sha256: 5734c23d03209bdbb4735f1a6938942dfa1353c50fa093a371ca539543d0cbf7
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom/(.Header.Role := Plan).Header.Work Sequence Number

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role: Plan).Header.Work Sequence Number: [int]{:0..1};

Atom/(.Header.Role: Plan).Header.Work Sequence Number.*[]{:0};

# instances
Atom/(.Header.Role: Plan)//$atom;

IF ($atom.Header.Work Sequence Number{=1})
THEN ($atom.Header.Work Sequence Number > 0);

UNIQUE(
  Atom/(.Header.Role: Plan)//$atom_2,
  (.Header.Relations.IS_CONTAINED_BY.atom, .Header.Work Sequence Number),
  (.Header.Status = Active) AND (.Header.Work Sequence Number{=1}) AND (.Header.Relations.IS_CONTAINED_BY.atom{=1})
);

UNIQUE(
  Atom/(.Header.Role: Plan)//$atom_3,
  (.Header.Relations.IS_CONTAINED_BY.scope_unit, .Header.Work Sequence Number),
  (.Header.Status = Active) AND (.Header.Work Sequence Number{=1}) AND (.Header.Relations.IS_CONTAINED_BY.scope_unit{=1})
)
```
