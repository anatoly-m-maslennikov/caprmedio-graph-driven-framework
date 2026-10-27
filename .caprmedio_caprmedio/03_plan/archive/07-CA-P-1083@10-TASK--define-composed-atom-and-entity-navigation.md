---
atom_id: CA-P-1083@10
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: 'Projection/Type: Extended Entities Graph'
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.Content
  - Subject/Domain/Node/Continuant/Atom.Subjects
  - Subject/Domain/Node/Continuant/Scope Unit
  - CAPRMEDIO Graph
  - Subject/Domain/Node/Continuant/Projection
  - 'Projection/Type: Atom Subjects Graph'
  - 'Projection/Type: Entities Graph'
  - Subject/Domain/Node/Continuant/Term
  - Subject
  - Subject/Graph/Relation
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan.Autonomous Confidence Threshold'
version: 10
updated_at: 2026-10-25 03:12:46 +0400
relations:
  depends_on:
  - CA-P-1082
status: Archived
current_scope_unit: caprmedio
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Define composed Atom and Entity navigation

the Assignee **must** establish a non-authoritative composed view of direct Atom relations, Subject references, **and** Entity qualification.

## Scope

(selected active RMEDO authority for derived model views **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL` limited **to** composition of already admitted graph facts for navigation); the CA-P-976 admission boundary applies, with accepted source changes from completed Tasks **and** the sealed CA-P-980 direct-Subjects stage. Drafts, archives, generated Applicable Methodology copies, runtime, Tool Implementation, Settings values, **and** unrelated CAP Atoms are excluded. existing execution evidence is read-only.

## Definition of Done

the Task is **not** Done **if** (composition creates an independently authoritative relation fact **or** a displayed relation loses its original graph kind **or** direction **or** source **or** a shared Subject silently creates an authored Atom dependency **or** transitive navigation is presented as a direct source edge).

## Details

reuse the Extended Entities Graph Projection Type defined by CA-R-1459 for the composed Entity **and** Atom view. this Task establishes its detailed navigation from already admitted source facts; it does **not** redefine that Projection Type **or** create another owner for the represented Relation Kinds. retain Atom Subjects Graph under CA-R-1281 as the distinct derived Projection Type of direct Subjects references, including admitted Entity, Action, **and** Process targets; the Extended Entities Graph composes the Entity structure with its governing **and** dependent Atoms **without** collapsing those two Projection purposes. this administrative alignment does **not** execute the Task.

support direct Atom links with their registered relation types, Atom GOVERNS target with other Atoms DEPENDS_ON that target, **and** related Entity targets through admitted bearer **or** allowed-value edges. the composition **may** reuse the Entity-related links of an Atom Subjects Graph **when** available **or** derive those links directly from source Atoms' Subjects under the same governing authority. do **not** require a materialized Atom Subjects Graph prerequisite **or** separately maintained authoritative links **or** duplicate graph-specific relation definitions. retain graph-qualified identities across the composed view. distinguish source facts from navigation paths **and** derived reverse links. permit filtering **without** concealing incomplete selection. specify sufficient authority under the accepted Content Role boundary; D belongs **to** CA-P-1084. control-flow schema remains with CA-P-980.

assign **every** Claim by the accepted Content Role boundary: R for model **and** selection invariants, M **only** for Implementation choices **or** conventions, E for checks, **and** O for **any** reusable Action **or** Process definition. reuse existing authority; do **not** require an Atom **in** **every** Content Role. D remains with CA-P-1084; Operation-specific composition **and** control-flow schema remain with CA-P-980.

execute sequentially, **only** **after** the explicit prerequisite is Done, with **every** Task assigned **to** its own subagent. review this sub-Epic **before** its first Task; **after** its completion, review the remaining parent sub-Epic **before** resuming CA-P-980. **if** confidence is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains. creating this Task does **not** execute its work.
