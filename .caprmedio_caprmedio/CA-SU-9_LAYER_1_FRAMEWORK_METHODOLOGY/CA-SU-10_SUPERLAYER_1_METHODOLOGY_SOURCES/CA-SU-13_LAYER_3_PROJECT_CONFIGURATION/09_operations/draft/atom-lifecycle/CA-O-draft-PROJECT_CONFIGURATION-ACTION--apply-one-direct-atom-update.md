---
atom_id: CA-O-draft
role: Operations
form: Action
status: Draft
version: 1
updated_at: '2026-11-03 19:01:50 +0400'
tier: 3
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Action'
  passive:
    - 'CAPRMEDIO_MODEL <+ Atom'
    - 'CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION'
relations: {}
---
## Summary

Apply one Direct Atom Update

## Claim scope

One exactly selected non-container Atom and its requested changes.

## Claim

Derive carrier filename and location under [CA-D-568](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/draft/lifecycle-in-place-edits/CA-D-568@20-draft-CORE_META_MODEL-DECISION--bind-draft-identity-continuity-evidence.md). Resolve the exact non-container target once, preserve expected source/currentness, and apply [CA-R-1432@28-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1432@28-draft-CORE_META_MODEL-RULE--classify-admitted-atom-changes-by-semantic-effect.md) safety checks and identity/Version rules; [CA-R-1788@19-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1788@19-draft-CORE_META_MODEL-RULE--refresh-updated-at-whenever-an-atom-changes.md) governs timestamps.

- **Draft:** edit content in place, including semantic Draft edits, and leave Current untouched.
- **Current:** allow only technical in-place edits preserving meaning, identity, Summary, Role and Status; synchronize filename/location. A semantic request is an explicit error; the caller may separately select Update.
- **Archived:** allow only technical in-place edits preserving identity, meaning and Status; synchronize filename/location. Do not publish Current or promote a Draft; semantic or identity changes are explicit errors.

Save and read back the carrier. For an actual business event, append its Journal record under [CA-R-807@35-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-807@35-draft-CORE_META_MODEL-RULE--record-replacement-transitions-in-the-journal.md).

### Outputs

`savedAtom`: the verified saved carrier. Diagnostic/failure results follow [CA-R-1432@28-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1432@28-draft-CORE_META_MODEL-RULE--classify-admitted-atom-changes-by-semantic-effect.md); Journal append warnings follow [CA-R-807@35-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-807@35-draft-CORE_META_MODEL-RULE--record-replacement-transitions-in-the-journal.md).
