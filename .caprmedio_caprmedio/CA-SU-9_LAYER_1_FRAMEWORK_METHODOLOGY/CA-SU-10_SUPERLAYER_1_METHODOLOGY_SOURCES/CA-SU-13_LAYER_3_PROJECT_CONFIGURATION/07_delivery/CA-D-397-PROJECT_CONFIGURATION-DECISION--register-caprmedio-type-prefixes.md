---
atom_id: CA-D-397
ref_id: CA-D-397
container:
  scope_unit: CA-SU-13
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection.Form
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Term//Artifact
  - CAPRMEDIO_MODEL <+ Atom.Header.Identity.ID
tier: 3
relations:
  depends_on:
  - CA-D-311
status: Active
version: 26
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-D-397-PROJECT_CONFIGURATION-DECISION--register-caprmedio-type-prefixes.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
---
## Summary

Register CAPRMEDIO Type prefixes

## Claim

### Prose Claim


fixed lowercase prefixes for listed Artifact Type values.


the following fixed lowercase prefixes **must** be registered **only** for the listed Type values under Artifact; Atom identities use class short names instead.

| Artifact form | Type | Prefix |
|---|---|---|
| `projection` | `catalog` | `catl` |
| `projection` | `map` | `maps` |
| `projection` | `hub` | `hubs` |
| `projection` | `implementation_record` | `irec` |
