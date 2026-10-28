---
subjects:
  governs: Subject
atom_id: CA-R-2006
content_role: Requirement
type: Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
version: 10
updated_at: 2026-10-27 20:00:07 +0400
author: Anatoly Maslennikov
relations: {}
tier: 1
---
# Summary

Define Subject Target Roots

## Scope

Canonical Subject paths.

## Claim

Bare Subject is the umbrella. A more-specific canonical Subject path identifies its namespace immediately after Subject. `Subject/CAPRMEDIO/...` contains shared framework vocabulary; `Subject/<Project Name>/...` contains project-specific concepts.

Under `Subject/CAPRMEDIO`, Graph and Carrier are separate branches. Graph contains Node, Relation and Rule as siblings. Node contains Project Model and Aspect as separate branches.

`Subject/CAPRMEDIO/Graph/Node/Project Model` includes Project, Atom, Governing Configuration, Scope Unit, Actor, History, Projection, Selection, Implementation, Runtime, Event and Execution. These branches retain the existing modeled meanings and their definitions; the list does not retire other source-backed targets by omission.

`Subject/CAPRMEDIO/Graph/Node/Aspect` includes Product, Project, Domain, Engineering, UX, Design and Documentation. `Subject/CAPRMEDIO/Graph/Relation` and `Subject/CAPRMEDIO/Graph/Rule` remain siblings of Node. `Subject/CAPRMEDIO/Carrier` remains outside Graph.

## Semantics

Namespaces distinguish shared vocabulary from project-specific concepts; they are not entity kinds or Scope Units. The owning Scope Unit does not determine an Atom's Subject namespace. Keep the full logical canonical path, including its namespace, when identifying or comparing Subject Targets.

Project Model names modeled things; Aspect names topics or perspectives that may concern those things. The Project Model Project and the Project aspect therefore have distinct meanings. A classification-axis Subject such as `Atom/Content Role` is valid without introducing another entity kind. Its value-qualified descendants name narrower Atom kinds and inherit Atom properties.

Implementation names logical Code, Prompts, Documentation and Resources that realize RMED. It is not a Projection merely because it realizes RMED. Projection names an output derived from its declared sources through a Workflow; edits belong in those sources and the view is rebuilt. Carrier names representation and storage independently of the represented Project Model or Aspect target.

Modeled Execution, Event and Action, Step and Workflow Runs retain their existing meanings as actual performance or occurrences, distinct from reusable definitions and historical records. Technical sessions and process/container execution belong to Runtime. This root rule preserves those definitions without settling every narrower target placement.
