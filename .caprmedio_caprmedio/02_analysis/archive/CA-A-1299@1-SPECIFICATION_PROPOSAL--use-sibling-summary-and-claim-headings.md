---
atom_id: CA-A-1299@1
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Model::CAPRMEDIO::Continuant/Governing Objects/Atom.content
version: 1
updated_at: 2026-10-29 03:59:38 +0400
relations: {}
tier: 3
---
# Summary

Use sibling Summary and Claim headings

## Decision

Use ## Summary instead of # Summary in the RMED body layout. Summary and Claim are sibling properties, not Summary.Claim. The registered top-level sections use the same heading level; a Formal claim remains a child of Claim:

````markdown
## Summary
(summary)

## Claim scope
(scope, when required)

## Claim
(required prose)

### Formal claim
```text
(optional formal expression, R only)
```

## Semantics
(optional explanation)

## Details
(optional support)
````

Normal heading hierarchy now gives atom.content.summary and atom.content.claim as siblings, and atom.content.claim.formal_claim as a child. No special Summary/root extraction exception is needed. The count and substantive-content rules are unchanged.

## Application boundary

Update the 45 RMED Drafts in the plain review packet and their layout references. The Analysis proposal/report headings and all unchanged Current sources remain outside this RMED Draft edit. The advanced-condition Draft is excluded and retained separately. Existing old Scope heading names and other independent review findings are not silently repaired by this change.

## State

The scoped Draft headings, Model layout description and RMED generator template are aligned. This resolves the heading-level contradiction PR-03 from A1298 for this prepared packet. The review report remains a point-in-time record; no source promotion, parser or runtime change is claimed.
