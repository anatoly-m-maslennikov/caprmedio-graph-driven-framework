---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
  - CAPRMEDIO <+ MODEL <+ Atom.Content
  - CAPRMEDIO <+ MODEL <+ Atom.Subjects
  - CAPRMEDIO <+ MODEL <+ Scope Unit
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO <+ MODEL <+ Atom
version: 47
updated_at: 2026-11-02 19:44:26 +0400
relations:
  evaluation_for:
  - CA-R-1595@21
  - CA-R-1596
  - CA-R-922
  - CA-R-923
  - CA-R-1588
  - CA-R-1271
  - CA-R-947
  - CA-R-944
  - CA-R-2100
  - CA-R-1202
  - CA-D-482
  - CA-D-495
atom_id: CA-E-240
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 7
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-240-CORE_META_MODEL-EVAL_CASE--validate-atom-scope-and-claim-scope.md
  source_atom_id: CA-E-240
  source_atom_revision: 47
  source_sha256: 6989878e50a2f12ddcde039ea0429ff9087232da28ae2e9df76719d6cdbc0a1b
  original_relations_sha256: 87d3ab0300acfc698201ed021ffe3ef2c189c47d9f2eebc0e21a96062d84be30
---
## Summary

Validate Atom Scope **and** Claim Scope

## Claim scope
independent resolution of Atom ownership, GOVERNS Subject, Claim Target Scope Unit, **and** textual applicability.

## Claim

**Claim checked.**

**every** Atom resolves its ownership, **`=1`** GOVERNS Subject, **and** zero **or** one Claim Target Scope Unit independently of **any** applicability restrictions **in** its Main Content. Applicable Goal and Demand rules, including the Operator-owned Project Goal, retain their required target conditions.

## Details

### Test case

create a Current-scope Atom with its own Scope Unit carried as the target; repeat with one GOVERNS target and with a narrower restriction **and** a composite restriction **in** its Claim scope section for RMED **or** the registered primary content for other roles. create a parent-owned Goal for a declared direct child, an external Project Goal with its Author's registered Operator name **and** an explicit Project target, **and** a permitted Demand. include a Plan **in** a Container Atom whose carried target is its owning Scope Unit.

**then** omit the GOVERNS Subject or a required target, provide two target values, supply a Container Atom **or** another non-Scope-Unit target, leave a reference unresolved, infer a different target merely from textual restrictions, change ownership from the target, make the referenced Scope Unit bearer-dependent, reorder Subject declarations, **or** use a forbidden Goal **or** Demand target.

### Acceptance criteria

**every** valid fixture retains its ownership, resolves **`=1`** canonical GOVERNS Subject **and** zero **or** one Claim Target Scope Unit, **and** preserves its applicability restrictions **in** the body sections registered by CA-D-495-CORE_META_MODEL-CORE-DELIVERY--carry-applicability-in-the-registered-body-sections. a Current-scope target is selected from the owning Scope Unit during authoring **and** carried explicitly where applicable; an external Goal requires its explicit Project target. narrower **or** composite Claim Scope alone does **not** create a distinct Target Scope Unit. a different permitted target does **not** transfer ownership **or** create Scope Unit ancestry. Subject ordering **and** Container Atom nesting do **not** change these facts. **every** invalid fixture fails with the exact affected fact identified.

### Failure disposition

report the invalid Atom **and** ownership, target, textual restriction, **or** Subject fact; do **not** repair unresolved references by guessing.
