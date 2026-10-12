---
atom_id: CA-P-2080
content_role: Plan
type: Plan
label: Task
work_sequence_number: 67
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Projection, Plan, Operator]
version: 2
updated_at: "2026-10-11 05:37:15 +0400"
relations:
  is_decomposition_of: [CA-P-1966]
---
# Summary

Resolve history and methodology mapping meanings

## Objective

Resolve the assigned mapping meanings from evidence without changing authoritative Subjects.

## Details

Estimated own work: at most 15 minutes. Research exactly the four Revision.Status and Applicable Methodology occurrences selected in the input manifest. Use the latest complete history and Applicable Methodology candidate rules together with current definitions and source-specific bodies. Distinguish the derived methodology artifact from the manual realization process and conformance usage. Do not introduce Revision.Status or infer a new historical Property merely because old source text uses it. Do not discard qualifiers to force a mapping.

Exact assigned IDs and input byte pins are in `.caprmedio_caprmedio/_projection/core-entity-review/stage2/semantic-reviews/followups-2078-2080.inputs.json`. Read the latest candidate and Operator decision record, current supplement contracts and exact owning Main Content. Pin every input and source span. Frozen/raw reports remain unchanged; separately pin current grammar. This Task does not claim to resolve other unassigned research.

Output only `.caprmedio_caprmedio/_projection/core-entity-review/stage2/semantic-reviews/task-2080.research.json`: schema_version 1, task_id, non_authoritative true, source_migration/native_admission not_performed, input_pins, and rows. Each assigned occurrence appears once with old_value, prior_disposition, decision (proposed/unresolved), nullable proposed_value, confidence, source evidence and precise reason. All rows executable false. A proposed mapping needs confidence at least 0.90; independent review is still required before ledger acceptance. Unresolved mapping stays null.

No Core, grammar, body, frozen input, runtime, MCP/FPF, Journal or Git writes. Workers are not alone; preserve others' work. Workers own only their output; Root owns Plans and Git. The unanswered conditional-owner notation choice is not inferred. No selector, @ operator, new Carrier binding or native relation is admitted by this research.

### Definition of Done

Not Done if assigned coverage or current evidence is missing, meaning is guessed, a prior qualifier is lost, a pending decision is inferred, an executable source effect is implied, or own work exceeds 15 minutes without decomposition.

### Completion

Researched every one of the 4 assigned occurrences. Root verified exact selection, current input/source/span pins, approved syntax and all rows non-executable. Two Applicable Methodology targets are supported as Projection/Applicable Methodology; manual realization is a process applied to that artifact, not a separate target object. Two historical Status targets remain unresolved; no historical Property or qualifier-dropping replacement is invented.

The receipt preserves independent review separately from the research proposals. Done means this bounded research is finished, not that unresolved mappings, the parent gate or source migration are complete. Version-1 Task input remains in Git at registration commit 82f720f29718f5af60152db8338e79db1d7a1020.
