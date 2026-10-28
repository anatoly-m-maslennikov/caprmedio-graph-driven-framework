---
atom_id: CA-R-2123
content_role: Requirement
type: Rule
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
relations: {}
version: 5
updated_at: 2026-10-27 20:00:07 +0400
tier: 1
---
# Summary

Limit PROGRAMMATIC Method and Delivery Types

## Scope

Method and Delivery Atoms whose Local Scope Unit is PROGRAMMATIC or one of its declared descendants.

## Claim

Each Current Atom in this Scope **must** use Type Eng Policy or Eng Decision.

## Details

Subjects and Content Roles remain independent. This rule restricts admitted Type values, not Subject branches or Tier numbers. Other Content Roles and specialized Types outside this Scope are not restricted by this rule.

Eng Policy ownership requires at least one actual declared child and automatic application to every child under genuine topic or environment conditions. A leaf may inherit a Policy but cannot locally own one. Eng Decision records a Scope-Unit-specific choice without automatic every-child inheritance.

Incomplete Drafts remain allowed. Apply this Type restriction before promotion to Current. During this Candidate #7 migration, classification-only Type corrections retain the base ID when Summary and Substance are unchanged.

The reusable definitions are CA-R-2119 and CA-R-2120 for Method, and CA-R-2121 and CA-R-2122 for Delivery. This source rule does not claim that their existing consumers have been migrated or that runtime validation implements it.
