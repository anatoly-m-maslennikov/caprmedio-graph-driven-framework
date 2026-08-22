---
subject_scopes:
  - framework-engine-software
version: 2
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Fuzz parsers and stateful boundaries

Use property-based generation for Markdown, TOML, JSON, filenames, paths, filters, and CLI envelopes whose valid and invalid spaces are broader than representative examples. Use rule-based state machines for lifecycle, file-change, Journal, lease, Hook, and background-service sequences where failures depend on operation order.

Define invariants from accepted RMED authority, preserve the minimal failing example or action sequence and seed, and add a deterministic regression case for every accepted defect. Bound normal runs and place expensive campaigns outside synchronous Hooks.

Candidate alignment: CA-E-001, CA-E-002, CA-M-005, CA-O-003, CA-R-861.

## Sources

- [Hypothesis documentation](https://hypothesis.readthedocs.io/en/latest/)
- [Hypothesis stateful testing](https://hypothesis.readthedocs.io/en/latest/stateful.html)
- [Hypothesis API reference](https://hypothesis.readthedocs.io/en/latest/reference/api.html)
