---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan"
  depends_on:
    ["Atom/Content Role: Plan/Type: Plan", "Entity/Node/Continuant/Atom.Substance", "Entity/Node/Continuant/Atom.Author", "Entity/Node/Continuant/Atom/Content Role: Plan.Assignee", "Entity/Node/Continuant/Atom/Content Role: Plan.Definition of Done", "Entity/Node/Continuant/Atom/Content Role: Plan.Details", "Entity/Node/Continuant/Atom/Content Role: Plan.Label", "Entity/Node/Continuant/Atom/Content Role: Plan.Status", "Hub Atom", "Entity/Node/Continuant/Scope Unit", "Autonomous Confidence Threshold"]
version: 10
updated_at: "2026-10-19 15:55:13 +0400"
relations: {"evaluation_for": ["CA-R-1574", "CA-R-1575", "CA-R-1576", "CA-R-1577", "CA-R-1581", "CA-R-1599", "CA-R-1583", "CA-R-1584", "CA-R-1587", "CA-R-1588", "CA-R-1589", "CA-M-306", "CA-D-470"]}
atom_id: "CA-E-501"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-501-CORE_META_MODEL-QA_CASE--validate-common-plan-authoring.md
  source_atom_id: CA-E-501
  source_atom_revision: 10
  source_sha256: e281af57c20d9e1942bae241cd62c482cd93f2c95abdb8cfaf385b88ffe1facb
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Validate common Plan authoring

## Scope

Plan authoring under the common model.

## Claim

the Plan authoring Evaluation **must** reject **any** Plan that violates the common model.

## Details

### cases

- accept a standalone file-backed Plan, a file-backed Hub with decomposed work **and** an optional directory, **and** a Plan with both own work **and** decomposition. reject a folder-only Plan.
- reject a Summary-only Plan with no own work **and** no decomposition; do **not** complete it by an empty all-of test.
- require **`=1`** intended work **or** outcome Claim **in** Objective **and** **`=1`** effective Author; require **`=1`** effective Assignee for own work, but **not** for a pure Hub.
- require **`=1`** observable, decidable Definition of Done under `### Definition of Done` inside Details **in** **every** Plan Markdown file, including a pure Hub. reject its absence.
- accept an atomic **or** explicitly grouped composite falsification expression; reject ambiguity **or** Details that introduce independent work **or** another completion claim.
- mark Done **only** **when** own work is complete, **all** directly decomposed Plans are Done, **and** its falsification expression is false. reject Canceled **or** Archived decomposition as completed work.
- change **only** the Label among Version, Objective, Epic, Task, **and** Subtask: authoring admission **and** completion **must** remain unchanged. reject treating those Labels as authoring Subtypes.
- select the owning Scope Unit as the default Claim Target Scope Unit during authoring regardless of Hub nesting, **and** require the resolved value inside the Atom; preserve a permitted different target **and** narrower Claim restrictions. reject an ancestor target **or** **any** Hub substituted as a Scope Unit target.
- accept inherited confidence values **without** copied overrides; reject an unresolved effective value **before** autonomous execution.

report the exact Plan identity **and** failed rule; a Label **must not** waive the failure.
