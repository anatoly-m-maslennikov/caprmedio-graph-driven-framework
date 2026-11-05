---
atom_id: CA-A-1291
ref_id: CA-A-1291
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Model::CAPRMEDIO::Graph Syntax.Format Notation
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 15:49:28 +0400
carrier_destination:
  file:
    name: CA-A-1291-CAPRMEDIO-SPECIFICATION_PROPOSAL--materialize-value-expressions-inside-format-conditions.md
    path: .caprmedio_caprmedio/02_analysis
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Materialize value expressions inside format conditions

## Decision

The bracket annotation [format, condition] establishes a value-evaluation context. Expressions there are materialized to the values needed to check the format and condition. An explicit materialization or execution function can be omitted.

```text
atom.version_number[int, >=1]
atom.scope_owner[string, in Selection//All Scope Unit.Name]
```

In the membership example, // identifies the named Selection All Scope Unit. The Selection is evaluated and .Name obtains each selected Scope Unit's Name, yielding the list of allowed strings. This is not the Selection entity's own Name. The condition checks each direct owner value against that result.

@ remains a graph-entity link, not materialization by itself. Within the bracket value context, linked or directly named operands supply their values before the condition is checked. Ordinary Model paths outside that context keep their declared graph meanings; this does not globally redefine property access.

## Scope

This refines A1290 by defining its value context and removes the need for the explicit call discussed in A1288 for this use. The explicit execute_selection() API remains a separate deferred proposal. General ID-composition formulas and arbitrary function-language grammar remain deferred under A1282. This decision admits the illustrated lower-bound and Selection-membership conditions into prepared syntax without implementing an evaluator, registering a Selection, renaming an Atom field or imposing a cache/storage policy.

## State

A Value Constraint Annotation Definition Draft and related R/M/E/D syntax Drafts are prepared. The main Model shows the already-required Version Number lower bound using the annotation. Current sources, tools and runtime are unchanged.
