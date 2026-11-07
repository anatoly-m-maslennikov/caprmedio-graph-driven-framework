---
atom_id: CA-R-3010
ref_id: CA-R-3010
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Code Synopsis)
tier: 3
status: Active
version: 2
updated_at: "2026-11-07 17:10:31 +0400"
carrier_destination:
  file:
    name: CA-R-3010-CORE_META_MODEL-DECLARATION--declare-code-synopsis-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-3010-CORE_META_MODEL-DECLARATION--declare-code-synopsis-form.md
  source_atom_id: CA-R-3010
  source_atom_revision: 2
  source_sha256: 650f5ebe630e5628d721ae8f0b934af7b550cd6ecbc39f0aed5915fd21204899
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Code Synopsis Form

## Claim

### Prose Claim

A Code Synopsis identifies one or more unambiguous code locations in its Project context. Its Claim describes the referenced code at the identified context and state. The referenced code determines actual behavior and structure.

### Formal Claim

```CFEL
# model
Atom/(.Header.Form := Code Synopsis);

Atom/(.Header.Form := Code Synopsis).Content.Summary ;> Atom/(.Header.Form := Code Synopsis).Content.Claim;

Atom/(.Header.Form := Code Synopsis).Content.Claim{::1}:: []{::0};
Atom/(.Header.Form := Code Synopsis).Content.Claim.*[string, in (Formal Claim, Prose Claim)]{::1..2};

Atom/(.Header.Form := Code Synopsis).Content.Claim.Prose Claim{::0..1}:: {::1};
Atom/(.Header.Form := Code Synopsis).Content.Claim.Prose Claim.*[]{::0};

Atom/(.Header.Form := Code Synopsis).Content.Claim.Formal Claim{::0..1}:: {::1};
Atom/(.Header.Form := Code Synopsis).Content.Claim.Formal Claim.*[]{::0};

Atom/(.Header.Form := Code Synopsis).Content.Claim.Prose Claim ;> Atom/(.Header.Form := Code Synopsis).Content.Claim.Formal Claim;

IF (Atom/(.Header.Form := Code Synopsis).Content.Claim.Formal Claim {=1}) THEN (
FENCED_LABELS(Atom/(.Header.Form := Code Synopsis).Content.Claim.Formal Claim):: [in (CFEL)]{::1}
);

# instances
Atom/(.Header.Form := Code Synopsis)//$synopsis.Header.Role:: [in (Implementation)]{::1}
```

## Semantics

A Code Synopsis is an authored, concise explanation of an actual code area and its relevant rationale.
