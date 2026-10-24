---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: branch-coverage
  depends_on:
  - programmatic software
version: 13
updated_at: 2026-10-24 02:14:24 +0400
relations:
  evaluation_for:
  - CA-M-285
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-396
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
type: Eval Case
tier: 1
---
# Use Python branch coverage as navigation evidence

## Claim checked

branch coverage locates unobserved alternatives **without** being treated as proof
of correctness.

## Test case

collect branch coverage for one changed decision unit with one intentionally
unobserved failure branch.

## Acceptance criteria

pass **only** **when** the missing branch is reported for review, the target **and**
omissions are stated, **and** acceptance depends on public-outcome assertions rather
than a percentage alone.

## Failure disposition

reject reliance based solely on the coverage percentage.

## Sources

- [Coverage.py: branch coverage](https://coverage.readthedocs.io/en/latest/branch.html)
- [CA-M-285 — Select software Evaluation techniques by failure mode](../05_method/CA-M-285-PROGRAMMATIC--select-software-evaluation-techniques-by-failure-mode.md)
