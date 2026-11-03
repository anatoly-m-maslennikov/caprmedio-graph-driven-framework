---
atom_id: CA-R-1888
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := "Analysis & Advisory").Header.Form
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := "Analysis & Advisory")
version: 16
updated_at: 2026-11-02 19:33:47 +0400
relations: {}
tier: 2
role: Requirement
form: Rule
---
## Summary

Register FPF Analysis Report for Analysis Atoms

## Claim

### Prose Claim


the CAPRMEDIO Project Configuration contribution to `Atom/(.Header.Role := "Analysis & Advisory").Header.Form`.


the CAPRMEDIO Project Configuration **must** register FPF Analysis Report as an additional value of `Atom/(.Header.Role := "Analysis & Advisory").Header.Form` under CA-R-1286. this registration does **not** change the Core contribution under CA-R-1232@28 **or** create another Form Property.

## Details

CA-R-1889 defines the registered Form. CA-D-581 defines its filename token. The Form remains within Role Analysis & Advisory.

