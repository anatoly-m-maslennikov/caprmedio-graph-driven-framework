---
atom_id: CA-D-664
ref_id: CA-D-664
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
version: 6
tier: 3
role: Delivery
form: Eng Decision
updated_at: 2026-11-03 23:25:51 +0400
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-D-664-CORE_META_MODEL-ENG_DECISION--deliver-atoms-to-markdown-files.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
---
## Summary

Deliver Atoms to Markdown files

## Claim

### Formal Claim

```CFEL
# instances
Atom//$atom >> Carrier//$carrier;

$atom.Header.** >> $carrier.frontmatter;

$atom.Content.** >> $carrier.markdown;

$carrier.filename == $atom.Header.Carrier Destination.File.Name;

$carrier.location == $atom.Header.Carrier Destination.File.Path
```

### Prose Claim

The selected Carrier is the Markdown file delivering the selected Atom. Its filename includes the extension, and its location is the containing directory relative to the repository root.

## Details

The file layout is:

```text
---
<yaml>
---
<markdown>
```
