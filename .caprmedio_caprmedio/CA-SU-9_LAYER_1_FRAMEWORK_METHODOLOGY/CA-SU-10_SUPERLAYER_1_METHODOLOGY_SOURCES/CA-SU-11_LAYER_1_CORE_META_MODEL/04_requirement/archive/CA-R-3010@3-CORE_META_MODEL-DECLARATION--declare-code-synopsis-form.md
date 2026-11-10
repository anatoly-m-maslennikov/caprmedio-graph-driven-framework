---
atom_id: CA-R-3010
ref_id: CA-R-3010@3
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Code Synopsis)
tier: 3
status: Archived
version: 3
updated_at: 2026-11-09 23:45:16 +0400
carrier_destination:
  file:
    name: CA-R-3010@3-CORE_META_MODEL-DECLARATION--declare-code-synopsis-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archive
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

Atom/(.Header.Form := Code Synopsis).Header.Status: Resolved;

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

For a Code Synopsis, **Resolved** means the review is complete:

- Every finding that needs fixing or adopting is covered by Active C or RMEDO Atoms; or
- The review found nothing to fix or adopt.

Drafts do not count as handoff. The resulting Atoms keep their own statuses. Resolved closes the Code Synopsis review; it does not mean the resulting Concerns are resolved or the RMEDO changes are implemented.
