# TOMLKit selection — bounded source review

Date: 2026-10-13. Derived review evidence, not a new source of authority.

The Operator approved a narrowly scoped TOMLKit dependency, its M/D/E rules and later private connector implementation. The proposed package is TOMLKit 0.15.1 in a new `connector-toml` group. No dependency, lockfile or implementation change has been made. The affected FPF review remains plan-first and unexecuted.

## Reviewed sources

All paths share `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/305_FEATURE_CONNECTOR_TOOLS/`.

| Source | Version | SHA-256 |
|---|---:|---|
| `05_method/CA-M-383-CONNECTOR_TOOLS-STANDARD-METHOD--select-tomlkit-for-pure-toml-materialization.md` | 1 | `e599bf5ff4869857e800ef4a40eb8683a47d9b8c25c7ac46cdfa4d268a91424b` |
| `07_delivery/CA-D-632-CONNECTOR_TOOLS-STANDARD-DELIVERY--deliver-the-bounded-tomlkit-materializer-dependency.md` | 1 | `c0c107fd7d46f40e7e75ea54b52c687186d037bf2c5d2dbe9c31fe908d3d8593` |
| `06_evaluation/CA-E-635-CONNECTOR_TOOLS-STANDARD-QA_CASE--verify-lossless-pure-toml-materialization.md` | 1 | `486adeba9fafce44762d81676d699f005a9c3511ad7891c26d3da5f9b1a56230` |

Author: `connector_binding_review`. Different reviewer: `epic_atom_read`.

The independent bounded semantic review passed these exact sources against M110, M281, D250, E254, R1936, O204 and D631. They preserve the default standard-library boundary; select only private changed TOML materialization; preserve Read/no-op independence; retain receiving schema, permission, currentness and publication boundaries; and state that configuration, code, tests and runtime acceptance are pending. Upstream metadata/license are selection evidence, not local preservation tests.

## Validation limits

Author and independent reviewer own-carrier validation each passed three files in existing-relation mode (`creating=False`). Full new-reference validation (`creating=True`) did not pass: the current inventory requires explicit identity/status/version on every discovered source before filtering requested targets. Existing legacy carriers fail that inventory. No references were removed and no validator was bypassed to claim admission.

The five current Plan carriers (P2256 and P2307–2310) passed independent source/structure review. P2308–2310 are correctly in the local `001_backlog`; P2307 is Active. The P2256 v2 archive matches its exact HEAD predecessor: `160e7773ecfc2ebef50f83b560a6995066b1d204b310d96fdd8067dc8dcc6ff8`. P2256 is now v3. The complete Plan validator remains unavailable because its supplied context cannot resolve the implicit Project `caprmedio` as a target Scope Unit; the unchanged predecessor has the same gap. This is not a full validator PASS.

## Next gate

P2307 remains Active. Show and obtain approval for the narrow affected FPF review before dependent implementation. P2308–2310 remain Backlog. P2297 still owns receiving-schema integration; source review does not close it. No live configuration writes, installed activation, Core migration or Markdown/YAML dependency changes are admitted by this record.
