---
atom_id: CA-P-2249@10
content_role: Plan
type: Plan
label: Task
work_sequence_number: 14
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Engineering/Action
  - Subject/Engineering/Workflow
  - Subject/Domain/Node/Continuant/Governing Configuration
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/History
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 10
updated_at: 2026-10-24 20:46:49 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
  blocks:
  - CA-P-2251
tier: 3
---
# Summary

Align Scope Unit Query and Read contracts

## Objective

Operation-specific Scope Unit Query and full Read contracts are independently accepted before their implementation.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Split concrete work larger than this bound into actual bounded children before execution. The Operator authorizes this bounded contract-authoring packet and its separate independent acceptance now. No implementation, runtime activation or migration is authorized.

Author the missing bounded R/M/E/D/O refinements of the shared Connector Core API. Define explicit logical Scope Unit identity/query, allowed filters, actual state and optional pin/history behavior, empty/multiple/not-found results, authorization, stable errors and effect-free reads. CA-O-046/047 are Atom-only; CA-D-622 alone is not an admitted Scope Unit operation binding. Deliver exact current/predecessor pins to a different independent reviewer. A packet-ready handoff permits review while this author Task is Active; neither author assertions nor Task status substitute for accepted manifest.

The author does not independently accept this packet. A precise accepted/rejected source manifest from a different reviewer is required; resolve blocking findings and re-review changed pins before Done.

Deliver the exact changed or reviewed manifest and focused check results to the independent integration/verification owner. Preserve historical receipts. No database build, new transport, Atom deletion, automatic batch retry/resume or publication-concurrency mechanism is included.

### Completion checkpoint

The actual [independent Scope Unit Query/Read acceptance](../../../_projection/core-entity-review/stage2/tools-first/scope-unit-query-read-contract-acceptance.md) is PASS for ten current operation-specific sources: Query CA-R-1937/CA-M-377/CA-E-629/CA-D-626/CA-O-211 and Read CA-R-1938/CA-M-378/CA-E-630/CA-D-627/CA-O-212, with 24 exact prior states. Its SHA256 is `00c88c994ff3087802694b337dab22853759c711de99d77120f5fb8129ea9fc8`. Root released closure only after this different-reviewer acceptance; author checks did not release it.

This Done state records source-contract acceptance only, not implementation, functional/runtime proof or live capability. The complete accepted 98-source RMEDO set is input to active CA-P-2251's approved read-only FPF review; no analytical result is claimed yet. All later implementation/fixture, applicable Core alignment and deferred retry/resume/publication gates remain binding.

### Definition of Done

The Plan is **not** Done if any required operation-specific source is absent, inconsistent or unpinned; exact history or a different reviewer's actual acceptance is missing; generic API readiness substitutes for the missing binding; or forbidden surfaces change. Own work must not exceed 15 minutes without prior decomposition.
