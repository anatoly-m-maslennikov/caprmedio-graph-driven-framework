# Previous generated content

These are the baseline generated versions used in the shorter-Summary comparison. They are test outputs, not archived source Atoms. See the [comparison](README.md).

## C1

````markdown
## Summary

Generated Step content violates the Workflow ordering boundary

## Concern

Generated Step content names its previous and next Steps. Step order belongs to the Workflow, so this content violates that boundary. No cause or remedy has been established.
````

## C2

````markdown
## Summary

A Method Summary may appear to permit unnecessary mechanisms

## Concern

A generated Method Summary may omit the condition that a new mechanism is allowed only when existing mechanisms cannot preserve a required outcome. That omission may make the Method appear to permit unnecessary mechanisms. This is a possible error, not an observed occurrence.
````

## P1

````markdown
## Summary

Plan standalone content-writing prompts for included roles

## Objective

Prepare standalone one-shot content-writing prompts for C, P, R, M, E, D and O. Treat the Summary as content. Review the role definitions, write the prompts, and try examples for every included role. Analysis reports are excluded from a fixed template.

## Details

### Definition of Done

Not Done if the role definitions have not been reviewed, a standalone prompt or tried example is missing for any included role, Summary is not part of the content, or a fixed template is applied to analysis reports.
````

## P2

````markdown
## Summary

Plan independent Step Summary updates

## Objective

Update the two Step Summaries so each states its own purpose. Remove previous/next-Step wording from the two Step bodies while keeping their calls, parameters, and results unchanged.

## Details

### Definition of Done

Not Done if either Step Summary does not state its own purpose, either Step body retains previous/next-Step wording, or a call, parameter, or result has changed.
````

## R1

````markdown
## Summary

PROGRAMMATIC owns all and only deterministic behavior of FRAMEWORK_ENGINE.

## Claim

PROGRAMMATIC owns all and only deterministic behavior of FRAMEWORK_ENGINE.
````

## R2

````markdown
## Summary

Define the Atom Version Number property

## Claim

Atom Version Number has exactly one value. Its value is an integer at least 1. A Boolean value is not an integer for this property.
````

## M1

````markdown
## Summary

DRY — Don’t repeat yourself

## Claim scope

Operating the Project

## Claim

Apply DRY (Don’t repeat yourself).
````

## M2

````markdown
## Summary

Add a new mechanism only when existing mechanisms cannot preserve the required outcome or a material distinction

## Claim

Add a new mechanism only when existing mechanisms cannot preserve the required outcome or a material distinction; convenience alone is insufficient.
````

## E1

````markdown
## Summary

Check Atom Version Number validity

## Claim

Pass only when exactly one non-Boolean integer Version Number at least 1 is present. Missing, multiple, Boolean, fractional, and below-1 values fail.
````

## E2

````markdown
## Summary

Evaluate leaf Step definition boundaries

## Claim

Check each leaf Step definition for its call, parameters, required inputs and returned results. Flag previous/next-Step claims and assignments of which sibling supplies an input, because the Workflow owns that information. Return findings only.
````

## D1

````markdown
## Summary

Represent Atom.Status with the `status` key in Markdown YAML frontmatter

## Claim

Atom.Status is represented by the `status` key in the YAML frontmatter of its Markdown carrier. Do not duplicate that value in Markdown content.
````

## D2

````markdown
## Summary

Minimal, governed YAML frontmatter for Markdown Atom Carriers

## Claim

Keep frontmatter limited to governed machine-readable fields while preserving parsing, validation, extensibility and readability. No exact field set is given here.
````

## O1

````markdown
## Summary

Review code in shared implementation context

## Operation

The Review Step calls the reusable Review Code Action in shared implementation context. Required input: `review_phase`, whose allowed values are `preliminary` and `final`. Result: review findings.
````

## O2

````markdown
## Summary

Update Atom through draft, archive, and promotion

## Operation

1. Call Create Draft Workflow.
2. Call Archive Current Atom Workflow.
3. Call Promote Draft Workflow.

Stop the Workflow if any call fails.
````

## O3

````markdown
## Summary

Prepare selected source content

## Operation

The Prepare Step contains these Substeps in order:

1. The Select Sources Substep calls the Select Sources Action with the supplied selection parameters.
2. The Fetch Sources Substep calls the Fetch Sources Action with the supplied selection parameters.

Result: fetched source content.
````
