---
cce_version: cce_1
cce_form: method
subjects:
  declared:
    continuant:
      - component-lifecycle
version: 1
updated_at: 2026-08-23 16:54:12 +0400
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Allocate owned state and lifecycle to objects

Use an object when one PROGRAMMATIC responsibility owns mutable technical
state, a resource, a lifecycle, or a replaceable adapter. Do not create an
object merely to group unrelated deterministic functions.

## Applicable when

Apply when a Tool, App backend service, or MCP component must retain state,
acquire or release a resource, transition through a lifecycle, or encapsulate
one replaceable technical adapter.

## Procedure

1. Name the one state, resource, lifecycle, or adapter responsibility that the
   object owns.
2. Make acquisition, use, failure, and release or recovery boundaries explicit.
3. Keep deterministic transformations outside the object unless they need its
   owned responsibility.

## Outcome

Each object has a bounded owner responsibility, a visible lifecycle, and no
unrelated function-grouping role.

## Failure or stop

Stop and split or redesign the object when it owns unrelated state or
lifecycle concerns, hides an external effect, or exists only as a namespace.
