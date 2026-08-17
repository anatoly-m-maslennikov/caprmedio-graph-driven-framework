---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-058
scope_path: layer:meta
subject_scope: development-flow
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-021
    - CAPRMADIO-REQUIREMENT-META-036
    - CAPRMADIO-REQUIREMENT-META-037
  child_of:
    - CAPRMADIO-REQUIREMENT-META-135-preserve-content-role-boundaries-through-caprmadio-loop
---
# Requirement — Route uncertain input through Exploration Mode

Exploration Mode permits brainstorming, discussion, research, analysis,
comparison, terminology work, and structural modeling without creating or
changing governed artifacts.

CAPRMADIO enters Exploration Mode when the operator's input primarily:

- asks for information, explanation, comparison, critique, alternatives, or a
  recommendation; or
- introduces an idea, explores it, or asks for feedback on it.

An explicit operator request to create or change governed state takes
precedence over question-shaped wording. Otherwise, Exploration Mode ends only
when the operator explicitly accepts a conclusion or requests its promotion.
CAPRMADIO then emits only the minimum artifacts required to preserve the accepted
meaning. A Projection may refresh only after its declared source Atoms exist.

Whether a mode transition is announced is a downstream interaction-reporting
choice and does not change this routing.

## Primary claim

Question and idea input stays non-persistent in Exploration Mode until explicit
operator acceptance authorizes the minimum durable artifacts.
