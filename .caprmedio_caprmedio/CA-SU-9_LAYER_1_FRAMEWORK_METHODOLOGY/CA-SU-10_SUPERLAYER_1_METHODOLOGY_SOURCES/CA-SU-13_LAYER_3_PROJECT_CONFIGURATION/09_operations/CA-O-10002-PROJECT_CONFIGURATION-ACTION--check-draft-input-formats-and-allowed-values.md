---
identity:
  atom_id: CA-O-10002
  ref_id: CA-O-10002
context:
  container:
    scope_unit: CA-SU-13
  role: Operations
  form: Action
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Action
    dependencies:
    - CAPRMEDIO_MODEL <+ Atom
    - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
  tier: 3
state:
  status: Active
  version: 2
  updated_at: 2026-11-11 14:19:47 +0400
destination:
  file:
    name: CA-O-10002-PROJECT_CONFIGURATION-ACTION--check-draft-input-formats-and-allowed-values.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations
---
## Summary

Check Draft input formats and allowed values

## Claim scope

One accumulated Draft request under its bound Project and applicable model.

## Claim

### Inputs

`parameters`, and the bound Project and applicable model context. The parameters are either `newAtom` properties, or an exact existing Atom selector plus requested property changes.

### Fixed parameters

None.

### Effect

Check input formats and allowed values against the applicable model without semantic review.

For an existing Atom selector, use the ordinary Project reader and form a transient candidate using the source transformation in [Create one Atom Draft](CA-O-10003-PROJECT_CONFIGURATION-ACTION--create-one-atom-draft.md), without materializing an Atom.

For full candidate validation, supply ID, Version, timestamps, Draft Status and placement as applicable tool-derived Draft metadata rather than caller parameters. In particular, validate the pending Draft Status, not a source Current Status such as `Active`. Do not request those fields from the caller.

Strip generated filename, output path and destination fields from logical `parameters` and return a short warning. The logical Scope Unit remains an input. For each missing or invalid logical value, add a `requested_input` entry keyed by its existing declared logical field (for example, `Summary` or `sourceCurrent`). Each checker entry is an object with required `error` (a short string) and at least one applicable `format` (a string) or `allowed_values` (an array). An empty `requested_input` is valid.

### Outputs

Return logical `parameters`, any carrier-field warning, and `requested_input`; [Present intermediate results and request input](CA-O-10004-PROJECT_CONFIGURATION-ACTION--present-intermediate-results-and-request-input.md) supplies waiting transport and an actual effect failure ends the invocation.
