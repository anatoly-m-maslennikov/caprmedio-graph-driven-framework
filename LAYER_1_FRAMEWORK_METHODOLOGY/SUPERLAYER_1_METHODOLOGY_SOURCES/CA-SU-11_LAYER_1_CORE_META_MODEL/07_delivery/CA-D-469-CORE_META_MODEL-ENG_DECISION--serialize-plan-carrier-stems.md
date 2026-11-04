---
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/File
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Label
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Work Sequence Number
  - CAPRMEDIO_MODEL <+ Atom.Content.Summary
  - CAPRMEDIO_MODEL <+ Atom.Header.ID
  - CAPRMEDIO_MODEL <+ Carrier
version: 25
updated_at: 2026-11-03 23:25:51 +0400
relations: {}
atom_id: CA-D-469
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize Plan Carrier stems

## Claim

### Prose Claim


identified Plan Carrier stems.


**every** identified Plan Carrier stem **must** use `[<WORK_SEQUENCE_NUMBER>-]<ATOM_ID>[-<LABEL>]--<SUMMARY_SLUG>`, with `.md` **only** on its File Carrier.

- the optional Label is a navigation token, **not** an Atom Type token; normalize it under CA-D-284.
- render the Summary under CA-D-282.
- **by default**, direct Plans decomposing the same Hub use unique leading Work Sequence Numbers **before** their Atom IDs, under CA-D-381 **and** CA-R-997.
- a same-bundle Directory Carrier **and** File Carrier use the same stem; number **or** Label changes preserve Atom identity **and** do **not** declare `BLOCKS`.
