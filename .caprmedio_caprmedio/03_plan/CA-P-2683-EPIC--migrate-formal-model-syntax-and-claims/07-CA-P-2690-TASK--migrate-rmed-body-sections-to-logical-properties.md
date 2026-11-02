---
atom_id: CA-P-2690
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Entity
version: 6
updated_at: 2026-10-29 11:24:13 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2683
tier: 4
---
## Summary

Migrate RMED body sections to logical properties

## Objective

Align the adopted and necessarily touched RMED bodies with the chosen sibling-heading and logical-property layout.

## Details

Stage 2 companion to P2688; finish necessary remaining cases before the final rebuild. Use ## Summary, optional ## Claim scope, required ## Claim, optional ## Semantics, optional ## Details, with R-only optional ### Formal claim under Claim.

Preserve meaning while moving it to the correct logical property. Required prose remains direct Claim content; formal expressions, Semantics and Details do not substitute for it. Each property's direct value count is independent; headings only supply nesting at their actual level, with fenced examples excluded from heading detection.

Use existing reviewed Drafts where possible. Do not start an unrelated whole-source prose rewrite or impose RMED headings on C/A/P/O. Preserve optional-section omission and conditional scope rules. Advanced expression proposals remain outside scope.

## Definition of Done

Adopted/touched in-scope bodies map to the chosen logical paths with no Summary.Claim nesting, no hidden operative meaning in supporting sections, and no prose accidentally included in a formal child. Unrelated content is preserved.

## Progress

Completed the sibling-heading and logical-property migration, including the 37 formerly held cases. The 17 malformed legacy carriers have eight canonical retentions and nine explicit retirements; missing direct Claims and six missing Governs were repaired. Empty optional sections were omitted. Final-source readback passes for every selected Current RMED carrier.
