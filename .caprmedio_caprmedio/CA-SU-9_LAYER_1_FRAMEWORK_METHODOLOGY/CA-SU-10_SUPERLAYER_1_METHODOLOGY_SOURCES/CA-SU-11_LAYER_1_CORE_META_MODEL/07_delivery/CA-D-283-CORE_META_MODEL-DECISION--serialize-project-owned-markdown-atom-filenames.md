---
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/File.Filename
  passive:
  - CAPRMEDIO_MODEL <+ Atom.Header.ID
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Content.Summary
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
  - CAPRMEDIO_MODEL <+ Atom.Header.Label
version: 32
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-283
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize Project-Owned Markdown Atom Filenames

## Claim

### Prose Claim


Identified Project-owned Markdown Atom filenames other than Plan filenames governed by CA-D-469.


**every** identified Project-owned Markdown Atom filename other than a Plan filename governed by CA-D-469 **must** match `<ATOM_ID>[-<CURRENT_SCOPE>][-<TIER>][-<LABEL>][-<TARGET_SCOPE>]--<SUMMARY_SLUG>.<EXT>`. When present, the `LABEL` segment uses the Atom's effective Label: its explicit Label when present, otherwise its Form name under CA-R-2705. Normalize that token under CA-D-284; an explicit Label replaces the Form name there and does not change the Atom's Form. **every** same-identity Atom Version **must** preserve its exact assigned Atom-ID segment **in** its Carrier filename **and** serialize its retained Summary under CA-D-282. A Draft filename uses the Draft marker as its Atom-ID segment as specified by CA-D-650. An Archived predecessor uses `<canonical-ID>@<old-version>` exactly once in that segment under CA-D-289; do not append a duplicate version suffix. Existing legacy archive filenames are not normalized automatically. a replacement filename **must** contain the successor Atom ID **and** the successor's Summary Slug; a Summary Slug **must not** be edited independently of its source Summary.

## Details

The `TIER` segment follows CA-D-651. It is mandatory for numeric Tier `0` and carries the registered `SCOPE_CONTRACT` token; for other Tiers its presence and numeric encoding follow the applicable filename grammar. Omitting an optional token does not omit, default or change the mandatory stored Tier. `SCOPE_CONTRACT` is the Tier representation, not the Atom's Form or effective Label. Do not restore `PRINCIPLE` or another unregistered legacy Tier token. A legacy filename remains nonconformant until its affected Carrier and references have an explicit migration disposition; old names are not grandfathered by this rule.

This generic Project-owned Carrier rule does not replace the dedicated filename rules for an Operator-owned Project Goal. It does not invent a default numeric Tier or revive the retired named/default-Tier rules.
