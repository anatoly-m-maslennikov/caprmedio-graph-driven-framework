---
atom_id: CA-R-2277
ref_id: CA-R-2277
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Named Selection//Extension Sources
tier: 1
status: Active
version: 4
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-R-2277-PROJECT_CONFIGURATION-RULE--define-extension-sources-selection.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-2277-PROJECT_CONFIGURATION-RULE--define-extension-sources-selection.md
  source_atom_id: CA-R-2277
  source_atom_revision: 4
  source_sha256: b2d4fe295a12a49b428c8d95603d769ffd5790273c801ba60da68c9562e5b4ba
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Extension Sources Selection

## Claim

### Prose Claim


Extension Sources is the named Selection of immutable installed Extension source Atoms available as candidate inputs to methodology compilation. Membership establishes availability, not activation. Framework Settings separately selects activation and the installed source version for an Extension; Applicable Methodology separately includes only sources applicable under those settings.


### Formal Claim

```CFEL
# model
Named Selection//Extension Sources
```

## Details

CA-R-1175 requires preservation of installed source versions as candidate inputs. CA-R-1228 governs the applicable Methodology subset, and CA-R-1724 separates installed availability from activation and version selection. This definition identifies their shared candidate population; it adds no activation procedure, new Scope Unit, or automatic conflict resolution.
