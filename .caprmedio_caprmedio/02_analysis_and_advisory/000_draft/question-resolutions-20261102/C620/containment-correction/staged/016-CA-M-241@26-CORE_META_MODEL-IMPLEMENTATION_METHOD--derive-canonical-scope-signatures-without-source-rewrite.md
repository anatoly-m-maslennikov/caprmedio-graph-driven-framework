---
subjects:
  active: Entity/Aspect/Engineering/Data Handling/Data Transformation
  passive:
  - Entity/Aspect/Engineering/Authoring/Controlled English
  - 'Entity/Object/Continuant/Projection/Type: Canonical Scope Signature'
  - Carrier/File
version: 26
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-M-121
atom_id: CA-M-241@26
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 4
role: Method
form: Implementation Method
---
## Summary

Derive Canonical Scope Signatures **without** Source Rewrite

## Claim scope

derivation of Canonical Scope Signatures from one caller-selected Atom Carrier folder.

## Claim

**to** derive Canonical Scope Signatures from one caller-selected Atom Carrier folder, the Tool **must** inspect **only** active Carriers with **`=1`** unwrapped Scope Expression **in** one `## Scope` section, resolve **every** atomic identity against active Atom IDs **in** that selected folder, derive a signature **only** **if** the Scope Expression satisfies the restricted Canonical Scope Signature grammar, emit source identity, source revision, source Carrier digest, source frontier digest, source expression, signature, **and** exclusion diagnostic, **and** make no source-Carrier rewrite, lifecycle change, Claim merge, authority decision, **or** dependency relation.
