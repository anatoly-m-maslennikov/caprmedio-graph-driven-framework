---
atom_id: CA-R-1981@5
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Framework Settings.Identifier
relations:
  child_of:
  - CA-R-1176
version: 5
updated_at: 2026-10-24 00:38:25 +0400
tier: 3
---
# Summary

Define Project.Framework Settings.Identifier

## Scope

the identifier of the Project's authoritative Framework Settings configuration.

## Claim

Framework Settings Identifier identifies the Project's authoritative Framework Settings configuration, **not** an Atom.

## Details

Evidence: CA-R-1402 defines the owning configuration; CA-R-1404 keeps it outside the Atom type; CA-D-358 supplies its concrete identifier. Candidate #6 decision 11 places Project under Continuant; concrete CAPRMEDIO identity encodings belong in Project Configuration. This definition does not duplicate the concrete identifier spelling or create an Atom ID.
