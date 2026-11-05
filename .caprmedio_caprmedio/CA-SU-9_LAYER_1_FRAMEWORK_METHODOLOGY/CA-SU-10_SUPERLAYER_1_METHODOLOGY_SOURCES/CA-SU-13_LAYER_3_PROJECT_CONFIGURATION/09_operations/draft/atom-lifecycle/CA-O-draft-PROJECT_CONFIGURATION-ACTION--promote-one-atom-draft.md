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

This Action publishes one exact selected Draft for one non-container Atom under the applicable model. It rejects containers, descendants, cascades, implicit archival, and overwrites.

## Claim

Derive carrier filename and location under [CA-D-568](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/draft/lifecycle-in-place-edits/CA-D-568@20-draft-CORE_META_MODEL-DECISION--bind-draft-identity-continuity-evidence.md). Read the selected Draft, require unchanged selection and Draft status, and apply [CA-R-1432@28-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1432@28-draft-CORE_META_MODEL-RULE--classify-admitted-atom-changes-by-semantic-effect.md) safety checks. The supplied Status must be Current under [CA-R-1521@33-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1521@33-draft-CORE_META_MODEL-RULE--resolve-lifecycle-changes-from-applicable-status-models.md); do not require a predecessor to remain Current.

Apply [CA-R-1630@42-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1630@42-draft-CORE_META_MODEL-RULE--gate-atomic-admission-and-promotion.md), [CA-R-1432@28-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1432@28-draft-CORE_META_MODEL-RULE--classify-admitted-atom-changes-by-semantic-effect.md), and [CA-R-1788@19-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1788@19-draft-CORE_META_MODEL-RULE--refresh-updated-at-whenever-an-atom-changes.md) for admission, identity, Version and publication time. Publish with the supplied Status and read back the Current carrier. Attempt the publication event under [CA-R-807@35-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-807@35-draft-CORE_META_MODEL-RULE--record-replacement-transitions-in-the-journal.md), then delete the Draft.

### Outputs

`savedCurrentAtom`: the verified Current carrier; `removedDraft`: the removed selected Draft. Diagnostic/failure results follow [CA-R-1432@28-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-1432@28-draft-CORE_META_MODEL-RULE--classify-admitted-atom-changes-by-semantic-effect.md); Journal append warnings follow [CA-R-807@35-draft](../../../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/lifecycle-in-place-edits/CA-R-807@35-draft-CORE_META_MODEL-RULE--record-replacement-transitions-in-the-journal.md).
