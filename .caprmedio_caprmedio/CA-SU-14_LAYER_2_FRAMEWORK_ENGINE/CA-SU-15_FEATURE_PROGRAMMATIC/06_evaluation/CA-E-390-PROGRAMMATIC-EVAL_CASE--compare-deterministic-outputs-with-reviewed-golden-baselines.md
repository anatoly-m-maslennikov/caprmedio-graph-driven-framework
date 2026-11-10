---
atom_id: CA-E-390
ref_id: CA-E-390
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
    <+ Verification <+ Dynamic Testing
  dependencies:
  - MODEL//CAPRMEDIO <+ Package/Project Package
tier: 5
relations:
  evaluation_for:
  - CA-M-424
  DERIVED_FROM:
  - CA-A-053
status: Active
version: 23
updated_at: 2026-11-10 20:47:54 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
carrier_destination:
  file:
    name: CA-E-390-PROGRAMMATIC-EVAL_CASE--compare-deterministic-outputs-with-reviewed-golden-baselines.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Compare deterministic outputs with reviewed golden baselines

## Claim

### Prose Claim

#### Claim checked

a large deterministic output changes **only** through a reviewed semantic diff.

#### Test case

change one deterministic Markdown **or** machine-envelope output **and** invoke its
golden comparison with **only** declared volatile fields normalized.

#### Acceptance criteria

pass **only** **when** the unexplained difference fails, critical invariants remain
focused assertions, **and** a replacement baseline requires explicit diff review.

#### Failure disposition

reject automatic baseline refresh **and** return the semantic difference for
review.

#### Sources

- [Syrupy snapshot testing](https://github.com/syrupy-project/syrupy)
- [CA-M-285 — Select software Evaluation techniques by failure mode](../05_method/CA-M-285-PROGRAMMATIC--select-software-evaluation-techniques-by-failure-mode.md)

##### Golden-corpus cases

- require mock inputs **and** controlled external boundaries paired with reviewed expectations derived from governing RED. execute the real implementation **and** compare its actual output **and** declared effects against those expectations.
- test good, malformed, rejected, boundary, **and** combined inputs. reject a missing expected case, a false positive on a good case, **or** an unexplained difference on a bad case.
- a golden corpus **may** include small outputs; its use is **not** limited **to** large snapshots. normalize **only** explicitly admitted volatile representation, never behavior under test.
- retain discovered failures as regression cases. an automatic overwrite of expected outputs **or** an oracle copied from the defective implementation fails this Evaluation.
