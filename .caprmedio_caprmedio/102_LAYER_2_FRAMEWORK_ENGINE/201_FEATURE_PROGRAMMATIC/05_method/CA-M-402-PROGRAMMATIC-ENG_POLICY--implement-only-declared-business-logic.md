---
atom_id: CA-M-402
content_role: Method
type: Eng Policy
current_scope_unit: PROGRAMMATIC
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Code Authoring
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
version: 11
updated_at: 2026-10-27 19:59:43 +0400
author: Anatoly Maslennikov
relations:
  derived_from:
  - CA-A-1185
tier: 1
---
# Summary

Implement only declared business logic

## Scope

New or changed PROGRAMMATIC implementation, including its tests.

## Claim

Implement business logic **only** as declared in the applicable Active RMED. **Do not** invent additional policies, restrictions, approval gates, lifecycle rules or workflows. **When** the specification has a gap or conflict affecting the behavior, ask the Operator **before** implementing that behavior.

## Details

Candidate source: [CA-M-384@1](archive/CA-M-384-PROGRAMMATIC-CORE-METHOD--implement-only-declared-business-logic@1.md)

1. Read the applicable Active RMED before changing behavior. A derived prompt helps find and use the rules; it does not add authority.
2. Choose ordinary implementation details freely within those rules. A choice of algorithm, function layout or internal data structure does not require its own policy when it preserves the declared behavior and constraints.
3. If an additional business rule seems necessary, explain the gap and the smallest proposed change to the Operator. Do not silently implement it or make tests require it. Continue independent work that does not depend on that decision.
4. After the Operator resolves the gap, align the affected RMED before implementing the new business rule. Do not create a new approval mechanism to enforce this Method.

## Outcome

Implementation and tests realize the declared behavior without adding an implicit second specification.

## Failure or stop

Pause the affected behavior when its business meaning requires an undeclared decision. This Method does not authorize removing existing checks or overriding applicable Active RMED without an Operator decision.
