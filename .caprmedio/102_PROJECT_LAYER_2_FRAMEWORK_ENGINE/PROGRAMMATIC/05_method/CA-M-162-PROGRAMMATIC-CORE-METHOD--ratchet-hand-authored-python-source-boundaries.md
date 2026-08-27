---
cce_version: cce_1
cce_form: method
subjects:
  declared:
    continuant:
      - source-boundary
version: 2
updated_at: 2026-08-27 04:58:31
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Ratchet hand-authored Python source boundaries

Keep new or materially changed hand-authored PROGRAMMATIC Python source within
the accepted source-size ratchet and require cyclomatic-complexity lint for
each changed executable unit while reviewing cohesion, responsibility,
dependency direction, and testability independently.

## Applicable when

Apply to each new or materially changed hand-authored Python file in Tools, App
backend services, or MCP components. Generated Runtime and Delivery outputs
are outside this source rule.

## Procedure

1. Target at most 200 physical lines per file.
2. Target at most 25 logical lines per executable unit; use 26–40 only for one
   coherent job.
3. Run the canonical admitted cyclomatic-complexity lint for every new or
   materially changed executable unit.
4. Reject a unit above the canonically configured complexity maximum unless one
   specific bounded exception records the measured value, applicable maximum,
   reason, and condition for reconsideration.
5. For an executable unit above 40 logical lines, record the specific
   source-size exception and retain its single responsibility.
6. Externalize large static mappings rather than treating size or complexity
   scores alone as correctness decisions.

## Outcome

Changed source ratchets toward readable, bounded units without declaring
existing oversized or over-complex source an immediate whole-repository
failure. Cyclomatic complexity cannot regress silently in changed executable
units.

## Failure or stop

Stop claiming conformance for a changed unit that exceeds its source-size or
cyclomatic-complexity boundary without a documented bounded exception. Stop
when no canonical admitted complexity-lint profile and maximum exist, or when
reducing a score would obscure a separate responsibility or needed recovery
boundary.
