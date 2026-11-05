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

Archive one Current Atom

## Claim scope

This Action operates on one exact selected non-container Current Atom. Archived inputs, containers, descendants, inferred replacements, and overwrites are invalid.

## Claim

Derive carrier filename and location under [CA-D-568](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/draft/lifecycle-in-place-edits/CA-D-568@20-draft-CORE_META_MODEL-DECISION--bind-draft-identity-continuity-evidence.md). Resolve the exact Current source; when nested Update supplied `expectedSource`, compare the original read with it before any effect, otherwise capture that read as `expectedSource`. Apply [CA-R-1432@28-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1432@28-draft-CORE_META_MODEL-RULE--classify-admitted-atom-changes-by-semantic-effect.md) safety checks and its expected-source comparison at the write boundary; [CA-R-1521@33-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1521@33-draft-CORE_META_MODEL-RULE--resolve-lifecycle-changes-from-applicable-status-models.md) supplies the applicable `Archived` status.

Write the archived carrier and read it back. [CA-R-1432@28-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1432@28-draft-CORE_META_MODEL-RULE--classify-admitted-atom-changes-by-semantic-effect.md) governs Version and failure handling, [CA-R-1788@19-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1788@19-draft-CORE_META_MODEL-RULE--refresh-updated-at-whenever-an-atom-changes.md) timestamps, and [CA-R-807@35-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-807@35-draft-CORE_META_MODEL-RULE--record-replacement-transitions-in-the-journal.md) the archived-predecessor Journal append.

### Outputs

`savedArchivedAtom`: the verified archived carrier. Diagnostic/failure results follow [CA-R-1432@28-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1432@28-draft-CORE_META_MODEL-RULE--classify-admitted-atom-changes-by-semantic-effect.md); Journal append warnings follow [CA-R-807@35-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-807@35-draft-CORE_META_MODEL-RULE--record-replacement-transitions-in-the-journal.md).
