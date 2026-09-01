---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - artifact-operations
    occurrent:
      - evaluation
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  evaluation_for:
    - CA-M-204
---
# Verify validate generated data-stage pipelines

## Claim checked

CA-M-204 accepts only registered forward-only source-to-derived pipelines whose materializations match their authority frontiers.

## Applicable when

Apply whenever a data-stage registration, dependency, source frontier, or materialized output changes.

## Test case

Construct one current src-to-stg-to-mrt-to-biz pipeline, then add an unregistered stage, a backward dependency, a stale materialization, and a derived row with no source provenance. Validate the combined fixture.

## Acceptance criteria

The original pipeline is accepted; each introduced defect produces one attributable blocking issue; no derived stage is treated as authority; and the report identifies exact source and materialization frontiers.

## Failure disposition

Reject the validator and preserve stage declarations, dependency graph, frontier digests, materializations, expected defects, and observed issue map.
