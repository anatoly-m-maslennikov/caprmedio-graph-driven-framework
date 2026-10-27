---
atom_id: CA-P-1078
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Projection
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - Subject/Graph Node/Domain/Continuant/Atom.Subjects
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Node/Domain/Continuant/Term
  - Subject
  - Subject/Graph Relation
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Autonomous Confidence Threshold'
version: 12
updated_at: 2026-10-25 17:32:27 +0400
relations:
  depends_on:
  - CA-P-979
status: Done
current_scope_unit: caprmedio
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Freeze the derived model view authority boundary

the Assignee **must** freeze the existing authority **and** ownership boundary for the derived model views.

## Scope

(a read-only selection of selected active RMEDO authority for derived model views **in** CORE_META_MODEL at `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`); the CA-P-976 admission boundary applies, with accepted source changes from completed Tasks **and** the sealed CA-P-980 direct-Subjects stage. Drafts, archives, generated Applicable Methodology copies, runtime, Tool Implementation, Settings values, **and** unrelated CAP Atoms are excluded. existing execution evidence is read-only.

## Definition of Done

the Task is **not** Done **if** (a relevant existing definition, graph Relation Kind, Subject link rule, Projection rule, **or** competing planned change is unaccounted for **or** the selected source identities **and** revisions are unresolved **or** an existing source Atom is assigned for uncoordinated mutation by multiple following Tasks).

## Details

use CA-R-1318, CA-R-1319, CA-R-1320, CA-R-1335, CA-R-1438, CA-R-1281, CA-R-1246, **and** CA-R-806 as starting points, **not** an exhaustive list. read their current Claims. shared read-only authority prerequisites are permitted. distinguish the Terms Graph, Entities Graph, direct Atom relations, **and** Subjects-based navigation. preserve the completed CA-P-980 direct-Subjects stage; its remaining Operation-specific schema is **not** a prerequisite for this inventory. identify reuse, gaps, proposed replacements, deferred work, **and** ownership **for** **every** following Task. record evidence outside authority sources; this Task changes no source Atoms.

execute sequentially, **only** **after** the explicit prerequisite is Done, with **every** Task assigned **to** its own subagent. review this sub-Epic **before** its first Task; **after** its completion, review the remaining parent sub-Epic **before** resuming CA-P-980. **if** confidence is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains. creating this Task does **not** execute its work.

completion evidence: [authority inventory](../../../execution_evidence/CA-P-1078-derived-model-view-authority-inventory.projection.json), [boundary report](../../../execution_evidence/CA-P-1078-authority-boundary-report.md), **and** [completion map](../../../execution_evidence/CA-P-1078-completion-map.projection.json). the inventory accounts for 212 selected current source Atoms, graph-relation signatures, competing mutation ownership, **and** successor-owned gaps. the Definition of Done falsifying condition is false; unresolved future schema decisions remain explicitly assigned **without** being guessed. no source Atom, Draft, prior archive, prior evidence, later Task, Tool Implementation, **or** Settings value changed. Git materialization remains pending.
