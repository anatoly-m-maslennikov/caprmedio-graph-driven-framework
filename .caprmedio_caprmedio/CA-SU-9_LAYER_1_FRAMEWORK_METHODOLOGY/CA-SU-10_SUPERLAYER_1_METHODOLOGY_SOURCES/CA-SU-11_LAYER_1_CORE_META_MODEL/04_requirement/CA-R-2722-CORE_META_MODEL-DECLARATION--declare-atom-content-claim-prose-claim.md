---
atom_id: CA-R-2722
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content.Claim.Prose Claim
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-2722-CORE_META_MODEL-DECLARATION--declare-atom-content-claim-prose-claim.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Atom.Content.Claim.Prose Claim

## Claim

### Formal Claim

```CFEL
Atom/(.Header.Role in RMED).Content.Claim.Prose Claim{:0..1}: [markdown]{:1};
Atom/(.Header.Role in RMED).Content.Claim.Prose Claim.*[]{:0}
```

### Prose Claim

Prose Claim is a child Property of an ordinary RMED Claim. Its value is ordinary Markdown; headings within that value are not Properties unless an applicable declaration admits them.
