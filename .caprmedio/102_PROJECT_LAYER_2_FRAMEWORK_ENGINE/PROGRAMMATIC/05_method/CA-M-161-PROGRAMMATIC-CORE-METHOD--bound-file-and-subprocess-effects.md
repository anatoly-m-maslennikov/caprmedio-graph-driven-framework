---
cce_version: cce_1
cce_form: method
subjects:
  declared:
    continuant:
      - external-effect
version: 1
updated_at: 2026-08-23 16:54:12 +0400
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Bound file and subprocess effects

Plan, validate, and bound each PROGRAMMATIC file mutation or subprocess
invocation before applying it; make partial failure diagnosable and recoverable
without guessing.

## Applicable when

Apply when a Tool, App backend service, or MCP component writes, replaces, or
removes a file, or invokes a subprocess.

## Procedure

1. Validate the target and preconditions before mutation.
2. Write replacement content through a secure temporary carrier on the
   destination filesystem, flush required bytes, and use an atomic replacement
   only where the supported boundary provides that guarantee.
3. Invoke a subprocess with an argument array, explicit timeout, checked exit
   status, controlled environment input, and shell execution disabled by
   default.
4. Return the target, inputs, outcome, and partial-failure context needed for
   diagnosis or recovery.

## Outcome

Every applicable effect has a declared precondition, bounded execution
surface, observable result, and explicit recovery limit.

## Failure or stop

Stop the effect when preconditions fail, an atomicity guarantee is unavailable
and no weaker recovery boundary is accepted, or subprocess completion,
timeout, and exit status cannot be observed.
