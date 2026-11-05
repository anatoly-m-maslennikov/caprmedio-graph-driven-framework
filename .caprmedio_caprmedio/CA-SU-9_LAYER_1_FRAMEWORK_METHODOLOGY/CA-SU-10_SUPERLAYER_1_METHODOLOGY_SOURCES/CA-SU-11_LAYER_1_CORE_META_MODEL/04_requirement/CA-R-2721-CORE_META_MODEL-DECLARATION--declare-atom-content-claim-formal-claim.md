---
atom_id: CA-R-2721
ref_id: CA-R-2721
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Content.Claim.Formal Claim
version: 2
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-04 05:21:15 +0400
carrier_destination:
  file:
    name: CA-R-2721-CORE_META_MODEL-DECLARATION--declare-atom-content-claim-formal-claim.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
container:
  scope_unit: CA-SU-11
---
## Summary

Declare Atom.Content.Claim.Formal Claim

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role in RMED).Content.Claim.Formal Claim:: {::0..1};

Atom/(.Header.Role in RMED).Content.Claim.Formal Claim.*[]{::0};

IF (Atom/(.Header.Role in RMED).Content.Claim.Formal Claim {=1}) THEN (
FENCED_LABELS(Atom/(.Header.Role in RMED).Content.Claim.Formal Claim):: [in (CFEL)]{::1}
)
```

### Prose Claim

Formal Claim is a child Property of an ordinary RMED Claim. Its value is Markdown and contains a CFEL-labelled code fence.
