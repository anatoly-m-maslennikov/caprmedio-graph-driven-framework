# CARMADIO

**The Vibe-Code-to-Production Framework**

CARMADIO — **Concern–Analysis–Requirement–Method–Assurance–Delivery–Implementation–Ops** — is a governed framework for carrying AI-assisted software work from an initial concern to production operation without losing the decisions, proof, delivery controls, or evidence needed to trust and maintain it.

The framework keeps desired outcomes separate from construction choices, assurance plans, delivery mechanisms, concrete implementation, and observed operational facts. That separation lets teams move quickly while retaining explicit authority, traceability, reviewability, and stop conditions.

## How CARMADIO works

CARMADIO classifies the primary contribution of governed work through eight Content roles:

| Role | Governs |
|---|---|
| Concern | A question, problem, risk, opportunity, conflict, or other matter requiring disposition |
| Analysis | Interpretation and understanding that inform a decision without independently establishing the desired result |
| Requirement | An outcome, obligation, or externally observable boundary the product or project must, may, or must not satisfy |
| Method | How an accepted Requirement will be realized or how an existing realization will be transformed |
| Assurance | How the project can establish that a Requirement, Method, Delivery path, or Implementation works as intended |
| Delivery | Packaging, release, deployment, distribution, installation, migration, upgrade, and rollback to end users |
| Implementation | Concrete code, configuration, schemas, executable tests and evaluations, packages, installers, and automation |
| Ops | Factual results from execution and use, including test results, delivery outcomes, runtime evidence, logs, incidents, and verification outcomes |

Governed artifacts take one of three forms: an **Atom** owns one independently replaceable claim, a **Journal** preserves an ordered append-only record, and a **Projection** provides a rebuildable non-authoritative view or an unaccepted planning surface. Applicable Requirement, Method, Assurance, and Delivery Atoms collectively form the distributed normative specification; Implementation realizes it, while Ops records what actually happened.

The ordered realization topology is:

```text
META → GOV → SPEC → PROFILES → IMPL → OPS
```

META owns universal meanings and invariants; GOV owns carriers, identity, lifecycle, provenance, applicability, and conflict governance; SPEC owns current project obligations and accepted choices; PROFILES owns selectable implementation and environment policies; IMPL owns concrete realization; and OPS owns delivery, release, runtime supportability, recovery, and hosted evidence.

For the current governed model, start with the [CARMADIO identity requirement](.carmadio/101_layer_meta/decision/CARMADIO-REQUIREMENT-META-087-carmadio-framework-identity.md) and the [active META Atom Catalog](.carmadio/101_layer_meta/CARMADIO-META-CATL-001-requirement--active-atoms-by-subject-scope.md).

## Repository contents

This repository is the public source for the reusable CARMADIO methodology, its Python toolchain, schemas, templates, tests, and 19 agent-facing skill-source folders. Source presence does not claim that a skill is installed, a package is released, or a workflow has been proven on a particular host.

| Surface | Purpose |
|---|---|
| [Project control hub](.carmadio/CARMADIO-CONTROL-HUB.md) | Applied CARMADIO settings, installed methodology, governed artifacts, and project truth |
| [Reusable source hubs](10_project/000_dset-project-hub.md) | Framework source; several carrier names remain from the pre-CARMADIO layout |
| [Skills source catalog](skills/README.md) | The 19 portable workflow skill sources and their boundaries |
| [Python toolchain](dset_toolchain/) | Local executable implementation |
| [Tests](tests/) | Deterministic toolchain and contract checks |
| [Migration tools](15_layer_implementation/tools/migrations/README.md) | Bounded internal migration tooling, not a general public migration service |
| [Delivery policy](.github/DELIVERY.md) | Repository delivery and publication boundary |

Every current governed project artifact lives under `.carmadio/`. Disposable and runtime-writing state is isolated under `.carmadio_runtime/`.

## Current migration boundary

CARMADIO is the canonical framework and repository identity. The Python distribution name `dset-spec-loops`, module `dset_toolchain`, CLI command `dset`, and some reusable-source carriers still retain legacy names for compatibility while their governed migration remains incomplete. Do not interpret those retained implementation identifiers as a second framework identity.

The settings carrier is [`.carmadio/carmadio_settings.toml`](.carmadio/carmadio_settings.toml), currently using settings schema `1.8`. The coordinated framework and Python-package baseline is `0.3.1`. These versions identify the declared baseline; they do not by themselves prove verification or release readiness.

## Methodology synchronization

Framework maintainers can inspect and explicitly synchronize reusable source into the installed project-local methodology:

```bash
python -m dset_toolchain methodology check .
python -m dset_toolchain methodology sync .
python -m dset_toolchain methodology sync . --execute
```

Synchronization is explicit and one-way: source edits do not automatically rewrite `.carmadio/000_carmadio_methodology/`, and installed files are not copied back to the reusable root. Review the preview before using `--execute`.

Supportability is not an afterthought: production work needs enough logs, provenance, state, and runbook context to investigate, contain, and repair failures. CARMADIO is intended to grow through bounded, evidence-backed adoption rather than documentation claims alone.
