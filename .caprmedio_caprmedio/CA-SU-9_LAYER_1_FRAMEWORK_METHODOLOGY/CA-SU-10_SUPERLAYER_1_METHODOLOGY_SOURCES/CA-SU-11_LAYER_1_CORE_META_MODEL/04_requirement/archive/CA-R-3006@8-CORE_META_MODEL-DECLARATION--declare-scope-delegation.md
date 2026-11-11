---
atom_id: CA-R-3006
ref_id: CA-R-3006@8
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Scope Delegation)
tier: 3
status: Archived
version: 8
updated_at: '2026-11-11 14:06:22 +0400'
carrier_destination:
  file:
    name: CA-R-3006@8-CORE_META_MODEL-DECLARATION--declare-scope-delegation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archive
---

## Summary

Declare Scope Delegation

## Claim

### Prose Claim

Scope Delegation is one generic Form for an external Atom whose Role is in RMEDO. Its active Subject identifies exactly one receiving non-Project Scope Unit within the Project. Its Container is that unit’s one direct structural Parent. Project may contain delegations for its children but is never their receiver. The direct Parent authors the structural declaration and assigns a contribution to the receiving unit; it retains its broader scope and accountability.

The Scope Delegation is the receiving unit’s sole structural declaration. It declares:

- Name;
- stable ID;
- ordering state;
- order.number when ordered;
- direct containing Scope Unit.

Label is optional.

Each concrete Scope Delegation Claim lists admitted local Role/Form pairs and typed HAS_ACTIVE_SUBJECT target selections. Plan / Work Report is admitted as a supporting Atom for an already admitted Task. It has that Task’s Container and remains within the applicable Subject selections. Its Role/Form pair needs no separate local listing.

For other local Atoms, admission requires the Header.Container-derived IS_CONTAINED_BY target to be the receiving Scope Unit, the HAS_ACTIVE_SUBJECT target to be in a listed selection, and the Role/Form pair to be listed or Analysis & Advisory / Code Synopsis, which is admitted by default. Solution, Direct Policy and Approach Policy are RMEDO Forms and require explicit inclusion in the local whitelist. Decision is a MEDO Form.

### Formal Claim

```CFEL
# model
Atom.Header.Form :: Scope Delegation;

# instances
FOR EACH $a[<Atom>, (.Header.Form = Scope Delegation)]:
(
    $a.Header.Role:: [in (Requirement, Method, Evaluation, Delivery, Operations)]{::1};
)
```
