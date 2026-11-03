---
atom_id: CA-R-2508
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom
version: 2
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
---
## Summary

Declare Atom

## Claim

```CFEL
Atom;
UNIQUE(Atom//, (.ID, .Version));
Atom ((NARROWER_THAN)) @Continuant
```

## Semantics

An Atom is the smallest independently governed Artifact.
