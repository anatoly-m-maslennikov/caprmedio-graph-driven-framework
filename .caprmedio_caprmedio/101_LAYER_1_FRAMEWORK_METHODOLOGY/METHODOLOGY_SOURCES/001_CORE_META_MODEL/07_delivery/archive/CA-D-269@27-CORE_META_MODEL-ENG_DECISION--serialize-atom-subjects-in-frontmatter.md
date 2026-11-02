---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Subjects
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Subjects
  - Entity/Graph Syntax > Relation//GOVERNS
  - Entity/Graph Syntax > Relation//DEPENDS_ON
  - Entity
  - Entity/Graph Syntax > Relation
version: 27
updated_at: 2026-10-29 08:06:42 +0400
relations: {}
atom_id: CA-D-269@27
content_role: Delivery
type: Policy
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
## Summary

Serialize Atom Subjects in Frontmatter

## Claim scope

New **or** migrated Markdown Atom Carriers.

## Claim

Follow YAML parsing for property values under A1296: unquoted asdf is a string, unquoted null or an empty value after a key is null, and quoted empty text or quoted null is a string. Preserve the intended parsed value through serialization; do not silently turn null or empty strings into omitted properties. Multiple values remain a sequence under one key.

Serialize Entity values as strings using the admitted Entity notation. The carrier type does not prove the target already existed; a defining Atom can introduce its target and path together under CA-A-1285. Keep the existing subjects.depends_on key spelling. This does not change explicit existing-kind references or create a second stored target-type field.

Preserve `{n}`, `{n+}` and `{n..m}` exactly in formal Claim text, including braces, plus sign and range dots. Do not serialize these annotations as new YAML fields or confuse them with YAML collection delimiters. In Markdown, keep the formal expression in its fenced Formal claim section. When a scalar carrier holds the expression, its decoded text retains the same characters. CA-A-1280 supplies the count meanings; this changes no Current carrier or parser.

A complete new or migrated Current Atom carries subjects as a mapping of child properties, with no direct subjects value. It carries exactly one scalar Entity Path in subjects.governs and zero or more dependency paths in the existing subjects.depends_on key. The dependency values are an unordered sequence of unique scalar paths; an omitted dependency key means zero dependencies. The mapping is the carrier for the nested properties and is not counted as a direct value of subjects. A Draft may remain incomplete before promotion.

Each YAML key occurs once within its immediate mapping. Store multiple values as a sequence under that one key, never as repeated sibling keys. Count direct scalar values or sequence members at the addressed property; do not count nested mapping keys or their values toward a grouping parent. YAML sequences are representation, not a list value Format. These rules follow CA-A-1283.

The governs or depends_on key encodes the Entity Relation Kind; the source Atom is implicit and each path encodes its target. Resolve each target under CA-R-1202 without an intermediate Entity/Reference property or a repeated target-kind field.

Preserve every scalar Entity Path through YAML decoding, including `//`, `/`, `.`, `:`, `>`, `@`, parentheses, and Entity backslashes. YAML outer quotes are not part of the expression. Prefer a single-quoted YAML scalar for an Entity escape; when double quotes are used, escape the YAML backslash so the decoded scalar still contains the intended Entity escape. Do not turn Entity notation into nested YAML fields, strip an existing-target marker, or move a reference boundary: `@(canonical Entity path)` remains intact through its matching close, and any continuation after that close remains outside the reference.

Preserve current reference identity when canonical paths change: migrate affected Current ordinary Entity paths and full-path references; an `@` reference using an unchanged unique primary-kind name remains valid, while a primary-kind rename also migrates its name-based references. Do not create old-path aliases or an alias registry. Distinct primary-kind declarations have unique names across the effective Entity model; repeated references do not declare duplicates, and properties may reuse names under different bearers. These serialization rules preserve admitted references without changing a Current carrier, parser, or Relation storage schema.

An unmigrated carrier may temporarily retain `subjects.<governs|depends_on>.<continuant|occurrent>` only until its explicitly assigned carrier-migration Task executes. That migration-limited layout preserves the same direct relation facts and target identities and is not a second canonical representation. Preserve `Source ((RELATION_TYPE)) Target` when carrying a formal Claim or readable model edge, distinct from the node selector stored in `subjects.governs` or `subjects.depends_on`; it introduces no reverse-direction field because its inverse is the declared derived Relation view of the direct source fact.

## Details

Legacy temporal-classification authority and bulk carrier conversion remain with their separately assigned migration Tasks. For example, an Entity escape can be serialized as `governs: 'Engineering/CI\/CD'`; `@(Module)` is an admitted existing-kind reference. Canonical target resolution and alternate-path choices follow their governing Entity rules; unsettled choices are tracked in CA-A-1236. See CA-A-1240.
