---
atom_id: CA-R-2508@3-draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom
version: 3
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
---
## Summary

Declare Atom

## Claim

### Formal Claim

```CFEL
Atom;
UNIQUE(Atom//, (.Header.ID, .Header.Version));
Atom.*[string,in(Header,Content)]{:2};
Atom ((NARROWER_THAN)) Continuant
```

## Semantics

An Atom is the smallest independently governed Artifact.
