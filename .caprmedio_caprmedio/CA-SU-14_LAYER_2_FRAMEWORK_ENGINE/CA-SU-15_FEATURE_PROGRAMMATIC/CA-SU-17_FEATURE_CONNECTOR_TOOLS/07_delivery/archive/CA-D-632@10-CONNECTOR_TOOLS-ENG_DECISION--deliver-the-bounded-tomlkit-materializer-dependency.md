---
atom_id: CA-D-632@10
content_role: Delivery
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Pure TOML Materializer Dependency Boundary
  depends_on:
  - Subject/Domain/Node/Continuant/Governing Configuration
  - Subject/Engineering/Carrier
  - Subject/Engineering/Implementation
  - Subject/Engineering/TOML Materialization
version: 10
updated_at: 2026-10-24 10:48:25 +0400
relations:
  delivery_for:
  - CA-R-1936
  depends_on:
  - CA-M-383
  - CA-D-250
  - CA-E-254
type: Eng Decision
tier: 5
---
# Summary

deliver the bounded TOMLKit materializer dependency

## Scope

the technical dependency exception **and** private pure TOML materializer Carriers selected by CA-M-383. this Delivery does **not** change the common logical connector interface **or** install a runtime.

## Claim

the bounded TOMLKit dependency record **must** bind its selecting Method CA-M-383, capability, exact canonical configuration/lock evidence, private interface, boundary cost, Operator selection **and** Evaluation evidence under CA-E-635 **and** CA-E-254.

- the canonical technical configuration remains root `pyproject.toml`. its named `connector-toml` dependency group carries the exact TOMLKit pin; root `uv.lock` carries the matching resolved package **and** artifact hashes. `required_runtime_dependencies = []`, existing groups **and** supported Python selection remain unchanged. another dependency **or** widened consumer requires separate admission.
- the private Implementation Carrier is `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/connector_toml_carrier.py`. its in-memory `materialize_toml` interface receives complete source bytes, explicit pure delta **and** private key bindings; it returns proposed bytes, complete native values **and** effective diff **or** a truthful refusal. the path is the existing TOOLS implementation boundary, **not** activation of CONNECTOR_TOOLS' future Delivery root.
- source bytes **and** native TOML values stay private inputs/results. the callable creates no public typed TOML encoding, logical target, schema authority, permission reference, outer service envelope **or** observed write effect.
- adjacent focused tests **and** `tests/test_connector_toml_carrier_independent.py` carry literal before/proposed byte ledgers, complete type/value checks, refusal **and** no-op controls. test execution **and** dependency caches use Project Temporary State, **not** governed source **or** runtime state.
- the boundary cost is one scoped third-party parse/edit/serialization dependency for changed pure materialization. Read **and** no-op retain the standard-library path; no launcher, installer, existing unrelated group **or** runtime image is changed by this Delivery. packaging retains upstream license notices **when** that separately admitted distribution includes the dependency.

## Details

the Operator-approved selection is recorded under CA-P-2307. this active source record defines the exception; it does **not** substitute for its accepted materialization. actual configuration, lock, Implementation **and** execution evidence are PENDING. each later acceptance record identifies exact source/code/configuration/lock/test pins, interpreter/dependency version, command, result **and** limits; absent evidence remains unavailable.

CA-D-250 retains ownership of the technical configuration Carrier **and** its declared dependency-record/Evaluation locations. this Delivery does **not** relocate those roots **or** claim they are installed. CA-E-254 blocks an incomplete exception. independent source acceptance **and** the affected Operator-approved FPF review precede dependent implementation; local tests do **not** establish installed admission.

CA-D-625 **and** CA-D-631 remain unchanged. receiving Project Structure **and** Project Settings Workflows retain source/schema/currentness/permission decisions; storage publication, Run recording, live routing, Core migration **and** stronger publication guarantees remain outside this exception.
