---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-122
scope_path: layer:meta
subject_scope: authority
tier: principle
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-091
      - CAPRMADIO-REQUIREMENT-META-092
      - CAPRMADIO-REQUIREMENT-META-093
      - CAPRMADIO-REQUIREMENT-META-103
      - CAPRMADIO-REQUIREMENT-META-121
---

# Requirement — Require falsifiable claims and stop conditions

Every CAPRMADIO claim used to accept work, select a Method, rely on an
Implementation, pass Assurance, declare Delivery or release readiness, or draw
an Ops conclusion identifies what observable condition could show the claim to
be false, unsupported, stale, or outside its valid scope.

The governed use identifies its acceptance or reliance boundary, required
evidence, material uncertainty, and the condition that stops, degrades, blocks,
or reopens the use. A definition that is not an empirical claim instead
provides a sharp inclusion and exclusion test. If neither a falsification
condition nor a boundary test can be stated, the matter remains a Concern or
explicit assumption and cannot silently carry normative or assurance force.

Evidence capable only of confirming the preferred interpretation is
insufficient when a reasonable disconfirming check is available. A missing,
unknown, or contradictory required input fails closed at the affected use
rather than being converted into a positive result.

## Primary claim

Every reliance-bearing CAPRMADIO claim has a disconfirming condition and explicit
stop or reopen boundary, while definitions have an explicit inclusion and
exclusion test.

## Rationale

This adapts FPF Pragmatic Utility and evidence discipline into a general
CAPRMADIO rule for falsifiable, bounded, and honest reliance.
