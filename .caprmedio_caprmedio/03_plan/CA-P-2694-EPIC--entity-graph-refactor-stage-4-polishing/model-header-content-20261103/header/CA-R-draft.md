---
atom_id: CA-R-draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header
version: 1
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Atom.Header

## Claim

### Prose Claim

Atom.Header groups the Atom Properties carried in YAML frontmatter, including for Draft Atoms.

### Formal Claim

```CFEL
Atom.Header{:1}: []{:0};
Atom.Header.*[string,in(ID, Role, Form, Version, Status, Updated At, Label, Tier, Subjects, Relations, Carrier Destination, Priority, AI Agent Confidence Threshold, Work Sequence Number)]{:0+}
```

