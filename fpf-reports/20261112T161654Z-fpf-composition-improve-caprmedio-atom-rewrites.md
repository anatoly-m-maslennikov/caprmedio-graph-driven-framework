## Task, scope, and boundaries

The next design needs to find safe cuts in CAPRMEDIO Atoms and preserve what each Atom says and when it applies. The comparison uses `CA-M-1014@1-draft`, the two evaluations of the same 50 pinned RMEDO Atoms, and seven primary research and authoring sources. The user owns the choice of which design to test. This run produced research and test proposals.

The first comparison improved clearer, faithful rewrites from 24/50 to 33/50. The newer instruction reduced total word count by 0.20%. The second comparison's focus check retained all six previously identified cut candidates and produced 12,413 words from a 12,407-word source corpus. In that review, four focus-check rewrites lost confirmed meaning versus three for the current wording. These are results on the same sample under separate reviews. [First comparison](/private/tmp/caprmedio-ste-paired.pfaP04/results.json) · [Focus-check comparison](/private/tmp/caprmedio-ste-focus.LVMjrb/results.json)

Saved report: fpf-reports/20261112T161654Z-fpf-composition-improve-caprmedio-atom-rewrites.md

### Composition receipt

- Exact invocation: `let's do [$fpf](/Users/am/.codex/skills/fpf/SKILL.md) sota harvest + design improvement how we can improve it, i'm out if ideas, we hit the wall here`
- Selected profile: none. Requested sequence and executed prefix: 1. `$fpf sota harvest`, 2. `$fpf options explore`. Unexecuted suffix: none.
- Typed edge: PASS. Step 2 consumed the validated evidence map, including the source records, local failure cases, differences between methods, and transfer limits.
- State: `COMPLETE`. Context ledger: 3 read, 3 used, 0 deferred. Issues I-01–I-03 and fixes F-01–F-04 carried forward.

## Issues, weak points, and improvements

### Native result

#### The first experiment

**Test a cut list and local patches against the current whole-Atom rewrite on ten pinned Atoms.** For each proposed deletion, ask the editor to show the exact passage to cut and the exact passage that retains its full meaning, with the same applicability and section function. Apply only the proposed local edits in the candidate. A second reviewer checks both directions: what the source requires still appears in the candidate, and everything the candidate requires comes from the source. If scope or meaning remains uncertain, retain the source passage or send it for review.

Measure how many adjudicated safe cuts each arm finds and makes. Also count unsafe proposals, material changes that pass review, readability, and total effort. This makes the known misses a direct test. Total word count remains a separate measure because an explicit condition sometimes costs words.

#### Evidence map

The harvest admitted English-language primary research and official writing guidance with a concrete mechanism related to the observed failures. It included foundational work and checked recent work through 12 November 2026. The three families have distinct aims and evidence. The transfer below is a design inference, and performance on CAPRMEDIO remains unmeasured.

