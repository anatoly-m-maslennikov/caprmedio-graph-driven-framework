---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Node/Engineering/Continuant/Carrier/File Carrier
  - Subject/Graph Node/Domain/Continuant/Atom.Property
  - Subject/Graph Node/Domain/Continuant/Project
version: 18
updated_at: 2026-10-25 17:32:27 +0400
relations:
  relates_to:
  - CA-R-1957
  - CA-R-1956
  - CA-D-416
atom_id: CA-D-463
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Eng Decision
---
# Summary

Give Every Atom Revision One Authoritative Carrier Bundle

## Scope

Atom Revision Authoritative Carrier Bundles.

## Claim

**every** Atom Revision **must** have **`=1`** authoritative Carrier Bundle on the Project filesystem containing **`=1`** Markdown File Carrier **and** **`>=0`** additional Carriers admitted by its applicable Delivery authority.

the Markdown file carries the Atom's own Properties under CA-D-478 **and** CA-D-479. additional Carriers represent that same Revision **without** replacing the mandatory file **or** independently redefining its Properties.

## Details
