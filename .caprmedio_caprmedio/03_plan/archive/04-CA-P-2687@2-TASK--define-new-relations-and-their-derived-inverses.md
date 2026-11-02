---
atom_id: CA-P-2687@2
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Formal Model
version: 2
updated_at: 2026-10-28 21:39:15 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2683
tier: 4
---
# Summary

Define new Relations and their derived inverses

## Objective

Define new Relations and their derived inverses.

## Details

After CA-P-2685, CA-P-2686.

Prepare Definition Atoms for the missing Relations, including IS_EXECUTION_OF, RECORDS and EXECUTES where those exact meanings remain supported. Specify direct meaning, both endpoint kinds, applicable cardinalities and the derived inverse meaning/name. Do not infer a type, inverse name or permission merely from its spelling.

Workflow Run executes one Workflow definition; Event Records describe occurrences/runs while Journal contains the records; the live Runtime executes work, not the Engineering topic or stored engine Code. Keep definitions, actual occurrences and records distinct. Bind existing short forms to their correct declared directions without introducing a backwards operator.

Apply endpoint and other valid-structure constraints inside the relevant Definition Claim. Do not create R/Type: Graph Rule instances or replace them with a new Rule population. Examples do not count as registered Relations until their defining sources are ready.

## Definition of Done

The named and short-form Relations have complete Definition Drafts, exact direct/derived directions, endpoint constraints and examples that preserve the approved meanings.

## Progress

Not started. Prior analysis and Drafts are inputs, not completion evidence.

## Prepared execution/record links

CA-A-1260 prepares IS_EXECUTION_OF and RECORDS Definitions, proposed derived inverses HAS_EXECUTION and IS_RECORDED_BY, the existing exactly-one-Workflow binding in a R1510 successor, and the Event Record occurrence link. The Formal Model Draft includes the connections. Current admission and Runtime EXECUTES remain uncompleted.
