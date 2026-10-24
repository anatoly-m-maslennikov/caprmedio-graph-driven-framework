---
atom_id: CA-M-383
content_role: Method
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Scope Unit//PROJECT_CONFIGURATION
  - Subject/Domain/Node/Continuant/Term//Property
  - Subject/Engineering/Carrier
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
version: 9
updated_at: 2026-10-24 02:14:24 +0400
relations:
  method_for:
  - CA-R-1936
  depends_on:
  - CA-M-415
  - CA-O-204
type: Eng Decision
tier: 4
---
# Summary

select TOMLKit for pure TOML materialization

## Scope

the private, effect-free construction of one proposed TOML document from supplied source bytes **and** an explicit admitted delta. filesystem access, receiving Workflow admission **and** public typed-value encoding are outside this Method.

## Claim

**to** construct the pure TOML materializer required by CA-R-1936 **and** CA-O-204, the Implementer **must** select TOMLKit's concrete-syntax representation for byte-preserving parse, edit **and** serialization, rather than construct a separate general TOML parser **or** normalize the complete document.

this bounded library selection is an exception under CA-M-415. the standard-library default remains unchanged. the exact dependency pin has one canonical owner: the `connector-toml` dependency group **in** root `pyproject.toml`, materialized with `uv.lock` under CA-D-632. this Method does **not** create another version setting.

- keep the existing pure delta semantics separate from concrete-syntax handling. use supplied private key bindings **only**; do **not** choose a configuration source, schema, permission **or** public value codec.
- require an exact baseline byte round trip **before** applying a changed proposal. refuse a representation that the selected library normalizes **or** cannot preserve; do **not** hide drift with a whole-document rewrite.
- use concrete-syntax edits confined **to** the explicit changed occurrence. an item edit **must not** become a whole-collection replacement; whole-set replacement requires the separately supplied whole-set delta.
- independently parse the complete proposed bytes **and** compare complete native values **and** types against the explicit intended result. preserve unrelated bytes **and** meanings. refuse malformed, duplicate, ambiguous, unsupported **or** lossy materialization.
- retain exact no-op source bytes **without** serialization **or** a fictitious effect. the library is needed **only** for changed materialization; effect-free Read **and** no-op do **not** acquire another runtime prerequisite through this selection.

## Details

CA-D-632 owns the dependency, private Implementation **and** evidence Carrier bindings. CA-E-635 checks preservation, refusal **and** no-op; CA-E-254 checks the complete technical exception. receiving Workflows retain complete schema, protected/generated-field, currentness **and** permission decisions under CA-R-1935 **and** CA-M-375.

the Operator authorized this bounded selection under CA-P-2307. independent source acceptance **and** the affected approved FPF review remain required **before** dependent implementation. implementation, local execution evidence **and** runtime admission are PENDING; this Method reports **none** of them as accepted.

this selection introduces no Tool, CLI, transport, changed public request/result, storage writer, history, Version/time policy, automatic retry, publication mechanism, installed activation **or** Core migration.

### Selection evidence

the [tagged upstream package metadata](https://raw.githubusercontent.com/python-poetry/tomlkit/0.15.1/pyproject.toml) identifies the selected package; its [license](https://raw.githubusercontent.com/python-poetry/tomlkit/0.15.1/LICENSE) is distribution evidence. upstream declarations are **not** proof of byte preservation **or** accepted local execution.
