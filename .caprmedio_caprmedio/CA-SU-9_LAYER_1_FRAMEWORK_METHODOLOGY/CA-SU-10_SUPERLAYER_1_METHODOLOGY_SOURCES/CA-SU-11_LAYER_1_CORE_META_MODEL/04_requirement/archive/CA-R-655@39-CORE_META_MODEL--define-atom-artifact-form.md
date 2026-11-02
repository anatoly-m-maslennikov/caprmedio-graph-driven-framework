---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom
  depends_on:
  - Entity
version: 39
updated_at: 2026-10-29 09:39:47 +0400
relations: {}
atom_id: CA-R-655@39
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary
Define Atom Artifact Form

## Claim scope
Atoms.

## Claim

an Atom **means** the smallest independently governed Artifact.

### Formal claim

```text
Atom.Content Role[string]{1}
Atom.Type[string]{1}
Atom.ID[string]{1}
Atom.Status[string]{1}
Atom.Updated At[datetime]{1}
Atom.Version Number[int]{1}
Atom.Author[string]{1}
Atom.Tier[int]{1}
Atom.Label[string]{0..1}
Atom.Content.Summary[string]{1}
Atom.Local Scope Unit[string]{0..1}
Atom.Target Scope Unit[string]{0..1}
Atom.Subjects{0}
Atom.Subjects.Governs[string]{1}
Atom.Subjects.Depends On[string]{0+}
Atom.Relations{0}
Atom.Content{0}
```

Authored relation endpoint permissions are separate from reusable Relation Type meaning:

- rationale_for is owned by a Rationale Analysis Atom and targets one RMED Atom it explains.
- method_for is owned by a Method Atom and targets one Requirement it serves.
- delivery_for is owned by a Delivery Atom and targets one Requirement or Method it realizes.
- concern_about is owned by a Concern Atom and targets the directly affected governed entity.

Each entry represents one directed source-Type-target tuple, not a restriction that an owner can store only one entry of that Type. An Atom target must resolve to its canonical Current version; Draft and Archived targets are not admitted merely because an ID-like string is present.

## Details

### Governing child_of endpoint constraints

a stored governing `child_of` relation **must** point from a Current child Atom to a Current applicable parent Atom. The target **must** be in the same Scope Unit with a strictly lower numeric Tier, **or** in a strict ancestor Scope Unit with no Tier comparison, **or** satisfy the exact same-Project Project Configuration → Core Meta-Model logical-role prerequisite declared by CA-R-1218 with no Tier comparison. Every other descendant or sibling target does not satisfy the ordering. The parent's Substance, Target Scope Unit when applicable, and Substance Scope **must** support the authority claimed by that relation.



Structural eligibility alone does not establish parenthood. Different Subjects are allowed when the parent actually governs the child's contribution; equal Subjects do not establish that governance. An ancestor-owned Goal may govern definitions that fulfill its result in the targeted child Scope Unit without changing either Atom's owner. An ordinary relational Atom's Target Scope Unit does not replace its Local Scope Unit in the ordering test. The admitted Operator-owned Project Goal case instead resolves its Target Project as the ordering context under CA-R-2149; the owner remains the Operator Actor. Preserve the admitted Project Goal-to-Project Principle case, orphan permissions, and the acyclic normative-authority boundary. No Content Role or Type-to-Tier restriction is introduced. Do not turn a dependency, classification, containment, or source-layer relation into `child_of` merely to fill parent coverage.

For ordering only, an endpoint verified as a Current Requirement of Type Project Goal under CA-R-2152 and CA-R-2132 uses its Target Project as its ordering Scope context. Its actual owner remains the Operator Actor. The Target Project must be the Project containing the other endpoint's declared Local Scope Unit; an unrelated Project does not qualify. Ordinary endpoints, including non-Project Goals, continue to use their Local Scope Unit. Compare the resulting contexts with the same lower-target-Tier, strict-ancestor, or exact declared Project Configuration → Core Meta-Model prerequisite rule under CA-R-2149. Unresolved logical-role identity, same-Project correspondence, or prerequisite declaration remains unresolved and does not pass. The prerequisite is one-way and non-transitive; it does not admit the reverse direction, the Project root, the Methodology Sources owner, an Extension, or a descendant source merely through containment. Do not create an Operator Scope Unit, change ownership, add a stored Property, or exempt a Project Goal from ordering. Unverified Goal identity, ownership, Tier or Project membership remains unresolved and does not pass.
