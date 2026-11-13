---
atom_id: CA-R-2719
ref_id: CA-R-2719@2-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header
tier: 3
status: Draft
version: 2
updated_at: 2026-11-05 03:53:43 +0400
carrier_destination:
  file:
    name: CA-R-2719@2-draft-CORE_META_MODEL-DECLARATION--declare-atom-header.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---
## Summary

Declare Atom.Header

## Claim

### Prose Claim

Atom.Header groups the Atom Properties carried in YAML frontmatter, including for Draft Atoms.

### Formal Claim

```python
# model
property_rule(address='Atom.Header', occurrences='1', value_format='', values='0')
allowed_children(address='Atom.Header', names=('Identity','Context','Relations','State','Destination'), name_format='string', occurrences='0+')
order_before(first='Atom.Header.Identity', second='Atom.Header.Context')
order_before(first='Atom.Header.Context', second='Atom.Header.Relations')
order_before(first='Atom.Header.Relations', second='Atom.Header.State')
order_before(first='Atom.Header.State', second='Atom.Header.Destination')
```

