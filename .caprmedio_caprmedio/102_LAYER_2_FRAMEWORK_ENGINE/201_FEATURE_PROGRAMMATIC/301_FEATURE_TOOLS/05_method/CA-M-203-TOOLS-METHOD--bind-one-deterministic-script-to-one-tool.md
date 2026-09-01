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
    - CA-R-1124
  derived_from:
    - CA-A-058
---
# Bind one deterministic script to one Tool

## Applicable when

Use this Method when admitting or reviewing executable deterministic scripts in the PROGRAMMATIC source tree.

## Procedure

1. Enumerate executable deterministic entry scripts and active Tool Scope Units within the selected frontier.
2. Read each script's declared Tool identity and each Tool's canonical executable entrypoint.
3. Require a one-to-one mapping: one executable entry script per Tool and one Tool per executable entry script.
4. Classify imported modules, workers, and shared libraries as implementation support rather than separate Tools unless they expose an independent governed interface.
5. Report missing, duplicate, cross-boundary, and orphan mappings with both source paths.

## Outcome

Every deterministic executable entry script has exactly one Tool owner and every Tool has exactly one canonical executable entry script.

## Failure or stop

Do not infer ownership from directory proximity alone; leave ambiguous or multi-owner scripts as blocking findings.
