---
atom_id: CA-P-2077@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 64
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject
  - Subject/Domain/Node/Continuant/Projection
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - Subject/Engineering/Tool
version: 6
updated_at: 2026-10-24 08:22:45 +0400
relations:
  is_decomposition_of:
  - CA-P-1966
tier: 3
---
# Summary

Audit current-source drift in mapping evidence

## Objective

Identify exact stale mapping inputs after grammar adoption without silently rebinding them.

## Details

Estimated own work: at most 15 minutes. Root owns this read-only audit and derived output `stage2/current-grammar-source-drift.json`. Compare the pinned inventory and all supplement file/evidence pins with current bytes. Distinguish the approved five-definition grammar effects from unrelated drift and historical captured inputs. Account for the R1204 to R1931 replacement explicitly.

Use existing parsers and small ad-hoc mechanics only. Do not overwrite the frozen inventory, baseline ledger, candidate, reports or sources; do not call stale evidence current or infer a semantic mapping. Keep findings precise enough for later bounded re-review/rebind. A drift audit does not authorize migration or change the captured-snapshot boundary.

### Definition of Done

Not Done if changed/missing/new current source identities or stale referenced pins are hidden, captured evidence is changed, a rebind or source write is implied, current pin hashes are unchecked, or own work exceeds 15 minutes without decomposition.

### Completion

The derived audit accounts for all 907 selected sources and all five approved grammar effects, including the R1204 replacement by R1931. Exactly three old referenced grammar pins are stale; they remain explicitly recorded, not rebound. All 13 input/report file pins passed.

An independent live inventory dry-run confirmed 907 sources, 4,534 Subject occurrences, eight quarantined sources and zero diagnostics. Root's full selected-frontier comparison found no additional IDs or changes beyond the declared replacement. The independent verifier confirmed aggregate counts and replacement presence, not an exhaustive selected-ID comparison.

No source, captured inventory, baseline ledger, candidate or existing report was changed. Raw reports are retained as research evidence; this audit does not semantically accept them or authorize migration. See the derived task-2077 receipt.
