# Role-writer trial outputs

These are the unedited generated outputs from the final sampled pass for each role. Each case used the selected standalone prompt and its source facts; no external review findings were supplied to that generation. See [review results](test-results.md).

## C1

Source: The generated Step content names its previous and next Steps. Step order belongs to the Workflow, so this content violates the boundary. No cause or remedy has been established.

Request: State the observed bug. Do not add a fix plan.

````markdown
## Summary

Generated Step content violates the Workflow ordering boundary

## Concern

Generated Step content names its previous and next Steps. Step order belongs to the Workflow, so this content violates that boundary. No cause or remedy has been established.
````

## C2

Source: A generated Method Summary may omit the condition that a new mechanism is allowed only when existing mechanisms cannot preserve a required outcome. That omission may make the Method appear to permit unnecessary mechanisms. This is a possible error, not an observed occurrence.

Request: Write the Risk without claiming it occurred.

````markdown
## Summary

A Method Summary may appear to permit unnecessary mechanisms

## Concern

A generated Method Summary may omit the condition that a new mechanism is allowed only when existing mechanisms cannot preserve a required outcome. That omission may make the Method appear to permit unnecessary mechanisms. This is a possible error, not an observed occurrence.
````

## P1

Source: Create standalone one-shot content-writing prompts for C, P, R, M, E, D and O. Summary belongs to content. Analysis reports are excluded from a fixed template. Review the role definitions, write the prompts, and try examples for every included role. No work has been completed yet.

Request: Write the Plan and derive an observable Definition of Done.

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

Source: Update two Step Summaries so each states its own purpose. Remove previous/next-Step wording from those two Step bodies. Keep their calls, parameters and results unchanged. The work is planned; no deadline or assignee has been chosen.

Request: Keep one bounded objective and Definition of Done; do not add unrelated migrations.

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

Source: PROGRAMMATIC owns all and only deterministic behavior of FRAMEWORK_ENGINE.

Request: Write the content without adding delivery or implementation mechanisms.

````markdown
## Summary

PROGRAMMATIC owns all and only deterministic behavior of FRAMEWORK_ENGINE.

## Claim

PROGRAMMATIC owns all and only deterministic behavior of FRAMEWORK_ENGINE.
````

## R2

Source: Atom Version Number has exactly one value. It is an integer at least 1. Boolean values are not integers for this property.

Request: Write this definition in prose. No formal expression has been supplied.

````markdown
## Summary

Define the Atom Version Number property

## Claim

Atom Version Number has exactly one value. Its value is an integer at least 1. A Boolean value is not an integer for this property.
````

## M1

Source: Summary: DRY — Don’t repeat yourself. Scope: Operating the Project. Claim: Apply DRY (Don’t repeat yourself).

Request: Keep the familiar Summary and direct instruction; do not expand DRY into new project rules.

````markdown
## Summary

DRY — Don’t repeat yourself

## Claim scope

Operating the Project

## Claim

Apply DRY (Don’t repeat yourself).
````

## M2

Source: Add a new mechanism only when existing mechanisms cannot preserve the required outcome or a material distinction. Convenience alone is insufficient.

Request: Write a direct Method; keep the necessity condition.

````markdown
## Summary

Add a new mechanism only when existing mechanisms cannot preserve the required outcome or a material distinction

## Claim

Add a new mechanism only when existing mechanisms cannot preserve the required outcome or a material distinction; convenience alone is insufficient.
````

## E1

Source: Check Atom Version Number. Pass only when exactly one non-Boolean integer at least 1 is present. Missing, multiple, Boolean, fractional and below-1 values fail. This evaluation has not run.

Request: Write the check definition and invalid cases; do not report observed results.

````markdown
## Summary

Check Atom Version Number validity

## Claim

Pass only when exactly one non-Boolean integer Version Number at least 1 is present. Missing, multiple, Boolean, fractional, and below-1 values fail.
````

## E2

Source: Check a leaf Step definition for its call, parameters, required inputs and returned results. Flag previous/next-Step claims and assignments of which sibling supplies an input, because the Workflow owns that information. Return findings only. No source artifact has yet been checked.

Request: Write the evaluation criteria without adding a repair procedure or score.

````markdown
## Summary

Evaluate leaf Step definition boundaries

## Claim

Check each leaf Step definition for its call, parameters, required inputs and returned results. Flag previous/next-Step claims and assignments of which sibling supplies an input, because the Workflow owns that information. Return findings only.
````

## D1

Source: Atom.Status is represented by the status key in the YAML frontmatter of its Markdown carrier. Do not duplicate that value in Markdown content.

Request: Write the representation rule without inventing a new Carrier entity or other fields.

````markdown
## Summary

Represent Atom.Status with the `status` key in Markdown YAML frontmatter

## Claim

Atom.Status is represented by the `status` key in the YAML frontmatter of its Markdown carrier. Do not duplicate that value in Markdown content.
````

## D2

Source: Summary: Minimal, governed YAML frontmatter for Markdown Atom Carriers. Keep frontmatter limited to governed machine-readable fields while preserving parsing, validation, extensibility and readability. No exact field set is given here.

Request: Keep the given Summary and scope. Do not supply an invented field schema.

````markdown
## Summary

Minimal, governed YAML frontmatter for Markdown Atom Carriers

## Claim

Keep frontmatter limited to governed machine-readable fields while preserving parsing, validation, extensibility and readability. No exact field set is given here.
````

## O1

Source: This Review Step calls the reusable Review Code Action in shared implementation context. It requires review_phase, whose allowed values are preliminary and final. It returns review findings. An old draft also says that it follows implementation and sends results to the next Step. Those sequencing statements belong in the Workflow and must be removed.

Request: Write this Step only. Preserve call, parameter constraint and result; do not copy Workflow sequencing into its Summary or body.

````markdown
## Summary

Review code in shared implementation context

## Operation

The Review Step calls the reusable Review Code Action in shared implementation context. Required input: `review_phase`, whose allowed values are `preliminary` and `final`. Result: review findings.
````

## O2

Source: The Update Atom Workflow calls Create Draft Workflow, Archive Current Atom Workflow, then Promote Draft Workflow, in that order. Stop if a call fails. No additional commit, validation, queue, retry or approval step is specified.

Request: Write the Workflow definition, preserving the sequence and failure condition. Do not execute it or add steps.

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

Source: The Prepare Step contains two Substeps in order: Select Sources, then Fetch Sources. Each Substep calls its correspondingly named Action with the supplied selection parameters. The Prepare Step has no Action or Workflow call of its own. It returns the fetched source content.

Request: Write the containing Step and its local Substep order. Do not invent enclosing Workflow order, parameters or calls.

````markdown
## Summary

Prepare selected source content

## Operation

The Prepare Step contains these Substeps in order:

1. The Select Sources Substep calls the Select Sources Action with the supplied selection parameters.
2. The Fetch Sources Substep calls the Fetch Sources Action with the supplied selection parameters.

Result: fetched source content.
````
