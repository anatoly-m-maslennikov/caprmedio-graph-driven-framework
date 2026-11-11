---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Identity.ID
  passive:
  - 'CAPRMEDIO_MODEL <+ Atom.Header.State.Status: Draft'
  - CAPRMEDIO_MODEL <+ Atom.Header.State.Version
  - CAPRMEDIO_MODEL <+ Atom
version: 20
updated_at: 2026-11-03 22:28:39 +0400
relations:
  depends_on:
  - CA-D-650
  - CA-D-378
  - CA-D-446
atom_id: CA-D-568@20-draft
status: Draft
tier: 4
role: Delivery
form: Decision
---
## Summary

Bind Draft Identity Continuity Evidence

## Claim

Draft marker and carrier representation follow the applicable lifecycle point. Admission follows [CA-R-1630](../../../04_requirement/draft/lifecycle-in-place-edits/CA-R-1630@42-draft-CORE_META_MODEL-RULE--gate-atomic-admission-and-promotion.md).

- Draft `atom_id` and marker encoding follow [CA-D-378](../CA-D-378@30-draft-CORE_META_MODEL-DECISION--serialize-assigned-atom-identities.md) and [CA-D-446](../CA-D-446@29-draft-CORE_META_MODEL-DECISION--give-every-non-draft-atom-revision-one-identifier.md); filename identity-segment serialization follows [CA-D-650](../CA-D-650@15-draft-CORE_META_MODEL-DECISION--serialize-numbered-version-qualified-draft-atom-filenames.md). The tool derives the Draft filename, path, and destination from logical `Scope`, `Role`, `Form`, `Status`, and `Summary`, its derived marker and Version, and Project rules. An agent or caller does not supply a generated filename, output path, or destination. Existing source selectors retain their declared input contract.
- Do not restore an old ID from archive or other history, do not release historical IDs for reuse, and do not make a canonical ID a Draft property or separate artifact.
- [CA-R-1432](../../../04_requirement/draft/lifecycle-in-place-edits/CA-R-1432@28-draft-CORE_META_MODEL-RULE--govern-atom-lifecycle-identity-and-version.md) governs semantic identity and Version outcomes; [CA-R-1788](../../../04_requirement/draft/lifecycle-in-place-edits/CA-R-1788@19-draft-CORE_META_MODEL-RULE--initialize-version-creation-timestamp.md) governs timestamps; and [CA-R-807](../../../04_requirement/draft/lifecycle-in-place-edits/CA-R-807@35-draft-CORE_META_MODEL-RULE--record-replacement-transitions-in-the-journal.md) governs Journal effects.
