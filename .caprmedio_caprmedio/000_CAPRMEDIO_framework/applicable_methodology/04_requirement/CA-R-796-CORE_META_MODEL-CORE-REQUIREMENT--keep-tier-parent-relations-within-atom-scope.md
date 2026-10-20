---
subjects:
  governs: "Entity/Relation/Type: child_of"
  depends_on:
  - "Entity/Node/Continuant/Atom.Global Tier"
  - "Entity/Node/Continuant/Atom.Owning Scope Unit"
  - "Entity/Node/Continuant/Atom.Target Scope Unit"
  - "Entity/Node/Continuant/Atom.Substance Scope"
version: 23
updated_at: "2026-10-19 15:54:23 +0400"
relations:
  child_of:
    - CA-R-1174
atom_id: "CA-R-796"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-796-CORE_META_MODEL-CORE-REQUIREMENT--keep-tier-parent-relations-within-atom-scope.md
  source_atom_id: CA-R-796
  source_atom_revision: 23
  source_sha256: 0a3a51c9f7854d1d22894b2afba837f9cbc919f8cb35b11ea15a4179de77b580
  original_relations_sha256: 4bbb4b930b4dba68ac5f2807086aabe7e4a23f53f26d95b54808e5edf87dfb4f
---
# Summary

Keep tier-parent relations within Atom Scope

## Scope

Tier-parent relations between tier-classified Atoms.

## Claim

a tier-parent relation **must** point from a child Atom to an applicable parent Atom permitted by the Global Tier topology. a parent in the child's Owning Scope Unit **must** have a lower Global Tier. a parent in a declared ancestor Scope Unit **may** have an equal or lower Global Tier. the parent's Substance, Target Scope Unit when applicable, and Substance Scope **must** support the authority claimed by that relation.

## Details

Structural eligibility alone does not establish parenthood. Different Subjects are allowed when the parent actually governs the child's contribution; equal Subjects do not establish that governance. An ancestor-owned Goal may govern definitions that fulfill its result in the targeted child Scope Unit without changing either Atom's owner. A relational Atom's Target Scope Unit does not replace its Owning Scope Unit in the structural test. Preserve the admitted Project Goal-to-Project Principle case, Type-specific restrictions, orphan permissions, and the acyclic normative-authority boundary. Do not turn a dependency, classification, containment, or source-layer relation into `child_of` merely to fill parent coverage.

