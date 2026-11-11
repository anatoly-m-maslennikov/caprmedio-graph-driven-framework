# MODEL continuation result

- Applied 89 reviewed source revisions and 19 retirements; exact predecessor bytes are retained in 108 archives. `IS_DECLARED_BY` uses new ID CA-R-2732.
- Applied the additional Role Rule repair CA-R-1283@33, with its exact @32 predecessor retained. The Rule defers to individual Role Declarations; the Property Declaration CA-R-2702 already had no value list.
- Checked all 1,148 selected Current sources for duplicate allowed-value lists. The Role list was the only high-confidence duplication. Contextual subsets, structural-name lists and independent domains retain their distinct rules.
- Migrated CFEL grouping and explicit instance binders across 1,148 selected sources: 263 files changed, zero held. Corrected 45 model/instance marker classifications without changing business expressions.
- Rebuilt seven MODEL-only projections. Concrete Node instances and STRUCTURE Subjects are excluded. Formats, cardinalities and Formal Claims use only Requirement / Declaration evidence.
- Independent preservation checks pass for exact archives, identity, Summary, metadata, literals, frozen mechanical references, final hashes and idempotence. Five reviewed semantic provenance removals are recorded separately.
- 412 graph tests pass. Five adoption guard tests and 16 migration tests pass. All 44 live Scope Declarations parse with instance markers; the three status domains retain their source-bound checks.

## Limits and remaining work

The source snapshot contains 1,148 pinned Current sources. Five pre-checkpoint source exceptions are recorded: four concurrent Core edits and the other chat's untracked WORKBENCH Scope Declaration. A later Workflow revision (R2464@5) is also included as an explicit input in the refreshed publication snapshot. These concurrent sources remain outside this commit; their snapshot hashes are verified, and fresh-checkout completeness depends on that chat's publication.

The MODEL-only audit still exposes 74 uncovered Subject expressions and 51 unresolved expressions, with inheritance and complex selectors kept separate. These are a remaining review queue, not a complete semantic census. MODEL IF-membership bodies remain opaque evidence in the reader; they are not executed by a new evaluator.

Epic CA-P-2694 remains Active for the existing P2707 Engine checks and the explicit model review queue. This work records manual source application; no native Workflow admission, Journal append or release is claimed.

## Evidence

- integration/adoption-plan.json and adoption-receipt.json
- integration/mechanical-plan.json and mechanical-receipt.json
- migration/group-correction-plan.json
- allowed-values/application/adoption-plan.json and adoption-receipt.json
- reviews/final-preservation.json
- allowed-values/audit.json
- projections-publication/generation-manifest.json

The migration preservation proof uses its immutable `final-source-frontier.json`. The latest publication uses `publication-source-frontier.json`, which records the newer concurrent Workflow input separately.
