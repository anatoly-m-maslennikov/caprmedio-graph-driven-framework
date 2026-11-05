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
version: 6
updated_at: 2026-11-03 23:25:51 +0400
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

The selected Carrier is the Markdown file delivering the selected Atom. Its filename includes the extension, and its location is the containing directory relative to the repository root.

### Formal Claim

```CFEL
# instances
Atom//$atom >> Carrier//$carrier;

$atom.Header.** >> $carrier.frontmatter;

$atom.Content.** >> $carrier.markdown;

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
