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
---

## Summary

Declare Atom.Content.Claim.Prose Claim

## Claim

### Prose Claim

Prose Claim is a child Property of Claim. Its value is ordinary Markdown; headings within that value are not Properties unless an applicable declaration admits them.
### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role in RMED).Content.Claim.Prose Claim:: {::0..1};

Atom/(.Header.Context.Role in RMED).Content.Claim.Prose Claim.*[]{::0}
```
