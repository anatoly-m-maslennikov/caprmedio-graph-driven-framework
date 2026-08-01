# DSET Spec Loops

DSET — **Domain, Supportability, Evals, Tests** — is a framework for making
AI-assisted software work reviewable: explicit domain truth, governed
decisions, supportability, deterministic tests, qualitative evaluations, and
evidence stay connected through a specification loop.

This repository is the public source for the reusable methodology, its Python
toolchain, schemas, templates, and 19 skill-source folders. Source presence
does not claim that skills are installed, released, or proven on a host.

## Current model

The target semantic topology is:

```text
META → GOV → SPEC → PROFILES → IMPL → OPS
```

The physical reusable root and applied project still use legacy `TOOL` and
`SKILL` layer names. Their migration to the target topology is open under
[`CARMADIO-PROBLEM-GOV-010`](.dset/102_layer_gov/problem/CARMADIO-PROBLEM-GOV-010-control-plane-uses-retired-layer-layout.md);
the names above do not assert that the migration is complete.

DSET separates a persisted artifact's revision mode from its meaning:

- `atomic` is one immutable governed unit;
- `append_only` preserves complete records in order; and
- `maintained` permits governed revision.

Implementation is a Content role for native project material such as code,
configuration, migrations, and test or evaluation implementations; it is not
a revision mode. META and GOV are currently in an atomic-only phase. This
README makes no active lifecycle-event claim.

The accepted vocabulary has seven Content roles and three Governance loci, but
the complete route/type catalog is not yet defined. The active boundaries are
recorded by:

- [`CARMADIO-PROBLEM-GOV-009`](.dset/102_layer_gov/problem/CARMADIO-PROBLEM-GOV-009-semantic-route-catalog-remains-incomplete.md)
  through [`CARMADIO-PROBLEM-GOV-012`](.dset/102_layer_gov/problem/CARMADIO-PROBLEM-GOV-012-atomic-identities-use-retired-grammar.md); and
- [`CARMADIO-QUESTION-GOV-013`](.dset/102_layer_gov/question/CARMADIO-QUESTION-GOV-013-which-artifact-subtypes-should-refine-route-types.md),
  [`015`](.dset/102_layer_gov/question/CARMADIO-QUESTION-GOV-015-what-external-review-envelope-is-sufficient.md),
  [`016`](.dset/102_layer_gov/question/CARMADIO-QUESTION-GOV-016-how-should-proof-currentness-be-represented.md), and
  [`017`](.dset/102_layer_gov/question/CARMADIO-QUESTION-GOV-017-which-types-complete-the-semantic-route-catalog.md).

There is therefore no canonical full type matrix here.

## Repository map

| Surface | Purpose |
|---|---|
| [Project](10_project/000_dset-project-hub.md), [META](11_layer_meta/000_dset-meta-hub.md), [GOV](12_layer_gov/000_dset-gov-hub.md) | Reusable source and governance roots |
| [TOOL](13_layer_tool/000_dset-tool-hub.md), [SKILL](14_layer_skill/000_dset-skill-hub.md), [IMPL](15_layer_implementation/000_dset-implementation-hub.md), [OPS](16_layer_ops/000_dset-ops-hub.md) | Current physical reusable-layer hubs |
| [Skills source catalog](skills/README.md) | The 19 agent-facing skill sources and their boundaries |
| [Python toolchain](dset_toolchain/) | Local executable implementation |
| [Migration tools](15_layer_implementation/tools/migrations/README.md) | Bounded internal migration tooling, not a general public migration service |
| [Delivery policy](.github/DELIVERY.md) | Repository delivery and publication boundary |
| [Project control hub](.dset/CARMADIO-CONTROL-HUB.md) | This repository's applied DSET control plane |

## Settings and baseline

The sole settings carrier is
[`.dset/dset_settings.toml`](.dset/dset_settings.toml), which declares schema
`1.8`. The coordinated package baseline is `0.3.1`. Neither fact proves a full
implementation, an exact repository head, verification, or release readiness.

## Methodology synchronization

Framework maintainers may inspect and explicitly synchronize reusable source
into the installed project-local methodology:

```bash
python -m dset_toolchain methodology check .
python -m dset_toolchain methodology sync .
python -m dset_toolchain methodology sync . --execute
```

Synchronization is explicit and one-way: source edits do not automatically
rewrite `.dset/000_dset_methodology/`, and installed files are not copied back
to the reusable root. Review the preview before using `--execute`.

Supportability remains a cross-cutting requirement: production work needs the
logs, provenance, state, and runbook context required to investigate and
repair failures. DSET is intended to expand through bounded, evidence-backed
adoption rather than documentation alone.
