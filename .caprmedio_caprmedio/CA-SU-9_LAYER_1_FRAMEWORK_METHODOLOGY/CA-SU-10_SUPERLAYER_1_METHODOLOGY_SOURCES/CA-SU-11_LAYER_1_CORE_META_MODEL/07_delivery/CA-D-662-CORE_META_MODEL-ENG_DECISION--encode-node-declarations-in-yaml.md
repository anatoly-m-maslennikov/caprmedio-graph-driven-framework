---
atom_id: CA-D-662
ref_id: CA-D-662
container:
  scope_unit: CA-SU-11
role: Delivery
form: Eng Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Declaration)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
tier: 3
status: Active
version: 4
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-D-662-CORE_META_MODEL-ENG_DECISION--encode-node-declarations-in-yaml.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Encode Node Declarations in YAML

## Claim

### Prose Claim


Node Declaration carriers require role, form and subjects.active. Encode passive Subjects as subjects.passive when present. Omit the author field.


- Encode subjects.active as one scalar path and subjects.passive as zero or more unique paths.
- Obtain the canonical HAS_ACTIVE_SUBJECT link from subjects.active. It is not a derived view of another Relation; do not store the same fact twice.
- Store authored instance references under relations.
- The containment reference key is its target kind: atom or scope_unit. The referenced target must match that kind.
- contained_by encodes IS_CONTAINED_BY; CONTAINS is derived.
- Relation links do not duplicate Subject membership.

### Formal Claim

```CFEL
# instances
Atom.Header.Role >> Carrier//Markdown file.frontmatter.role;

Atom.Header.Form >> Carrier//Markdown file.frontmatter.form;

Atom.Header.Topics.Main Subject >> Carrier//Markdown file.frontmatter.subjects.active;

Atom.Header.Topics.Dependencies >> Carrier//Markdown file.frontmatter.subjects.passive;

Atom.Header.Relations >> Carrier//Markdown file.frontmatter.relations
```

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
