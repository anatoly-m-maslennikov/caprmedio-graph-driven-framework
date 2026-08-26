---
cce_version: cce_1
cce_form: method
subjects:
  declared:
    continuant:
      - deterministic-transformation
version: 1
updated_at: 2026-08-23 16:54:12 +0400
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Allocate deterministic transformations to functions

Implement one deterministic PROGRAMMATIC transformation as a function whose
result follows from its declared inputs and whose responsibility does not own
mutable state, a resource, a lifecycle, or a replaceable adapter.

## Applicable when

Apply when Tools, App backend services, or MCP components parse, classify,
validate, plan, project, format, or otherwise transform explicit input into a
result.

## Procedure

1. State the function's input, result, and failure values explicitly.
2. Keep its result independent of filesystem, process, clock, environment,
   network, persistence, and logging-export effects.
3. Pass required observations and settings as explicit inputs rather than
   obtaining them implicitly.

## Outcome

The transformation is reproducible from its declared input and can be reused
or checked without constructing component lifecycle state.

## Failure or stop

Stop treating the unit as a deterministic function when it must own mutable
state, a resource, a lifecycle, a replaceable adapter, or an external effect;
allocate that responsibility to its proper Method boundary instead.
