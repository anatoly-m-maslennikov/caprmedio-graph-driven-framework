---
atom_id: CA-O-189@7
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step//Public release/Step: discover matching main PR'
  depends_on:
  - Subject/Graph Node/Carrier/Pull Request
  - Subject/Graph Node/Carrier/Git Repository
  - Subject/Graph Node/Domain/Continuant/History/Journal
version: 7
updated_at: 2026-10-27 06:04:45 +0400
relations:
  part_of:
  - CA-O-188
  invokes:
  - CA-O-190
tier: 3
---
# Summary

Discover a matching public `main` PR

## Step

This Step invokes CA-O-190 once before public-source freeze and records zero or one actual open Pull Request from `amm/dev` to `main` on the selected personal remote.

## Details

More than one match, a nonmatching base/head, an unsafe URL, or unavailable observation stops the Workflow. Discovery is read-only and does not infer a future URL.
