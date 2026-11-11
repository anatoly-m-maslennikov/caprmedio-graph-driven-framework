---
atom_id: CA-D-664
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Delivery
form: Eng Decision
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
@Carrier//Markdown file.filename{:1}: [string]{:1};
@Carrier//Markdown file.location{:1}: [string]{:1};
@Carrier//Markdown file.frontmatter.author{:0}
```
