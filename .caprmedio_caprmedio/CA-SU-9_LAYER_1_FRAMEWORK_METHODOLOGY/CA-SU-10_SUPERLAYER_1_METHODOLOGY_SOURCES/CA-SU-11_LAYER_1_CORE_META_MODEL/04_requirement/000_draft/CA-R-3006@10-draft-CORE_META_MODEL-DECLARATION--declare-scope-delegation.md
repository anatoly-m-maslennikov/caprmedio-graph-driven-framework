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

A Scope Delegation states the receiving Scope Unit's responsibilities and admits Main Subject selections in its Prose Claim. The Scope Unit Declaration states the receiving unit's structural facts in its Formal Claim.

For local admission, the Atom's Container resolves to the receiving Scope Unit. Its Main Subject resolves to an endpoint admitted by at least one applicable Scope Delegation. The Model determines valid Role and Form combinations.

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
