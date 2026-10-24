---
subjects:
  governs: 'Subject/Graph/Relation/Type: child_of'
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Tier
  - Subject/Domain/Node/Continuant/Atom.Scope Unit
  - Subject/Domain/Node/Continuant/Atom.Target Scope Unit
  - Subject/Domain/Node/Continuant/Atom.Substance Scope
version: 27
updated_at: 2026-10-23 23:17:14 +0400
relations:
  child_of:
  - CA-R-1174
atom_id: CA-R-796@27
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
status: Archived
author: Anatoly Maslennikov
global_tier: 9
---
# Summary

Keep tier-parent relations within Atom Scope

## Scope

Tier-parent relations between tier-classified Atoms.

## Claim

a stored governing `child_of` relation **must** point from a Current child Atom to a Current applicable parent Atom. The target **must** be in the same Scope Unit with a strictly lower numeric Tier, **or** in a strict ancestor Scope Unit with no Tier comparison. A descendant or sibling target does not satisfy the ordering. The parent's Substance, Target Scope Unit when applicable, and Substance Scope **must** support the authority claimed by that relation.

## Details

Structural eligibility alone does not establish parenthood. Different Subjects are allowed when the parent actually governs the child's contribution; equal Subjects do not establish that governance. An ancestor-owned Goal may govern definitions that fulfill its result in the targeted child Scope Unit without changing either Atom's owner. A relational Atom's Target Scope Unit does not replace its Owning Scope Unit in the ordering test. Preserve the admitted Project Goal-to-Project Principle case, orphan permissions, and the acyclic normative-authority boundary. No Content Role or Type-to-Tier restriction is introduced. Do not turn a dependency, classification, containment, or source-layer relation into `child_of` merely to fill parent coverage.

