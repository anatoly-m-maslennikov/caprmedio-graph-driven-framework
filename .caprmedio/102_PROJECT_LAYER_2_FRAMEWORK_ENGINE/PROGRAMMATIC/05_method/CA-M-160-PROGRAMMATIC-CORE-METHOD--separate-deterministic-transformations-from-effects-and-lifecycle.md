---
cce_version: cce_1
cce_form: method
subjects:
  declared:
    continuant:
      - effect-boundary
version: 1
updated_at: 2026-08-23 16:54:12 +0400
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Separate deterministic transformations from effects and lifecycle

Plan PROGRAMMATIC decisions through deterministic transformations, then apply
filesystem, process, clock, environment, network, persistence, or
logging-export effects through named effect and lifecycle boundaries.

## Applicable when

Apply when a Tool, App backend service, or MCP component combines a decision
with an external effect, asynchronous work, or lifecycle transition.

## Procedure

1. Form the decision, target, ordering, and expected outcome from explicit
   observations before applying an effect.
2. Pass the resulting plan to the one bounded effect or lifecycle owner.
3. Return typed observations or completion facts to the decision boundary;
   do not let the effect owner invent, reorder, or suppress a decision.

## Outcome

Decision logic is replayable and effects have a visible owner, ordered input,
and recoverable result boundary.

## Failure or stop

Stop execution when the plan is incomplete, an effect owner would make a new
business decision, or the lifecycle boundary cannot report a typed result.