| Family and source record | What the evidence supports and how it transfers |
|---|---|
| **Finding overlap and restricting edits** · S-01 Carbonell and Goldstein, SIGIR 1998, criterion definition. S-02 Filippova et al., EMNLP 2015, abstract and §1. | One method uses similarity to find overlapping material in extractive summaries. The other studies sentence compression through deletion and evaluates readability and informativeness separately. Use similarity to nominate cuts and restrict the edits to exact source spans. Check whether the retained passage carries the same meaning before deleting. [Overlap criterion](https://www.cs.cmu.edu/afs/cs/Web/People/jgc/publication/MMR_DiversityBased_Reranking_SIGIR_1998.pdf) · [Sentence compression by deletion](https://aclanthology.org/D15-1042.pdf) |
| **Preserving conditional scope** · S-03 NASA Systems Engineering Handbook Rev. 2, Appendix C. S-04 Mavin et al., RE 2009 and author guide. S-05 Fischbach et al., 2023 journal study, author manuscript v2, abstract. | NASA separates requirements and rationale. EARS distinguishes preconditions, triggers, actors, and responses. CiRA studied extracting conditional relationships to derive acceptance tests. Borrow the separation of actor, modality, condition, exception, and action when restructuring a block. Keep CAPRMEDIO's own form and terminology. [NASA checklist](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/) · [EARS original record](https://research.manchester.ac.uk/en/publications/easy-approach-to-requirements-syntax-ears/) · [Author guide](https://alistairmavin.com/ears/) · [CiRA study](https://arxiv.org/abs/2202.00932) |
| **Checking what disappeared** · S-06 Song et al., ACL 2024, §§3.1–3.2. S-07 Dejl et al., Findings of ACL, July 2026, abstract. | FineSurE separates completeness, conciseness and faithfulness by comparing key facts and summary sentences. Dejl et al. compare checks based on atomic statements, questions, and direct model assessment. Their direct check performed well, with lower robustness, interpretability, and granularity. For Atom edits, use cited passage pairs to make missing obligations or changed applicability inspectable. A model check can triage uncertain cases. [FineSurE](https://aclanthology.org/2024.acl-long.51.pdf) · [Factual recall evaluation](https://aclanthology.org/2026.findings-acl.1744/) |

Source discovery covered those three families and excluded general advice and prompt-token compression. Summaries may select important content. An Atom rewrite must preserve required content, including exceptions and Details that carry their own function. The evidence gives candidate mechanisms and no common performance threshold. The trace below identifies the FPF edition and the bounded sections used.

#### Designs worth comparing

| Design | What changes | Trade-off |
|---|---|---|
| **C-0 · Current whole-Atom rewrite** | Keep `CA-M-1014@1-draft` as the comparison baseline. | Low workflow overhead. The benchmark shows readability gains and missed repeated passages. |
| **C-1 · Cut list and local patches** | Find exact spans to remove or merge. Cite the retained equivalent and its scope. Copy the remaining prose exactly. | Small review surface. Distributed or paraphrased repetition may remain. |
| **C-2 · Preserve scope before splitting** | Record each targeted block's actor, modality, conditions, exceptions, order, and governed actions. Use a shared lead-in or repeat the condition for all affected actions. | Addresses the observed scope failures. Word count can rise when applicability needs to be explicit. |
| **C-3 · Map obligations before a whole-Atom rewrite** | Inventory the source meaning by section. Link each obligation or qualification to its output span and each deletion to a retained counterpart. | Can address repetition across sections at higher annotation and review cost. A missed item in the inventory can hide an omission, so the reviewer also checks the source. |

C-1 targets the missed cuts, C-2 targets condition scope, and C-3 targets distributed repetition. All three are untested on these Atoms. Keep C-2 as a separate comparison for condition-heavy text. Test C-3 if local patches leave substantial cross-section redundancy.

#### Concrete checks

- **`CA-M-396`**. Propose removing the second verbatim scope under the retained invalid-input controls. Cite the first occurrence and keep the broader shared-public-boundary scope. Test the repeated runtime-only `ERROR` reminder while preserving the separate all-invalid-result rule.
- **`CA-D-667`**. Test deleting the sentence that restates the Unordered naming rule already shown in the table. Keep the adjacent absent-Label rule.
- **`CA-O-169`**. Keep state protection, clearing only replaceable Framework members, and copying under one installation lock. A safe example puts all three actions under the lead-in “Under one installation lock, perform all of the following.” Preserve the exact copy path and order in the full edit.
- **`CA-O-216`**. A recheck after the authorization window closes must remain impermissible. The benchmark split the safety checks and the recheck and detached the explicit window condition from the latter under both prompt variants.
- **`CA-E-628` and `CA-D-613`**. Preserve the duty to verify connector prohibitions and the explicit classification of URL-only finalization as mechanical, respectively. The actions themselves survived the benchmark rewrites that lost these meanings. [Scored omission evidence](/private/tmp/caprmedio-ste-focus.LVMjrb/results.json)

#### Paired pilot and stop conditions

Use `CA-M-396@17`, `CA-D-570@26`, `CA-D-667@4`, `CA-O-169@24`, `CA-O-216@12`, `CA-M-439@4`, `CA-D-613@19`, `CA-E-628@11`, `CA-M-116@31`, and `CA-R-1942@12`. The last is a comparison control. `CA-M-116` tests whether ambiguous scope is retained or referred for review. Before generation, adjudicate the six identified cuts as safe, unsafe, or unresolved. Include a deliberately unsafe near-duplicate among reviewer controls. [Pinned source revisions](/private/tmp/caprmedio-ste-paired.pfaP04/design.json)

Rerun both arms on the same source snapshots with the same model version and sampling settings, one generation attempt per Atom, fixed forms and exact terms, and reviewers blind to arm labels. Count safe cuts found and made, unsafe cuts proposed and accepted, confirmed or possible meaning loss, unsupported additions, faithful readability, words removed and added for explicit scope, and time or model calls including review. Record disagreements and adjudication. A material change blocks the edit. A no-change result is appropriate where there is no safe cut, and deferrals remain visible in the yield.

If local patches recover safe cuts without accepted material regressions, compare on a fresh, role-diverse holdout before adopting the design or setting a length target. Stop if the method leaves the diagnosed failures in place or the extra review outweighs the cuts. These are proposed test conditions for the user's decision.

### Issue registry

| ID and state | Issue and consequence | Issue confidence, basis, and limit | Fix |
|---|---|---|---|
| I-01 · OPEN | The whole-Atom instructions left six known candidate cuts in place and total length near the source. | 99% for the corpus observation. The cause and prevalence elsewhere remain unknown. | F-01, F-04 |
| I-02 · OPEN | Splitting changed explicit scope in `CA-O-169`, `CA-O-216`, and `CA-M-439`, which can change permitted actions or section restrictions. | 98% for the reviewed changes. Frequency outside this benchmark is unknown. | F-02, F-03, F-04 |
| I-03 · OPEN | Fluent edits can lose a verification duty or classification. The reviewed examples include `CA-E-628` and `CA-D-613`. | 98% for the reviewed cases. `CA-M-116` remains ambiguous, and automatic checks are uncalibrated on this corpus. | F-03, F-04 |

### Fix and improvement register

| ID, issue, relationship, and state | Proposed change and expected result | Confidence, authority, and verification |
|---|---|---|
| F-01 · I-01 · complementary · PROPOSED | Pilot C-1. Identify exact cut and retained spans before patching. Expect a small review surface with some distributed duplicates still present. | 80% it is useful to test, based on S-01–02 and local misses. The user owns pilot authorization. Discover, patch, then compare recovery of adjudicated cuts. **Preferred** for the first comparison. |
| F-02 · I-02 · complementary · PROPOSED | Pilot C-2 on condition-heavy blocks. Preserve each binding before splitting. Expect clearer actions and possible added words. | 90% the check addresses the named failures, based on S-03–05 and the scored edits. The user owns pilot authorization. Compare before and after scope, including lock and authorization-window boundary cases. **Acceptable**. |
| F-03 · I-02, I-03 · required prerequisite · PROPOSED | Independently compare source and candidate in both directions after generation. Retain original wording or send ambiguous changes for review. Expect more traceable omission decisions and added review effort. | 85% the check gives useful pilot evidence, based on S-06–07 and local omissions. The user owns pilot authorization. Test detection of seeded losses and acceptance of intact paraphrases before relying on it. **Preferred** as a safeguard. |
| F-04 · I-01–I-03 · alternative · PROPOSED | Pilot C-3 when cross-section restructuring warrants an upfront meaning map. Expect broader reach at higher effort. | 65% it adds useful coverage over local patches. The user owns pilot authorization. Check the source map before rewriting, use F-03 afterward, and compare safe cross-section cut yield and omission detection. **Acceptable** for a later comparison. |

## Unresolved evidence gaps

- **GAP-01 · I-01, F-01, F-04.** Repetition is visible in the sample. Its safe removal rate elsewhere is unknown, so a compaction target has no basis yet. Label candidate cuts and test a fresh holdout.
- **GAP-02 · I-02, I-03, F-02–F-04.** Reviews found explicit scope changes. Automatic detection remains uncalibrated, so treat its flags as review inputs. Compare those flags with blinded human judgments on real and seeded omissions and intact paraphrases.
- **GAP-03 · F-01–F-04.** Relative cost and performance of the designs remain unmeasured. Run the paired pilot before choosing an editing method.

## Skills used

1. `$fpf sota harvest`
2. `$fpf options explore`

### FPF sources consulted (3 read; 3 used)

Edition `fb3b6a4ad1d51d732a365f75f7d68337c7a751e2`.

- **Used** · G.2, `FPF-Knowledge-Graph/G_Discipline SoTA Patterns Kit/03_02_Harvest and Synthesize SoTA for a CG-Frame/00_G.02 - Harvest and Synthesize SoTA for a CG-Frame.md`. Problem frame, Problem, Forces, Solution 4.2–4.4, and Consequences.
- **Used** · B.5.2.1, `FPF-Knowledge-Graph/B_Trans-disciplinary Reasoning Cluster/04_05_Choose the Next Reasoning Contribution (Canonical Reasoning Cycle)/12_02_Generate and Compare Candidate Explanations (Abductive Loop)/02_B.05.02.01 - Instrument Abductive Hypothesis Generation with Novelty-Quality-Diversity (NQD).md`. §§1–4 and trade-offs 10a.
- **Used** · G.9, `FPF-Knowledge-Graph/G_Discipline SoTA Patterns Kit/10_09_Parity and Benchmark Harness/00_G.09 - Parity and Benchmark Harness.md`. Problem frame, Forces, and Solution 4.2–4.3.
