---
atom_id: CA-A-1243@1
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Formal Model
version: 1
updated_at: 2026-10-28 19:44:00 +0400
relations: {}
tier: 3
---
# Summary

Define a Type-specific Claim with an optional formal child

## Decision

One Claim means one complete primary contribution under the Atom's Content Role and Type. A Definition can contain formal structure and complementary prose in the same Atom. They do not become separate Claims merely because their representations differ. The universal complete-RMED contract remains content.claim{1}.

The Claim's own text is its prose. The optional formal child is content.claim.formal_claim{0..1}. At least prose or the formal expression must be substantive; both may be present and must agree. There is no additional content.claim.prose field. Semantics and Details remain optional outside the Claim and do not introduce operative constraints.

## Markdown and property path

````markdown
# Summary
(summary)

## Claim scope
(scope, when needed)

## Claim
(prose, when present)

### Formal claim
```text
(formal expression, when present)
```

## Semantics
(meaning, when useful)

## Details
(supporting details, when useful)
````

The Operator explicitly chose ### Formal claim → atom.content.claim.formal_claim because the path follows the real Markdown outline. Names normalize to lowercase with spaces replaced by underscores and characters other than letters, numbers, underscore and hyphen removed. Its parent is Claim, so the child is not atom.content.formal_claim.

## Safety and unresolved implementation

Lossy normalization can collapse distinct headings. Rejecting empty/duplicate keys within one parent and allowing flattened shortcuts only when unambiguous are proposed safeguards, not already implemented behavior. Skipped heading levels should follow the nearest actual parent rather than fabricate empty nodes. Current carriers, readers and code are not migrated by this packet.

## Supersession

This latest decision supersedes the earlier whole-Claim single-fence/either-prose-or-formal restrictions in A1241/A1242. It does not restore two Claim fields, two Atoms for representations, a Graph Rule instance branch, or a new property/text grouping layer. Type remains Definition for model definitions; Graph Syntax remains the notation branch. The related successor Drafts and CA-A-1239 are refined in place.
