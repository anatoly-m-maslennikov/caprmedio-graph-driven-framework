# Pure TOML materializer — independent acceptance

Derived verification record for CA-P-2308 and CA-P-2309. Not receiving authority or live-write approval.

## Accepted scope

Private materialize_toml(source, delta, keys) returns proposed bytes, complete native values and effective diff. Existing semantic edit validation is reused. No file IO or schema/permission/source-admission decisions are added. Exact no-op returns original bytes without importing the optional dependency. Changed input must round-trip exactly; unsupported lossy edits refuse. Complete output native values and types are checked independently of CST rendering.

## Actual checks

Python 3.14.7 and TOMLKit 0.15.1: 20 tests PASS (13 independently authored, 7 author). Independent final-pin review PASS. Literal-byte assertions cover item/full-set/value edits, quoted and dotted keys, comments, whitespace, LF/CRLF, exact no-op, malformed and unsupported inputs, effect denial and mutation controls. Additional scalar-table preservation and structural AoT refusal probes passed. Two independent regressions first failed: duplicate private paths could normalize a net no-op; removing the first array member lost retained member indentation. Both are fixed and pass.

All existing uv.lock package records/groups, Python requirements and resolution markers remain unchanged. Only TOMLKit is added; lock serializer revision changes from 3 to 5 and removes the empty manifest section. The optional connector-toml group pins 0.15.1.

## Final SHA-256

Paths below are under 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ unless root-qualified:

- connector_toml_carrier.py: 0399a5ea176d94ec6dae8f4b042c91e8ec63afbbbe50c2ceb920e78cec39a913
- tests/test_connector_toml_carrier.py: f123d942beffa2ff57ad041ba67e69a3c7a8f5fe6eac7a2c2cc43d56ce98d17c
- tests/test_connector_toml_carrier_independent.py: eec1145150b2ad8c765048c5d73676f39f3afc78905eeee8f7b7465a31536cdc
- root pyproject.toml: 7f5051801ba00a8f7250fbb4ced7e6929a4fbf5e3cde5c7a53f4e599d050e289
- root uv.lock: c152ce49f2f0a18c1fd0edd04da3a7df2cceb27cbe5886a9470756248a341104

Current source pins: M383 v3 827e8dc12fd05776b16679522d70de322bdd028c15dc2c846c0dc3ddb4a73078; D632 v3 27d8d765370eac76ff3a50a75e121651387cc227730269165fa6175b782ade48; E635 v2 fb385a9835b1fd0edc7108ac23c66bb79cfc37c483fbc0fa76071800a18aa8f5. Finite source admission is recorded in typed-toml-relations-acceptance.md.

## Remaining work

P2310 connects the helper to the existing connector; P2297 retains distinct receiving-schema obligations. Structural Table/AoT occurrence edits and layouts whose removal loses unrelated trailing delimiters refuse. This is an explicit unsupported-layout result, not permission to normalize unrelated text. No receiver/writer/public codec, packaging activation, broad E254 acceptance or runtime operation was proved here.
