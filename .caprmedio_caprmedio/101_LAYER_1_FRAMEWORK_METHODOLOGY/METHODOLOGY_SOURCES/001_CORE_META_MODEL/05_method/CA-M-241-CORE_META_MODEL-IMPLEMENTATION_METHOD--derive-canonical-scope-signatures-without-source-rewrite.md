---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Transformation
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Controlled English
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Canonical Scope Signature'
  - Subject/CAPRMEDIO/Carrier/File
version: 22
updated_at: 2026-10-27 19:59:41 +0400
relations:
  child_of:
  - CA-M-121
atom_id: CA-M-241
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 4
type: Implementation Method
---
# Summary

Derive Canonical Scope Signatures **without** Source Rewrite

## Scope

derivation of Canonical Scope Signatures from one caller-selected Atom Carrier folder.

## Claim

**to** derive Canonical Scope Signatures from one caller-selected Atom Carrier folder, the Tool **must** inspect **only** active Carriers with **`=1`** unwrapped Scope Expression **in** one `## Scope` section, resolve **every** atomic identity against active Atom IDs **in** that selected folder, derive a signature **only** **if** the Scope Expression satisfies the restricted Canonical Scope Signature grammar, emit source identity, source revision, source Carrier digest, source frontier digest, source expression, signature, **and** exclusion diagnostic, **and** make no source-Carrier rewrite, lifecycle change, Claim merge, authority decision, **or** dependency relation.

## Details
