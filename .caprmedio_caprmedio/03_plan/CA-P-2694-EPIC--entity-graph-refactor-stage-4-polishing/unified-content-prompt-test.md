# One prompt for complete Atom content

The writer produces the whole Markdown content, including Summary. Its default is one generation pass with an internal check. If an external review finds an issue, the same writer can accept the source, draft and findings as input. No separate Summary or fix prompt is needed.

## Final test

- Twelve source Atom bodies were supplied with their original Summaries removed.
- Generation used three fresh worker contexts, four cases each. Each worker used only the source, Content Role and the unified writing prompt.
- There was no external review–fix round during generation. Independent reviewers checked the completed results afterward.
- Body fidelity: 12/12 passed. The bodies remained identical to their sources apart from outer whitespace.
- Joint content/Summary style: 12/12 passed. The Summary was read with the Claim and its scope, not treated as a second operative Claim.
- The twelve validation cases were disjoint from the prompt’s teaching examples. The information-display case B03 became a teaching example and was excluded from blind validation.
- All 38 tracked source Atoms and all 38 older corpus files retained their hashes. No generated content was applied.

## Prompt development

| Candidate | Cases | Body fidelity | Joint content/Summary review |
| --- | ---: | ---: | ---: |
| v3 | 12 | 12 passed | 10 passed; Step context and Evaluation title needed work |
| v4 | 12 | 12 passed | 12 passed |

The final change kept the context that distinguishes a Step and moved an Evaluation’s checklist out of its title. Earlier heading-only pilot results are retained in the evidence bundle; they are not directly comparable because they treated some omitted body qualifiers as standalone Summary defects.

## Generated Summaries

| Atom | Summary |
| --- | --- |
| CA-R-2446 | Show gateway health, recent Tool and Workflow observations, and safe errors |
| CA-O-238 | Check code candidates against the complete applicable Method-policy set and current Evaluation and diagnosis evidence |
| CA-O-239 | Review code candidate evidence and applicable Method policy during shared implementation of Evaluations before required behavior |
| CA-E-667 | Check Project-wide foundation and Core commitments for valid ownership, support, and classification |
| CA-R-2449 | MCP owns provider-neutral discovery, schema, and dispatch for Tools, Prompts, and Workflows |
| CA-R-2450 | The Project has exactly five ordered Layers |
| CA-R-705 | The CAPRMEDIO Framework includes all Project outputs delivered to root Implementation Folders; downstream Layers and direct Features have distinct Project roles |
| CA-R-2430 | PROGRAMMATIC owns all and only deterministic behavior of FRAMEWORK_ENGINE |
| CA-R-2452 | Create and evolve CAPRMEDIO so any Operator can create, deliver, run and maintain any feasible Project with AI Agents |
| CA-M-005 | Admit or retain only mechanisms needed to preserve required outcomes or material governed distinctions |
| CA-M-006 | Maintain coherence across Project governance and Implementation |
| CA-D-657 | Minimal, governed YAML frontmatter for Markdown Atom Carriers |

## Use and limits

[Writer](atom-content.prompt.md) · [Optional reviewer](atom-content.eval.prompt.md) · [Usage](atom-content-prompts.md) · [Results table](unified-content-prompt-results.tsv) · [Frozen evidence](golden-writing-test/unified-content/).

This is a small development corpus used to refine the prompt. It tests preserving supplied content and generating a Summary. It does not prove general reliability on unknown specifications, incomplete notes or every model. The internal check is an instruction, not an independent quality guarantee.
