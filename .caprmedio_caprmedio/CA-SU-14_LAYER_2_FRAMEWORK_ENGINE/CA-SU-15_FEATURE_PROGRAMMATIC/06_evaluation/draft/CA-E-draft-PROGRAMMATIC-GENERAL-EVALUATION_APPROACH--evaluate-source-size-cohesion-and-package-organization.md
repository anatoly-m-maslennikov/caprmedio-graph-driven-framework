---
atom_id: CA-E-draft
content_role: Evaluation
type: Evaluation Approach
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
tier: 2
status: Draft
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-23 19:06:37 +0400"
subjects:
  governs: Subject/Engineering/Source Unit Responsibility
  depends_on:
    - Subject/Engineering/Source Check Adoption
relations:
  relates_to:
    - CA-E-539
    - CA-M-419
    - CA-M-411
---
# Summary

Evaluate source size, cohesion and package organization

## Scope

New or materially changed hand-authored PROGRAMMATIC source and its directly
owned tests and non-code assets. Do not implicitly migrate all legacy source,
vendor code, generated output or frozen fixtures into this Evaluation.

## Claim

Evaluate a changed source by resolving its applicable Method policy first,
then measuring the source and comparing the measurements with that Method's
declared rules. The Evaluation returns pass, fail or unresolved evidence; it
does not own independent thresholds, exceptions or interpretations. Unknown or
unavailable rules or measurements are unresolved and must not be silently
replaced by another policy or counting profile.

## Details

- Resolve the bound Method source
  `05_method/draft/CA-M-draft-PROGRAMMATIC-CORE-ENG_POLICY--organize-cohesive-modules-packages-and-assets.md`
  and obtain its current applicability, unit names, thresholds, exception
  semantics, asset rules and LOC measurement definitions. That Method draft
  is the rule authority for the checker; CA-E-539 is not the rule source.
- Measure every applicable standalone function, method, async function,
  nested function and classmethod independently using the resolved Method
  measurement profile. Never count a whole class as one function or use class
  size to excuse a method. Measure module physical LOC using the resolved
  Method definition, including its treatment of comments and docstrings.
- Generate the isolated boundary matrix from the resolved Method limits:
  soft-1, soft, soft+1, hard-1, hard and hard+1 for function/method cases and
  for module cases, with standalone, method, classmethod, async and nested
  forms plus comment/docstring variants. Include a class above the method
  limit whose individual methods remain within their limits. Exactly-boundary
  outcomes and hard-limit exception semantics must be those of the Method, not
  a new Evaluation interpretation.
- Compare measurements with the resolved Method rules and return the exact
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

## Adoption notes

This is a Draft with the numeric draft schema and no stable Atom identity. It
is not current authority and does not change CA-E-539. On coordinated
promotion, it can check the promoted Method's own thresholds and rules through
the normal identity, predecessor and consumer-rebinding process. Until then,
CA-E-539, existing complexity checks, Ruff configuration and ratchets remain
untouched and authoritative.

Companion Method: [cohesive source organization](../../05_method/draft/CA-M-draft-PROGRAMMATIC-CORE-ENG_POLICY--organize-cohesive-modules-packages-and-assets.md).
