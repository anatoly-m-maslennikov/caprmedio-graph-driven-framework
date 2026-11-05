---
atom_id: CA-R-2974
ref_id: CA-R-2974@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: Subject
tier: 3
status: Draft
version: 1
updated_at: 2026-10-28 17:07:35 +0400
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
---
# Summary

Require Unique Primary Kind Names

## Scope

Primary-kind declarations in the effective Subject model, including shared and project-local branches.

## Claim

Distinct primary-kind declarations **must** have unique canonical names across the effective Subject model. An existing-kind reference **may** use that name inside `@(...)`, as in `@(Module)`, and **must** resolve to exactly one declared kind. Repeated references to the same kind are not new declarations. An ambiguous name **must not** be resolved by choosing a branch or merging distinct targets.

## Semantics

This is declaration-name uniqueness, not uniqueness of every raw path component or every displayed occurrence. Property names may repeat under different bearers; classification-axis names and allowed values remain qualified by their existing rules. Instance naming remains governed within its kind and is not made globally unique by this rule. Escaping changes representation, not the intended kind's name.

A branch move alone leaves a unique-name reference valid. A primary-name rename requires reference migration. A current full canonical path may still identify the same kind; retired paths do not become aliases. No alias registry is introduced.

## Details

This Draft records the Operator's explicit Yes to Q07 in CA-A-1236. Existing distinct same-label kinds, including Aspect Documentation and actual Implementation Documentation, require a reviewed naming correction before this rule can be applied across Current sources. This Draft does not perform those renames or implement lookup. No numeric Atom ID is allocated until promotion preparation.
