---
atom_id: CA-R-2103@1
content_role: Requirement
type: Rule
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Archived
version: 1
updated_at: 2026-10-22 16:16:53 +0000
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Type
relations: {}
---
# Summary

Permit classification-only Type corrections during Candidate #7 migration

## Scope

Type assignments in this project's one-time Candidate #7 migration.

## Claim

Adding or correcting an Atom's Type during this migration keeps its Atom ID when its Summary and Substance are unchanged. This exception does not apply to ordinary Type changes outside this migration or to a changed Summary or Substance.

## Semantics

The Operator approved this exception for classification corrections. It does not make Type generally identity-neutral. CA-R-1766 continues to govern ordinary Type changes. A retained-ID Current update still advances Version by one, records the actual Updated At and preserves its predecessor as an Archived Atom.
