---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-161
scope_path: layer:gov
subject_scopes:
  - carrier-format
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-181-simple-outside-necessarily-complex-inside
    - CAPRMADIO-REQUIREMENT-META-139-use-canonical-carrier-address-as-authority
    - CAPRMADIO-REQUIREMENT-META-149-keep-an-atom-summary-immutable
    - CAPRMADIO-REQUIREMENT-163-semantic-irreducibility
    - CAPRMADIO-REQUIREMENT-META-166-write-context-complete-minimal-atom-prose
    - CAPRMADIO-REQUIREMENT-GOV-116-job-based-carrier-policy
---

# Render filename summaries as readable H1 titles

Every Markdown Atom must begin its body with exactly one H1 that repeats only
the immutable filename summary in human-readable form. The H1 uses spaces
instead of filename hyphens and may apply normal capitalization and punctuation
without changing, narrowing, extending, or interpreting the summary's meaning.

The H1 must not repeat the Artifact Type, subtype, identity, scope, lifecycle
position, or other carrier-derived fact. It is a derived navigation label, not
an independent semantic claim or source of authority.
