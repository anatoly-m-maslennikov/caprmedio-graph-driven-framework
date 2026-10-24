# Binding drift report — P2613 preparation

Generated: 2026-10-23T00:07:58+0400
Scope: CA-P-2582 candidate binding/fixture preparation
Authority: CA-C-576
Disposition: mechanical evidence only; no publication or live binding mutation

## Candidate

- In-memory CA-O-016@18 candidate: valid.
- Candidate SHA256: ad385a288efa2bb1857c3d9f11c019d40485569090ccda17854182b56b93d861.
- Raw Project manifest: fails the retired CA-O-091 unique-current check.
- No candidate emission, admission, or visible Project projection update was performed.

## Drift

- All 15 non-target route pins and both query admissions differ by version, path and digest only.
- No shape, order or flag drift was observed.
- Query observations: CA-O-158@5 -> CA-O-158@7 (ProjectConfiguration); CA-O-161@4 -> CA-O-161@6; CA-O-163@6 -> CA-O-163@8; CA-O-162@4 -> CA-O-162@6.
- R1847@16 lines 37-42 and E567@7 lines 25, 36 and 40 define/expect 15 operations and omit move_atom; the canonical Project manifest has 16 including move_atom, selected_route_spec.py line 33 permits OPTIONAL_SELECTED_ROUTE_NAMES, and O127 supports Move. This public-declaration versus Project/code mismatch is owned by the lifecycle review and is not a renaming of R1847.
- A1142 remains v2 with historical W09; no A1142 edit was made.

## Preserved baselines

- Project projection: f6577216b7ee914d9abf3939677df9208d9658a3e91fe74ad13b34c09539329c
- Engine legacy: d6dca70bbaa3530958d5950278104ed5628b7a282539675fecd9f9a58845b684

## Mechanical inventory

- 12 leaves each: create_atom, move_atom, build_entities_graph, build_terms_graph, find_and_fetch_journal_events
- 14: change_atom_status
- 15: replace_atom
- 23: update_atom
- 57 each: create_scope_unit, rename_scope_unit, move_scope_unit, remove_scope_unit, build_applicable_methodology
- 3: find_and_fetch_artifacts
- 12: revert_changes
- 15 query-admission pin leaves
- The source graph has 29 edges; 13 terminal edges map to the complete sentinel; the source retains distinct completed/blocked terminal targets

These are mechanical counts, not coverage, semantic qualification, or publication evidence. CA-P-2612 source wording review is accepted with 99% independent-review confidence. The visible Project binding, runtime and production MCP remain unchanged.


## Source-contract review verdict — 23 October 2026

Accepted exact source pins: CA-R-1847@16, CA-R-1848@9, CA-D-547@12, CA-E-567@7 and CA-E-568@8. Parser/body checks and independent review passed. This closes CA-P-2612's source-only package. CA-P-2613 remains Backlog pending the Operator's choice between reviewing all 15 non-target route pins plus both query admissions and retaining the focused hold. No candidate emission, A1142 edit, live binding mutation or admission was performed.


## Full binding-review authorization — 23 October 2026

The Operator authorized all 15 non-target route-pin comparisons plus both query-admission checks before publication. Review lanes are active as follows:

| Plan | Lane | Scope | Status |
| --- | --- | --- | --- |
| CA-P-2614 | lifecycle | 5 route pins | Done |
| CA-P-2615 | Scope Units | 4 route pins | Done |
| CA-P-2616 | graph builders | 2 route pins | Done |
| CA-P-2617 | applicable methodology | 1 route pin | Done |
| CA-P-2618 | revert | 1 route pin | Done |
| CA-P-2619 | queries and admissions | 2 route pins + both admissions | Done |

The route-pin total is 15; query-admission leaf counts remain a separate mechanical inventory. No candidate emission, A1142 edit, live binding mutation or admission is authorized by this report.


## Semantic review completion — 23 October 2026

The six lanes are review-complete: CA-P-2614 through CA-P-2619 are Done as
planning records. The aggregate is 8 PASS findings and 7 binding-closure HOLD
findings. CA-C-583 records the confirmed Journal receipt/completion conflicts
against R1525@11, R1720@22 and D340@17; CA-C-584 records the exact 15-operation
R1847/E567 public contract versus the canonical Project/code frontier of 16
including move_atom. See semantic-review-report.md for the full verdicts.
CA-P-2613 remains Active; CA-P-2620 and CA-P-2621 are conditional Backlog
follow-ups. No candidate, live binding, runtime, release or deployment change
was made.

## Bounded repair planning queue — 23 October 2026

