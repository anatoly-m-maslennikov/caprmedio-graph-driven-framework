---
atom_id: CA-A-1265@1
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Formal Model
version: 1
updated_at: 2026-10-28 23:06:08 +0400
relations: {}
tier: 3
---
# Summary

Allow formulas as allowed-value expressions

## Decision

The colon keeps its existing meaning: x: y declares an allowed value for x. Its right-hand side can be a literal value, such as Requirement, or a formula specifying the allowed value. A formula is not a quoted literal containing the formula's text.

Use the Operator's ID expression with the colon:

```text
Atom.id: @(Project.name.prefix)-@(content role.first letter)-number[int, unique(its current kind)]{1}
```

This is still an allowed-value declaration, not an assignment or editing command. Do not introduce an equals operator for this purpose. Structural containment keeps >. The governed Subject of this Atom-ID rule remains the ID property; the formula belongs in the formal Claim, not a newly invented Subject instance.

## Scope and remaining work

This settles the meaning of colon and the formula's role. It does not by itself complete formula grammar, the bindings of the referenced properties, the contextual number Selection, or a parser/evaluator. Formula is not added as a primitive value Format or a primary entity kind. The function API proposal remains separate.

## State

Notation and proposal Drafts are refined; no Current source or runtime is changed.
