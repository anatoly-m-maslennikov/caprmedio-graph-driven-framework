# TOML writer integration — acceptance

Derived local verification for CA-P-2310, 2026-10-13.

The existing connector_toml_write.modify_configuration now gets payload, complete proposed values and diff from materialize_toml. Its existing complete schema validation, permission/source revalidation, late byte comparison, no-op result, observed write/error state and final readback are retained. No new public receiver, schema mapping or publication guarantee is added.

Actual full TOML suite: 60 PASS (0.298 seconds), including 11 independent integration checks and 6 author cases. Before hookup, the new author suite produced 12 byte/layout failures; they pass after hookup. Independent final-pin connected-code review PASS. Independent cases exercise exact CRLF/hex/trivia bytes, dependency-free/write-free no-op, schema/stale/permission/late-authority refusal, unsupported-lossy refusal, known effect with write error, unknown/unavailable readback and schema failure after a known write. Diff check PASS.

Final SHA-256 (under 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/):

- connector_toml_write.py: 9bd45ab5c479c28ab10dfc0ccdbcd2d7e476b57f78ffc541d925bc2972eac074
- tests/test_connector_toml_materialization_integration.py: e5e281382d92a420c2ed1281ee65f55c69cd7ba4ce5ee775231b9490002d942a
- tests/test_connector_toml_materialization_integration_independent.py: e1153b39546dd7c7348ca7713ea94547f07e65a1e83706bcb3241847c2c00069

Pure helper/dependency/source acceptance remains in toml-materializer-acceptance.md. Actual receiving Workflow mapping, accepted publication conditions and installed runtime remain separate; no live configuration was modified.
