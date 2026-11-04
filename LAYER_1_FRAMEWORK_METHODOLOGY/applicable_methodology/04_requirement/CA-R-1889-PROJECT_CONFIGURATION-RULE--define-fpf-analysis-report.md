---
atom_id: CA-R-1889
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := "Analysis & Advisory")/(.Header.Form := FPF Analysis Report)
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := "Analysis & Advisory")
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := "Analysis & Advisory")/(.Header.Form := Analysis Report)
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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1889-PROJECT_CONFIGURATION-RULE--define-fpf-analysis-report.md
  source_atom_id: CA-R-1889
  source_atom_revision: 20
  source_sha256: 772e86a9d053f3795dc9da11abeaeaa5880eb967e59b7d5f336e6ce75a764cb0
  original_relations_sha256: 3435f8757c90dd20c1ec967f027979b866b3148b4ae7ae12df23a154ee1990fd
---
## Summary

Define FPF Analysis Report

## Claim

### Prose Claim


the registered FPF Analysis Report Form under Role Analysis & Advisory.


an FPF Analysis Report **means** a specialized Analysis Report whose bounded inquiry **or** interpretation product records an FPF analytical command, composition, **or** directly related analytical follow-up, retaining its findings **and** stated evidence limits as reporting content rather than adopting them as normative authority.

## Details

The common Analysis & Advisory body Properties remain Question, Scope, Approach, Results and TLDR under CA-D-479. The Analysis & Advisory lifecycle and applicable Status model remain governed by CA-R-1727@30 and CA-R-1875; this Form does not introduce another Status domain or transition rule. A Done report can retain unresolved questions and rejected candidates. Done does not mean that its proposals were adopted, its issues were closed, or a tested implementation succeeded.

Historical statements remain bound to their original report context. Missing invocation, source revision, author, or execution evidence remains missing; the conversion must not invent it.

