---
atom_id: CA-P-1912
content_role: Plan
type: Plan
label: Task
work_sequence_number: 28
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Projection
  depends_on: [Entity, Term, Atom, Property, Carrier, Plan]
version: 2
updated_at: "2026-10-10 23:24:00 +0400"
relations:
  is_decomposition_of: [CA-P-1872]
  blocks: [CA-P-1969]
---
# Summary

Verify the migrated Core graph reproduction

## Objective

Verify that the approved migrated Core Subjects reproduce the separately accepted graph without unexpected source or meaning changes.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent.

This Task owns the sole migration reproduction receipt consumed by CA-P-1969. Check the exact approved minimum grammar-body exception allow-list, preserved ordinary content/all unrelated frontmatter, and actual Version/time/status/history/recording effects. Use an independently authored expected ledger rather than the producer as its own oracle; fixture producer corruption must fail.

Readiness condition: CA-P-1911 is Done. Inputs: its exact changed source snapshot and applied-change record, the authorized preview and grammar contracts, CA-P-1909's separately accepted graph and hash, and the complete occurrence and node ledgers.

Read the migrated Core and rebuild into a new derived projection without changing authoritative sources, old outputs or history. Compare qualified nodes, graph-owned relations and directions, inherited constraints, allowed values, source references and all ledger dispositions with the accepted graph. Check source-backed Carrier bindings separately: `@` remains display notation, not a serialized Subject operator unless separately admitted. Planned drop/consolidation/generalization marks are traceable decisions, not automatic node or historical deletion.

Verify the exact allowed before/after changes, required revisions and grammar checks, preserved excluded and unrelated files, and absence of unexpected Core meaning changes. Bind current source identities, versions and hashes. Explain every difference; an unresolved mismatch or unsupported region is not reproduction success. Report failures with the authorized recovery boundary instead of repairing or replaying migration.

Output: the new reproduced derived graph and its canonical hash, exact source/grammar pins, accepted-versus-reproduced comparison, complete ledger coverage and preservation report. Confirm that only the approved changes occurred and all required checks were actually performed.

Exclusive scope: read-only migrated sources and evidence, a new separate derived projection, and verification/handoff records only. No source, grammar, code, runtime, binding or history repairs; no old-output overwrite and no live MCP execution or Run/Journal claim. Full native MCP delivery and its actual admission, runtime and receipt gates remain separate and pending; local reproduction cannot complete the whole Epic.

Inherit CA-P-1872's explicit 90% confidence threshold and local-without-MCP authorization. Ask the Operator before deciding below that threshold. Split into bounded direct child Plans before execution if the ready work cannot fit 15 minutes. Creation of this Task does not start, authorize or complete this stage.

### Definition of Done

the Plan is **not** Done **if** ((CA-P-1911 is **not** Done) **or** (the new separate projection, canonical hash, current source/grammar pins, comparison, complete ledgers **or** preservation report is missing) **or** (a required qualified node, relation, constraint, allowed value, source reference **or** Carrier binding fails to reproduce the accepted graph) **or** (an unexpected source/meaning change, lost historical reference, unapproved deletion **or** unsupported serialization is found) **or** (a required check is failed, stale, unresolved **or** unverified) **or** (verification changes an authoritative source, old output, code, runtime, binding **or** history) **or** (uncertainty below the confidence threshold was silently resolved **or** work exceeds the admitted boundary) **or** (any direct decomposing Plan is **not** Done)).
