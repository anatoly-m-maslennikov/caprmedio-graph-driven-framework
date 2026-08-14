---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-093
scope_path: layer:meta
subject_scope: assurance
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-049
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-086
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-091
      - CAPRMADIO-REQUIREMENT-META-092
---

# Requirement — Keep Assurance Atoms mechanism-neutral and chains distinct

A mechanism-neutral Assurance Atom defines what claim is checked, the applicable conditions, the acceptance criteria, and the disposition rule. It does not prescribe whether the check is realized by an automated test, model-judged evaluation, statistical assessment, rubric, manual review, or another implementation mechanism.

One Assurance Atom may be realized by multiple distinct assurance implementations. One implementation may realize multiple Assurance Atoms only when its result remains attributable to every covered claim. Coverage is many-to-many but never implicit.

Deterministic Test implementations and qualitative, probabilistic, statistical, rubric-based, or model-judged Evaluation implementations retain distinct chains. Each chain keeps its executable Implementation, configuration or rubric, factual Ops result, Evidence, and Verification judgment distinguishable. A shared runner, prompt, judge, report, or gate does not merge their meanings, results, or coverage.

Test and Evaluation describe implementation mechanisms, not META-defined Assurance subtypes. The Assurance Atom remains the authority; executable mechanisms are Implementation, and their enacted results are Ops.

## Primary claim

Assurance Atoms remain mechanism-neutral authority, while Test and Evaluation implementations and their factual Ops results remain distinct, attributable chains.
