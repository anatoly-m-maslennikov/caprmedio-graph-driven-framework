---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-151
scope_path: layer:gov
subject_scope: artifact-catalog
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-148
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-137
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-133
      - CAPRMADIO-REQUIREMENT-GOV-147
---

# Register the Implementation Record Projection

GOV registers `implementation_record` with prefix `IREC` as an internal
Implementation-role Projection Type. It presents the current realization,
coverage, source-to-target bindings, relevant provenance, and unresolved gaps
derived from its declared source frontier.

The Projection declares the exact normative Atom, native-target, provenance,
and any registered implementation-lineage frontier it represents. Regeneration
replaces its rendered content without converting it into an Atom or granting it
authority over the native project, normative specification, Ops evidence, or
Verification.

Its storage and retention policy is configured separately. A generated runtime
copy may be disposable; a committed current view may be reviewable history.
Neither storage choice changes the Projection's semantic role.

## Rationale

The predecessor incorrectly bundled Change Plan and Implementation Record under
one Implementation-role Projection rule. The split preserves the record while
routing Change Plan to the new Plan Atom family.
