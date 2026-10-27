---
atom_id: CA-P-2644@1
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom
version: 1
updated_at: 2026-10-26 05:06:46 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2639
tier: 4
---
# Summary

Align archival with preservation of the existing Version

## Objective

Align the conflicting archival contracts with D05: archiving an existing
version does not create a new Version merely for archival.

## Details

Addresses I07/G02. Estimated own work: up to 15 minutes.

- Read Current R1989 and R868 and their directly relevant lifecycle clauses.
  The audit observed R1989@9 and R868@25; reopen Current definitions rather
  than using fixed source pins.
- For standalone retirement of Current CA-R-123 at Version 3, preserve Version
  3 and use its Archived representation CA-R-123@3. Do not generate Version 4
  solely to archive it.
- Preserve the same historical-Version meaning when archiving the predecessor
  of an actual update; the successor receives its normal next Version.
- Reconcile instructions about Archived Status, qualified identity/filename
  and archive location with the Operator's existing representation decisions.
  Do not restore the obsolete exact-old-bytes rule.
- Do not infer a new Updated At policy from this Version decision. Retain
  established timestamp meaning where unambiguous; report a concrete remaining
  timestamp contradiction instead of silently choosing one.
- Preserve existing Drafts and Archives and unrelated sources. Changes to
  Current governing definitions receive their normal predecessor history.
- Record changed source IDs/versions and bounded checks of an update and a
  standalone retirement. Split any wider lifecycle repair into another Task.

Only methodology/source-contract correction is included. No tool, runtime,
Journal implementation or existing-archive normalization is authorized.

## Definition of Done

- Touched contracts do not increment Version solely for archival.
- Standalone retirement and update-predecessor archival preserve the Version
  being archived; a real update still creates the next Current version.
- Archived representation instructions agree with the accepted Status,
  identity and carrier model.
- Any unresolved timestamp conflict is explicit, not reported fixed.
- Actual source changes and predecessor history are recorded separately from
  this Plan; existing historical carriers remain unchanged.
