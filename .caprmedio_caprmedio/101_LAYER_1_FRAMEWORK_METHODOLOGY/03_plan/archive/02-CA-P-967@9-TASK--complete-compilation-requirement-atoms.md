---
atom_id: CA-P-967@9
cce_version: cce_1
cce_form: obligation
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow//Applicable Methodology Compilation'
  depends_on:
  - Subject/Domain/Node/Continuant/Scope Unit//CORE_META_MODEL
  - Applicable Methodology/Sources
  - Methodology Source/Expansion Boundary
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  - Subject/Domain/Node/Continuant/Atom.Content
  - Extension
  - Local Configuration
  - Subject/Engineering/Confidence Threshold
version: 9
updated_at: 2026-10-24 19:39:48 +0400
relations:
  depends_on:
  - CA-P-966
status: Archived
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
