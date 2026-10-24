---
subjects:
  governs: 'Subject/Graph/Relation/Type: child_of'
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Tier
  - Subject/Domain/Node/Continuant/Atom.Local Scope Unit
  - Subject/Domain/Node/Continuant/Atom.Target Scope Unit
  - Subject/Domain/Node/Continuant/Atom.Substance Scope
version: 30
updated_at: 2026-10-24 03:43:56 +0400
relations:
  child_of:
  - CA-R-1174
atom_id: CA-R-796
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Keep tier-parent relations within Atom Scope

## Scope

Tier-parent relations between tier-classified Atoms.

## Claim

a stored governing `child_of` relation **must** point from a Current child Atom to a Current applicable parent Atom. The target **must** be in the same Scope Unit with a strictly lower numeric Tier, **or** in a strict ancestor Scope Unit with no Tier comparison. A descendant or sibling target does not satisfy the ordering. The parent's Substance, Target Scope Unit when applicable, and Substance Scope **must** support the authority claimed by that relation.

## Details

Structural eligibility alone does not establish parenthood. Different Subjects are allowed when the parent actually governs the child's contribution; equal Subjects do not establish that governance. An ancestor-owned Goal may govern definitions that fulfill its result in the targeted child Scope Unit without changing either Atom's owner. An ordinary relational Atom's Target Scope Unit does not replace its Local Scope Unit in the ordering test. The admitted Operator-owned Project Goal case instead resolves its Target Project as the ordering context under CA-D-637; the owner remains the Operator Actor. Preserve the admitted Project Goal-to-Project Principle case, orphan permissions, and the acyclic normative-authority boundary. No Content Role or Type-to-Tier restriction is introduced. Do not turn a dependency, classification, containment, or source-layer relation into `child_of` merely to fill parent coverage.

For ordering only, an endpoint verified as a Current Requirement of Type Project Goal under CA-R-2152 and CA-R-2132 uses its Target Project as its ordering Scope context. Its actual owner remains the Operator Actor. The Target Project must be the Project containing the other endpoint's declared Local Scope Unit; an unrelated Project does not qualify. Ordinary endpoints, including non-Project Goals, continue to use their Local Scope Unit. Compare the resulting contexts with the same lower-target-Tier or strict-ancestor rule. Do not create an Operator Scope Unit, change ownership, add a stored Property, or exempt a Project Goal from ordering. Unverified Goal identity, ownership, Tier or Project membership remains unresolved and does not pass.
