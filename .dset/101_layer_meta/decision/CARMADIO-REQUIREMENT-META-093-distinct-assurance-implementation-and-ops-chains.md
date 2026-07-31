---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-093
scope_path: layer:meta
subject_scopes:
  - assurance
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-REQUIREMENT-META-049
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-086
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-091
      - CARMADIO-REQUIREMENT-META-092
---

# Requirement — Keep QA Cases mechanism-neutral and assurance chains distinct

A QA Case is one mechanism-neutral Assurance atom defining what claim is checked, the applicable conditions, the acceptance criteria, and the disposition rule. It does not prescribe whether the check is realized by an automated test, model-judged evaluation, statistical assessment, rubric, manual review, or another implementation mechanism.

One QA Case may be realized by multiple distinct assurance implementations. One implementation may realize multiple QA Cases only when its result remains attributable to every covered Case. Coverage is many-to-many but never implicit.

Deterministic Test implementations and qualitative, probabilistic, statistical, rubric-based, or model-judged Evaluation implementations retain distinct chains. Each chain keeps its executable Implementation, configuration or rubric, factual Ops result, Evidence, and Verification judgment distinguishable. A shared runner, prompt, judge, report, or gate does not merge their meanings, results, or coverage.

Test and Evaluation describe implementation mechanisms, not Assurance subtypes. The QA Case remains the Assurance authority; executable mechanisms are Implementation, and their enacted results are Ops.

## Primary claim

QA Cases remain mechanism-neutral Assurance authority, while Test and Evaluation implementations and their factual Ops results remain distinct, attributable chains.

## Rationale

Mechanism-neutral Cases prevent one assurance obligation from being duplicated merely because it has several realizations. Distinct Implementation and Ops chains prevent deterministic correctness from being collapsed into qualitative judgment.
