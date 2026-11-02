# Role-writer trial

Seven standalone writers were tried on fifteen small cases: two for each of C, P, R, M, E and D, and three for O. Summary was generated with the body. A was excluded from the fixed-template set.

## Results

| Role | Accepted | Cases |
| --- | ---: | --- |
| C | 2/2 | Observed Bug; possible Risk |
| P | 2/2 | New prompt-writing Plan; bounded Step-content corrections |
| R | 2/2 | PROGRAMMATIC responsibility; Version Number definition |
| M | 2/2 | DRY; adding mechanisms only when needed |
| E | 2/2 | Version Number pass/fail check; findings-only Step check |
| D | 2/2 | Status YAML mapping; minimal governed frontmatter |
| O | 2/3 | Leaf Step; Workflow; containing Step |

The independent review accepted fourteen outputs. It flagged one clarity omission in O3: the output contains only ordered Substep calls, but does not repeat the supplied statement that the containing Step makes no Action or Workflow call of its own. The reviewer recommends adding that sentence. The raw output is preserved without a review-driven fix.

[Read every complete output with its source](examples.md)

After this earlier trial, terminology preservation and shorter Summary guidance were added. The [new fifteen-case trial](short-summary-trial/README.md) tests the updated writers; the results below remain the historical earlier sample.

## Method and limits

These were agent-based development trials, not blind evaluations. Each sampled output was generated once from the supplied facts and final role prompt, allowing the prompt's internal check. Independent review followed. Earlier development rounds found errors and led to prompt refinements; the final sample is not an untouched first attempt at prompt design.

The first round accepted eleven of fourteen cases. It found an overstated Risk Summary, an omitted Plan requirement and invented pass criteria for a findings-only Evaluation. Later checks also caught repeated evaluation text and incomplete completion criteria. The final prompts address these patterns, but O3 shows that an internal check does not guarantee complete wording in every result.

The sample is small and simple; several cases resemble the prompts' examples. It does not establish reliable results for arbitrary specifications, every Type or template, missing context, or broad rewriting of existing Atoms. A may still need a task-specific report brief and structure.

No source Atom, runtime code or tool was changed by this task. The ten consulted role-source files were unchanged at the final hash check. The Epic remains Active.

## Records

- [Inputs](tests/inputs.jsonl)
- [Raw outputs](tests/outputs.jsonl)
- [Independent result review](tests/independent-review.json)
- [Initial prompt review](tests/initial-prompt-review.json)
- [Focused prompt recheck](tests/prompt-recheck.json)
- [Trial scope and final prompt hashes](tests/trial.json)
