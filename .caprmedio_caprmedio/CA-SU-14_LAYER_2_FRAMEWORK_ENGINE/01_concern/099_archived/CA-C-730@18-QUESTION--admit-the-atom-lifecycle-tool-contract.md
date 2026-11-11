---
identity:
  id: CA-C-730
  ref_id: CA-C-730@18
context:
  container:
    scope_unit: CA-SU-14
  role: Concern
  form: Question
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 3
state:
  status: Archived
  version: 18
  updated_at: 2026-11-11 15:21:04 +0400
destination:
  file:
    name: CA-C-730@18-QUESTION--admit-the-atom-lifecycle-tool-contract.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern/archived
author: Anatoly Maslennikov
relations:
  concern_about:
  - CA-P-2934
  - CA-R-1093
  - CA-M-374
  - CA-D-623
  - CA-R-1432
  - CA-R-1788
  - CA-E-521
  - CA-O-10009
  - CA-O-10011
  - CA-O-10016
  - CA-O-10018
  - CA-O-10023
  - CA-O-10024
---

## Summary

Admit the Atom Lifecycle Tool contract

## Concern

What remains to admit and publish the six Atom Lifecycle Tools selected for CA-P-2934?

## Details

The six Workflows and supporting Atoms are Current. The Operator chose direct calls to the Project runtime over MCP. Success returns only operation Status. Git integration is deferred. For missing input, return the requested fields. A later call in the same Project, client session and Tool can supply only those fields and optionally correct others.

A disposable Project passed all six paths through MCP HTTP, including a correction-only call and an Update that preserved Current Status across a Scope Unit change. Local release and direct image builds compile model assets at build time. See CA-P-2977.

The candidate checks now include declared Header presence, Concern Priority values, required Content headings and direct Markdown values. CA-P-2978 records the live declaration compile and disposable checks. The compiler now follows named Workflow inheritance and checks the declared child keys of Header groups. Lifecycle Status writes use the required lowercase YAML spelling, and reads accept both declared canonical names and their unambiguous Carrier spelling. Scope-owned Archived leaves can be renamed or relocated by Direct Update without changing Version or Updated At. The staged gateway passed all six Tools. See CA-P-2979.

The formal Role/Form domain is still incomplete. Concrete Scope Delegations such as CA-R-2763 list local pairs in Prose Claim, while their formal claims establish the Scope Unit. Which declared source should the checker use for pairs without a formal admission? Lifecycle now writes unambiguous declared Role and Form values in lowercase and reads them back through the compiled model. The shared readers accept these spellings where they compare declared names, while Workbench still exposes the factual Header. The exact encoded spelling of Analysis & Advisory and authoritative admission for unclassified Forms remain open. See CA-P-2980.

For folder-backed parents, CA-R-1521 requires separate actions for latest descendants and preserves older archives. Plan Archive now handles trees whose older archives already live outside the moving Directory Carriers. It archives the selected Plans child-first into the shared Archive, preserves assets, and reports effects and remaining targets on failure. See CA-P-2981. CA-D-664 requires the stored destination to match the actual location. If a parent move carries an older archive whose stored path would change, which rule controls? CA-D-461 also leaves the Done and Canceled placement for Plans with no containing Atom undecided. Keep those writes unavailable until the Carrier rules are settled.
