---
atom_id: CA-R-2500
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content.Claim
version: 4
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2500-CORE_META_MODEL-DECLARATION--declare-atom-content-claim.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Atom.Content.Claim

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role in RMED).Content.Claim{:1}: []{:0};

Atom/(.Header.Role in RMED).Content.Claim.*[string, in (Formal Claim, Prose Claim)]{:1..2};

Atom/(.Header.Role in RMED).Content.Claim.Formal Claim{:0..1}: [markdown]{:1};

Atom/(.Header.Role in RMED).Content.Claim.Prose Claim{:0..1}: [markdown]{:1}
```

### Prose Claim

A complete ordinary RMED Claim has at least one of Formal Claim and Prose Claim. Sibling names are unique. Formal Claim contains a CFEL-labelled code fence; Prose Claim contains ordinary Markdown. A Markdown heading inside Prose Claim is part of its value, unless an applicable declaration expressly declares it as a child Property.

