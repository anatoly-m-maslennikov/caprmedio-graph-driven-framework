---
atom_id: CA-R-2474
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Node
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---
## Summary

Bind direct Property values on instances

## Claim

### Prose Claim


HAS_VALUE binds a Property on an instance to its admitted literal value. For example, the version Property of Atom instance CA-P-123 has value 1. The Property declaration supplies its value format, admitted domain and cardinality; the literal 1 is not a separately declared graph Node and requires no Declaration Atom.

HAS_VALUE is a value binding rather than an ordinary Node-to-Node graph Relation. It must not create graph endpoints or independently authored inverse facts for literals. A Primary Node has no direct value. A Property on a Primary Node instance may hold direct values where its effective declaration permits them, including inherited Property declarations. Applying a declared Property to an instance does not instantiate that Property through HAS_INSTANCE or give its declaration another bearer.
