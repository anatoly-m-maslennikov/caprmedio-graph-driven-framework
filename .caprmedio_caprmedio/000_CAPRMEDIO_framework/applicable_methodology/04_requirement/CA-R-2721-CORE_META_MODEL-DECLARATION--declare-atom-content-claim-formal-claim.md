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
version: 2
updated_at: 2026-11-04 05:21:15 +0400
carrier_destination:
  file:
    name: CA-R-2721-CORE_META_MODEL-DECLARATION--declare-atom-content-claim-formal-claim.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2721-CORE_META_MODEL-DECLARATION--declare-atom-content-claim-formal-claim.md
  source_atom_id: CA-R-2721
  source_atom_revision: 2
  source_sha256: c63aaa714ba91f3cc4b7e6099e2aa2b67f90c25224036f76fca806ca5c9cb71a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Content.Claim.Formal Claim

## Claim

### Prose Claim

Formal Claim is a child Property of an ordinary RMED Claim. Its value is Markdown and contains a CFEL-labelled code fence.
### Formal Claim

```CFEL
# model
Atom/(.Header.Role in RMED).Content.Claim.Formal Claim:: {::0..1};

Atom/(.Header.Role in RMED).Content.Claim.Formal Claim.*[]{::0};

IF (Atom/(.Header.Role in RMED).Content.Claim.Formal Claim {=1}) THEN (
FENCED_LABELS(Atom/(.Header.Role in RMED).Content.Claim.Formal Claim):: [in (CFEL)]{::1}
)
```

