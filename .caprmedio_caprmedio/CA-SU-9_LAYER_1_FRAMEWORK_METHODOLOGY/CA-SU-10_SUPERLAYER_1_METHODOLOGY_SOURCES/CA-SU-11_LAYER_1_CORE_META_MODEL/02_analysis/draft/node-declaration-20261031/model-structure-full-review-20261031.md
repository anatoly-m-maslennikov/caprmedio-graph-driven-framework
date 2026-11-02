# MODEL / PROJECT STRUCTURE review — 2026-10-31

Reviewed 108 registered Drafts: 74 Declarations (27 Primary and 47 Property) and 34 other Atoms. Read the proposal and Epic Draft. The substantive Declaration review found no verified defect after checking shared governing Rules. Four stale checks remain in the migration-readiness Evaluation.

1. **Subject syntax — P2, line 30.** [Readiness Evaluation](../../../06_evaluation/draft/node-declaration-20261031/CA-E-draft-CORE_META_MODEL-EVAL_POLICY--check-node-declaration-migration-readiness.md) rejects := unconditionally. A valid Subject such as Atom/(.Role := Method) would fail. Accept the Subject-only form while retaining separate Formal Claim meanings.
2. **Declaration ownership — P2, line 27.** The Evaluation counts Current owners without resolving the selected effective MODEL. An inherited base and explicit local replacement could be counted as two owners. Evaluate one effective Current Declaration per Node after override resolution.
3. **Inherited Property source — P2, line 28.** The Evaluation always resolves an inherited Property to its original Declaration. Add the explicit local MODEL replacement exception; unchanged inheritance continues to reuse the original.
4. **ENGINE Scope — P2, line 33.** The unconditional base ENGINE restriction does not account for an explicit local MODEL override of that rule. Check its effective Scope under the selected MODEL. Merely introducing a local MODEL still grants no wider Scope.

There are **26 Claims with prose** in Node descendants and their Properties: Projection, Journal and MODEL, plus 23 Properties. This excludes the Node root and all Semantics sections. The other 47 descendant Declarations have formal-only Claims. Remaining prose includes identity, lifecycle, derivation and Model-inheritance constraints; its presence alone is not a defect. See the [exact excerpts](remaining-node-claim-prose-20261031.md).

Shared Rules already supply Project-scoped UNIQUE, per-effective-MODEL ownership and the typed CAPRMEDIO roots. The reviewer retracted three initial findings after checking these Rules. No duplicate rules were added to Declarations.

Metadata, register hashes, local links and Declaration Subject uniqueness pass. Properties have occurrence, value and dependent-name contracts and no Semantics. All 750 snapshotted Current Core Requirements and Current Epic 38 are unchanged.

[Evidence and adjudication](declaration-expansion/model-structure-full-review-20261031.json)

No Atom Draft was changed. MODEL inheritance naming, effective selection/override binding and other already-declared adoption gates remain open. This is a document review, not parser, runtime, source-adoption or deferred execution-instance validation.
