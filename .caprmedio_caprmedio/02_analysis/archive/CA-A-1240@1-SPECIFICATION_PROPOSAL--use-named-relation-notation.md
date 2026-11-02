---
atom_id: CA-A-1240@1
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Formal Model
version: 1
updated_at: 2026-10-28 19:00:34 +0400
relations: {}
tier: 3
---
# Summary

Use Named Relation Notation

## Decision

The Operator accepted `Source ((RELATION_TYPE)) Target` as the general notation for a Relation without a short spelling, including the three examples below. No separate backward notation is needed because reverse navigation uses each Relation's defined derived inverse. This is a notation decision, not source admission of undefined Relation Types or approval of a parser/runtime change.

### General named-relation notation

`Source ((RELATION_TYPE)) Target` expresses the named directed Relation from Source to Target. Use this general form where no short operator exists; it may also spell a defined Relation explicitly without changing its meaning. The name between `((` and `))` identifies one declared Relation Type, not a new kind, arbitrary prose label or automatically registered Relation. Endpoint restrictions and counts come from the Relation definition and applicable Graph Rules.

There is no separate backward notation. To navigate or display the opposite direction, use the defined derived inverse Relation name in the same form with the endpoints exchanged. Persist the direct fact only, not a second independent inverse fact. No inverse name or inverse meaning is guessed from spelling.

The matching unescaped `((` and `))` delimit the Relation Type name. Existing backslash escaping handles literal delimiter characters. Existing `/`, `//`, `.`, `:`, `::`, `>`, `@(...)` and format/cardinality annotations keep their meanings. The double parentheses are relation syntax, not a function invocation. This decision defines a binary relation expression; it does not silently choose precedence for arbitrary mixed chains or turn a whole relation statement into a node selector for subjects.governs.

The Operator supplied these schema-level examples:

```text
Workflow Run ((IS_EXECUTION_OF)) Workflow
Event Record ((RECORDS)) Workflow Run
Runtime ((EXECUTES)) Workflow Run
```

These expressions connect modeled kinds and do not create actual Runs or records. Their Relation Type definitions and derived-inverse declarations must be authored before source admission; notation alone does not establish that they are already registered. The Runtime in the last expression is the live executor, not the Engineering topic or stored engine Code.

## Draft adoption

The existing successor Drafts R1931@13, R2150@11, M228@29, M232@27, E383@35 and D269@25 are refined in place. The Formal Model primary/properties review Draft CA-A-1239@1-draft includes the decision and examples. No Current RMED source is promoted or migrated. Existing stored direct/inverse policy is retained; no new reverse operator, Relation Type, endpoint permission, cardinality or inference rule is invented by this record.

## Remaining work

Prepare the requested Relation definitions and their declared inverse meanings, then review their endpoint rules before admission. IS_EXECUTION_OF, RECORDS and EXECUTES are not claimed to be registered merely because their names occur here. Formal Claim count constraints discussed separately remain outside this notation-only increment.
