---
atom_id: CA-R-2722
ref_id: CA-R-2722
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Content.Claim.Prose Claim
tier: 3
status: Active
version: 4
updated_at: "2026-11-07 17:10:31 +0400"
carrier_destination:
  file:
    name: CA-R-2722-CORE_META_MODEL-DECLARATION--declare-atom-content-claim-prose-claim.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2722-CORE_META_MODEL-DECLARATION--declare-atom-content-claim-prose-claim.md
  source_atom_id: CA-R-2722
  source_atom_revision: 4
  source_sha256: 39e5e6b469828628220882bba13884f91836bbf58656265ff71f70803c86ccda
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Atom.Content.Claim.Prose Claim

## Claim

### Prose Claim

Prose Claim is a child Property of Claim. Its value is ordinary Markdown; headings within that value are not Properties unless an applicable declaration admits them.
### Formal Claim

```CFEL
# model
Atom/(.Header.Role in RMED).Content.Claim.Prose Claim:: {::0..1};

Atom/(.Header.Role in RMED).Content.Claim.Prose Claim.*[]{::0}
```
