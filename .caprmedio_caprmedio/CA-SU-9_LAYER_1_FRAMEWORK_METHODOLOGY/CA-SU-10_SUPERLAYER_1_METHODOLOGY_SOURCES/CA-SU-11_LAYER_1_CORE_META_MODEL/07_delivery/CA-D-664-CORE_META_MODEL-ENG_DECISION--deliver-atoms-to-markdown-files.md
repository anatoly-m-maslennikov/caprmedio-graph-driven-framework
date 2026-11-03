---
atom_id: CA-D-664
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom
version: 5
relations: {}
tier: 3
role: Delivery
form: Eng Decision
updated_at: 2026-11-03 00:20:05 +0400
---
## Summary

Deliver Atoms to Markdown files

## Claim

### Formal Claim

```CFEL
Atom >> Carrier//Markdown file;
Atom.**!(.Content, .Content.**) >> Carrier//Markdown file.frontmatter;
Atom.Header.Carrier Destination.File.Name >> Carrier//Markdown file.frontmatter.carrier_destination.file.name;
Atom.Header.Carrier Destination.File.Path >> Carrier//Markdown file.frontmatter.carrier_destination.file.path;
Atom.Content.** >> Carrier//Markdown file.markdown;
Atom.Header.Carrier Destination.File.Name >> Carrier//Markdown file.filename;
Atom.Header.Carrier Destination.File.Path >> Carrier//Markdown file.location;
Carrier//Markdown file.filename{:1}: [string]{:1};
Carrier//Markdown file.location{:1}: [string]{:1};
Carrier//Markdown file.frontmatter.author{:0}
```

### Prose Claim


The Carrier below is the Markdown file delivering this Atom.

Frontmatter starts at the beginning of the file:

1. An opening line containing `---`.
2. YAML data.
3. A closing line containing `---`.

Location is the directory path relative to the repository root.

