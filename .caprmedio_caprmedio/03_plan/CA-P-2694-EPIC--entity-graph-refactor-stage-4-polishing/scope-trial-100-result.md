# Scope Definition and Summary trial — 100 sources

The practical coherence rule fits better than “one predicate per Atom”: keep related statements together when one concise Summary faithfully covers their whole meaning. Replacing Goal is feasible as a model direction, but a mechanical Goal → Scope Definition relabel would lose the distinction between a unit's standing responsibility and a specific required outcome.

## Result

- **100 Current sources reviewed**, including **all 47 Current Goals** and 53 other RMEDO sources. Four disjoint Terra-high lanes read full content. This is a purposive sample, not a statistical estimate for the whole repository.
- The 47 Goals produce **22 Scope Definition proposals and 26 supplementary Requirements**. Two source Goals consolidate; other sources split where they contain separately meaningful obligations. The outputs are candidates, not 48 admitted replacements.
- The 53 ordinary sources produce 55 candidates. The main split is R655: Atom definition, governing relation ordering, and relation endpoint restrictions.
- Total: **103 source-based Drafts**, plus **one supporting Scope property Definition**, so **104 actual Draft files**. This trial does not demonstrate fewer documents; it avoids a predicate-per-file explosion while keeping explicit boundaries.
- Review disposition: **82 Ready for further review, 21 Hold**. “Ready” means the lane found a coherent proposal; it does not authorize promotion or establish Type/schema/runtime admission.
- **All 103 source-based candidate Summaries fit 100 characters**, including spaces. Equally faithful ≤70-character alternatives were established for **42**. The other 61 were not optimized to exhaustion; this does not prove that 70 is impossible. Neither length limit is adopted.

## What fits

Standing responsibility definitions for units such as PROGRAMMATIC, AGENTIC, METHODOLOGY_SOURCES and CORE_META_MODEL can state purpose, responsibility, expected results and boundary together. One definition per resolved target is clearer than relabeling every old Goal separately.

Specific outcomes such as Operator control, observability and diagnostic behavior remain supplementary Rs. Their existing explicit Target Scope Units are preserved, including the 13 FRAMEWORK_ENGINE targets approved by the Operator. A Claim naming the wider framework does not invalidate that explicit target. Root Project responsibility remains Operator-owned; it does not create an Operator Scope Unit.

Long operational procedures and Evaluation cases can remain one Atom when their steps and conditions form one meaning. All 30 E/D/O candidates preserve their original operative text and existing section locations; the Summary is replaced, and a Claim/Operation heading is added where the source had unheaded operative prose; the excerpt in the review handoff is not substituted for the body. Their proposed metadata placement remains separate from live relocation.

## What needs work before adoption

1. **Goal conversion does not define every Scope.** The sampled Engine-targeted Goals chiefly state specific outcomes; none provides a complete FRAMEWORK_ENGINE responsibility contract. A later pass must fill such missing scopes from accepted responsibilities rather than hide them in a vague definition.
2. **Source addressing defects remain explicit.** Thirteen Goals lack target metadata. Draft targets are proposed only when the original meaning identifies one. GIT, FPF, OPERATOR_PROMPTS, ACTION_PROMPTS and AGENT_HOST_PLUGINS are absent from the supplied registry; the TOOLS subgroup list conflicts with it. Drafts do not register or move these units.
3. **R1434 has a real target conflict.** Its metadata says PROJECT_CONFIGURATION while its Claim and governed Subject concern CORE_META_MODEL. Its candidate is held; no silent correction is adopted.
4. **Type and template consumers need coordinated migration.** R925, R2152, R655, R2132, R2149, M115 and D292 retain Goal-related assumptions. The trial includes replacement/type and authoring prototypes, but does not rewrite all consumers. The proposed Scope Definition owner is explicit; no new blanket parent-owner rule is introduced. Project-root Actor ownership and governing order remain review points for that migration.
5. **Other concrete holds are separate from Summary length.** E307 has a recovery conflict; O175 is absent from O164's complete workflow graph; O031 mixes business meaning with technical execution conditions. Compressing their names cannot resolve those issues.
6. **Scope has a supporting property Definition Draft.** It describes the textual responsibility contract expressed by the defining R. It does not require a duplicate Scope value in TOML. Exact Scope-property cardinality and formal value format remain open for adoption, rather than being asserted by this trial. D292's existing Project Goal filename rule remains a held source-preserving trial; the eventual generalized `DEFINES_SCOPE_FOR` contract still needs adoption.

## Files and checks

[Source-to-Draft trace](scope-trial-100.tsv) has one row per source, including its Version and SHA-256. [Draft index](scope-trial-100-drafts.tsv) lists each candidate's owner, target, Summary, lengths, hold status and actual Draft path. The supporting Definition is:

[Scope property Definition Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/scope-trial-100/CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-scope-unit-scope.md)

The 100 original paths and hashes were checked before and after staging. All 104 files parse as Drafts; source-based IDs use either an unallocated role Draft ID or the next-version Draft form, without allocating Current IDs. Existing Drafts were not overwritten. No sampled Current Atom was changed, archived, promoted or retired. Only the trial's control Plan and Epic progress are updated.

Formal admission, whole-project reference validation, runtime behavior and release tests are outside this draft-only trial. Goal replacement, a Summary length limit and model-wide migration remain undecided pending review of the result.

## Completed review lanes

| Deliverable | Owner | Exclusive edit scope | Dependency | Acceptance | Status |
| --- | --- | --- | --- | --- | --- |
| 29 Engine-oriented Goals | Terra high | Engine Goal handoff | Pinned inputs | Full meaning, target and Summary review | Done |
| 18 Model/Project Goals | Terra high | Model Goal handoff | Pinned inputs | Consolidation and root ownership review | Done |
| 23 ordinary R/M sources | Terra high | R/M handoff | Pinned inputs | Whole-meaning coherence review | Done |
| 30 ordinary E/D/O sources | Terra high | E/D/O handoff | Pinned inputs | Operative-text preservation review | Done |
| 104 Draft files and thin traces | Parent | Trial Drafts and control Plans | Four handoffs | Readback, lengths, hashes and coverage | Done |
| Bounded integration review | Terra high | Read-only staged Drafts | Staged outputs | Flagged corrections rechecked | Done |

The integration review found and corrected duplicate Summary values in legacy `# Summary` carriers, a missing space, and an overasserted Scope cardinality. The corrected transformation was checked across all 30 preservation candidates. Its readback was bounded; it is not a second full semantic review of all 104 Drafts.
