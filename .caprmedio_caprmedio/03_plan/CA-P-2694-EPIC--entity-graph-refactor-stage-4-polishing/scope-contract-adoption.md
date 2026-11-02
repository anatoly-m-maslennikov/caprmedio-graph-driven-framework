# Goals outside; Scope Contracts inside — adoption result

[A1313](../../02_analysis/done/CA-A-1313-SPEC_PROPOSAL--goals-outside-and-scope-contracts-at-tier-zero.md) records the accepted decision. [P2701](done/07-CA-P-2701-TASK--adopt-goals-outside-and-tier-zero-scope-contracts.md) and A1313 are Done. The reviewed Scope Contract model is adopted in Current methodology; remaining legacy and held work is explicitly deferred below.

## Final model

- Keep a Goal outside its Target Scope Unit, owned by the parent. Project Goal keeps its Operator Actor owner and Tier −1.
- Inside a unit, numeric Tier **0** names its foundation. Its readable label is **Scope Contract** and its filename Tier token is **SCOPE_CONTRACT**. No new Type or frontmatter flag is added; Atom.Label stays separate.
- Preserve Content Role and Type. In particular, an O Atom remains Workflow, Action or Step. Tiers 1–4 retain Core, General, Standard and Detail; 5+ needs no predefined name.
- The parent’s external Goal may be part of that parent’s own Tier-0 contract. “Outside” is relative to the child target, not outside every scope. This does not duplicate the child’s contract.
- Within the same Local Scope Unit, an appropriate already-admitted typed M/E/D/O Tier-0 relation may target R Tier 0. Other equal-Tier directions remain forbidden. Cross-Scope rules and endpoint admissions remain applicable. This is not an automatic conflict winner.
- Project-wide applicability, canonical invariant ownership and Operator conflict safeguards are preserved. A local Tier label alone does not grant Project-wide authority.

## Initial Draft preparation

| Group | Drafts |
| --- | ---: |
| Model, Tier and evaluation successors | 14 |
| Goal → local Tier-0 Rule conversions | 8 |
| Core promotion candidates | 4 |
| Methodology/project consumer corrections | 30 |
| Existing Project Tier-0 filename changes | 23 |
| Filename delivery rules | 2 |
| **Total** | **81** |

The initial preparation contained **78 review-ready candidates and 3 held promotion Drafts**. The actual packet and outcome below supersede that preparation count. **35 Draft filenames carry SCOPE_CONTRACT**, each exactly once. No Scope Contract Type definitions were created.

The eight Goal conversions preserve each complete Claim and Summary, with lossless heading normalization, use Requirement/Rule, and move proposed ownership to the explicitly identified registered local unit: PROGRAMMATIC, AGENTIC, MCP, SKILLS, PROMPTS, GRAPH_SERVER, GRAPH_UI and WORKFLOW_ORCHESTRATOR. They do not create identical duplicate Goals/contracts. The 47-Goal review retains 25 external Goals and holds 14 unresolved classifications. Human-approved FRAMEWORK_ENGINE targets remain unchanged.

M003 is the supported Core promotion: its method of sufficient information exposure serves R1420, so the Draft changes Tier to 0 and replaces its broad child_of link with method_for. Three other promotion Drafts remain held: E002’s generic evidence commitment does not establish the proposed evaluation_for; R007 has a plausible governing R1407 dependency; and reversing R686’s general Method dependencies is not sufficiently evidenced. Their Current Tier 1 and relations remain authoritative. The task does not require promoting all four.

## Reviews and corrections

Four preparation lanes covered 35 Project foundation candidates, all 47 Goals, the direct model definitions and a 2,444-source dependency scan. Terra reviewed cross-lane model composition and all 30 consumer diffs. Corrections include all-local-Scope Tier-0 coverage in R030, conservative Project-wide conflict boundaries, and the final Principle allowed-value Subject in E477. Existing Workflow routing, old Global Tier/freshness mechanisms and deferred execution-policy questions were not redesigned.

The [thin Draft index](scope-contract-drafts.tsv) gives Atom ID, old/new Subject, status, path, source Version/hash and Draft hash. The [decision table](scope-contract-decisions.tsv) gives retained/converted/held dispositions. The [dependency table](scope-contract-dependencies.tsv) has one row per selected source; the acquisition scan found 151 relevant sources, including 40 Engine-later consumers. All 81 source hashes and Draft hashes were checked, and source-preserving candidates retain their entire body. See [checks](scope-contract-verification.json).

## Actual adoption

The reviewed packet published **86 Current successors**, including eight new identities for changed Summaries, six local Goal-to-Rule conversions retaining their original numeric Tiers, eight local Tier-0 responsibility Rules, the supported M003 promotion, consumer repairs and filename changes. R1434 was archived at its existing Version without a replacement. E379’s sole live link to it was removed while retaining its other content.

A separate one-Atom correction normalized the external Project Goal R2155 to Version 17 and mapped its Governs to `Entity/Aspect/Product: CAPRMEDIO Framework`, exactly as the Operator chose. The Claim, Operator owner, Project target and Tier −1 are unchanged. In total, this Task performed **87 Current updates and one retirement**, with **88 predecessor/history archives**. The three held Core promotions remain unchanged at Tier 1.

All eleven required predecessor references across nine consumers were rebound to eight new IDs. No Engine reference-only edits were needed. The actual packet includes the already reviewed eight Engine Goal owner/classification moves and four local Engine outcome classifications; no Engine code/runtime implementation was changed.

The three graph views (CA-PROJ-014/015/016) were rebuilt from **1,261 actual Current sources**, with 33 named Relation Types. Source, native-reference, renderer and artifact readback checks pass: no missing/ambiguous native targets, no duplicate selected IDs and no source/hash mismatches. Current discovery now reads physical authoritative sources rather than using old paths as its membership list. This includes the previously omitted Operator-owned Project Goal and other Current Term-related sources; it does not modify those unrelated sources. The projection scope list contains five registered Scope Units, never the Operator Actor as a Scope Unit.

The final verification and graph report are saved with the Task. Stable projection IDs and source selection are retained. The scope excludes code/runtime tests, Engine implementation, the Terms Graph and advanced formulas. Old installed Framework copies and historical P2700 trial Drafts were not migrated. The old trial is superseded as an adoption batch.

## Explicit remaining work

- Four technical Engine Goal cases are deferred to [CA-P-2702](../CA-P-2637-EPIC--migrate-engine-rmed-atoms/backlog/CA-P-2702-TASK--reconcile-deferred-engine-scope-goals.md). They are not silently dropped or assigned invented targets.
- GIT/FPF Goals R1469, R1474 and R1482 stay deferred under the prior Operator decision.
- The three unsupported additional Core promotions and nine earlier text-style/classification Drafts are recorded in [CA-P-2703](backlog/CA-P-2703-TASK--review-deferred-foundation-and-notation-drafts.md).
- The legacy CAPRMEDIO-R-800 documentation carrier and pre-existing Engine/reference issues remain outside this source adoption; no claim of whole-repository conformance is made.

The parent polishing Epic remains Active. P2701’s declared adoption/rebuild is complete.
