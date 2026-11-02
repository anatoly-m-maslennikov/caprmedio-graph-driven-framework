---
subjects:
  governs: Entity/Carrier/File.Main Content
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Content.Summary
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - Entity/Object/Continuant/Governing Objects/Atom.Content.Details
  - Entity/Object/Continuant/Term//Property
  - Entity/Carrier/File
version: 25
updated_at: 2026-10-29 09:57:57 +0400
relations: {}
atom_id: CA-D-479
content_role: Delivery
type: Policy
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
---
## Summary

Use stable headings for Atom body Properties

## Claim scope

Structured Main Content of Markdown Atom Carriers; the changed layout below is RMED-only.

## Claim

A complete RMED Atom must carry one ## Summary and one ## Claim as sibling properties at the same heading level, with optional ## Claim scope before Claim and optional ## Semantics then ## Details after it. Prose is directly under ## Claim. An optional ### Formal claim child contains one complete fenced formal expression. Its logical path is atom.content.claim.formal_claim. The prose is mandatory for a complete RMED Atom; the R-only Formal claim is independently optional. Child text does not satisfy the direct prose count. Both remain one Type-defined contribution. Do not create a separate Prose claim section, duplicate Claim field, or use the Summary value as the ## Summary heading.

Use a code-fence-aware heading outline to extract body-property paths. A section ends at the next real heading of the same or a higher level, or at end of Main Content. A lower-level real heading nests beneath the current parent; equal-level headings create sibling properties, and skipped heading numbers create no empty properties. Registered RMED sections at ## therefore remain siblings, while ### Formal claim nests only under ## Claim. Heading-like text inside a fenced block is content, not a body-property boundary. Nested supporting headings have their own paths and counts; their text does not count as direct Claim prose, and grouping headings may have zero direct text while declaring children.

Normalize each real heading name to lowercase, replace spaces with underscores, and strip characters other than letters, numbers, underscore and hyphen. Reject an empty normalized key or a duplicate normalized key under the same parent rather than overwriting or merging values. A flattened lookup is admissible only when its target is unambiguous; canonical paths retain their actual parent chain. These rules define the body-property mapping; executable support is a separate Engine responsibility.

Omit optional sections when absent rather than creating empty placeholders.

## Details

The registered RMED skeleton is:

````markdown
## Summary
(summary)

## Claim scope
(scope, when needed)

## Claim
(required prose)

### Formal claim
```text
(formal expression, when present)
```

## Semantics
(meaning, when useful)

## Details
(supporting details, when useful)
````

The conditional Claim scope requirement remains governed by R2160/D495.

The existing C/A/P/O layouts are unchanged: Analysis uses Question, Scope, Approach, Results and TLDR; Concern uses Concern, Evidences and Blast radius; Plan uses Objective and Details; Operations uses Operation and Details. Their own Type-specific and nested-property rules remain applicable. A Draft may be incomplete but must satisfy the complete applicable contract before promotion. This packet does not impose RMED Claim headings on other Roles.

The skeleton illustrates the ordinary same-level sibling and lower-level nesting rules: ## Claim followed by ### Formal claim yields content.claim.formal_claim.

R-only scope refinement (CA-A-1244): the optional ### Formal claim / content.claim.formal_claim is admitted only for Requirement Atoms for now. Method, Evaluation and Delivery have prose Claims with no operative formal child; code examples remain examples. Any earlier generic optional-formal wording in this Draft is limited by that Role condition. The complete one-Claim contract and optional supporting sections remain unchanged.
