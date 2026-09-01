---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - artifact-operations
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  method_for:
    - CA-R-1149
  derived_from:
    - CA-A-058
---
# Extract one Extension candidate from Project Adaptation

## Applicable when

Use this Method when an operator selects reusable Project Adaptation authority for extraction as one Extension candidate.

## Procedure

1. Seal the operator-selected adaptation Atoms and resolve their direct dependency closure across current active authority.
2. Separate reusable capability from project-specific settings, secrets, runtime state, and unrelated local authority.
3. Require every retained dependency to be included exactly or declared as an external compatibility requirement.
4. Assign the candidate its own stable identity and preserve exact source Atom revisions and provenance.
5. Emit the bounded candidate and an explicit list of excluded, unresolved, and external dependencies.

## Outcome

One independently identified Extension candidate contains the selected reusable capability and a complete attributable dependency boundary.

## Failure or stop

Stop on unresolved required dependencies, hidden project-specific state, stale source revisions, or a candidate boundary that cannot be made independent.
