---
atom_id: CA-O-176
content_role: Operations
type: Step
current_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/caprmedio/Step//Release Version/Step: build candidate image'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Carrier/Docker Image
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 12
updated_at: 2026-10-27 19:59:47 +0400
relations:
  part_of:
  - CA-O-164
  invokes:
  - CA-O-168
tier: 3
---
# Summary

Build the candidate release image

## Step

This Step invokes CA-O-168 once with phase `candidate_image_build`, binding CA-O-175's staged package, exact source/context rows and immutable candidate image identity. The frozen Docker worker has no Docker socket and cannot substitute for host Candidate E2E.

## Details

It creates no authority from a tag, cached image or successful build alone. A build mismatch, host mount, stale package/source, unsafe context, failed result or missing Journal receipt stops without proof, promotion or old-image removal.
