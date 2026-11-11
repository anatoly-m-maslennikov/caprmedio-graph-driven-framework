---
atom_id: CA-D-662
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom/(.Role := Requirement)/(.Form := Declaration)
  passive:
  - Atom
version: 4
updated_at: 2026-11-02 07:52:54 +0400
relations: {}
tier: 3
role: Delivery
form: Eng Decision
---
## Summary

Encode Node Declarations in YAML

## Claim

Node Declaration carriers require role, form and subjects.active. Encode passive Subjects as subjects.passive when present. Omit the author field.

```CFEL
Atom.Role >> @Carrier//Markdown file.frontmatter.role;
Atom.Form >> @Carrier//Markdown file.frontmatter.form;
Atom.Subjects.Active >> @Carrier//Markdown file.frontmatter.subjects.active;
Atom.Subjects.Passive >> @Carrier//Markdown file.frontmatter.subjects.passive;
Atom.Relations >> @Carrier//Markdown file.frontmatter.relations
```

- Encode subjects.active as one scalar path and subjects.passive as zero or more unique paths.
- Obtain the canonical HAS_ACTIVE_SUBJECT link from subjects.active. It is not a derived view of another Relation; do not store the same fact twice.
- Store authored instance references under relations.
- The containment reference key is its target kind: atom or scope_unit. The referenced target must match that kind.
- contained_by encodes IS_CONTAINED_BY; CONTAINS is derived.
- Relation links do not duplicate Subject membership.

## Details

```yaml
role: Requirement
form: Declaration
subjects:
  active: "<active Node path>"
  passive:
    - "<passive Node path>"
relations:
  contained_by:
    scope_unit: ENGINE
```
