---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - artifact-operations
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  method_for:
    - CA-R-1125
  derived_from:
    - CA-A-058
---
# Validate generated data-stage pipelines

## Applicable when

Use this Method when validating a registered generated-data pipeline from source carriers through derived stages.

## Procedure

1. Load the registered source, staging, intermediate, mart, and business stage declarations and their materializations.
2. Resolve every dataset's authoritative source frontier and declared dependencies.
3. Check registered prefixes, forward-only stage dependencies, acyclic order, stable identity, and the absence of derived-to-source authority inversion.
4. Recompute stage frontier digests and compare materialized outputs with the current declared inputs.
5. Report unregistered stages, backward edges, stale materializations, missing source provenance, and independently authored derived facts.

## Outcome

The pipeline has an attributable forward-only source-to-derived topology and current materializations, or explicit violations.

## Failure or stop

Block acceptance when a stage lacks a source frontier, depends backward, claims authority, or cannot prove currentness.
