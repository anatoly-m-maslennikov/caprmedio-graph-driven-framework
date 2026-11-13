---
atom_id: CA-D-664
ref_id: CA-D-664
container:
  scope_unit: CA-SU-11
role: Delivery
form: Eng Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
tier: 3
status: active
version: 9
updated_at: '2026-11-13T05:43:12.969816+00:00'
carrier_destination:
  file:
    name: CA-D-664-CORE_META_MODEL-ENG_DECISION--deliver-atoms-to-markdown-files.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Deliver Atoms to Markdown files

## Claim

### Prose Claim

The selected Carrier is the Markdown file delivering the selected Atom. Its filename includes the extension and equals the Atom Header Destination File Name. Its location equals the Atom Header Destination File Path and is the containing directory relative to the repository root.

Deliver the complete Header recursively as YAML frontmatter, preserving its declared nesting. Deliver declared Content Properties as Markdown sections.

For YAML, encode names and named values in lowercase words joined by single underscores. This is Carrier encoding; canonical model names and object identities retain their meaning. IDs, opaque references, free text and typed scalar data retain their exact values. Carrier metadata retains its exact spelling, including filenames, paths and locator values copied into Header destination fields.

### Formal Claim

```python
# instances
deliver(source="Atom//$atom", carrier="Carrier//$carrier")
```

## Details

The file layout is:

```text
---
<yaml>
---
<markdown>
```
