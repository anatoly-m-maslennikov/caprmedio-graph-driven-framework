---
atom_id: CA-P-975
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/Graph Node/Engineering/Methodology
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Scope Unit//CORE_META_MODEL
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - Subject/Graph Node/Domain/Continuant/Atom.Content.Scope
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Node/Domain/Continuant/History
  - Subject/Graph Node/Domain/Continuant/Atom/Content Role
  - Subject/Graph Node/Domain/Continuant/Atom.Tier
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - Subject/Graph Node/Engineering/Methodology
  - Subject/Graph Node/Engineering/Confidence Threshold
version: 14
updated_at: 2026-10-25 17:32:27 +0400
relations:
  depends_on:
  - CA-P-974
status: Active
author: Anatoly Maslennikov
current_scope_unit: FRAMEWORK_METHODOLOGY
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Validate Core Meta-Model placement recommendations

the Assignee **must** deliver a validated disposition register for the reviewed responsibility boundaries of CORE_META_MODEL.

## Scope

(active CORE_META_MODEL authority covered by this Epic **and** its consolidated placement-review evidence)

## Definition of Done

the Task is **not** Done **if** ((a preceding Task is **not** Done) **or** (an active in-scope Atom lacks a final disposition) **or** (a changed source Revision has **not** received a delta review) **or** (recommendations conflict with Project Principles, accepted Operator decisions, **or** one another) **or** (a proposed transfer creates duplicate authority, an authority gap, **or** an unaddressed broken reference) **or** (an unresolved decision below the effective Confidence Threshold is presented as settled) **or** (the report omits evidence, destination, rationale, impact, **or** prerequisite decisions for a proposed change) **or** (review completion is presented as migration completion)).

## Details

reconcile Settings **and** non-Settings findings Claim by Claim. provide one final Atom-level disposition with any necessary mixed-Claim subdispositions; keep retain, move, split, deduplicate, retire, role correction, **and** Local Tier correction distinct. include retained Atoms so coverage is checkable, **not** just a list of suspected problems.

refresh the source frontier **and** check **all** proposals together for Single Source of Truth, completeness, coherent Terms **and** Subjects, permitted Core expansion, configuration ownership, **and** source traceability. use Project Principles **to** resolve proposals first; ask the Operator about remaining choices below the effective Confidence Threshold, one question at a time.

deliver grouped findings with exact source Carrier **and** Revision references, proposed owner **and** representation, retained generic authority, affected references **and** dependencies, risks, **and** a safe future change sequence. distinguish high-confidence recommendations from decisions requiring approval; a review finding itself is **not** permission **to** change an authoritative source.

report Task completion as completion of this read-only review **only**. do **not** execute the proposed migration, create remediation Tasks **or** another Epic, edit existing methodology Atoms **or** Settings, implement Tools, rebuild Projections, **or** execute CA-Epic-007. review outputs are evidence, **not** new governing authority.
