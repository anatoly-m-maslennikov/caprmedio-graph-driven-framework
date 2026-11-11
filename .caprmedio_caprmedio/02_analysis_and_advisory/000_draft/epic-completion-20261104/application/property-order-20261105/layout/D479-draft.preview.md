---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/File
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Content.Summary
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
  - CAPRMEDIO_MODEL <+ Atom.Content.Details
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ Atom.Content.Claim
  - CAPRMEDIO_MODEL <+ Atom.Content.Claim.Formal Claim
  - CAPRMEDIO_MODEL <+ Atom.Content.Claim.Prose Claim
  - CAPRMEDIO_MODEL <+ Workflow.Content.Claim.Mermaid Scheme
  - CAPRMEDIO_MODEL <+ Step.Content.Claim.Mermaid Scheme
version: 31
updated_at: 2026-11-05 21:06:18 +0400
relations: {}
atom_id: CA-D-479@31-draft
status: Draft
tier: 3
role: Delivery
form: Policy
carrier_destination:
  file:
    name: CA-D-479@31-draft-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/draft
container:
  scope_unit: CA-SU-11
---
## Summary

Use stable headings for Atom body Properties

## Claim

### Prose Claim

Applicability: Structured Main Content of Markdown Atom carriers.

Serialize Content headings in the declared sibling Property order, omitting absent optional Properties. Place other admitted sibling Properties after the ordered Properties, with no required order among them. For a Step, place `### Mermaid Scheme` first within Claim when present, before Prose Claim and Formal Claim.

For ordinary RMED, Claim structure and value constraints follow [CA-R-2500](../../04_requirement/CA-R-2500-CORE_META_MODEL-DECLARATION--declare-atom-content-claim.md), [CA-R-2721](../../04_requirement/CA-R-2721-CORE_META_MODEL-DECLARATION--declare-atom-content-claim-formal-claim.md), and [CA-R-2722](../../04_requirement/CA-R-2722-CORE_META_MODEL-DECLARATION--declare-atom-content-claim-prose-claim.md).

Map declared headings to their Property paths with a code-fence-aware outline. Only headings admitted as children by an applicable declaration are Properties. Other headings within a Markdown value, including unknown `##` headings within Prose Claim, remain part of that value and do not terminate it. For declared `Workflow.Content.Claim.Mermaid Scheme` and `Step.Content.Claim.Mermaid Scheme`, the Property value ends at the matching closing fence; subsequent role-specific Claim text is direct parent Claim content. Every other recognized Property section ends at the next recognized sibling or ancestor heading, or at the end of Main Content. Heading-like text in a fence is content. Direct value counts and dependent Property counts are independent. Retrieving a Property subtree includes its selected heading and its descendants.

Normalize recognized Property heading names to lowercase, replace spaces with underscores, and strip characters other than letters, numbers, underscore and hyphen. Reject an empty normalized key or duplicate normalized key under one parent. A flattened lookup is admissible only when unambiguous; canonical paths retain their parent chain.

Legacy layouts remain readable during migration. The existing C/A/P/O primary-content headings and their own Role-specific content rules remain applicable. A Draft may be incomplete but must satisfy the applicable complete contract before promotion.

