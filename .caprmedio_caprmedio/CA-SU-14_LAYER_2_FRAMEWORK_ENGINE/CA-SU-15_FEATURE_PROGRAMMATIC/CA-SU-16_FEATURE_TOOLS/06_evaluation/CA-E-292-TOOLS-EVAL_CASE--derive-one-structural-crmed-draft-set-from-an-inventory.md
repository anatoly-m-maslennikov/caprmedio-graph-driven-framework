---
atom_id: CA-E-292
ref_id: CA-E-292
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Data Transformation"
tier: 3
relations:
  evaluation_for:
  - CA-M-102
  derived_from:
  - CA-A-057
status: Active
version: 21
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Derive one structural CRMED draft set from an Inventory

## Claim checked

structural CRMED drafts derived from one Inventory remain reviewable candidates **without** acquiring active authority.

## Test case

derive candidates from one Inventory containing a folder **and** file hierarchy.

## Acceptance criteria

**every** resulting carrier is a draft, retains its observed source boundary, **and** does **not** create an active Scope Unit **or** requirement.

## Failure disposition

stop adoption reconciliation **and** report the first authority **or** source-boundary invention.
