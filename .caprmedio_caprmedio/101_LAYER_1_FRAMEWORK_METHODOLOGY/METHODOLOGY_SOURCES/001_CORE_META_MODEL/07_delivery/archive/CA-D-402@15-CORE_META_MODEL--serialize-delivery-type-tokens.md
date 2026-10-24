---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery/Type'
  depends_on:
  - Subject/Engineering/Carrier
version: 15
updated_at: 2026-10-23 23:43:05 +0400
relations: {}
atom_id: CA-D-402@15
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
status: Archived
author: Anatoly Maslennikov
global_tier: 11
---
# Summary

Serialize Delivery Type Tokens

## Scope

the serialization of Delivery Type tokens in a Delivery Atom File Carrier filename.

## Claim

a Delivery Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283-CORE_META_MODEL-DELIVERY--serialize-project-owned-markdown-atom-filenames **and** CA-D-284-CORE_META_MODEL-DELIVERY--serialize-filename-token-case:

- Eng Policy: `ENG_POLICY`.
- Eng Decision: `ENG_DECISION`.
- Release Definition: `RELEASE_DEFINITION`.
- Environment Definition: `ENVIRONMENT_DEFINITION`.

these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.

## Details

The YAML `type` field remains the single admitted Type value under CA-D-276; a filename Type token is only its carrier encoding, not a second Type or a Label. An explicit `label` field is the effective Label when present; when absent, the effective Label is derived from the Atom Type name under CA-R-1594. Do not infer Type from a filename token or from that derived Label.

Release Definition and Environment Definition remain outside PROGRAMMATIC and its declared descendants under CA-R-1665; CA-R-2123 governs the Method and Delivery Type restriction in that scope.
