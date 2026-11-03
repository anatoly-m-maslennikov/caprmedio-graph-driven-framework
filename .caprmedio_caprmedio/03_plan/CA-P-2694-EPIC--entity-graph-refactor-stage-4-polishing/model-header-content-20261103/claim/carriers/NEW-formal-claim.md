---
atom_id: CA-R-draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content.Claim.Formal Claim
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Atom.Content.Claim.Formal Claim

## Claim

### Formal Claim

```CFEL
Atom/(.Header.Role in RMED).Content.Claim.Formal Claim{:0..1}: [markdown]{:1};
Atom/(.Header.Role in RMED).Content.Claim.Formal Claim.*[]{:0};
FENCED_LABELS(Atom/(.Header.Role in RMED).Content.Claim.Formal Claim): [in (CFEL)]{:1}
```

### Prose Claim

Formal Claim is a child Property of an ordinary RMED Claim. Its value is Markdown and contains a CFEL-labelled code fence.
