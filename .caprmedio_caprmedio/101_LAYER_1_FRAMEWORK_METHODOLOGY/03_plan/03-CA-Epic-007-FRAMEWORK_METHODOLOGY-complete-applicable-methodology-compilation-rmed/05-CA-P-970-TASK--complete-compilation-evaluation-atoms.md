---
atom_id: CA-P-970
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/Graph Node/Engineering/Validation
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Scope Unit//CORE_META_MODEL
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Applicable Methodology'
  - Subject/Graph Node/Engineering/Methodology
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Graph Relation/Type: evaluation_for'
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Node/Domain/Continuant/History
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Engineering/Confidence Threshold
version: 11
updated_at: 2026-10-25 17:32:27 +0400
relations:
  depends_on:
  - CA-P-969
status: Active
author: Anatoly Maslennikov
current_scope_unit: FRAMEWORK_METHODOLOGY
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Complete compilation Evaluation Atoms

the Assignee **must** complete falsifiable Evaluation authority for the compilation Requirement, Method, **and** Delivery package **in** CORE_META_MODEL.

## Scope

(Evaluation authority for Applicable Methodology compilation **in** CORE_META_MODEL, including necessary new **or** replacement Evaluation Atoms)

## Definition of Done

the Task is **not** Done **if** ((an E gap accepted from CA-P-966 remains unaddressed) **or** (an Evaluation lacks explicit references to the R, M, **or** D authority it checks) **or** (a required positive, negative, **or** recovery case lacks observable input **and** expected result) **or** (completeness, consistency, source traceability, conformance, approval, **or** Carrier correctness lacks check coverage) **or** (an Evaluation silently introduces a new Requirement) **or** (a changed prior Revision is lost) **or** (an edit exceeds this Claim Scope)).

## Details

reuse CA-E-379 **and** connect additional independent cases to their exact checked authority through evaluation_for. keep Er, Em, **and** Ed as ordinary E Atoms grouped by checked R, M, **and** D authority, **not** additional Content Roles.

cover zero applicable Extensions; a newly installed conforming Extension with an unknown name; changed conforming Local Configuration contents; omitted eligible input; ineligible input; duplicate identities; Core-boundary violations; missing, ambiguous, **or** stale approval; source changes during a run; invalid source links **or** output placement; deterministic repetition; **and** failed publication **without** corruption of the preceding valid Projection. express these as concrete Evaluation cases **and** expected outcomes. implementing Tool tests **or** executing a compilation is outside this Task.
