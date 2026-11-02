---
atom_id: CA-A-1288
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Model::CAPRMEDIO::Graph Syntax
version: 1
updated_at: 2026-10-29 03:18:20 +0400
relations: {}
tier: 3
---
# Summary

Execute named Selections to obtain their defined results

## Decision

Use execute_selection() as the explicit operation name in the deferred Selection-execution proposal. It replaces the tentative materialize() spelling; no alias or second equivalent method is proposed.

```text
@(Selection//All Scope Units Names).execute_selection()
```

The @ expression links to the named Selection entity; it does not materialize its result. The // operator identifies the named Selection instance, not a narrower kind. Calling execute_selection() evaluates that Selection and returns its declared result. All Scope Units Names returns names; a Selection defined to return Scope Unit objects returns objects. The Selection defines both membership and the output being selected, so callers do not need an additional property-extraction operation for the Names Selection.

A proposed membership constraint can use the result:

```text
atom.scope_owner[string, in @(Selection//All Scope Units Names).execute_selection()]
```

This keeps the link, operation and returned values distinct. It does not introduce or register an actual named Selection, rename an Atom property or define a storage/cache policy.

## State

This is a separate deferred Specification Proposal under CA-A-1282, not admitted current syntax. No Core Definition, executable workflow, parser or runtime implementation is changed.
