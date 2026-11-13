---
atom_id: CA-D-662
ref_id: CA-D-662@6
container:
  scope_unit: CA-SU-11
role: Delivery
form: Eng Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)/(.Header.Context.Form
    := Declaration)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
tier: 3
status: archived
version: 6
updated_at: 2026-11-09 00:03:55 +0400
carrier_destination:
  file:
    name: CA-D-662@6-CORE_META_MODEL-ENG_DECISION--encode-node-declarations-in-yaml.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Encode Node Declarations in YAML

## Claim

### Prose Claim

Deliver a Node Declaration’s Header through the common recursive Atom-to-YAML mapping. Preserve its declared Property hierarchy and value cardinalities. Header names and named values use the common lowercase-and-underscore encoding.

The declared Main Subject identifies the canonical HAS_ACTIVE_SUBJECT target. Direct Relation facts have one authored source; their encoded names retain that Relation’s meaning. Container references retain the declared target kind and exact target ID.

### Formal Claim

```CFEL
# instances
$declaration[<Atom>, (.Header.Context.Role = Requirement) AND (.Header.Context.Form = Declaration)] >> $carrier[<Carrier>];

$declaration.Header >> $carrier.frontmatter
```

## Details

Named-value encoding examples: `Requirement` becomes `requirement`; `Declaration` becomes `declaration`. IDs retain their exact spelling.
