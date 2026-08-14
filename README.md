# CAPRMADIO

**The Vibe-Code-to-Production Framework**

CAPRMADIO is a governed framework for carrying AI-assisted software work from an initial concern to production operation without losing intent, rationale, specification, assurance, delivery controls, implementation traceability, or operational feedback.

CAPRMADIO expands to **Concern–Analysis–Plan–Requirement–Method–Assurance–Delivery–Implementation–Ops**. The name describes how the framework achieves its outcome; “vibe code to production” describes the outcome itself.

## Status

The current version is **0.3.10**.

The META and GOV foundation is mostly finalized. It now establishes the core semantics, invariants, carrier rules, naming, lifecycle, provenance, scope, and traceability model. The reusable methodology, tools, skills, profiles, adapters, assurance assets, and documentation are the next implementation surface; their root folders are intentionally empty placeholders while the new foundation is applied.

This is therefore a framework-foundation release, not yet a claim that the complete end-user toolchain is implemented or production-proven.

## The CAPRMADIO loop

CAPRMADIO separates nine noun-named Content roles:

| Role | Owns |
|---|---|
| **Concern** | A question, problem, risk, opportunity, conflict, or other matter requiring disposition |
| **Analysis** | Investigation, synthesis, alternatives, explanation, and rationale |
| **Plan** | Short-lived accepted action points for changing governed artifacts or their realization |
| **Requirement** | What the product or project must, may, or must not provide |
| **Method** | How an accepted Requirement will be realized or an existing realization transformed |
| **Assurance** | How the project establishes that governed claims and their realization work as intended |
| **Delivery** | Packaging, release, deployment, distribution, installation, migration, upgrade, and rollback |
| **Implementation** | The actual project realization outside `.caprmadio/` |
| **Ops** | Factual results from execution and use, including evidence, logs, incidents, and verification outcomes |

The canonical forward loop is:

```text
Concern → Analysis → Plan → Requirement → Method → Assurance
        → Delivery → Implementation → Ops → Concern
```

The framework name can also be read as **CAP · RMAD · IO**:

- **CAP** develops and accepts the work to perform.
- **RMAD** is the distributed Specification: what should exist, how it should be realized, how it will be assured, and how it reaches users.
- **IO** connects the native project realization to operational facts and new concerns.

Requirement is the only universally mandatory Atom role. Other roles are introduced when the work needs them, but anything created under a role must keep that role’s canonical meaning.

## The framework axes

CAPRMADIO keeps independent classifications independent.

### Content role

The nine Content roles above state the artifact’s primary semantic contribution. A role is not inferred from workflow state or file format.

### Artifact form

Every governed artifact has one form:

- **Atom** — the smallest independently governed unit under its role’s atomicity model, with a stable identity and an indivisible lifecycle.
- **Journal** — an ordered append-only sequence of admitted records.
- **Projection** — a reproducibly generated, non-authoritative view over declared governed sources. Projections are never directly edited.

### Structural scope

Structural scope says where authority applies:

- **Layer** — an ordered vertical boundary. Dependencies flow forward through the layer order, never backward.
- **Feature** — a horizontal product or framework capability within a layer. Features may have explicit lateral contracts.

Layers and Features use a flat numbered storage layout. Features in SPEC and IMPLEMENTATION share the canonical set: Methodology, Tools, Skills, Profiles, Adapters, Assurance, and Documentation.

### Subject scope

`subject_scopes` identify what an Atom is about inside its structural scope. Subjects improve focused discovery and review; they do not duplicate or replace the Layer, Feature, Content role, or carrier location.

### Applicability tier

RMAD Atoms may distinguish:

- **principle** — an abstract rule that governs the current project;
- **core** — a rule applying to the Atom’s full current structural scope;
- **standard** — a rule applying to a narrower subsegment.

Default values are omitted from frontmatter rather than repeated.

## Governance model

META owns the meanings and invariants that every later layer must obey. GOV turns those semantics into deterministic repository conventions: carrier placement, identifiers, filenames, frontmatter, lifecycle directories, relations, provenance, and validation rules.

### Main META principles

The active META principle tier establishes eight project-wide rules:

