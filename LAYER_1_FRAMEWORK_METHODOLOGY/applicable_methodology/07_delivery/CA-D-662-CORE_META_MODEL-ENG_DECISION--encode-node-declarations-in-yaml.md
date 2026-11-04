---
atom_id: CA-D-662
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Declaration)
  passive:
  - CAPRMEDIO_MODEL <+ Atom
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Delivery
form: Eng Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-662-CORE_META_MODEL-ENG_DECISION--encode-node-declarations-in-yaml.md
  source_atom_id: CA-D-662
  source_atom_revision: 4
  source_sha256: f311699df3697e761666ff198ebd40b9959c4f1e553db3425160055f0a647135
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Encode Node Declarations in YAML

## Claim

### Formal Claim

```CFEL
# instances
Atom.Header.Role >> Carrier//Markdown file.frontmatter.role;

Atom.Header.Form >> Carrier//Markdown file.frontmatter.form;

Atom.Header.Subjects.Active >> Carrier//Markdown file.frontmatter.subjects.active;

Atom.Header.Subjects.Passive >> Carrier//Markdown file.frontmatter.subjects.passive;

Atom.Header.Relations >> Carrier//Markdown file.frontmatter.relations
```

### Prose Claim


Node Declaration carriers require role, form and subjects.active. Encode passive Subjects as subjects.passive when present. Omit the author field.


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
