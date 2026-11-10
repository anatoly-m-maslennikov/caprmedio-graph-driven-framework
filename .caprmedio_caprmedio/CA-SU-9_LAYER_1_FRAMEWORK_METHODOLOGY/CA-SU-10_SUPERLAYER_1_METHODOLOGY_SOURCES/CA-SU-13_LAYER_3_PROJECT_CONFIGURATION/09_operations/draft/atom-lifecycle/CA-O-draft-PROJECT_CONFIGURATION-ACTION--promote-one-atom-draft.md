---
atom_id: CA-O-draft
role: Operations
form: Action
status: Draft
version: 1
updated_at: '2026-11-03 18:54:48 +0400'
tier: 3
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Action'
  passive:
    - 'CAPRMEDIO_MODEL <+ Atom'
    - 'CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION'
relations: {}
---
## Summary

Promote one Atom Draft

## Claim scope

This Action publishes one exact selected Draft for one non-container Atom under the applicable model. Replacement targets explicitly named by the Draft are archived as part of promotion.

## Claim

Resolve every distinct target named by `IS_REPLACEMENT_FOR`, including targets with different IDs and many-to-one replacement. Before publishing the Draft as Current, archive each eligible Current target once and skip every target already Archived, including one archived by composed Update. Preserve archived targets' Version and Updated At. Then publish the Draft using the supplied allowed Current Status and remove its Draft carrier. If Summary or Content Role changed from its source, promote a new identity at Version 1; otherwise retain the existing Draft Version without an additional increment. Derive the filename and location from the model. On an effect failure stop and report completed and incomplete effects. Journal business observations are independent and nonblocking.

For missing or invalid input format or allowed value, give a short explanation and request an additional input dictionary. Wait for it; the caller may cancel while waiting, without interrupting an Action.

### Outputs

`savedCurrentAtom`, archived replacement targets and `removedDraft`, a request for additional input, or an explicit failure; any Journal warning is separate.
