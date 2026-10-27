---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action//Persist Atom Replacement'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.Version Number
  - Subject/Graph Node/Carrier/File
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Carrier/File.Filename
version: 20
updated_at: 2026-10-27 06:04:45 +0400
relations:
  depends_on:
  - CA-R-807
atom_id: CA-O-051
content_role: Operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
type: Action
tier: 3
---
# Summary

Persist Atom replacement through ordered Carrier transitions

## Operation

Persist Atom Replacement **means** the reusable Action that persists **`=1`** accepted Atom replacement through its successor activation **and** predecessor archival under CA-R-1432 **and** CA-R-807. its boundary is this replacement transition; it does **not** select **or** authorize the replacement. the execution **must** perform **all** of:

1. persist the successor as Active **before** archiving the predecessor.
2. archive the predecessor as one whole Carrier under CA-D-303 **and** record the corresponding replacement **in** the authoritative Journal with explicit predecessor **and** successor Atom IDs under CA-R-807.
3. retain the predecessor's exact prior Revision bytes as history, including its prior Version, Status **and** Updated At, **without** another metadata edit to them. materialize the predecessor's Archived representation with its prior Version and Updated At, version-qualified identity and governed history location; archival alone does not increment Version or refresh Updated At. the Active successor receives Version **`N+1`** and the actual Project-time Updated At for the real replacement update. change its basename **only** by adding the canonical `@<version>` Archive suffix for that predecessor Version under CA-D-289.
4. keep replacement history out of predecessor **and** successor Atom frontmatter; formal replacement relations **and** inverse navigation remain deferred under CA-R-807.

## Details
