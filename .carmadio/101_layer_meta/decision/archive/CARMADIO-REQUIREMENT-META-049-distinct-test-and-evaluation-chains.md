---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-049
scope_path: layer:meta
subject_scopes:
  - assurance
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-REQUIREMENT-META-002
      - CARMADIO-REQUIREMENT-META-007
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-028
      - CARMADIO-REQUIREMENT-META-047
      - CARMADIO-REQUIREMENT-META-048
---

# Requirement — Keep QA Cases mechanism-neutral and assurance chains distinct

A QA Case is one mechanism-neutral Assurance atom defining what claim is
checked, the applicable conditions, the acceptance criteria, and the
disposition rule. It does not prescribe whether the check is realized by an
automated test, model-judged evaluation, statistical assessment, rubric,
manual review, or another implementation mechanism.

One QA Case may be realized by multiple distinct assurance implementations.
One implementation may realize multiple QA Cases only when its result remains
attributable to every covered Case. Coverage is therefore many-to-many but
never implicit.

Deterministic Test implementations and qualitative, probabilistic,
statistical, rubric-based, or model-judged Evaluation implementations retain
distinct chains. Each chain keeps its executable implementation, configuration
or rubric, factual Observation, evidence, and Verification judgment
distinguishable. A shared runner, prompt, judge, report, or gate does not merge
their meanings, observations, or coverage.

Test and Evaluation describe implementation mechanisms, not Assurance
subtypes. The QA Case remains the Assurance authority; executable mechanisms
are Implementation, and their results are Observation.

## Rationale

Mechanism-neutral Cases prevent the same assurance obligation from being
duplicated merely because it has several realizations. Preserving distinct
implementation and observation chains still prevents deterministic correctness
from being collapsed into qualitative judgment.
