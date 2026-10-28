---
atom_id: CA-R-1889@11
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Analysis/Type: FPF Analysis Report'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Analysis'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Analysis/Type: Analysis Report'
version: 11
updated_at: 2026-10-27 06:04:45 +0400
relations:
  depends_on:
  - CA-R-1727
  - CA-R-1875
  - CA-D-479
tier: 2
type: Definition
---
# Summary

Define FPF Analysis Report

## Scope

the registered FPF Analysis Report Type under Content Role Analysis.

## Claim

an FPF Analysis Report **means** a specialized Analysis Report whose bounded inquiry **or** interpretation product records an FPF analytical command, composition, **or** directly related analytical follow-up, retaining its findings **and** stated evidence limits as reporting content rather than adopting them as normative authority.

## Details

The common Analysis body Properties remain Question, Scope, Approach, Results and TLDR under CA-D-479. The Analysis lifecycle and applicable Status model remain governed by CA-R-1727 and CA-R-1875; this Type does not introduce another Status domain or transition rule. A Done report can retain unresolved questions and rejected candidates. Done does not mean that its proposals were adopted, its issues were closed, or a tested implementation succeeded.

Historical statements remain bound to their original report context. Missing invocation, source revision, author, or execution evidence remains missing; the conversion must not invent it.
