# Consolidated candidate review

This is a derived comparison of all 706 captured identities with the latest
Operator-authored candidate. It does not adopt Core, change Subjects, remove
entities, or replace the accepted review or the original Operator tree.

## Inputs and ownership

The candidate input is `../presentation/operator.entity-graph.candidate.json`.
The captured source commit is `a971d0e00c33c779f485fc8cad63194894d440fb`.
Use `../nodes/support/snapshot_sources.py`, whose 951 source pins have passed
verification. Read `../nodes/snapshot.context.md`, `../nodes/contract.md` and
`../nodes/scope.omission.decision.md`. Do not read current Core as replacement
evidence. Latest Operator directions in the candidate override earlier
candidate proposals; keep them separate from captured source Claims.

The nine existing `../nodes/inputs/nodes.batch-N.input.json` files are disjoint
and cover 706 identities. Each reviewer owns only `reviews/batch-N.review.json`
and an optional `reviews/support/batch_N.py` helper. The tooling worker owns
`support/consolidate.py` and `support/test_consolidate.py`. Root owns candidate
edits, integration, Git, final review and generated consolidated outputs.
Workers are not alone: preserve all other edits and never change another lane.

## Review receipt schema

Each receipt is a JSON object containing:

- `schema_version`: 1.
- `batch`: the existing input batch number.
- `kind`: `Captured nodes against Operator candidate`.
- `non_authoritative`: true.
- `native_admission` and `source_migration`: `not_performed`.
- `captured_core_commit`: the commit above.
- `candidate_sha256`, `input_sha256`, `baseline_sha256`, `prior_review_sha256`:
  hashes of the exact input files, not canonical-value hashes.
- `review_method`: explain use of the old reviewed meanings plus verified
  captured Main Content and the latest Operator directions. Do not claim a
  fresh exhaustive audit of all 951 sources or all source candidates.
- `nodes`: every assigned original identity exactly once.

Each node contains:

- `identity`: unchanged original identity.
- `prior_disposition`: from the accepted disposition ledger.
- `action`: one of `retain`, `rebase`, `inherit`, `delivery_policy`,
  `operation_or_method`, `projection_view`, `syntax_context`, `drop_candidate`,
  `review_required`, `concrete_conflict`.
- `candidate_root`: one of Artifact, Scope Unit, Actor, Relation, Revision,
  Carrier, Execution; null for context or unresolved mapping.
- `candidate_path`: a proposed human-readable display path, or null. It is
  not a native edge, executable selector or replacement identity.
- `content_view`: R, M, E, D, O, P, C, A, mixed, or unclassified.
- `confidence_percent`: confidence in the proposed classification. Below 90,
  leave the mapping `review_required` or `concrete_conflict`, with no committed
  `candidate_path`.
- `reason`: identity-specific, not a blanket statement that all slash paths
  are narrower-than, all labels are meaningless, or all old nodes disappear.
- `operator_rules`: candidate JSON paths/rules supporting the comparison.
- `evidence_refs`: global keys from `../nodes/nodes.dispositions.json`'s
  evidence catalogue. Reuse exact old evidence; new evidence must be added
  through root integration, never fabricated. Verify quoted line spans against
  captured bytes; read the pertinent Main Content. Metadata alone is not proof.
- `checked_source_atom_ids`: captured sources actually checked for this row.
- `preserved_distinctions`: constraints, qualified meanings, allowed-value
  domains, reference or lifecycle distinctions retained by this proposal.
- `question`: null, or an object with `kind` (`concrete_conflict`, `source_gap`,
  `technical_followup`) and `text`. Only concrete unresolved conflicts go to
  the Operator; missing evidence or primitive names remain review work.

Do not equate inheritance of an obligation with inheritance of a concrete
Carrier. Do not collapse qualified Status fields or allowed-value domains just
because their labels repeat. Do not delete unproved or apparently empty nodes;
use `review_required` when no checked meaning supports a mapping. A drop is a
mark, with its meaning and risks preserved, not a deletion.

## Current decision boundaries

- Seven root Entities; named dependent Entities have no separate lifecycle.
- Dependent ID example: `atom(atom_id="CA-R-123").status`; pseudocode only.
- Scope ID `(project prefix)-SU-(number)` remains stable. Full metadata folder
  names retain ID, LABEL and NAME_NAME; project-root folders stay unchanged.
- Carrier ID is not its filename/path; general Core D policies describe field
  and storage conventions. No per-Property Carrier edges or D Atoms.
- Every Atom update increments Version by 1. Current version Active; older
  versions archived history. No permanent-ID archive-inheritance rule.
- Git preserves Atom contents/versions; Journal registers Atom IDs projected
  Active, projected archived, or authored in Project Configuration.
- Projection copies keep source ID and Version and a relative source link;
  whole Projection set has its own lifecycle/rebuild tracking. New originals
  are authored in Project Configuration, not synthesized in the Projection.
- Substance covers Claim/Objective/Question/Issue/Operation. Substance Scope
  is applicability, not ownership; omission requires the whole Subject AND
  whole owning Scope Unit. Optional Details does not remove typed requirements.
- M/E are views, not new roots; Operations definitions and actual Executions
  differ. Ad hoc Executions need no O Atom. Operator decides repeatability.
- Revision is historical state, separate from Artifact and its Properties.
  FROM_REVISION/TO_REVISION are deferred; history binding stays loose.
- A heading, contextual grouping or alias does not automatically create an
  Entity. A missing native relation proof is not a new Operator question.

## Verification and persistence

Use uv only, no system Python. Keep cache/temporary output under
`.caprmedio_tmp/` and use `python -B`. Author files with apply_patch;
deterministic create-only generation of derived JSON/text is permitted.
Generated outputs must carry input hashes, verify every old identity exactly
once, preserve source references, and never imply native admission. The
compiler must default to no writes, have explicit create-only `--persist`, and
verify existing byte-identical outputs; mismatch fails without overwriting.

Review lanes are bounded to 15 minutes. Return truthful coverage and any
remaining work; never fabricate completion. Root can assign a continuation.