| Plan | Owner lane | Exclusive scope | Depends on | Status |
| --- | --- | --- | --- | --- |
| CA-P-2622 | source-proposal lane | generic-six C583 clause-to-Core review | CA-C-583 | Done |
| CA-P-2623 | compiler-preparation lane | compiler/refactor boundary and compatibility map | CA-P-2622, CA-C-583 | Active |
| CA-P-2624 | compiler-regression lane | separate focused regression plan | CA-P-2623, CA-C-583 | Backlog |
| CA-P-2625 | fresh-inventory lane | public MCP versus Project/code frontier inventory | CA-C-584 | Active |
| CA-P-2626 | frontier-review lane | C584 reconciliation proposal | CA-P-2625, CA-C-584 | Active |
| CA-P-2627 | journal_compiler_repair lane | current O016@20 compatibility/admission preparation | CA-P-2612, CA-P-2625 | Active |
| CA-P-2628 | journal_compiler_repair lane | focused isolated current O016@20 tests | CA-P-2627, CA-P-2612 | Active |

This queue is read-only planning; it does not emit or admit a candidate. The
detached candidate direction is to omit optional move_atom while preserving
the optional implementation capability. O127's internal Move does not admit a
public MCP route. The live Project manifest remains at 16 operations and is
untouched until a separately validated publication decision. CA-C-584 remains
Active until that correction is validated; CA-P-2620 and CA-P-2621 remain
conditional Backlog leaves.

The fresh inventory reports O016@20 with body bytes unchanged from the exact
O016@18 archive. The new compatibility lanes preserve exact legacy-17 and
direct-18 support and do not broaden to every version greater than 18. They do
not alter the public 15-operation route or the live Project manifest.

The generic-six source review in CA-P-2622 passed at 99% or higher with these
current carrier hashes:

| Atom | Version | SHA-256 |
| --- | ---: | --- |
| CA-O-130 | 9 | 21a26982bad475063e49f733777959d25090c2805e781e722e5a197357453597 |
| CA-O-131 | 9 | 389f2bb12c7be94c95f530f16e6f9739a1fbbd806c80c50c4ff4c9e8328208f2 |
| CA-O-133 | 9 | af6ca9fa5d87d6c835209eeac58ee8ad0ff5ce726650886f67d44ba676506ea1 |
| CA-O-134 | 9 | 04f3630e4da5bca03366bee71c0cdde4de05afc72ec9a23a9500359ad5a675db |
| CA-O-136 | 9 | 86f6acf8d1032e6446bcbb95be58d5e5ac26f8ed723dff6da8f84eafc5243dcb |
| CA-O-137 | 9 | 4e08fdb21b3ab2ed1d41f39ec766e86386631f5e8095f105039d072ee11fe185 |

This closes only the generic-six review. CA-C-583 remains Active for the
R1317/O007/O155/O156 source alignment and compiler/Engine implementation gap.

## R1317 Journal-boundary decision — 23 October 2026

The Operator resolved CA-C-585: Journal recording is non-blocking for
methodology approvals and recovery; actual OperatorDecision and independent
Run/effect evidence remain required. The bounded follow-up queue is:

| Plan | Owner lane | Exclusive scope | Depends on | Status |
| --- | --- | --- | --- | --- |
| CA-P-2629 | source-proposal lane | explicit R1317/O007/O155/O156 source alignment | CA-C-585, CA-C-583, CA-P-2622 | Active |
| CA-P-2631 | compiler_rmed_reconciliation lane | seven current compiler/shared-run RMED contracts | CA-C-585, CA-C-583, CA-P-2629 | Active |
| CA-P-2630 | journal_compiler_repair lane | compiler admitted-evidence contract | CA-P-2623, CA-P-2629, CA-P-2631, CA-C-585 | Backlog |

The compiler contract must consume existing admitted decision, Run and effect
evidence and must not accept an authoritative caller approval flag. CA-C-583
remains Active: current Project Configuration versions are O130@9, O131@9,
O133@9, O134@9, O135@7, O136@9, O137@9 and O138@7, with source review still
open. No source, code, binding, runtime, publication, release or deployment
mutation is claimed by this planning checkpoint.

CA-C-586 is an additional Active Question: whether O011 should reuse the
interactive MCP loop to obtain the actual OperatorDecision, retaining
independent Run/effect evidence, or defer and report the integration gap.
CA-P-2630 remains Backlog until that question is answered; no trusted-evidence
or public decision-reference contract is admitted.

## Methodology source review and Engine replacement planning — 23 October 2026

