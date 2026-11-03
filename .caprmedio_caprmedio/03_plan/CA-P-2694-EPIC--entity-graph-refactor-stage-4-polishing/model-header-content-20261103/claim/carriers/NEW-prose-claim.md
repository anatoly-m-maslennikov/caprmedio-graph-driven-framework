---
atom_id: CA-R-draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content.Claim.Prose Claim
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Atom.Content.Claim.Prose Claim

## Claim

### Formal Claim

```CFEL
Atom/(.Header.Role in RMED).Content.Claim.Prose Claim{:0..1}: [markdown]{:1};
Atom/(.Header.Role in RMED).Content.Claim.Prose Claim.*[]{:0}
```

### Prose Claim

Prose Claim is a child Property of an ordinary RMED Claim. Its value is ordinary Markdown; headings within that value are not Properties unless an applicable declaration admits them.
