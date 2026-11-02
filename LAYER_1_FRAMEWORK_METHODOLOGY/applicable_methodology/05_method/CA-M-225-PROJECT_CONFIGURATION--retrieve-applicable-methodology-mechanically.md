---
subjects:
  governs: "Entity/Node/Continuant/Projection/Type: Applicable Methodology"
  depends_on:
    ["Entity/Node/Continuant/Projection/Type: Applicable Methodology", "Entity/Node/Continuant/Atom.Subjects"]
version: 21
updated_at: "2026-10-19 15:56:13 +0400"
relations: {}
atom_id: "CA-M-225"
content_role: "Method"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/05_method/CA-M-225-PROJECT_CONFIGURATION--retrieve-applicable-methodology-mechanically.md
  source_atom_id: CA-M-225
  source_atom_revision: 21
  source_sha256: f0d75c082c944801e33203001c6b6a16f77eee0dd06682dae22a97911aacd920
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Retrieve Applicable Methodology Mechanically

## Scope

Applicable Methodology retrieval for one Subject **or** Workflow query.

## Claim

**to** retrieve Applicable Methodology for one Subject **or** Workflow query, the Retriever **must** derive GOVERNS **and** DEPENDS_ON indexes on demand from projected Atom Subjects, select matching GOVERNS paths, add DEPENDS_ON authority **only** through transitive prerequisite closure, retain Applicable Methodology membership order, make no inference, **and** return no Atom **if** no matching GOVERNS path exists.

## Details