CA-P-2629 is Done for the independent review of the four current methodology
carriers. The accepted pins are CA-R-1317@18 (SHA-256
`7eca1569caf1e9442c6b116e5b3ce2a0da2fd4049e97115f9ac72b8b415c46a2`),
CA-O-007@14 (`208e2665922bc4948d8e6f6780eeec36a660c6dc8d59581ae70e94959345ed70`),
CA-O-155@10 (`084318013d9192c049ca163b94bee872f1e47056b9f7d22c4687e5216cf0934a`)
and CA-O-156@11 (`5eb7eb70aacdd09c05f118b8246e9d994a9a9a1887a31ec050b16b2f76446193`).
The review passed at 99% or higher and confirms the non-blocking Journal
recording boundary with actual OperatorDecision and independent Run/effect
evidence still required.

CA-P-2630 remains Backlog: the methodology package is reviewed, but the
CA-P-2631 compiler/shared-run RMED package and the open CA-C-586 O011
interactive-decision question remain prerequisites.

CA-P-2632 is Active under CA-P-2631 for the identity-safe CA-R-1841 successor
and rebinding of CA-R-1840, CA-R-1842, CA-E-560, CA-E-561, CA-D-541,
CA-D-542 and CA-D-543. The proposed CA-R-2118 reservation is currently
occupied by an unrelated current applicable-methodology carrier, so the
writer must perform a fresh retained-carrier collision check and reallocate
without overwriting or merging that carrier. The replacement mapping is not
yet a Journal event; wait for actual predecessor/successor paths, versions and
hashes. No source, code, binding, runtime, release or deployment mutation is
claimed by this checkpoint.

## Superseding source closure and cold-start queue — 23 October 2026

CA-P-2627 and CA-P-2628 are Done. Independent Terra review found no
findings; 34 focused current-O016@20 checks passed with Ruff and strict
Mypy. The checks covered the exact allowlist, boolean/unknown refusal,
canonical mapping, no MCP queue fallback and operative dispatch. The
candidate remains detached from the live binding and does not publish or
admit O016@20.

CA-P-2629, CA-P-2631 and CA-P-2632 are Done for their reviewed source
packages. The identity-safe source mapping is CA-R-1841@2 archived to
CA-R-2118@1 active; E560@4 and D543@2 repairs and the active consumer
rebind are recorded in CA-P-2632 and the business Journal. CA-P-2635 is
Done for O029@13 (SHA-256
d554911c94588378540171d7cddc6447243ff5584df649dc28e56437ada760e7) and
O031@9 (SHA-256
9bd7426e10d48f9722253b40e90dbaef2fc8f96bf8b093d030e533bab942b21b7).
The 21-current-source closure is source-only; CA-P-2630 remains Backlog
for compiler implementation while CA-C-586 remains Active.

CA-C-587 is Active for the measured cold-start test-budget mismatch:
fixture/discovery is 30 seconds, production Gateway readiness is 90
seconds, and the disposable bounded harness is 120 seconds. CA-P-2633 is
Active to refactor the canonical legacy harness first. The worker has reduced
the observed 305 source lines to 200 and added a 200-line support helper;
focused checks and independent review remain pending. CA-P-2634 is Active to
align the bounded test startup to 120 seconds without changing the production
Gateway. The separate sanitized ValueError/source-drift hypothesis remains
unproven. No full suite, live binding, release or deployment claim follows
from this report.

## Final inventory and execution checkpoint — 23 October 2026

The final current-source inventory passed 50/50 with stable reads at
09:25:19Z and 09:25:22Z. The retained evidence artifacts are:

- `execution_evidence/p2613/current-source-pins.post-reconciliation-20261023.json`
  — SHA-256 `f0acd20b450b056f61312eb560cd1c742d6fd0cf9a8972de8dfd41db7bf6ed8f`.
- `execution_evidence/p2613/source-review-verification.post-reconciliation-20261023.json`
  — SHA-256 `b7a98738e69ea2e982eae089fd965acf5fba2eb12c95ab7e8e4a9cabd938a348`.
- `execution_evidence/p2613/binding-drift-report.post-reconciliation-20261023.md`
  — SHA-256 `871ee20e4b9e79398590f7652973a9543764b76f366154c53f34a39b0ae27b19`.

CA-P-2627 and CA-P-2628 are Done for candidate code admission and focused
verification: 34 checks passed with independent Terra review, Ruff and strict
Mypy, plus two separate Root registration checks passed in 6.649 seconds.
These results are not live binding admission or publication.

CA-P-2633 is Active execution: the worker refactored the legacy 305-line
stdio test harness to 200 lines and added a 200-line support helper; focused
checks are ongoing and independent review is pending. CA-P-2634 is Active
execution: the worker aligned the bounded test startup/readiness boundary to
120 seconds while leaving the production Gateway 90-second boundary unchanged;
focused checks are ongoing and final acceptance follows CA-P-2633 review.

CA-C-586 remains open. No live binding, runtime admission, release,
deployment or full-suite claim follows from this checkpoint.
