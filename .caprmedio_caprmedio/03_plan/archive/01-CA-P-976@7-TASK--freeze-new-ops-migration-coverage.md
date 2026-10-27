---
atom_id: CA-P-976@7
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: AI Agent
autonomous_confidence_threshold: 99
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Content
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - Subject/Domain/Node/Continuant/Atom.Subjects
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Atom.Tier
  - Subject/Graph/Relation
  - Subject/Domain/Node/Continuant/Actor
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan.Autonomous Confidence Threshold'
version: 7
updated_at: 2026-10-24 19:39:48 +0400
relations: {}
status: Archived
current_scope_unit: caprmedio
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Freeze New Ops migration coverage

the Assignee **must** produce the approved New Ops migration input inventory.

## Scope

(the current canonical RMEDO authority **in** caprmedio **and** its Methodology Sources, plus **only** CA-P-032, CA-P-033, **and** CA-P-034); this Task establishes the common admission boundary **without** modifying migration-source Atoms.

## Definition of Done

the Task is **not** Done **if** ((an eligible source lacks **any** required path, identity **or** draft locator, Version, content digest, current Scope Unit, Content Role, Local Tier, Global Tier, **or** Status) **or** (the Active versus Draft admission boundary has no explicit Operator disposition) **or** (a generated Projection is selected as source authority) **or** (an out-of-scope CAP **or** I Atom is admitted except the three approved P Actor policies) **or** (a current eligible Scope Unit **or** tier is omitted from the execution queue)).

## Details

read current Project Principles first; the latest Operator decisions override older Claims. sources are `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources` **and** `.caprmedio_caprmedio`. identify active authority roots from actual sources rather than obsolete duplicate folders **or** compiled copies. preserve a pre-migration snapshot of the complete TOOLS RMEDO subtree for the later harvest. inventory installed Extensions **without** assuming **any** are installed; an empty source is a recorded no-op. archive/history/bootstrap copies, Implementation code, runtime state, Settings values, **and** unrelated Plans are **not** migration targets. creation of this Epic **and** its P Tasks is planning administration, **not** a CAP migration. the Operator selected Active RMEDO **and** **only** the previously approved CA-P-032, CA-P-033 **and** CA-P-034 exceptions; Drafts are excluded. the existing per-tier/per-unit Tasks are a scheduling inventory, **not** proof that folder prefixes **or** filename labels are authoritative; reconcile them with current tier **and** structural authority **before** execution. add **or** adjust a narrowly scoped Task **if** this inventory finds a missing admitted batch; never silently skip it.

**if** confidence **in** a decision is below the effective Autonomous Confidence Threshold, check Project Principles first **and** ask the Operator **if** uncertainty remains; do **not** silently select a new design. no migration is executed merely by creating this Task.

Completion evidence: [coverage freeze report](../../execution_evidence/CA-P-976@7-coverage-freeze-report.md), [exact Active source inventory](../../execution_evidence/CA-P-976@7-active-source-inventory.projection.json), **and** [pre-migration TOOLS bytes](../../execution_evidence/CA-P-976@7-tools-pre-migration-snapshot.projection.json). 1,557 Active Atoms occupy 51 Scope Units **and** 84 owner/tier groups; 53 Drafts are excluded. **every** admitted group has a scheduled batch. all 455 Active TOOLS source carriers are preserved byte-for-byte. Installed Extensions is empty **and** recorded as a no-op. the independent completeness **and** integrity checks pass, so the Definition of Done falsifying condition is false. no migration-source Atom was modified.
