---
atom_id: CA-P-2335
ref_id: CA-P-2335
container:
  atom: CA-P-2307
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Continuant/Tool
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Relation
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2307
status: Done
version: 6
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 10-CA-P-2335-TASK--replace-untyped-toml-rule-relations.md
    path: .caprmedio_caprmedio/03_plan/30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/21-CA-P-2256-TASK--implement-toml-item-and-full-set-edits/done/2-CA-P-2307-TASK--select-tomlkit-for-preserving-configuration-text/done
work_sequence_number: 10
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
---
# Summary

Replace untyped TOML rule relations

## Objective

M383, D632 and E635 carry meaningful admitted typed relations instead of relates_to.

## Details

Estimated own work: up to 15 minutes. The Operator rejected a context-only workaround and requires typed relations. Review every existing broad link against source content and the admitted Relation Kind definitions. Do not substitute a generic related_to alias, invent a kind, or force an incorrect type just to preserve an edge. Identify inverse relations already owned by another Atom and ask about unclear or removed links before mutation.

Independently review the mapping first, then narrowly update the three source relation collections with exact predecessor archives, Version +1 and actual Updated At. Keep Summary, Subjects and body content unchanged unless a concrete approved correction requires otherwise. Independently check the final sources and run actual finite PRMEDO admission. Keep C/A, live publication and Core migration outside this task.

### Definition of Done

The Plan is not Done if a relation is untyped, an endpoint is silently lost or guessed, current source admission fails, exact predecessor history is missing, or independent semantic and final-source review is absent.

### Accepted outcome

All 21 broad links were independently adjudicated: eight became evidenced typed relations, thirteen redundant/contextual pointers were removed under Operator approval, and five existing precise edges remain. Exact predecessor archives, unchanged bodies and other metadata passed independent review. Actual finite PRMEDO complete-carrier admission passed M383 v3, D632 v3, E635 v2 and P2307 v8 with 13 checks each, zero findings/gaps, no relation bypass and all twelve source/target/parent-chain pins current. See typed-toml-relations-acceptance.md in the tools-first evidence directory. This closes the source gate, not TOML implementation or runtime readiness.
