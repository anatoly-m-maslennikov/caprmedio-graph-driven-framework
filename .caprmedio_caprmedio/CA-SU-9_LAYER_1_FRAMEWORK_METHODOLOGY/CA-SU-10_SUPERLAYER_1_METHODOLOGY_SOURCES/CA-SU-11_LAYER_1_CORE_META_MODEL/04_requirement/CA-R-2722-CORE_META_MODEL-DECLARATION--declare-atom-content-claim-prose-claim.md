---
atom_id: CA-R-2722
ref_id: CA-R-2722
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Content.Claim.Prose Claim
version: 2
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-04 05:21:15 +0400
carrier_destination:
  file:
    name: CA-R-2722-CORE_META_MODEL-DECLARATION--declare-atom-content-claim-prose-claim.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
container:
  scope_unit: CA-SU-11
---
## Summary

Declare Atom.Content.Claim.Prose Claim

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role in RMED).Content.Claim.Prose Claim:: {::0..1};

Atom/(.Header.Role in RMED).Content.Claim.Prose Claim.*[]{::0}
```

### Prose Claim

Prose Claim is a child Property of an ordinary RMED Claim. Its value is ordinary Markdown; headings within that value are not Properties unless an applicable declaration admits them.
