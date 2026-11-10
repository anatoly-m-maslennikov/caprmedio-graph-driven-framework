---
atom_id: CA-E-792
ref_id: CA-E-792
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Direct Policy
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
    <+ Verification <+ Static Analysis
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring
    <+ Code Authoring
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture
    <+ Component Structure
tier: 2
relations:
  evaluation_for:
  - CA-M-498
status: Active
version: 2
updated_at: 2026-11-10 20:47:54 +0400
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
destination:
  file:
    name: CA-E-792-PROGRAMMATIC-GENERAL-DIRECT_POLICY--evaluate-source-size-cohesion-and-package-organization.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Evaluate source size, cohesion and package organization

## Claim scope

New or materially changed hand-authored PROGRAMMATIC source and its directly
owned tests and non-code assets. Do not implicitly migrate all legacy source,
vendor code, generated output or frozen fixtures into this Evaluation.

## Claim

### Prose Claim

Evaluate a changed source by resolving its applicable governing policies first,
then measuring the source and comparing the measurements with those policies'
declared rules. The Evaluation returns pass, fail or unresolved evidence; it
does not own independent thresholds, exceptions or interpretations. Unknown or
unavailable rules or measurements are unresolved and must not be silently
replaced by another policy or counting profile.

## Details

- Resolve the shared organization Method and the applicable language-specific source-size and measurement policies. Use each policy only within its declared source boundary. Python acceptance remains with its current source-size Evaluation authority; frontend limits remain with the frontend Method. Do not treat the shared organization Method as a universal numeric threshold source. Missing or conflicting authority is unresolved.
- Measure every applicable standalone function, method, async function,
  nested function and classmethod independently using the resolved measurement
  profile. Never count a whole class as one function or use class
  size to excuse a method. Measure module physical LOC using the resolved
  policy definition, including its treatment of comments and docstrings.
- Generate the isolated boundary matrix from the resolved applicable limits:
  soft-1, soft, soft+1, hard-1, hard and hard+1 for function/method cases and
  for module cases, with standalone, method, classmethod, async and nested
  forms plus comment/docstring variants. Include a class above the method
  limit whose individual methods remain within their limits. Exactly-boundary
  outcomes and hard-limit exception semantics must be those of the governing policy, not
  a new Evaluation interpretation.
- Compare measurements with the resolved applicable rules and return the exact
  result with source, unit, measured value, limit name and evidence. A missing
  rule or unavailable measurement is unresolved. Do not claim that an LOC
  result proves cohesion, responsibility or naming quality.
- Send cohesion, meaningful-helper, package/subfolder, descriptive-filename
  and asset-placement questions to human review when they are not mechanically
  provable. Report unresolved rather than inventing a numeric folder/file cap
  or a pass from line counts alone. Do not reward meaningless helpers,
  wrappers, indirection or line compression that bypass a Method rule.
- Apply the resolved Method's applicability to new or materially changed
  hand-authored source only. Do not infer a full legacy, vendor, generated or
  frozen-fixture migration. Preserve the existing complexity, Ruff and ratchet
  checks; this Evaluation only evaluates the Method's declared criteria.

These are Evaluation checks for Method policies, not a duplicate Method
policy. The result must identify the exact changed source, bound Method
carrier, rule name, measurement and evidence.
