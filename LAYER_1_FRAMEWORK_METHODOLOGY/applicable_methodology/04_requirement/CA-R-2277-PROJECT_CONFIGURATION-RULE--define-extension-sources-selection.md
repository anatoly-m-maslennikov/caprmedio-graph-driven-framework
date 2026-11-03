---
atom_id: CA-R-2277
current_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 1
subjects:
  active: CAPRMEDIO <+ STRUCTURE <+ Named Selection//Extension Sources
relations: {}
version: 4
updated_at: 2026-11-02 08:06:47 +0400
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-2277-PROJECT_CONFIGURATION-RULE--define-extension-sources-selection.md
  source_atom_id: CA-R-2277
  source_atom_revision: 4
  source_sha256: c396f6f2ca4a1e03ef0ad32f5da4ffb60b81c3beede99a380e283dccc3480ebd
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Extension Sources Selection

## Claim

Extension Sources is the named Selection of immutable installed Extension source Atoms available as candidate inputs to methodology compilation. Membership establishes availability, not activation. Framework Settings separately selects activation and the installed source version for an Extension; Applicable Methodology separately includes only sources applicable under those settings.

```CFEL
Named Selection//Extension Sources
```

## Details

CA-R-1175 requires preservation of installed source versions as candidate inputs. CA-R-1228 governs the applicable Methodology subset, and CA-R-1724 separates installed availability from activation and version selection. This definition identifies their shared candidate population; it adds no activation procedure, new Scope Unit, or automatic conflict resolution.
