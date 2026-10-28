---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Selection
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Serialization
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Applicable Methodology'
version: 20
updated_at: 2026-10-27 19:59:30 +0400
relations:
  evaluation_for:
  - CA-R-1491
  - CA-R-803
  - CA-R-804
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-214
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Resolve a governed subject through canonical Artifact authority

## Claim checked

trigger observation **and** commit-context gathering **must not** mistake an Atom-like filename for authoritative Atom classification.

## Cases

1. observe changes **to** a registered Atom, a narrative Markdown document, a Projection, an unknown Markdown file, **and** a non-Markdown Carrier with Atom-like punctuation.
2. repeat with a registered Atom whose filename violates the current naming convention.
3. remove the classification evidence while keeping the observed file action **and** digest available.

## Acceptance

- capture records **every** selected observable file action **without** admitting lookalikes **to** the Atom graph.
- authoritative classification identifies the registered Atom **when** its evidence is available; filename punctuation alone does **not** assign **or** reject that classification.
- unavailable **or** conflicting classification leaves Atom identity unresolved, but preserves the native Carrier observation for Journal recording under CA-R-1491.
- repeated identical input returns the same observation **without** mutation.
- passing context capture does **not** certify Project conformance.

## Failure disposition

reject the logger Implementation **if** it invents Atom identity, blocks a recordable file event solely on naming **or** classification defects, **or** mutates state during capture.