1. **MECE canonical decompositions.** Every taxonomy or decomposition that claims complete coverage must be non-overlapping and complete inside an explicit boundary. Independent questions belong on independent axes; MECE does not require every Cartesian combination to exist.
2. **Human comprehension and decisive structure.** Present the smallest structure that lets the intended reader understand, review, and act. Add terminology, metadata, hierarchy, or ceremony only when it exposes a materially useful distinction, boundary, obligation, or action.
3. **Strict semantic distinctions.** Keep independently governed meanings separate even when one document, workflow, or code change presents them together. A Requirement is not a Method, a Method is not its Implementation, Assurance is not its result, provenance is not evidence, and observation is not authority.
4. **Materially distinct constructs only.** Add a durable Type, relation, axis, scope, Layer, Feature, or lifecycle state only when the existing model would lose a reviewable distinction and the addition has a sharp, action-facing inclusion and exclusion boundary.
5. **Bounded meaning across structural scales.** Preserve meaning and explicit applicability when authority is inherited, specialized, overridden, or summarized across project, Layer, Feature, and deeper configured scopes. Recursion never widens authority, evidence, Assurance, or Implementation coverage.
6. **Falsifiable claims and stop conditions.** State what could disconfirm an empirical claim and what must stop, degrade, block, or reopen work. Missing, unknown, or contradictory required input fails closed at the affected use.
7. **DRY governed meaning.** Store governed meaning once under one canonical owner. Other uses reference, derive, generate, or adapt it; necessary materialized copies remain non-authoritative and declare how they are regenerated or reconciled.
8. **Semantic irreducibility.** Keep only content whose removal would cause material semantic or operational loss to the Atom’s role-specific unit. Use canonical terms and relations instead of creating a second authority; keep rationale in Analysis.

Core META rules apply these principles through one independently replaceable claim per RMAD Atom, code-agnostic Requirements, active-to-active RMAD lineage, forward-only Layer dependencies, Git-backed revision history, governed Journals, generated Projections, and Exploration Mode for questions and ideas.

The framework applies recursively: CAPRMADIO governs its own development using the same META and GOV rules it provides to other projects.

## Repository structure

The repository separates the applied project control plane from the reusable framework implementation.

```text
.caprmadio/
├── 000_caprmadio_framework/     # relative links to reusable root sources
├── 100_LAYER_1_META/
├── 200_LAYER_2_GOV/
├── 300_LAYER_3_SPEC/
├── 301_FEATURE_METHODOLOGY/
├── 302_FEATURE_TOOLS/
├── 303_FEATURE_SKILLS/
├── 304_FEATURE_PROFILES/
├── 305_FEATURE_ADAPTERS/
├── 306_FEATURE_ASSURANCE/
├── 307_FEATURE_DOCUMENTATION/
├── 400_LAYER_4_IMPLEMENTATION/
├── 401_FEATURE_METHODOLOGY/
├── 402_FEATURE_TOOLS/
├── 403_FEATURE_SKILLS/
├── 404_FEATURE_PROFILES/
├── 405_FEATURE_ADAPTERS/
├── 406_FEATURE_ASSURANCE/
├── 407_FEATURE_DOCUMENTATION/
├── 500_LAYER_5_DELIVERY/
└── 600_LAYER_6_OPS/

01_METHODOLOGY/
02_TOOLS/
03_SKILLS/
04_PROFILES/
05_ADAPTERS/
06_ASSURANCE/
07_DOCUMENTATION/
README.md
LICENSE
version.md
```

All governed project artifacts live under `.caprmadio/`. Runtime state, caches, and disposable script outputs belong under `.caprmadio_runtime/`, with one runtime folder per script.

The visible numbered root folders are the reusable framework’s native Implementation. In this self-hosting repository, `.caprmadio/000_caprmadio_framework/` contains relative links to those sources for convenient recursive use; it is not a mirrored copy. Project-specific version, release, and changelog material is not part of that reusable link set.

## Repository history

The framework was renamed twice as its semantic model became clearer:

1. **DSET** established the initial production-oriented framework.
2. **CARMADIO** aligned the name with the expanded Content-role model.
3. **CAPRMADIO** added Plan as an independent role between Analysis and the distributed RMAD Specification.

Historical names remain meaningful only in archived history. CAPRMADIO is the current framework and repository identity.

## Acknowledgments

CAPRMADIO owes an enormous intellectual debt to **Anatoly Levenchuk** and the **First Principles Framework (FPF)**. Without FPF’s disciplined approach to ontology, distinctions, boundaries, reasoning, and engineering knowledge, I would not have been able to develop this framework. My deepest thanks to Anatoly Levenchuk for creating FPF and making it publicly available.

- [Original First Principles Framework by Anatoly Levenchuk](https://github.com/ailev/FPF)
- [My LLM-friendly FPF knowledge-graph toolkit](https://github.com/anatoly-m-maslennikov/levenchuk-fpf-knowledge-graph-toolkit)

## Next vertical cut

The next cut will populate the seven reusable implementation surfaces and prove one complete path from project initialization through governed work, assurance, delivery, and operational feedback. Until that proof exists, this repository intentionally distinguishes a coherent foundation from a finished toolchain.
