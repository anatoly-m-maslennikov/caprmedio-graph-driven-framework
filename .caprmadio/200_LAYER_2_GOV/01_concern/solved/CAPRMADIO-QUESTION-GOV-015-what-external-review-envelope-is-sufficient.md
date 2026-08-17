---
artifact_type: concern
artifact_subtype: question
artifact_id: CAPRMADIO-QUESTION-GOV-015
scope_path: layer:gov
subject_scopes:
  - external-boundary
priority: medium
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-QUESTION-GOV-007
---

# Question — What external-review envelope is sufficient?

What minimum structured identity, provenance, scope, finding, and disposition
envelope should CAPRMADIO require when importing an external review, while allowing
the review's analysis body and native attachments to remain free-form?

The resolution should distinguish:

- the external review carrier from CAPRMADIO's internal Analysis and Ops
  artifacts;
- mandatory review provenance from optional reviewer-specific fields;
- machine-actionable findings from unrestricted narrative;
- imported evidence from project Verification; and
- a stable interoperability contract from provider-specific report schemas.

This successor removes the obsolete CAPRMADIO 0.3 deadline and asks only the still
open governance question.
