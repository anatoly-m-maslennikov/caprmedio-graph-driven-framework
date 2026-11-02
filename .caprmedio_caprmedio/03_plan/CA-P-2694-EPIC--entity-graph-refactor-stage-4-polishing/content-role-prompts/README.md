# One-shot Atom content writers

Choose the Content Role and use its prompt with the supplied facts or draft, relevant context, Type/template and requested changes. Each prompt is standalone: the shared style rules are already included.

| Role | Prompt | Main purpose |
| --- | --- | --- |
| C | [Concern](C-concern.prompt.md) | State the concern and its uncertainty or consequence. |
| P | [Plan](P-plan.prompt.md) | State bounded intended work and its completion condition. |
| R | [Requirement](R-requirement.prompt.md) | State a required result, behavior or model definition. |
| M | [Method](M-method.prompt.md) | Explain the approach or means. |
| E | [Evaluation](E-evaluation.prompt.md) | Define a check or acceptance criterion. |
| D | [Delivery](D-delivery.prompt.md) | Define a representation, encoding or storage rule. |
| O | [Operations](O-operations.prompt.md) | Define an Action, Workflow, Step or Substep. |

When creating or rewriting from Operator input, keep the Operator’s wording as close as possible. Correct grammar and organize fragments into coherent statements with the simplest syntax possible. Keep clear wording; do not introduce synonyms or formal paraphrases.

When rewriting, preserve source terms, names and key concepts. Do not replace DRY, MECE or other terminology with synonyms; simplify the surrounding prose.

By default, one Atom carries one coherent Claim with optional Semantics and Details. Summary is a faithful short version of the whole Atom; for RMED it is normally a statement. Form templates may explicitly override these defaults. R / Form: Declaration may contain multiple statements in prose, GFEL formal expressions or both, and may use a topic Summary such as “Define Run”.

Summary is part of content. One invocation returns the complete Markdown after an internal check and correction. There is no separate Summary prompt or mandatory review–fix cycle. The body follows its role; Summary follows the default or an explicit Form override.

For O, the Workflow owns cross-Step order, routing and data wiring. A leaf Step owns its call, parameters, required inputs and returned results. A containing Step orders its own Substeps. A reusable Action does not know its caller Workflows.

## A is an exception

Analysis reports vary in purpose, size and structure. Choose the report brief and Type-specific structure for the task. These seven writers do not impose a short universal A template.

## Optional review

Use [Review Atom content](../atom-content.eval.prompt.md) with the source, output and selected role prompt. If it finds a real issue, use the same role writer again with those findings. No separate fix prompt is needed.

These prompts write content only. Applying it to an Atom, allocating an ID, creating history or changing metadata is separate work.

## Basis and trial

The profiles use the consulted Core role definitions CA-R-1336, CA-R-1338–CA-R-1342 and CA-R-1530; Concern Types from CA-R-1231; the supplied M/Term Definition profile from CA-R-2453; Plan layout from CA-D-470; and writing guidance from CA-M-442–CA-M-444. The Operator’s latest instructions govern Summary headings and Workflow/Step boundaries.

The earlier trials below predate the current Summary defaults and Form overrides and do not validate the revised prompts.

[Earlier trial: shorter Summaries](short-summary-trial/README.md) · [Earlier trial](test-results.md)
