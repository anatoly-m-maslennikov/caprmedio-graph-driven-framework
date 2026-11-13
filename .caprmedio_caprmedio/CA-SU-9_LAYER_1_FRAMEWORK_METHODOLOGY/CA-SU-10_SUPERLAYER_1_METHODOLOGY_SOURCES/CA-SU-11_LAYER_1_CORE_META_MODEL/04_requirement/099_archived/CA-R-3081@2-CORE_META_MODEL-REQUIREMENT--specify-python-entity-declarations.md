---
identity:
  atom_id: CA-R-3081
  ref_id: CA-R-3081@2
context:
  role: requirement
  form: requirement
  tier: 3
  container:
    scope_unit: CA-SU-11
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom.Content.Claim.Formal Claim
state:
  version: 2
  status: archived
  updated_at: '2026-11-12T17:46:13.961621+00:00'
destination:
  file:
    name: CA-R-3081@2-CORE_META_MODEL-REQUIREMENT--specify-python-entity-declarations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
---
## Summary

Specify Python entity declarations

## Claim

### Prose Claim

- Declare each named Model Entity, Property, or instance with `declare_entity`.
- For a narrower kind, pass its Python class as `entity_class`. A singleton uses an explicit instance population cardinality in the Project. Declare the parent using ordinary Python class syntax. Derive the narrower Model address from that parent and the declared name.
- Use `qualification_property_path` when the declared name is an allowed Property value. A Form class extends its Role class.
- For a Property, pass `entity_name`, `relation_name="IS_PROPERTY_OF"`, and its bearer as `base_path`. Declare Property occurrence, direct value, and dependent Property cardinalities separately.
- Put Model and instance Relation permissions in separate declaration fields.
- For a conditional instance rule, define a named Python function with a Model-typed parameter and a `bool` return. Pass it to `declare_entity` as `instance_check`.

## Details

The Core Model resolver binds Python class imports to declared Model addresses. A Claim supplies its own imports and declaration arguments. Primary Entities are Python classes. Properties become typed data fields on their bearers. Use standard dataclass field machinery when a class needs a data representation. Keep each inherited field’s Property Declaration on its original bearer. An Entity's local rule overrides an inherited rule for the same Property or Relation. A local MODEL override explicitly identifies the inherited rule it replaces.

- Register each class by its full qualified Model address. Each Role-scoped Form has its own class identity.
- Represent Properties as typed dataclass fields on their declared bearer. Assemble nested records from their Property Declarations and retain field provenance.
