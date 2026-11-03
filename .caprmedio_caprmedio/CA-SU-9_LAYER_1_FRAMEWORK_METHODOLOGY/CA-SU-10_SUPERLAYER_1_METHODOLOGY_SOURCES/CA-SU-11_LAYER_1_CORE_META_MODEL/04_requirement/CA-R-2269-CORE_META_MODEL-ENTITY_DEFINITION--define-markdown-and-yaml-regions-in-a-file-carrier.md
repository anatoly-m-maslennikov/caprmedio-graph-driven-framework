---
atom_id: CA-R-2269
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/File
relations: {}
version: 3
updated_at: 2026-11-02 00:18:22 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Rule
---
## Summary

Define Markdown and YAML regions in a File Carrier

## Claim

### Prose Claim


For a Markdown File Carrier, Main Content is its Markdown body and YAML Frontmatter is its optional structured metadata region. Main Content can contain Paragraphs and CCE Operator occurrences; these are content parts, not additional Files. A Frontmatter Scalar is one direct primitive value within a declared metadata field. These logical regions are not separate Carriers.

The Filename may contain zero or more Scope Unit Tokens. Each serialized Scope Unit reference uses one token under CA-D-302; this does not require all File names to carry such a token.


```text
Carrier/File.Main Content[string]{0..1}
Carrier/File.Main Content.Paragraph[string]{0+}
Carrier/File.Main Content.CCE Operator[string]{0+}
Carrier/File.YAML Frontmatter{0}
Carrier/File.YAML Frontmatter.Scalar[scalar]{0+}
Carrier/File.Filename.Scope Unit Token[string]{0+}
```

## Details

The declared File format and applicable D Policy determine required regions, tokens and actual encoding. Complete RMED Atom Markdown still requires its Summary and Claim. This definition adds no section, field, token or file to those policies.
