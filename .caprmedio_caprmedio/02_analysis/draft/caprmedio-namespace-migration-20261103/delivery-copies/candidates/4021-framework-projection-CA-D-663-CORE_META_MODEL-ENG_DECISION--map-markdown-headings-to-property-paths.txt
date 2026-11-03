---
atom_id: CA-D-663
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/File/Markdown
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Delivery
form: Eng Decision
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-663-CORE_META_MODEL-ENG_DECISION--map-markdown-headings-to-property-paths.md
  source_atom_id: CA-D-663
  source_atom_revision: 2
  source_sha256: 83926b3b757564cd02cfe61b80f34f00a9cacd2a9a4218c1177cad5c604a32a3
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Map Markdown headings to Property paths

## Claim

- Map heading ancestry to nested Content Properties.
- The first heading may have any level.
- Skipped levels create no empty Properties.
- Fenced heading-like text creates no section.
- Preserve the actual heading tree.

## Details

Both examples expose content.1.2.3 with direct value 4:

```markdown
# 1
## 2
### 3
4
```

```markdown
## 1
### 2
5
#### 3
4
```

In the second example, content.1.2 has its direct content 5 and a child section 3 containing 4. Retrieving the parent section returns its descendant subtree as well. Value cardinality counts direct content, not the children's values. Property declarations independently permit or forbid direct values and children; no special double-dot Property notation is introduced.

Normalize each heading name to lowercase, replace spaces with underscores, and remove characters other than letters, numbers, underscore and hyphen. Reject an empty normalized key or two equal normalized keys under the same parent; never merge or overwrite their content. Equal keys under different parents retain distinct paths. A failed mapping leaves the original Markdown intact and reports the conflict; it does not prevent retaining or reading the source as Markdown.

Retrieving a section returns its selected heading and the entire descendant subtree through the next real heading of the same or higher level. In the second example, retrieving `content.1.2` returns `### 2`, its direct content `5`, and the child heading `#### 3` with content `4`. The selected heading and child content do not add to the direct-value count.

Parsing arbitrary Markdown does not establish Atom Form conformance or graph authority.
