---
atom_id: CA-R-2707
ref_id: CA-R-2707
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Tier.Label
tier: 3
status: Active
version: 4
updated_at: "2026-11-07 15:18:44 +0400"
carrier_destination:
  file:
    name: CA-R-2707-CORE_META_MODEL-DECLARATION--declare-atom-header-tier-label.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2707-CORE_META_MODEL-DECLARATION--declare-atom-header-tier-label.md
  source_atom_id: CA-R-2707
  source_atom_revision: 4
  source_sha256: ab0f1996bd3f119090b61fcbad6f7c8375ddc807d1288c4849cc6f2e0bc54a82
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Atom.Header.Tier.Label

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Tier.Label:: [string]{::0..1};

Atom.Header.Tier.Label.*[]{::0};

# instances
Atom//$atom_2;

IF (($atom_2.Header.Tier.Label{=1}) AND ($atom_2.Header.Tier = 1)) THEN ($atom_2.Header.Tier.Label == Core);

Atom//$atom_3;

IF (($atom_3.Header.Tier.Label{=1}) AND ($atom_3.Header.Tier = 2)) THEN ($atom_3.Header.Tier.Label == General);

Atom//$atom_4;

IF (($atom_4.Header.Tier.Label{=1}) AND ($atom_4.Header.Tier = 3)) THEN ($atom_4.Header.Tier.Label == Standard);

Atom//$atom_5;

IF (($atom_5.Header.Tier.Label{=1}) AND ($atom_5.Header.Tier = 4)) THEN ($atom_5.Header.Tier.Label == Detail)
```
