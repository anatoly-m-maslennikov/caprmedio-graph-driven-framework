---
atom_id: CA-O-draft
role: Operations
form: Action
status: Draft
version: 1
updated_at: '2026-11-05 18:54:16 +0400'
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Action
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
relations: {}
---

## Summary

Check Draft input formats and allowed values

## Claim scope

One accumulated Draft request under its bound Project and applicable model.

## Claim

### Inputs

`parameters`, and the bound Project and applicable model context. The parameters are either `newAtom` properties, or an exact existing `sourceCurrent` selector plus requested property changes.

### Fixed parameters

None.

### Effect

Apply [CA-R-1630@42-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1630@42-draft-CORE_META_MODEL-RULE--gate-atomic-admission-and-promotion.md)'s mechanical admission validation to the applicable-model candidate, without semantic review.

For `sourceCurrent`, use the ordinary authorized Project reader and form a transient candidate using the source transformation in [Create one Atom Draft](CA-O-draft-PROJECT_CONFIGURATION-ACTION--create-one-atom-draft.md), without materializing an Atom.

For full candidate validation, supply ID, Version, timestamps, Draft Status and placement as applicable tool-derived Draft metadata rather than caller parameters. In particular, validate the pending Draft Status, not a source Current Status such as `Active`. Do not request those fields from the caller.

Strip [CA-D-568](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/draft/lifecycle-in-place-edits/CA-D-568@20-draft-CORE_META_MODEL-DECISION--bind-draft-identity-continuity-evidence.md)-defined generated-carrier fields from logical `parameters` and return a short warning. For each missing or invalid logical value, add a `requested_input` entry keyed by its existing declared logical field (for example, `Summary` or `sourceCurrent`). Each checker entry is an object with required `error` (a short string) and at least one applicable `format` (a string) or `allowed_values` (an array). An empty `requested_input` is valid.

### Outputs

Return logical `parameters`, any carrier-field warning, and `requested_input`; [Present intermediate results and request input](CA-O-draft-PROJECT_CONFIGURATION-ACTION--present-intermediate-results-and-request-input.md) supplies waiting transport and [CA-R-1432@28-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1432@28-draft-CORE_META_MODEL-RULE--classify-admitted-atom-changes-by-semantic-effect.md) supplies failure handling.
