---
cce_version: cce_1
cce_form: method
subjects:
  declared:
    continuant:
      - performance-measurement
version: 1
updated_at: 2026-08-23 16:54:12 +0400
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Measure before optimizing PROGRAMMATIC performance

Measure a PROGRAMMATIC performance concern before accepting an optimization;
use a representative workload for its Hook, interactive, batch, MCP, App, or
background surface rather than treating one surface as universal.

## Applicable when

Apply when a Tool, App backend service, or MCP component proposes or assesses
a performance-sensitive change.

## Procedure

1. Select the applicable surface and representative workload.
2. Preserve the input, environment, baseline, observed distribution, and
   comparison threshold with the measurement.
3. Compare the change to the recorded baseline before accepting the claimed
   improvement.
4. Leave numeric budgets to a later bounded authority until current baselines
   and Operator priorities establish them.

## Outcome

An accepted performance claim is tied to one reproducible workload and
measurement boundary instead of a universal or unmeasured optimization claim.

## Failure or stop

Stop the performance claim when no representative workload, preserved
baseline, or comparable observation exists; do not invent a numeric budget.
