---
atom_id: CA-P-2043
content_role: Plan
type: Plan
label: Task
work_sequence_number: 53
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Subject
  depends_on: [Atom, Subject, Term, Property, Carrier, Scope Unit, Projection, Plan, Operator]
version: 10
updated_at: "2026-10-22 22:05:30 +0400"
relations:
  is_decomposition_of: [CA-P-1966]
  depends_on: [CA-P-2049]
---
# Summary

Integrate current Subject mapping ledger

## Objective

Produce one current Candidate #7 occurrence ledger from the fresh seven-lane worklist, with every owner and occurrence represented as supported target, unchanged, held or unresolved.

## Details

Use .caprmedio_caprmedio/_projection/core-entity-review/presentation/candidate-7.remaining-subject-worklist.json as the sole current ownership/frontier input. Integrate the lane outputs after re-reading current source bodies and preserving source paths, versions, hashes, qualifiers, governing/dependency direction and full literal target paths. Do not add old fixed counts, old manifests or canceled review packets to the ledger.

The ledger covers Candidate #7 methodology only: Subjects, defining R/D rules, properties, Types and IDs. A classification-only Type correction retains the Atom ID only when Summary and Substance are unchanged. Mapping research does not apply source edits, ordinary content updates, tool/schema/MCP changes, tests, Settings changes or runtime effects.

Keep uncertain or below-90% rows explicit and unchanged. A full canonical path is not semantic acceptance without source evidence. Preserve excluded/held owners as whole owners where required; never emit a supported subset of an unresolved or excluded owner.

### Decomposing Plans

- CA-P-2045 — integrate the reviewed current Subject mappings

### Definition of Done

Not Done if the fresh worklist is absent or stale, any lane row is missing or duplicated, source evidence is not current, a target is guessed, unresolved/excluded coverage is hidden, or the result is presented as a migration receipt or live graph. Source application is owned separately by CA-P-1968.
