---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Tier
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
version: 13
updated_at: 2026-10-29 14:16:32 +0400
relations: {}
atom_id: CA-R-2124@13
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 1
status: Archived
author: Anatoly Maslennikov
---
## Summary

Define Numeric Tier as an Atom Property

## Claim scope

Atom Claims within their governing authority context.

## Claim

the Atom Property Tier **means** exactly one integer graph-ordering level carried by one complete independently replaceable Atom Claim within its governing authority context. It is used for the approved governing-relation ordering and owner/range admission only; it does not classify semantic abstraction, importance, Claim Scope breadth, Content Role, Type, Source ownership, filename, structural depth, or a second global rank. No second stored Global Tier or Structural Level exists.

Tier has a general integer lower bound of -1. The owner- and purpose-specific ranges remain governed in prose: Project Goals use -1 with Operator ownership, ordinary Project-local Atoms use Tier >=0, and other ordinary Atoms use Tier >=1. The general lower bound does not waive those more specific conditions.

Tier may have an optional readable Label under the Tier Label Definition; the Label does not replace the integer or create a second ordering.

Tier admission does not impose a Content-Role or Type-to-Tier restriction. Relation endpoint and other content rules remain independently governed.

### Formal claim

```text
atom.tier[int]
```

## Details

A1297 keeps the format-only expression in the review packet and leaves numeric bounds and owner-specific rules in prose; A1294 retains the separate bound-annotation proposal. A1295 defers case-specific function machinery. 
