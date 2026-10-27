---
subjects:
  governs: Subject/Domain/Node/Continuant/Scope Unit//PROJECT_CONFIGURATION
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - Subject/Domain/Node/Continuant/Term//Artifact
  - Subject/Domain/Node/Continuant/Atom.Version Number
  - Subject/Domain/Node/Continuant/Atom.Content
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Graph/Relation
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Subject/Domain/Node/Continuant/Project.Settings
version: 23
updated_at: 2026-10-25 03:12:46 +0400
relations: {}
atom_id: CA-O-008@23
content_role: Operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
type: Action
tier: 3
---
# Summary

Apply approved source corrections

## Operation

Apply Approved Source Corrections **means** the reusable Action that applies **only** the exact upstream corrections authorized for the current proposal, conflict, **and** source frontier.

1. **before** mutation, revalidate the actual Operator authorization **and** relevant current source state. authorization **may** be an explicit decision recorded under CA-O-007 **or** an active Operator delegation that covers **every** proposed action, subject **to** CA-R-1551 **and** the calling Workflow's stricter approval requirements. missing, rejected, stale, partial, ambiguous, **or** mismatched authorization blocks mutation.
2. apply the authorized correction through the owning source's governed change workflow. resulting Claims remain **in** their owning source Atoms; resulting selections remain **in** their owning settings. compilation **and** an approval record do **not** themselves grant source-change authority.
3. for archival, verify CA-O-006's coverage conditions against live sources, complete prerequisite repairs, **and** preserve the predecessor under CA-O-051: retain its exact prior Revision bytes as history **without** changing prior Version, Status **or** Updated At; retain the current predecessor's body, Summary, identity **and** all metadata except Version, archived Status **and** archive-time Updated At, incrementing Version by exactly **`1`** for that actual update. apply replacement **or** absorption recording under CA-R-807 **when** applicable; a withdrawn obsolete Claim does **not** require an invented successor.
4. record actual execution, changes, failures, **and** partial effects **in** the Journal. report the resulting source frontier **or** exact failure; a Journal record describes those effects **without** replacing current source authority.
5. return changed sources for renewed selection, conflict assessment, Principle alignment, **and** affected coverage checks. do **not** report completion **until** required checks confirm no remaining conflict **or** coverage gap **in** the affected authority.

this Action **must not** edit projected Claims as a conflict fix, infer additional corrections, create a duplicate approval Atom, **or** claim completion **after** a failed correction. retries **and** recovery require their applicable accepted authority **and** bounds; this Action does **not** authorize automatic rollback **or** unbounded repetition.

## Details
