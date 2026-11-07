---
atom_id: CA-R-3006
ref_id: CA-R-3006
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Scope Delegation)
tier: 3
status: Active
version: 4
updated_at: "2026-11-07 17:10:31 +0400"
carrier_destination:
  file:
    name: CA-R-3006-CORE_META_MODEL-DECLARATION--declare-scope-delegation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-3006-CORE_META_MODEL-DECLARATION--declare-scope-delegation.md
  source_atom_id: CA-R-3006
  source_atom_revision: 4
  source_sha256: 8b5ef46544b35bf5afeb6cdaff57a49b318a58a26155116b1ea8c351827efab2
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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

Each concrete Scope Delegation Claim lists admitted local Role/Form pairs and typed HAS_ACTIVE_SUBJECT target selections. A local Atom is admitted only when its Header.Container-derived IS_CONTAINED_BY target is the receiving Scope Unit, its HAS_ACTIVE_SUBJECT target is in a listed selection, and its Role/Form pair is listed or is Implementation / Code Synopsis, which is admitted by default. Solution, Direct Policy and Approach Policy are RMEDO Forms and require explicit inclusion in the local whitelist. Decision is a MEDO Form.

### Formal Claim

```CFEL
# instances
Atom/(.Header.Form := Scope Delegation)//$scope_delegation;
$scope_delegation.Header.Role:: [in (Requirement, Method, Evaluation, Delivery, Operations)]{::1};
```
