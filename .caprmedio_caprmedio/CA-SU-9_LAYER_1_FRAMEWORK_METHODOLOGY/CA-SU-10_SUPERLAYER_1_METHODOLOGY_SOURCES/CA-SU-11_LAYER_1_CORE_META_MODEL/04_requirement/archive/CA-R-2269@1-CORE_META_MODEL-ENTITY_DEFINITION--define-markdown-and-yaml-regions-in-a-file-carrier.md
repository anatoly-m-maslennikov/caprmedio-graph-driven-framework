---
atom_id: CA-R-2269@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Carrier/File
relations: {}
version: 1
updated_at: 2026-10-29 09:55:37 +0400
---
## Summary

Define Markdown and YAML regions in a File Carrier

## Claim

For a Markdown File Carrier, Main Content is its Markdown body and YAML Frontmatter is its optional structured metadata region. Main Content can contain Paragraphs and CCE Operator occurrences; these are content parts, not additional Files. A Frontmatter Scalar is one direct primitive value within a declared metadata field. These logical regions are not separate Carriers.

The Filename may contain zero or more Scope Unit Tokens. Each serialized Scope Unit reference uses one token under CA-D-302; this does not require all File names to carry such a token.

### Formal claim

```text
Entity/Carrier/File.Main Content[string]{0..1}
Entity/Carrier/File.Main Content.Paragraph[string]{0+}
Entity/Carrier/File.Main Content.CCE Operator[string]{0+}
Entity/Carrier/File.YAML Frontmatter{0}
Entity/Carrier/File.YAML Frontmatter.Scalar[scalar]{0+}
Entity/Carrier/File.Filename.Scope Unit Token[string]{0+}
```

## Details

The declared File format and applicable D Policy determine required regions, tokens and actual encoding. Complete RMED Atom Markdown still requires its Summary and Claim. This definition adds no section, field, token or file to those policies.
