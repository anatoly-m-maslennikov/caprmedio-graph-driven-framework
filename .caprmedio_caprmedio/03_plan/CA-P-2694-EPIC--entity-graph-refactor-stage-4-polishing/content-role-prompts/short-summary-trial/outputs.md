# Complete short-Summary trial outputs

These are unedited generated outputs from the final sample. See [trial results and limits](README.md).

## C1

````markdown
## Summary

Generated Step content violates the Workflow boundary

## Concern

The generated Step content names its previous and next Steps. Step order belongs to the Workflow, so this content violates the boundary. No cause or remedy has been established.
````

## C2

````markdown
## Summary

Method Summary may omit the new mechanism condition

## Concern

A generated Method Summary may omit the condition that a new mechanism is allowed only when existing mechanisms cannot preserve a required outcome. That omission may make the Method appear to permit unnecessary mechanisms. This is a possible error, not an observed occurrence.
````

## P1

````markdown
## Summary

Create role-specific content-writing prompts

## Objective

Create standalone one-shot content-writing prompts for C, P, R, M, E, D and O. Summary belongs to content. Review the role definitions, write the prompts, and try examples for every included role. Analysis reports are excluded from a fixed template. No work has been completed yet.

## Details

### Definition of Done

Not Done if the role definitions have not been reviewed, a standalone one-shot content-writing prompt or tried example is missing for C, P, R, M, E, D or O, Summary does not belong to content, or analysis reports have a fixed template.
````

## P2

````markdown
## Summary

Update Step Summaries

## Objective

Update two Step Summaries so each states its own purpose. Remove previous/next-Step wording from those two Step bodies. Keep their calls, parameters and results unchanged. The work is planned; no deadline or assignee has been chosen.

## Details

### Definition of Done

Not Done if either Step Summary does not state its own purpose, either Step body retains previous/next-Step wording, or their calls, parameters or results have changed.
````

## R1

````markdown
## Summary

PROGRAMMATIC owns all and only deterministic FRAMEWORK_ENGINE behavior

## Claim

PROGRAMMATIC owns all and only deterministic behavior of FRAMEWORK_ENGINE.
````

## R2

````markdown
## Summary

Atom Version Number has exactly one integer value at least 1

## Claim

Atom Version Number has exactly one value. It is an integer at least 1. Boolean values are not integers for this property.
````

## M1

````markdown
## Summary

DRY

## Claim scope

Operating the Project

## Claim

Apply DRY (Don’t repeat yourself).
````

## M2

````markdown
## Summary

Add new mechanisms only when needed

## Claim

Add a new mechanism only when existing mechanisms cannot preserve the required outcome or a material distinction. Convenience alone is insufficient.
````

## E1

````markdown
## Summary

Check Atom Version Number validity

## Claim

Pass only when exactly one non-Boolean integer Version Number at least 1 is present. Missing, multiple, Boolean, fractional and below-1 values fail.
````

## E2

````markdown
## Summary

Check leaf Step definition boundaries

## Claim

Check a leaf Step definition for its call, parameters, required inputs and returned results. Flag previous/next-Step claims and assignments of which sibling supplies an input, because the Workflow owns that information. Return findings only.
````

## D1

````markdown
## Summary

`status` key represents Atom.Status in YAML frontmatter

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

Review Code in shared implementation context

## Operation

This Review Step calls the reusable Review Code Action in shared implementation context. It requires `review_phase`, whose allowed values are `preliminary` and `final`. It returns review findings.
````

## O2

````markdown
## Summary

Update Atom

## Operation

The Update Atom Workflow calls these Workflows in order:

1. Create Draft Workflow
2. Archive Current Atom Workflow
3. Promote Draft Workflow

Stop if a call fails.
````

## O3

````markdown
## Summary

Prepare fetched source content

## Operation

The Prepare Step contains these Substeps in order:

1. Select Sources calls the Select Sources Action with the supplied selection parameters.
2. Fetch Sources calls the Fetch Sources Action with the supplied selection parameters.

The Prepare Step has no Action or Workflow call of its own. It returns the fetched source content.
````
