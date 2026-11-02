---
atom_id: CA-A-1260@1
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Formal Model
version: 1
updated_at: 2026-10-28 21:39:15 +0400
relations: {}
tier: 3
---
# Summary

Connect Workflow definitions, runs and Event Records

## Decision

Add the requested direct connections: Workflow Run ((IS_EXECUTION_OF)) Workflow; Event Record ((RECORDS)) Workflow Run. A Workflow is a reusable definition, Workflow Run an actual Occurrent, and Event Record a persistent description in Journal. None is the same thing as another.

Prepare HAS_EXECUTION as the derived inverse name of IS_EXECUTION_OF, and IS_RECORDED_BY as the derived inverse name of RECORDS. These names are proposed in the Relation Definition Drafts, not automatically registered runtime behavior. Store each direct fact once; derive the opposite view.

The general RECORDS meaning is not limited to Workflow Runs: an Event Record can describe other actual occurrences. No universal one-record-per-run, one-run-per-record or record-existence obligation is introduced. R1510 already requires exactly one Workflow definition per Workflow Run; its prepared successor makes that binding formal.

## Prepared Drafts

- CA-R-draft-CORE_META_MODEL-DEFINITION--define-is-execution-of-relation.md
- CA-R-draft-CORE_META_MODEL-DEFINITION--define-records-relation.md
- CA-R-1510@17-draft successor: Workflow Run binding.
- Existing Event Record Definition Draft, refined in place.

## Scope

This increment defines the two requested links. Runtime ((EXECUTES)) Workflow Run remains an earlier example awaiting its own Relation Definition. No actual Runs, Journal facts, Current sources, parser or runtime are changed.
