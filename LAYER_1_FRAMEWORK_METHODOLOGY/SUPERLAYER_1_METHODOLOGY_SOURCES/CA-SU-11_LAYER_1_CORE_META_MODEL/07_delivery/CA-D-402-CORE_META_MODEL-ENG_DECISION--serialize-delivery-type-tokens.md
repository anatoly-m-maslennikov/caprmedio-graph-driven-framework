---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery).Header.Form'
  passive:
  - CAPRMEDIO_MODEL <+ Carrier
version: 27
updated_at: 2026-11-02 00:55:09 +0400
relations: {}
atom_id: CA-D-402
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize Delivery Type Tokens

## Claim

### Prose Claim


the serialization of Delivery Type tokens in a Delivery Atom File Carrier filename.


a Delivery Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283-CORE_META_MODEL-ENG_DECISION--serialize-project-owned-markdown-atom-filenames **and** CA-D-284-CORE_META_MODEL-ENG_DECISION--serialize-filename-token-case:

- Eng Policy: `ENG_POLICY`.
- Eng Decision: `ENG_DECISION`.
- Release Definition: `RELEASE_DEFINITION`.
- Environment Definition: `ENVIRONMENT_DEFINITION`.

these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.

## Details

The YAML `form` field carries the Atom Form under CA-D-657; a filename Type token is only its carrier encoding, not a second Type or a Label. An explicit `label` field is the effective Label when present; when absent, the effective Label is derived from the Atom Type name under CA-R-2705. Do not infer Type from a filename token or from that derived Label.

Release Definition and Environment Definition remain outside PROGRAMMATIC and its declared descendants under CA-R-1665; CA-R-2123 governs the Method and Delivery Type restriction in that scope.
