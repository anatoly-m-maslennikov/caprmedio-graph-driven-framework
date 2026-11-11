---
identity:
  id: CA-R-3006
  ref_id: CA-R-3006@10-draft
context:
  container:
    scope_unit: CA-SU-11
  role: requirement
  form: declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Form := Scope Delegation)
  tier: 3
state:
  status: draft
  version: 10
  updated_at: '2026-11-11T16:37:55+04:00'
destination:
  file:
    name: CA-R-3006@10-draft-CORE_META_MODEL-DECLARATION--declare-scope-delegation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---


## Summary

Declare Scope Delegation

## Claim

### Prose Claim

Scope Delegation is one generic Form for an external Atom whose Role is in RMEDO. Its active Subject identifies exactly one receiving non-Project Scope Unit within the Project. Its Container is that unit’s direct structural Parent. The Parent assigns a contribution to the receiving unit and retains its broader scope and accountability.

A Scope Delegation states responsibilities and local admissions in its Prose Claim. The Scope Unit Declaration states the receiving unit’s structural facts in its Formal Claim.

Each Scope Delegation lists admitted local Role/Form pairs and exact active Subject targets in its Prose Claim. Plan / Work Report is admitted as a supporting Atom for an already admitted Task. It has that Task’s Container and remains within the applicable Subject selections. Its Role/Form pair needs no separate local listing.

For other local Atoms, admission requires the Header.Context.Container-derived IS_CONTAINED_BY target to be the receiving Scope Unit, the HAS_ACTIVE_SUBJECT target to be in a listed selection, and the Role/Form pair to be listed or Analysis and Advisory / Code Synopsis, which is admitted by default. Solution, Direct Policy and Approach Policy are RMEDO Forms and require explicit inclusion in the local whitelist. Decision is a MEDO Form.

When a unit has multiple Scope Delegations, each local Atom that requires a listed Role/Form pair must have both its pair and its active Subject admitted by the same Scope Delegation.

### Formal Claim

```CFEL
# model
Atom.Header.Context.Form :: Scope Delegation;

# instances
FOR EACH $a[<Atom>, (.Header.Context.Form = Scope Delegation)]:
(
    $a.Header.Context.Role:: [in (Requirement, Method, Evaluation, Delivery, Operations)]{::1};
    $a ((HAS_ACTIVE_SUBJECT)) Scope Unit//$unit;
    $unit {::1}((IS_CONTAINED_BY)) Scope Unit//$parent;
    $a ((IS_CONTAINED_BY)) $parent;
)
```
