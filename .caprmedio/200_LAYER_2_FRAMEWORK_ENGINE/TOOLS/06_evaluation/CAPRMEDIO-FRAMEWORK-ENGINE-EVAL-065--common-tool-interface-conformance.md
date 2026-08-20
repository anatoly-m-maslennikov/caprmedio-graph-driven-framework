---
artifact_subtype: qa_case
subject_scopes:
  - evaluation
version: 3
updated_at: 2026-08-19 03:45:53
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-549--provide-a-tool-router-cli
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-602--use-a-common-tool-cli-interface
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-603--use-one-project-local-tool-runtime
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-604--register-extensible-tool-capability-classes
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-605--accept-common-atom-target-selectors
    - CAPRMEDIO-FRAMEWORK-ENGINE-METH-076--route-and-invoke-tools-through-the-common-cli
---
# Common Tool interface conformance

## Claim checked

Every registered Tool is discoverable and invocable through one common interface while capability-specific safety and targeting obligations remain enforced.

## Applicable conditions

1. Ask the router for representative Finder, Checker, source-editing Doer, and Projection-materializing Doer intents and require every applicable option plus sufficient machine-readable how-to after selection.
2. Validate identical capability, help, input-schema, result-envelope, diagnostics, and exit-status fields for every registered Tool.
3. Resolve targets independently from structural-unit, Type, and subtype filters and from explicit Atom filenames, and require the same stable target set before execution.
4. Snapshot all Atom bytes, run every Finder and Checker fixture, and require no Atom, relation, lifecycle, or authoritative carrier change.
5. Run every source-editing Doer fixture in dry-run mode, require complete planned effects and validation results with no mutation, then apply an approved plan and require the realized effect to match it.
6. Run representative Projection-materializing Doer fixtures first in dry-run mode and then in apply mode, and require writes only to declared governed Projections or non-authoritative runtime rendering outputs.
7. Inspect every process environment and dependency resolution path and require the one project-local environment under `.caprmedio_runtime` with no Tool-specific environment.

## Acceptance criteria

Every Tool conforms to the common contract, resolves identical targets, and satisfies its registered capability boundary without undeclared writes.

## Failure disposition

Reject Tool registration or execution, identify the first divergent interface or unauthorized effect, and record a Concern before Tool-surface readiness.
