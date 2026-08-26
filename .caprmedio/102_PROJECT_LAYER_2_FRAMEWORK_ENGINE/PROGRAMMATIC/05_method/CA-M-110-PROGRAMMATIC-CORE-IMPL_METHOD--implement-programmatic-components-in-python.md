---
cce_version: cce_1
cce_form: method
subjects:
  declared:
    continuant:
      - programmatic-components
version: 7
updated_at: 2026-08-23 16:54:12 +0400
relations:
  method_for:
    - CA-R-1047
  derived_from:
    - CA-A-053
---
# Implement PROGRAMMATIC components in Python

Use Python for applicable PROGRAMMATIC Tools, App backend services, and MCP
components under the technical contract in `pyproject.toml`, table
`tool.caprmedio.framework_engine_software`. The table, not this Method, owns
the selected supported runtime, default dependency boundary, and the locations
for admitted exceptions. This Method does not govern Skills or make Python a
discipline-independent CAPRMEDIO meaning.

## Applicable when

Apply when a Tool, App backend service, or MCP component is added or materially
changed, or when its Python realization, runtime dependency, or non-Python
exception is proposed.

## Procedure

1. Read the current technical contract before selecting the realization.
2. Use the standard library when it provides the required behavior with
   comparable clarity and reliability.
3. For each necessary dependency or non-Python exception, record its required
   capability or native-interface need, bounded carrier set, integration
   contract, added boundary cost, supporting evidence, and Operator acceptance
   at the contract's declared Delivery and Evaluation locations.

## Outcome

Every applicable component conforms to one selected technical contract or has
one complete, bounded, accepted exception; selected configuration values retain
their sole owner in `pyproject.toml`.

## Failure or stop

Stop admission or release of the affected component when the contract is
absent, its selected boundary is exceeded, or the exception record is
incomplete. Do not infer a platform-support claim from local execution.
