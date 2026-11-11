---
atom_id: CA-R-2721
ref_id: CA-R-2721
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Content.Claim.Formal Claim
tier: 3
status: Active
version: 4
updated_at: "2026-11-07 17:10:31 +0400"
carrier_destination:
  file:
    name: CA-R-2721-CORE_META_MODEL-DECLARATION--declare-atom-content-claim-formal-claim.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Declare Atom.Content.Claim.Formal Claim

## Claim

### Prose Claim

Formal Claim is a child Property of Claim. Its value is Markdown and contains a CFEL-labelled code fence.
### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role in RMED).Content.Claim.Formal Claim:: {::0..1};

Atom/(.Header.Context.Role in RMED).Content.Claim.Formal Claim.*[]{::0};

IF (Atom/(.Header.Context.Role in RMED).Content.Claim.Formal Claim {=1}) THEN (
FENCED_LABELS(Atom/(.Header.Context.Role in RMED).Content.Claim.Formal Claim):: [in (CFEL)]{::1}
)
```
