---
atom_id: CA-R-1930@11
content_role: Requirement
current_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-26 00:46:35 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Architecture/Communication
  depends_on:
  - Subject/Graph Node/Engineering/Continuant/Tool.Self Description
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Engineering/Model
  - Subject/Graph Node/Engineering/Tool Discovery Binding
  - Subject/Graph Node/Engineering/Admission
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
tier: 1
type: Rule
---
# Summary

Require uniform Tool self-description

## Scope

The common machine-readable description exposed by every Tool in TOOLS and its child Scope Units.

## Claim

**every** Tool **must** expose one complete canonical description through the same machine-readable interface, so consumers can discover, validate, register, and invoke new or updated Tools without Tool-specific integration logic.

## Details

- The description includes the Tool's identity, version, purpose, accepted inputs, structured results, executable binding, bound Actions, effects, permission requirements, availability and admission conditions, source references, diagnostics, and failure behavior.
- Input and output schemas are derived from the Tool's canonical models rather than maintained as a second source of truth.
- CLI, MCP, and other consumers use this description. Their representation and entrypoint rules belong to Delivery specifications.
- Describing or registering a Tool does not execute it or grant Operator permission. Effect hints describe behavior; they do not authorize it.
- Missing, stale, conflicting, or ambiguous information makes the affected Tool unavailable with attributable diagnostics.
