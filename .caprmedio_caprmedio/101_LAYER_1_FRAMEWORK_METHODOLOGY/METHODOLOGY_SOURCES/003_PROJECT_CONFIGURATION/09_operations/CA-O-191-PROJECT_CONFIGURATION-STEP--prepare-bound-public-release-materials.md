---
atom_id: CA-O-191
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/caprmedio/Step//Public release/Step: prepare materials'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Documentation
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Release.ID
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 12
updated_at: 2026-10-27 19:59:47 +0400
relations:
  part_of:
  - CA-O-188
  invokes:
  - CA-O-192
tier: 3
---
# Summary

Prepare bound public-release materials

## Step

This Step invokes CA-O-192 once for the sole public-release content prompt: the full PR description and concise selected-Version History summary.

## Details

README, Version History, Git, and PR updates are mechanical later steps. A newly created actual PR URL is appended only by CA-O-198; this Step does not guess a URL, publish, or merge.
