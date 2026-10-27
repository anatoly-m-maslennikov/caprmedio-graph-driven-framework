---
atom_id: CA-P-967
cce_version: cce_1
cce_form: obligation
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow//Applicable Methodology Compilation'
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Scope Unit//CORE_META_MODEL
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Applicable Methodology'
  - Subject/Graph Node/Engineering/Methodology
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement'
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - Subject/Graph Node/Engineering/Extension
  - Subject/Graph Node/Domain/Continuant/Scope Unit//PROJECT_CONFIGURATION
  - Subject/Graph Node/Engineering/Confidence Threshold
version: 13
updated_at: 2026-10-25 17:32:27 +0400
relations:
  depends_on:
  - CA-P-966
status: Active
author: Anatoly Maslennikov
current_scope_unit: FRAMEWORK_METHODOLOGY
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Complete compilation Requirement Atoms

the Assignee **must** complete the Requirement authority for Applicable Methodology compilation **in** CORE_META_MODEL by reusing current Atoms **and** adding **or** repairing **only** missing **or** inadequate Claims.

## Scope

(Requirement authority for Applicable Methodology compilation **in** CORE_META_MODEL, including necessary new **or** replacement Requirement Atoms)

## Definition of Done

the Task is **not** Done **if** ((an R gap accepted from CA-P-966 remains unaddressed) **or** (eligible source inclusion, source preservation, expansion boundaries, **or** non-authoritative output lacks an unambiguous Requirement owner) **or** (Core requires a particular installed Extension name **or** Project-specific Local Configuration contents) **or** (an independent Claim has duplicate authority owners) **or** (a changed source identity **or** prior Revision is lost) **or** (an edit exceeds this Claim Scope)).

## Details

start from CA-R-1434, CA-R-1228, CA-R-1314 through CA-R-1317, **and** CA-R-1375 as already-existing authority. refresh their current Carriers **before** editing; do **not** recreate them merely because this Epic was created later.

specify complete eligible active input from Core Meta-Model, applicable installed Extensions, **and** Local Configuration; an empty Extension contribution is a valid case, **not** a prohibition on Extensions. retain the current RMEDO member eligibility, immutable source traceability, non-authoritative Projection boundary, expansion-only conformance, **and** Operator control over corrections. keep procedures **and** Carrier encodings out of independent Requirement Claims. inherit Author, Assignee, **and** Confidence Threshold according to current authority; preserve prior Revisions **when** changing existing Atoms.
