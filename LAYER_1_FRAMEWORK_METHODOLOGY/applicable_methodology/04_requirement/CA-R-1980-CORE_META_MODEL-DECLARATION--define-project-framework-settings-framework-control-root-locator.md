---
atom_id: CA-R-1980
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Project.Settings.Framework Control-Root Locator
relations:
  child_of:
  - CA-R-1176
version: 16
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-04 05:21:15 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1980-CORE_META_MODEL-DECLARATION--define-project-framework-settings-framework-control-root-locator.md
  source_atom_id: CA-R-1980
  source_atom_revision: 16
  source_sha256: 6db52d1f6c7c2b2ed8100adc7420266bb4dcd7cf3637c7e0d7a65a48855f3459
  original_relations_sha256: 9e3e53a370b31aee7f492cc3fbaba3b8b30f92b5773698d221265754db5d0402
---
## Summary

Define Project.Framework Settings.Framework Control-Root Locator

## Claim

### Formal Claim

```CFEL
# model
Project.Settings.Framework Control-Root Locator: [string]{:0..1};

Project.Settings.Framework Control-Root Locator.*[]{:0}
```

### Prose Claim


the Project's framework control-root reference in Framework Settings.



## Details

Evidence: CA-D-370 requires the locator to resolve to the Directory Carrier prescribed by CA-D-317 without selecting another authority root. Candidate #6 keeps concrete CAPRMEDIO mechanisms in Project Configuration. This definition adds no path or alternative authority root; those remain Delivery rules.
