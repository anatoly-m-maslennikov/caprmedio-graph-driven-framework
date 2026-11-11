# Event recording contracts

The proposed chain has three explicitly declared directions: Runtime `EXECUTES` Execution; Execution `PRODUCES` Event; and Event Record `RECORDS` Event. Their reverse Relations are explicitly Derived views, not separately stored facts. The Event Record is distinct from the Event. A Workflow Run retains Runtime execution coverage through Execution inheritance.

The latest decision is represented as follows; only Event Record → Event has an explicit upper bound:

| Relation direction | Proposed count | Meaning |
| --- | --- | --- |
| Event Record → Event (`RECORDS`) | `1` | Every Event Record records exactly one Event. |
| Event → Event Record (`IS_RECORDED_BY`) | `0+` | Recording is permitted but not mandatory for an Event. |
| Event → Execution (`IS_PRODUCED_BY`) | `1+` | Every Event has at least one producing Execution. |
| Execution → Event (`PRODUCES`) | `0+` | An Execution may produce no Events. |
| Execution → Runtime (`IS_EXECUTED_BY`) | `1+` | Every Execution operates in at least one Runtime. |
| Runtime → Execution (`EXECUTES`) | `0+` | A Runtime may execute no work. |

The count clauses belong to the Node endpoint Declarations; Relation-object Declarations carry typed endpoint patterns without duplicate count slots. The inverse Relations remain views of the same facts. The existing Event Record → Journal containment remains unchanged. A bounded Current source scan found no narrower explicit Runtime/Execution subtype count; verify that alongside any later source-specific constraints before adoption. Binding a variable creates no actual instance or Relation fact.

Existing Event Record fields remain in place; the proposed field move is withdrawn. Exactly one Event per Record does not imply inverse uniqueness or that every Event has a record.

The Execution copy overlaps the separate Execution-to-definition lane and needs integration by the owner. R2246's old generic occurrence and direct Workflow Run endpoints are deliberately removed under the latest decision; existing data and consumers need separate reconciliation and must not be silently retargeted. The Node and new Relation Declarations remain unallocated Drafts. Review the pinned packet atomically before promotion; no Current application, data migration, runtime behavior or regression test is claimed.
