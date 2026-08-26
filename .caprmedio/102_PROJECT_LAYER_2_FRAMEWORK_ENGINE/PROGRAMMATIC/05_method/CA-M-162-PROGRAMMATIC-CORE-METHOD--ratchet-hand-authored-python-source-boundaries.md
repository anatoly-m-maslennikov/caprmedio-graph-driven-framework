---
cce_version: cce_1
cce_form: method
subjects:
  declared:
    continuant:
      - source-boundary
version: 1
updated_at: 2026-08-23 16:54:12 +0400
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Ratchet hand-authored Python source boundaries

Keep new or materially changed hand-authored PROGRAMMATIC Python source within
the accepted source-size ratchet while reviewing cohesion, responsibility,
dependency direction, complexity, and testability independently.

## Applicable when

Apply to each new or materially changed hand-authored Python file in Tools, App
backend services, or MCP components. Generated Runtime and Delivery outputs
are outside this source rule.

## Procedure

1. Target at most 200 physical lines per file.
2. Target at most 25 logical lines per executable unit; use 26–40 only for one
   coherent job.
3. For an executable unit above 40 logical lines, record the specific
   exception and retain its single responsibility.
4. Externalize large static mappings rather than treating size alone as a
   correctness decision.

## Outcome

Changed source ratchets toward readable, bounded units without declaring
existing oversized source an immediate whole-repository failure.

## Failure or stop

Stop claiming conformance for a changed unit that exceeds its bound without a
documented exception, or when a size reduction would obscure a separate
responsibility or needed recovery boundary.
