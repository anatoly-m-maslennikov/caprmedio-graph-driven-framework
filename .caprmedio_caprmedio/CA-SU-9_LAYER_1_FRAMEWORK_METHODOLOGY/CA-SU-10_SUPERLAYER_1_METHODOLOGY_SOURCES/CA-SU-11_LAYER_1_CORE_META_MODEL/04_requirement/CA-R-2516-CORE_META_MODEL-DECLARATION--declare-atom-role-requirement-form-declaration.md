---
atom_id: CA-R-2516
ref_id: CA-R-2516
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)/(.Header.Context.Form := Declaration)
tier: 3
status: Active
version: 6
updated_at: '2026-11-11 14:06:22 +0400'
---
## Summary

Declare Atom/(.Role := Requirement)/(.Form := Declaration)

## Claim

### Prose Claim


A Declaration states the applicable contract for its active Subject. Its Claim may contain several prose statements, CFEL formal expressions, or both when they form one coherent declaration about one topic.

Scope Unit Declaration is a Requirement Form using this template. It is not another Atom Role.

### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role in (Requirement)).Header.Context.Form :: Declaration;
```
