---
subjects:
  governs: "Persist Atom Replacement"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/Atom", "Entity/Node/Continuant/History/Revision/Type: Atom", "Atom Carrier", "Entity/Node/Continuant/History/Journal", "Artifact Archive Carrier Basename"]
version: 11
updated_at: "2026-10-19 11:49:16 +0000"
relations: {relates_to: [CA-R-1432, CA-R-807]}
atom_id: "CA-O-051@draft"
content_role: "Operations"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
---
# Summary

Persist Atom replacement through ordered Carrier transitions

## Operation

Persist Atom Replacement **means** the reusable Action that persists **`=1`** accepted Atom replacement through its successor activation **and** predecessor archival under CA-R-1432 **and** CA-R-807. its boundary is this replacement transition; it does **not** select **or** authorize the replacement. the execution **must** perform **all** of:

1. persist the successor as Active **before** archiving the predecessor.
2. archive the predecessor as one whole Carrier under CA-D-303 **and** record the corresponding replacement **in** the authoritative Journal with explicit predecessor **and** successor Atom IDs under CA-R-807.
3. retain the predecessor's exact prior Revision bytes as history, including its prior Version, Status **and** Updated At, **without** another metadata edit to them. preserve the current predecessor's body, Summary, identity **and** every frontmatter value except Version, lifecycle `status` **and** `updated_at`; increment Version by exactly **`1`**, serialize `status: Archived` **and** refresh `updated_at` to the actual archive time. change its basename **only** by adding the canonical `@<version>` Archive suffix for that resulting Version under CA-D-289.
4. keep replacement history out of predecessor **and** successor Atom frontmatter; formal replacement relations **and** inverse navigation remain deferred under CA-R-807.

## Details
