---
identity:
  atom_id: CA-D-712
  ref_id: CA-D-712@1-draft
context:
  container:
    scope_unit: CA-SU-44
  role: Delivery
  form: Decision
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Storage
    dependencies:
    - CAPRMEDIO_MODEL <+ Atom
    - CAPRMEDIO_MODEL <+ Carrier
    - CAPRMEDIO_MODEL <+ Journal
    - CAPRMEDIO_MODEL <+ Projection
    - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Storage <+ Temporary
      State
  tier: 3
state:
  status: Draft
  version: 1
  updated_at: 2026-11-10 12:28:12 +0400
destination:
  file:
    name: CA-D-712@1-draft-GRAPH_UI-DECISION--GRAPH_UI-DELIVERY--separate-interface-state-from-governed-sources.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-44_APP_GRAPH_UI/07_delivery/draft
author: Anatoly Maslennikov
relations:
  delivery_for:
  - CA-R-1076
  depends_on:
  - CA-D-437
  - CA-M-153
cce_version: cce_1
cce_form: serialization
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
---
## Summary
Separate interface state from governed sources

## Claim

### Prose Claim

GRAPH_UI interface-state Carriers **must** remain separate from governed source Artifacts **and** from the delivered frontend assets.

- filter **and** focused-node state use their existing URL representation under CA-M-153; transient interface state remains session-local **unless** an explicit retained-state binding applies.
- retained UI service state uses its declared project-local runtime location. disposable frontend build output **and** caches use Project Temporary State under CA-D-437.
- retained state identifies its interface owner **and** referenced source frontier; it **must not** carry an independently authoritative copy of an Atom, Journal, **or** graph Projection.

The frontend Delivery declaration retains ownership of frontend placement. this state boundary does **not** split embedded assets, select a new browser-output filename, **or** change the declared App service contract.
