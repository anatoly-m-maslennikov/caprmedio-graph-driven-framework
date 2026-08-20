---
subject_scopes:
  - principles
tier: core
version: 1
updated_at: 2026-08-20 03:40:53
relations:
  child_of:
    - CA-D-003-PRINCIPLE-DELIVERY--use-the-graph-as-the-operating-model
    - CA-E-001-PRINCIPLE-EVALUATION--make-accepted-requirements-checkable
  evaluation_for:
    - CAPRMEDIO-REQU-026--define-the-project-principle-universe
---
# Principle-first alignment

## Claim checked

For every selected Structural level and given scope, the complete active Atom set is aligned with every active Project Principle.

## Check

Load the complete active Project Principle set first, resolve the Structural level and scope, collect the complete active Atom set, and evaluate every Atom against every Principle before applying lower-tier authority.

## Acceptance

Pass only when no Atom conflicts with a Project Principle and no lower-tier interpretation weakens or overrides one.

## Failure

Report every conflicting Atom and Principle pair; only the operator may resolve a conflict between Principles.
