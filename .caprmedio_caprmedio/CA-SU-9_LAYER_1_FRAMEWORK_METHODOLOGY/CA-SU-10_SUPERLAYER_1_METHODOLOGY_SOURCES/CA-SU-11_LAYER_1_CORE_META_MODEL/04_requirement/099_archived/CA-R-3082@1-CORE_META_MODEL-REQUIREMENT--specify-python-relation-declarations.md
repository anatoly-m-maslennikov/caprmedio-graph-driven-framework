---
identity:
  atom_id: CA-R-3082
  ref_id: CA-R-3082@1
context:
  role: requirement
  form: requirement
  tier: 3
  container:
    scope_unit: CA-SU-11
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom.Content.Claim.Formal Claim
state:
  version: 1
  status: archived
  updated_at: '2026-11-12T12:28:45.296398+00:00'
destination:
  file:
    name: CA-R-3082@1-CORE_META_MODEL-REQUIREMENT--specify-python-relation-declarations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
---
## Summary

Specify Python relation declarations

## Claim

### Prose Claim

- Declare the canonical Relation name, endpoint domains, and any written aliases with `declare_relation`.
- Declare an inverse alias against its canonical Relation. Its source and target slots swap, including their cardinality bounds. Expose the reverse link as a Derived Relation from the same fact.
- Give each endpoint a Model or instance level where the Relation permits that level. An Entity's Model and instance permissions resolve separately.
- Declare direction-specific permissions and apply the appropriate source and target bounds. Unlisted Relations are forbidden where the Entity declares a closed whitelist.
- Declare the inheritable contracts on `NARROWER_THAN`. Python class bases establish the narrowing path. Resolve schema rules through the class MRO and explicit MODEL overrides.

- A canonical Relation declaration has Direct classification by default.
- Endpoint address forms identify canonical Relations, inverse alias addresses, base Atom IDs, and exact represented-content versions. Resolve inverse alias addresses through canonical Relation metadata.
