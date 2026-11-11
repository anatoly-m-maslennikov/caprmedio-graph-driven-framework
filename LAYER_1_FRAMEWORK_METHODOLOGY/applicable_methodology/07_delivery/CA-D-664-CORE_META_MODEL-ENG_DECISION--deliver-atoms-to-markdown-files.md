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
status: Active
version: 8
updated_at: 2026-11-09 00:03:55 +0400
carrier_destination:
  file:
    name: CA-D-664-CORE_META_MODEL-ENG_DECISION--deliver-atoms-to-markdown-files.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-664-CORE_META_MODEL-ENG_DECISION--deliver-atoms-to-markdown-files.md
  source_atom_id: CA-D-664
  source_atom_revision: 8
  source_sha256: 0fa7400feb2fcad6ff5dea9c3dd8d2c994c458b3306366e9ec556de2ab5ba31c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Deliver Atoms to Markdown files

## Claim

### Prose Claim

The selected Carrier is the Markdown file delivering the selected Atom. Its filename includes the extension, and its location is the containing directory relative to the repository root.

Deliver the complete Header recursively as YAML frontmatter, preserving its declared nesting. Deliver declared Content Properties as Markdown sections.

For YAML, encode names and named values in lowercase words joined by single underscores. This is Carrier encoding; canonical model names and object identities retain their meaning. IDs, opaque references, free text and typed scalar data retain their exact values. Carrier metadata retains its exact spelling, including filenames, paths and locator values copied into Header destination fields.

### Formal Claim

```CFEL
# instances
Atom//$atom >> Carrier//$carrier;

$atom.Header >> $carrier.frontmatter;

$atom.Content >> $carrier.markdown;

$carrier.filename == $atom.Header.Carrier Destination.File.Name;

$carrier.location == $atom.Header.Carrier Destination.File.Path
```

## Details

The file layout is:

```text
---
<yaml>
---
<markdown>
```
