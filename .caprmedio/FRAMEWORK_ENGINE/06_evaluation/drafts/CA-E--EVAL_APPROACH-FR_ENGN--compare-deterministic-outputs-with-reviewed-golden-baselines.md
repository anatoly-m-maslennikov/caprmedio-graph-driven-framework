---
subject_scopes:
  - framework-engine-software
version: 2
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Compare deterministic outputs with reviewed golden baselines

Use reviewed golden baselines for large deterministic Markdown, HTML, JavaScript-data, CLI-envelope, or diagnostic outputs when individual assertions would hide their complete observable shape. Normalize only explicitly non-semantic volatile fields before comparison and keep the normalization rules visible.

Fail on every unexplained difference. Accept a new baseline only after reviewing the semantic diff against the governing change; never update baselines automatically merely to make an evaluation pass. Keep focused invariant assertions beside the baseline when they communicate critical meaning more directly.

Candidate alignment: CA-E-001, CA-E-002, CA-M-002, CA-D-002, CA-R-861.

## Sources

- [Syrupy snapshot testing](https://github.com/syrupy-project/syrupy)
- [Pytest: assertion introspection](https://docs.pytest.org/en/stable/how-to/assert.html)
