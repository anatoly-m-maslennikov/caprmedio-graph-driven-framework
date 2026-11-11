---
atom_id: CA-R-1889
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := "Analysis & Advisory")/(.Form := FPF Analysis Report)
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := "Analysis & Advisory")
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := "Analysis & Advisory")/(.Form := Analysis Report)
version: 20
relations:
  depends_on:
  - CA-R-1727@30
  - CA-R-1875
  - CA-D-479
tier: 2
role: Requirement
form: Rule
updated_at: 2026-11-02 19:33:47 +0400
---
## Summary

Define FPF Analysis Report

## Claim scope

the registered FPF Analysis Report Form under Role Analysis & Advisory.

## Claim

an FPF Analysis Report **means** a specialized Analysis Report whose bounded inquiry **or** interpretation product records an FPF analytical command, composition, **or** directly related analytical follow-up, retaining its findings **and** stated evidence limits as reporting content rather than adopting them as normative authority.

## Details

The common Analysis & Advisory body Properties remain Question, Scope, Approach, Results and TLDR under CA-D-479. The Analysis & Advisory lifecycle and applicable Status model remain governed by CA-R-1727@30 and CA-R-1875; this Form does not introduce another Status domain or transition rule. A Done report can retain unresolved questions and rejected candidates. Done does not mean that its proposals were adopted, its issues were closed, or a tested implementation succeeded.

Historical statements remain bound to their original report context. Missing invocation, source revision, author, or execution evidence remains missing; the conversion must not invent it.

