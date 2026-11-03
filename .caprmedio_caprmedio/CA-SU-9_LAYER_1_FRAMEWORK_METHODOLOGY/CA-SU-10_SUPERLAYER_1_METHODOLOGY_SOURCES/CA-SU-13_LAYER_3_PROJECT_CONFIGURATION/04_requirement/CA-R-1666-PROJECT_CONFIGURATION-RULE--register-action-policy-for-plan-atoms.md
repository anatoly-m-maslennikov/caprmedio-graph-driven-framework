---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Form'
version: 37
updated_at: 2026-11-02 19:44:26 +0400
relations:
  depends_on:
  - CA-R-1286
atom_id: CA-R-1666
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Register Action Policy for Plan Atoms

## Claim

### Prose Claim


the CAPRMEDIO Project Configuration registration of `Atom/(.Header.Role := Plan).Header.Form` values.


the CAPRMEDIO Project Configuration **must** register Action Policy as an additional value of `Atom/(.Header.Role := Plan).Header.Form`; Plan retains its canonical admission under CA-R-1574@21-CORE_META_MODEL-DEFINITION--define-the-common-plan-atom; navigation Labels do **not** add further Type values.
