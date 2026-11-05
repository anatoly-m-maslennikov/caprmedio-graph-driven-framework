---
atom_id: CA-C-618
ref_id: CA-C-618
current_scope_unit: caprmedio
status: Resolved
topics:
  main_subject: CAPRMEDIO_MODEL <+ Project.Settings
version: 3
tier: 3
role: Concern
form: Question
updated_at: 2026-11-02 15:25:54 +0400
container:
  scope_unit: CA-SU-00
---
## Summary

Resolve the logical status of release retention settings

## Question

Where does release-specific rollback information belong?

## Resolution

The Operator confirmed that rollback information belongs to its Release. The block is removed from Framework Settings. Existing release evidence retains the image identity.
