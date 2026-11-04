---
atom_id: CA-D-664
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom
version: 6
relations: {}
tier: 3
role: Delivery
form: Eng Decision
updated_at: 2026-11-03 23:25:51 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-664-CORE_META_MODEL-ENG_DECISION--deliver-atoms-to-markdown-files.md
  source_atom_id: CA-D-664
  source_atom_revision: 6
  source_sha256: 751a86d2ae43330bf75ba0d41c1887cb418c24caa2b5ba4885970fb02427e5aa
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
