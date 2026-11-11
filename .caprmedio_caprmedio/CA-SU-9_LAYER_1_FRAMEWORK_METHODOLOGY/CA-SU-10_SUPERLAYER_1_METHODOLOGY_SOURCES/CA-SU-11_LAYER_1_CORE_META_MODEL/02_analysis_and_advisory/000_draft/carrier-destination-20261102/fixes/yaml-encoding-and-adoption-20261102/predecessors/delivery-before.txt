---
atom_id: CA-D-664@3-draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  active: Atom
version: 3
relations: {}
tier: 3
role: Delivery
form: Eng Decision
updated_at: 2026-11-02 21:35:35 +0400
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
Atom.Content.** >> @Carrier//Markdown file.markdown;
Atom.Carrier Destination.File.Name >> @Carrier//Markdown file.filename;
Atom.Carrier Destination.File.Path >> @Carrier//Markdown file.location;
@Carrier//Markdown file.filename{:1}: [string]{:1};
@Carrier//Markdown file.location{:1}: [string]{:1};
@Carrier//Markdown file.frontmatter.author{:0}
```
