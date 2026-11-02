# Summary regeneration from Atom content

The original Summary was hidden. Each generator received only anonymized Markdown content and the writing guide. Source IDs, filenames, old Summaries and expected answers were not supplied. The test covers the same twenty Atoms and eighteen other project Tier-0 Atoms. Generated titles were not applied to source Atoms.

The latest feedback-guided set has 38 accepted candidates and 0 flagged cases. The 30 accepted titles from run 3 stayed unchanged. This required repeated review and repairs; it is not a one-shot success rate. [Iteration 4](summary-regeneration-iteration-4.md) records the full rerun, regressions and repairs. Several titles remain longer than the older corpus; source Summaries were not renamed automatically.

## Runs

| Run | Model | Instruction | Accepted | Flagged |
| --- | --- | --- | ---: | ---: |
| 1 | Luna | General writing guide | 28 | 10 |
| 2 | Luna | Explicit short title | 15 | 23 |
| 3 | Terra | Preserve the main assertions while shortening | 30 | 8 |
| 4 | Terra | Revised general instruction, full rerun | 23 | 15 |
| Repair sequence | Terra and parent-model workers | Keep accepted drafts fixed; repair rejected drafts with feedback and other corpus examples | 38 | 0 |

The first run often returned abstracts. The second compressed away important meaning. Run 3 improved meaning preservation. Both the model and instruction changed then; that comparison cannot isolate their effects. Runs 2 and 3 use the same content. Run 1 precedes the two small source-fidelity corrections.

## Cases flagged in run 3 (before repair)

| Atom | Generated Summary | Review finding | Suggested correction |
| --- | --- | --- | --- |
| [CA-M-448](../../05_method/CA-M-448-CAPRMEDIO-SCOPE_CONTRACT-ENG_POLICY--show-what-is-needed-keep-the-rest.md) | Preserve all governed information; show only the complete, currently justified task-sufficient set and retain all unexposed information for retrieval. | “All governed information” broadens the source beyond information needed for governed use. | Show what is needed; keep the rest |
| [CA-R-2446](../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/04_requirement/CA-R-2446-PROGRAMMATIC-GOAL--expose-bounded-read-only-mcp-health-and-call-history.md) | MCP exposes a bounded, non-authoritative `/health` browser diagnostic view without changing machine readiness semantics or inferring successful Tool or Workflow execution. | The title leaves out recent call and Workflow observation history, a central part of the view. | Expose bounded, read-only MCP health and call history |
| [CA-O-238](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/003_PROJECT_CONFIGURATION/09_operations/CA-O-238-PROJECT_CONFIGURATION-ACTION--review-code-candidate-evidence-and-applicable-method-policy-without-editing.md) | Code Candidate Semantic Review is a read-only assessment of a candidate, its current evidence, and the complete bound applicable Method-policy set, retaining gaps and returning only status justified by that assessment. | Retelling the assessment inputs, gap handling and status conditions makes this an overloaded description of the operation. | Review code-candidate evidence and applicable Method policy without editing |
| [CA-O-239](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/003_PROJECT_CONFIGURATION/09_operations/CA-O-239-PROJECT_CONFIGURATION-STEP--review-code-in-shared-implementation-context.md) | Shared Implementation Review Step invokes exactly one read-only review Action in explicit Integrated context, with an explicit phase and complete source-bound inputs, then passes its actual result to the enclosing Workflow. | The title retells call count, phase, input bindings and result handoff rather than naming the Step. | Review code in shared implementation context |
| [CA-E-667](../../06_evaluation/CA-E-667-CAPRMEDIO-EVAL_POLICY--check-the-project-wide-foundation-and-core-set.md) | Project-wide foundation and Core set Evaluation fails for any listed ownership, breadth, support, duplication, or Atom-role/tier defect; otherwise it may pass the reviewed frontier without claiming undiscovered gaps are impossible. | The defect-category inventory and reviewed-frontier exception overload the title and obscure the main Evaluation. | Check the Project-wide foundation and Core set |
| [CA-R-2449](../../102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/04_requirement/CA-R-2449-PROGRAMMATIC-SCOPE_CONTRACT-GOAL--mcp-owns-provider-neutral-discovery-schema-and-dispatch.md) | MCP owns the provider-neutral Model Context Protocol discovery, schema, and dispatch interface, not Tool behavior, prompt content, Workflow coordination, Skill procedures, application behavior, or agent-host packaging. | Listing every excluded ownership area makes the title an unnecessary recitation of the Claim. | MCP owns provider-neutral discovery, schema and dispatch |
| [CA-R-2450](../../04_requirement/CA-R-2450-CAPRMEDIO-SCOPE_CONTRACT-RULE--the-project-has-five-layers-in-local-order.md) | The Project has exactly five ordered Layers: FRAMEWORK_METHODOLOGY, FRAMEWORK_ENGINE, OPERATOR_DOCUMENTATION, CORE_EXTENSIONS, and RELEASES, with Local Orders 1 through 5. | Naming all five Layers and orders retells the full ordered list, which belongs in the Claim. | The Project has five Layers in Local Order |
| [CA-R-705](../../04_requirement/CA-R-705-CAPRMEDIO-SCOPE_CONTRACT-RULE--define-framework-composition.md) | The CAPRMEDIO Framework comprises all caprmedio Project outputs delivered to the repository root Implementation Folders. | The title narrows Framework composition to root-folder outputs and omits the separate Layer and Feature composition. | Define Framework composition |

## Reuse

[All 38 results](summary-regeneration-results.tsv) · [Frozen test inputs, outputs, prompts and reviews](golden-writing-test/) · [Source corpus ledger](golden-writing-corpus.tsv).

Keep the existing Summary when it is already clear. Regenerated alternatives need review for lost restrictions, changes from checking to doing, vague generalization and excessive detail. No fixed word count or exact-string score was imposed. This experiment was not added to the runtime test suite.
