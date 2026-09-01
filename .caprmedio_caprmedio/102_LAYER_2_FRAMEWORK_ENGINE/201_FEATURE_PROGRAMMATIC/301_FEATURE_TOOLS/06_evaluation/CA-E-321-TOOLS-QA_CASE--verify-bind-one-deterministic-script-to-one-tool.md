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
    - CA-M-203
---
# Verify bind one deterministic script to one tool

## Claim checked

CA-M-203 establishes a one-to-one mapping between deterministic executable entry scripts and Tool owners while excluding support modules.

## Applicable when

Apply whenever an executable script, Tool Scope Unit, or canonical entrypoint declaration changes.

## Test case

Create a fixture with one correctly bound Tool script, one Tool with two entry scripts, one orphan executable, one Tool with no entrypoint, and two imported worker modules. Resolve the ownership map twice.

## Acceptance criteria

The correct pair is accepted; duplicate, orphan, and missing bindings are distinct findings; worker modules are not treated as Tools; repeated resolution produces the same mappings and findings.

## Failure disposition

Reject the binding method and preserve executable inventory, Tool declarations, import classification, mappings, findings, and repeated result.
