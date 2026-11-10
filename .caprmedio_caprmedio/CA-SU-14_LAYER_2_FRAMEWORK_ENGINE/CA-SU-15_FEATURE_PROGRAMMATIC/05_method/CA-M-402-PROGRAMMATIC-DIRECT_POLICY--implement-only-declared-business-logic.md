---
identity:
  atom_id: CA-M-402
  ref_id: CA-M-402
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Authoring <+ Code Authoring
    dependencies:
    - MODEL//CAPRMEDIO <+ Package/Project Package
    - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution
      Control <+ Effect Authorization
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Requirement)
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Method)
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Evaluation)
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Delivery)
    - MODEL//CAPRMEDIO <+ Actor/Operator
  tier: 1
relations:
  DERIVED_FROM:
  - CA-A-1185
state:
  status: Active
  version: 14
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-402-PROGRAMMATIC-DIRECT_POLICY--implement-only-declared-business-logic.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
current_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---

## Summary

Implement only declared business logic

## Claim



### Prose Claim
Implement business logic **only** as declared in the applicable Active RMED. **Do not** invent additional policies, restrictions, approval gates, lifecycle rules or workflows. **When** the specification has a gap or conflict affecting the behavior, ask the Operator **before** implementing that behavior.

## Details

### Scope

New or changed PROGRAMMATIC implementation, including its tests.


1. Read the applicable Active RMED before changing behavior. A derived prompt helps find and use the rules; it does not add authority.
2. Choose ordinary implementation details freely within those rules. A choice of algorithm, function layout or internal data structure does not require its own policy when it preserves the declared behavior and constraints.
3. If an additional business rule seems necessary, explain the gap and the smallest proposed change to the Operator. Do not silently implement it or make tests require it. Continue independent work that does not depend on that decision.
4. After the Operator resolves the gap, align the affected RMED before implementing the new business rule. Do not create a new approval mechanism to enforce this Method.

### Outcome

Implementation and tests realize the declared behavior without adding an implicit second specification.

### Failure or stop

Pause the affected behavior when its business meaning requires an undeclared decision. This Method does not authorize removing existing checks or overriding applicable Active RMED without an Operator decision.
