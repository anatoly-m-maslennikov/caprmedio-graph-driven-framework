---
atom_id: CA-A-1290
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Model::CAPRMEDIO::Graph Syntax
version: 1
updated_at: 2026-10-29 03:20:19 +0400
relations: {}
tier: 3
---
# Summary

Project selected object names through Selection paths

## Decision

Use this readable Selection-result expression in the deferred value-expression proposal:

```text
Selection//All Scope Unit.Name
```

The named Selection is All Scope Unit. In this expression, .Name takes the Name from each selected Scope Unit, producing a list of names. It does not ask for the named Selection entity's own Name. The // remains the named-instance operator, not specialization. This example does not create or register a named Selection.

A proposed membership use is:

```text
atom.scope_owner[string, in Selection//All Scope Unit.Name]
```

The output is a collection of strings. A separate Names Selection, a list comprehension or an explicit execute_selection() call is not required for this property-projection form. This latest choice refines the example in CA-A-1288; the earlier explicit execution operation remains a separate deferred proposal for other uses.

## Boundary

This is proposed value-expression behavior over Selection results. It does not redefine ordinary bearer-to-property model paths or @ graph-entity links. Exact admission and disambiguation from a Selection entity's own property remain part of the deferred expression design, not an implemented parser contract. CA-A-1289's explicit, understandable naming preference remains in force.

## State

Recorded as a separate Specification Proposal under the deferred expression work in CA-A-1282. Current Model syntax Drafts, Core sources and runtime are unchanged.
