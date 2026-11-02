---
atom_id: CA-A-1282@2
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Model::CAPRMEDIO::Graph Syntax
version: 2
relations: {}
tier: 3
updated_at: 2026-10-29 21:51:04 +0400
---
# Summary

Defer general formula expressions

## Decision

Defer formula expressions in general, rather than only the Atom ID formula. Retain them as a separate Specification Proposal; they are not part of the syntax being prepared for adoption now.

The retained syntax includes relationship operators and existing-kind references, cardinality `{...}`, value format `[...]` and general named relations `Source ((RELATION_TYPE)) Target`. Keep cardinality counts, direct/inverse meanings and literal allowed values. Do not use `@(...)` as a property-value interpolation mechanism in this increment.

## Deferred proposal

Preserve this composed-value example for future design:

```text
atom.id: (@(Project.name.prefix)-@(content role.first letter)-number[int, unique(its current kind)]){1}
```

The proposal would group a composed allowed value in parentheses and apply its count to the whole group. It would need property-value binding, value construction, component formats, named-selection uniqueness and a complete expression grammar. Those mechanisms, function-style forms such as `unique(...)` and formula-based count calculations remain deferred. No executor, parser or automatic migration is requested.

Earlier A1265 and A1281 preserve the design discussion; this later decision defers its adoption. The independent content-getter proposal A1237 remains separate and deferred too.

## State

The main Model proposal and affected R/M/E/D syntax Drafts omit operative formulas and interpolation/grouping requirements. Existing ID rules remain in force; no new ID-generation model or Subject rename is introduced. Current methodology and runtime are unchanged.
