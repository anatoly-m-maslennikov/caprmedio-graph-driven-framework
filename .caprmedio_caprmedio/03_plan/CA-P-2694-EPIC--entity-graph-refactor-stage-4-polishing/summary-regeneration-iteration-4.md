# Summary regeneration — iteration 4

After feedback-guided repair, 38 of 38 candidate Summaries pass the review. The original 30 accepted titles are unchanged. The eight rejected candidates were revised; no source Atom or source Summary was changed.

## What happened

The full blind rerun used the same Terra worker role, source content and writing guide as run 3. Only the generation instruction changed. It scored 23/38: four old failures were fixed, four remained and eleven accepted cases regressed. That instruction was not adopted as an improvement.

Repairs therefore started from the better run-3 set. Each pass changed only rejected drafts, using the source content and reviewer comments. Review comments supplied problems, not suggested answers. For the last four cases, five accepted examples from other Atoms showed the desired level of detail. Those example keys were disjoint from the target keys. Original target Summaries stayed hidden.

| Stage | Drafts revised | Accepted in the assembled set |
| --- | ---: | ---: |
| Run 3 baseline | 38 | 30 |
| Full blind rerun | 38 | 23 |
| Feedback repair: eight drafts | 8 | 33 |
| Precision repair: five drafts | 5 | 34 |
| Corpus examples: four drafts | 4 | 36 |
| Final scope correction: two drafts | 2 | 38 |

## The eight previously flagged cases

| Atom | Repaired candidate | Result |
| --- | --- | --- |
| CA-M-448 | Keep all unexposed preserved information retrievable; show only the justified task-sufficient set | Pass |
| CA-R-2446 | Provide bounded, read-only MCP /health diagnostics with recent Tool and Workflow observations | Pass |
| CA-O-238 | Review code candidates, evidence and all bound applicable Method policy without editing | Pass |
| CA-O-239 | Review code in the shared implementation context without editing | Pass |
| CA-E-667 | Project-wide foundation and Core set Evaluation | Pass |
| CA-R-2449 | MCP provider-neutral discovery, schema, and dispatch | Pass |
| CA-R-2450 | The Project has exactly five Layers in a fixed Local Order. | Pass |
| CA-R-705 | CAPRMEDIO Framework, Layer, and Feature Composition | Pass |

## Limits

This is a reviewed repair result on one known corpus, not 38/38 success from a single generation call. It shows that keeping accepted drafts fixed and repairing specific failures works better here than rewriting everything. Several titles remain longer than the older corpus. Source Summaries were not renamed automatically.

[All 38 candidates](summary-regeneration-results-iteration-4.tsv) · [Frozen inputs, outputs and reviews](golden-writing-test/iteration-4/) · [Earlier runs](summary-regeneration-review.md).
