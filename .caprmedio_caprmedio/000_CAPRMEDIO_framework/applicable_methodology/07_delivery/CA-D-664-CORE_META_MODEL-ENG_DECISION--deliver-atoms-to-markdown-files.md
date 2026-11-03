---
atom_id: CA-D-664
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom
version: 5
relations: {}
tier: 3
role: Delivery
form: Eng Decision
updated_at: 2026-11-03 00:20:05 +0400
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-664-CORE_META_MODEL-ENG_DECISION--deliver-atoms-to-markdown-files.md
  source_atom_id: CA-D-664
  source_atom_revision: 5
  source_sha256: 4f4837b4cf678e28db99550d032a7fe2a01911a3046012252a61056ce4aa1358
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Deliver Atoms to Markdown files

## Claim

The Carrier below is the Markdown file delivering this Atom.

Frontmatter starts at the beginning of the file:

1. An opening line containing `---`.
2. YAML data.
3. A closing line containing `---`.

Location is the directory path relative to the repository root.

```CFEL
Atom >> @Carrier//Markdown file;
Atom.**!(.Content, .Content.**) >> @Carrier//Markdown file.frontmatter;
Atom.Carrier Destination.File.Name >> @Carrier//Markdown file.frontmatter.carrier_destination.file.name;
Atom.Carrier Destination.File.Path >> @Carrier//Markdown file.frontmatter.carrier_destination.file.path;
Atom.Content.** >> @Carrier//Markdown file.markdown;
Atom.Carrier Destination.File.Name >> @Carrier//Markdown file.filename;
Atom.Carrier Destination.File.Path >> @Carrier//Markdown file.location;
@Carrier//Markdown file.filename{:1}: [string]{:1};
@Carrier//Markdown file.location{:1}: [string]{:1};
@Carrier//Markdown file.frontmatter.author{:0}
```
