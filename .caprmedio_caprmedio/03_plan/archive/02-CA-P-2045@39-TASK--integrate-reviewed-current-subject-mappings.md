---
atom_id: CA-P-2045@39
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject
  depends_on:
  - Atom
  - Subject
  - Term
  - Property
  - Carrier
  - Scope Unit
  - Projection
  - Plan
  - Operator
version: 39
updated_at: 2026-10-24 06:04:10 +0400
relations:
  is_decomposition_of:
  - CA-P-2043
  depends_on:
  - CA-P-2049
tier: 3
---
# Summary

Integrate reviewed current Subject mappings

## Objective

Integrate the fresh Candidate #7 lane results into a complete occurrence ledger without reopening canceled children or importing stale mapping assignments.

## Details

Read .caprmedio_caprmedio/_projection/core-entity-review/presentation/candidate-7.remaining-subject-worklist.json and the seven lane outputs it names. Re-read each current source owner before accepting a row; preserve full-owner coverage, source/version/hash provenance, exact Subject qualifiers and GOVERNS versus DEPENDS_ON direction.

Admit only an evidence-backed Candidate #7 target or an explicit unchanged, held or unresolved disposition. Include Subjects, defining R/D rules, properties, Types and IDs where the source meaning requires them. A classification-only Type change keeps the existing ID only when Summary and Substance are unchanged. Full paths alone do not establish semantic acceptance.

CA-P-2188 and CA-P-2189, the old Candidate #3/#4 packets and all fixed-count manifests are historical/canceled inputs, not current completion gates. Do not require canceled children to be Done and do not create a substitute Plan ID. This task changes no source Atom, ordinary content, code, schema, MCP, test, Settings or runtime.

### Definition of Done

Not Done if the fresh worklist or any lane output is missing/stale, whole-owner or occurrence coverage is incomplete, a mapping is guessed, unresolved/held rows disappear, or the ledger is treated as source application, graph admission or content authorization. The actual source effect and later frontier verification remain separate.
