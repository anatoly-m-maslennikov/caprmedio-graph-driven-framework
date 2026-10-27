---
atom_id: CA-R-1840
content_role: Requirement
type: Rule
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 19
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Data Handling/Data Validation
  depends_on:
  - Subject/Graph Node/Implementation/Code/Tool
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow//Applicable Methodology Compilation'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.Version Number
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Domain/Continuant/Projection
relations: {}
tier: 3
---
# Summary

Assess every Applicable Methodology conflict while retaining candidates and proposal boundaries.

## Scope

The deterministic CA-O-153 assessment boundary after one complete selected source frontier.

## Claim

`COMPILE_APPLICABLE_METHODOLOGY` **must** report every detected applicable-methodology conflict and its deterministic candidate proposal without silently dropping, merging, reordering, or editing a source.

## Details

Assessment consumes one CA-R-1839 frontier and produces a digest-bound report of complete boundary, identity, definition, replacement, incompatibility, priority, output-path, stale/currentness, and coverage findings. Every finding retains all involved source references and exactly one deterministic proposed selection or correction proposal; a proposal is neither a selected result nor authority to change a source.

An exact current Operator decision may select an already-existing candidate only when the conflict, proposed selection, and frontier digest are covered by that actual decision together with independently verified admitted Run and effect evidence. A Journal reference may accompany those inputs as observational provenance, but Journal presence or digest is not permission, proof, completion, or recovery authority. A conflict requiring a source correction produces a separately authorized correction proposal instead. Source ordering, revision freshness alone, configuration precedence, an LLM inference, or a TOML or Journal record alone must not resolve a conflict. Before a selected decision can support publication, the Tool reselects and reassesses the then-current frontier under CA-R-2118.

The result is `{ outcome: "assessed", source_frontier_digest, conflicts, proposals, decision_statuses, evidence_refs }`; an unresolved, unsupported, stale, or incomplete finding sets `publishable: false`. Assessment performs no source mutation, no projection mutation, and no invented Journal event.

### Sources

- CA-O-011 v12 and CA-O-153 v2; CA-O-005 v8.
- CA-P-1442 v1, conflict and approval scenario walk; CA-A-1142 v2, W13 handoff.
