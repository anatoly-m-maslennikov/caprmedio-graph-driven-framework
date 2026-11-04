---
atom_id: CA-O-draft
role: Operations
form: Action
status: Draft
version: 1
updated_at: '2026-11-04 22:27:14 +0400'
tier: 3
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Action'
  passive:
    - 'CAPRMEDIO_MODEL <+ Atom'
    - 'CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION'
relations: {}
---

## Summary

Present intermediate results and request input

## Claim scope

One bound Workflow Run that needs additional input before its current Step can continue.

## Claim

### Inputs

The bound Project, Workflow Run and current Step; intermediate results; and a `requested_input` dictionary. Each key identifies a needed field and may state its description or constraint.

### Fixed parameters

None.

### Effect

Return the intermediate results and `requested_input` dictionary to the MCP caller. The in-session agent may decide how to obtain the requested values. Wait for a later MCP call bound to the same Project, Run and Step that supplies the requested input dictionary.

Waiting is neither a completed Step nor an error. Continue only after the requested input is supplied and accepted.

Validate the resumed Project, Run and Step binding and the supplied dictionary against `requested_input`. Return the accepted dictionary as the Action result.

### Outputs

While waiting, return the intermediate results and `requested_input` dictionary. After a valid resumed call, return the accepted input dictionary to the caller. On failure, return the explicit error and actual completed results under [CA-R-1432@28-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1432@28-draft-CORE_META_MODEL-RULE--classify-admitted-atom-changes-by-semantic-effect.md).
