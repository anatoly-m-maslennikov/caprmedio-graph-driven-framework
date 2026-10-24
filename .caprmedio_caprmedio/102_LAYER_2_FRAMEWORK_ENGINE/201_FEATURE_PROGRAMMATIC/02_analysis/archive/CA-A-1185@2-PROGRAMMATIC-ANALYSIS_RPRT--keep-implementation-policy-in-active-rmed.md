---
atom_id: CA-A-1185@2
content_role: Analysis
type: Analysis Report
current_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 6
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: programmatic software
  depends_on:
  - Atom/Content Role: Method
  - Implementation
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Projection
  - Scope Unit
version: 2
updated_at: 2026-10-23 03:06:32 +0400
relations: {}
---
# Summary

Keep implementation policy in Active RMED

## Question

How can the general PROGRAMMATIC prompt prevent invented business logic without spreading feature-specific rules to unrelated implementations?

## Scope

General PROGRAMMATIC Methods, their selected implementation prompt, and the ownership of conditional Methods included in that prompt.

## Analysis

The Operator reports that AI-assisted implementation became overcomplicated: extra behavior cost time and tokens to implement, test and later remove. This is the Operator's assessment, not a measured cost estimate.

An implementation can accidentally become a second specification when an agent fills gaps with extra restrictions, approvals, history checks or workflow steps. Tests can then preserve the invented behavior instead of the intended behavior.

Active RMED should own business decisions. Implementation should realize those decisions. Ordinary technical choices remain the implementer's work; changing business meaning requires the Operator's decision. CA-M-384 records this boundary. It adds no runtime gate and does not authorize removing existing declared protections.

## Conditional Methods and descendant ownership

"Applicable to this task" describes when a Method is loaded; it does not decide which Scope Unit owns the Method.

- Keep shared implementation rules at PROGRAMMATIC: functional core, objects for owned lifecycle, small units, Python environment, file/subprocess safety (M161), structured diagnostics (M163), measurement before optimization (M165), and structured boundary validation (M286). Their conditions can apply across Tools and Apps.
- Keep the shared Settings-reader consumption rule (M284) at PROGRAMMATIC: several descendants use that same boundary. A reader's private implementation rules belong with the reader.
- Review M193, MCP Tool-frontier publication, for relocation to the Scope Unit that owns MCP exposure. Its current procedure governs one capability, not all PROGRAMMATIC implementations.
- Review M191, mutation Initiative propagation, for the appropriate common owner of the affected mutation Workflows. Do not move it to one Tool if several descendants depend on it.

These are ownership candidates from a bounded reading of M161, M163, M165, M191, M193, M284 and M286. The complete Method set and all consumers were not audited. No existing Method is moved or retired by this Analysis. Before relocation, confirm the actual owning Scope Unit and consumers, preserve IDs/history, and update the prompt's source locations.

## Result

Use CA-M-384 in the common implementation prompt. Load additional Methods only when their stated conditions apply. Separate shared conditional rules from descendant-specific rules; do not treat either as permission to invent business behavior.

## Sources

- Operator instructions in this Codex conversation, 2026-10-15: implement only business logic declared in Active RMED; ask about gaps; reconsider task-specific Method ownership.
- Current PROGRAMMATIC Methods M161, M163, M165, M191, M193, M284 and M286, and the compact PROGRAMMATIC Method projection.
