# CAPRMEDIO

**The Graph-Driven Development Framework**

## The Goal

If it can be built, CAPRMEDIO should help anyone build it if they are willing to invest the time and effort.

In practice, it should make AI-assisted development reliable from the first idea to production without losing meaning, traceability, or learning.

## What CAPRMEDIO is

CAPRMEDIO stores project knowledge as small artifacts connected by typed links. Humans and AI use this graph to understand the project, make changes, check consistency, and generate useful views.

The name describes four connected parts:

- **CAP** — tasks: Concern, Analysis, and Plan.
- **RMED** — the specification: Requirement, Method, Evaluation, and Delivery.
- **I** — the actual code.
- **O** — evidence from running and using it.

## Current boundaries

- More than one person can use CAPRMEDIO on a project, but the framework does not yet provide native support for team workflows.
- CAPRMEDIO is not only local-first; it is currently local-only.

## Status

The current released version is declared in [version.toml](version.toml). The framework foundation is under active development; this is not yet a complete production toolchain.

## Why graph-driven

1. **Vibe coding is unreliable.** Prompts and decisions live inside a session, while LLM context is temporary.
2. **Spec-driven development is better, but specs become monoliths.** They grow hard to read, write, structure, and maintain—and consume too many tokens, too much time, and too much money.
3. **TDD, development loops, agentic workflows, RAG, and memory systems all help, but each solves only part of the problem.** None of them alone preserves the project’s meaning, structure, and traceability.
4. **For now, graph-driven development is the only approach that solves the whole problem.** It keeps knowledge in small artifacts with explicit relations, loads only the context needed for the current task, and reconstructs the larger picture when required.

## Framework model

CAPRMEDIO keeps three axes independent:

```text
Artifact form × Content role × Governance locus
```

### Artifact form

- **Atom** — one independently governed unit.
- **Journal** — an append-only sequence of records.
- **Projection** — a generated, non-authoritative view.

### Content role

```text
O → C → A? → P → RMED → I → O
```

Reasoning may remain in the operator’s mind, exist ephemerally in a session, happen in an unrecorded discussion, or be preserved in an Analysis Atom. In the flow, `A?` marks that a governed Analysis Atom may or may not be present.

| Role | Owns | Coordinate |
|---|---|---|
| **Concern** | A matter to resolve | Priority |
| **Analysis** | Preserved investigation and reasoning | — |
| **Plan** | Accepted short-lived change steps | Priority |
| **Requirement** | What the project must, may, or must not provide | Tier |
| **Method** | How accepted work will be done | Tier |
| **Evaluation** | How claims are checked | Tier |
| **Delivery** | Release, deployment, installation, and rollback | Tier |
| **Implementation** | The actual code | — |
| **Ops** | Evidence from running and using the system | — |

Requirement is the only universally mandatory Atom role.

### Governance locus

- **Internal** — this project owns the meaning.
- **External** — an identified external source owns the meaning.
- **Relation** — the meaning exists between explicit endpoints.

## Project structure

Project Layers are ordered. Project-owned and Layer-owned Features are not.

```text
001_FRAMEWORK_METHODOLOGY/       — Framework Methodology: defines framework rules and methods without I/O.
002_FRAMEWORK_ENGINE/       — Framework Engine: applies the methodology through executable interfaces.
├── SKILLS/       — Skills: give operators and LLMs the primary framework interface.
├── TOOLS/        — Tools: find, check, and change CAPRMEDIO source artifacts.
└── APPS/         — Applications and agent-host plugin packages.
    ├── GRAPH_APP/          — Graph App: indexes sources and serves database-backed local views.
    └── AGENT_HOST_PLUGINS/ — Agent Host Plugins: package CAPRMEDIO for supported agent hosts.
        └── CODEX_PLUGIN/   — Codex Plugin: provides the Codex-specific plugin package and host wiring.
003_OPERATOR_DOCUMENTATION/    — Operator Documentation: explains how declared operators use and control the framework.
004_CORE_EXTENSIONS/         — Core Extensions Layer: contains CAPRMEDIO-owned extension capabilities.
005_RELEASES/                — Releases Layer: packages and publishes versioned framework changes.
010_COMMUNITY_EXTENSIONS/    — Community Extensions Feature: catalogs externally maintained extensions.
010_FIELD/                   — Field Feature: captures evidence and feedback from operating CAPRMEDIO instances.
```

## Principles

1. **The graph is the operating model.** Framework work reads or changes the typed project graph.
2. **Use only necessary complexity.** Add a mechanism only when it preserves an important distinction or required result.
3. **Scale through structure.** Manage growing information through structure and selective views, not by losing it.
4. **Extend without redefining.** Extensions add capabilities through explicit extension points without copying core authority.
5. **Configure without changing meaning.** Projects may select, combine, tune, or disable available capabilities while preserving their meaning.
6. **MECE.** When a model claims to cover a whole area, its parts must not overlap or leave gaps.
7. **DRY.** Keep one canonical owner for each meaning. Other uses reference, derive, generate, or adapt it.
8. **Make claims testable.** Every governed claim needs a condition that can show it is false, unmet, or out of scope.
9. **State reliance boundaries.** Say what evidence permits reliance and what must stop, block, degrade, or reopen it.
10. **Keep the core discipline-independent.** Adapt disciplines through Extensions and Project Adaptations without changing the core model.
11. **Keep substrates replaceable.** Authority must not depend on one operating system, language, model, provider, or agent host.
12. **Preserve operator sovereignty.** The operator controls the whole project and every CAPRMEDIO Artifact.
13. **Organize authority as a hierarchy.** Governed authority forms explicit, configurable hierarchies inside the typed graph.
14. **Improve from observed results.** Turn material project outcomes into evaluated improvements at the narrowest affected scope.

## Governance

META defines meanings and invariants. GOV defines deterministic repository rules. The complete active authority lives in [.caprmedio](.caprmedio/); this README is only a short introduction.

## Thanks

- **[Anatoly Levenchuk](https://t.me/ailev_blog)**, creator of the [First Principles Framework](https://github.com/ailev/FPF). I could never have built this project without FPF. I also maintain an [LLM-friendly FPF knowledge-graph toolkit](https://github.com/anatoly-m-maslennikov/levenchuk-fpf-knowledge-graph-toolkit).
- **[Daniel Kravtsov](https://improvado.io/blog-authors/daniel-kravtsov)**, CEO and co-founder of [Improvado](https://improvado.io/company/about), for giving me the challenge of building a knowledge graph for my team. It showed me what graphs can achieve in practice. At Improvado, I also tried for the first time to build an internal product both with AI and by AI.
- **[Andrej Karpathy](https://en.wikipedia.org/wiki/Andrej_Karpathy)**, for his fresh ideas—especially about graphs. His [LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) says it vividly: “Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.” His [Software 3.0 talk](https://www.youtube.com/watch?v=XdbpCM4yGyE) develops the graph perspective further.
- **[Ivan Petrovich Churukhov](https://lad24.ru/about#lider)**, for showing me how to think openly, structure ideas clearly, and apply them to real business problems.
- **[Professor Nikolai Sergeevich Stepanov](https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B5%D0%BF%D0%B0%D0%BD%D0%BE%D0%B2,_%D0%9D%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B9_%D0%A1%D0%B5%D1%80%D0%B3%D0%B5%D0%B5%D0%B2%D0%B8%D1%87)** and the Radiophysics Faculty, for teaching both the laws of physics and how each law was found and formed. That became a foundation for my systems thinking and showed me how to create something truly new.
- **[Dmitry Yurievich Kuznetsov](https://xn----7sb3aehik9cm.xn--p1ai/sotrudniki/dmitrij-yurevich-kuzneczov/)**, for the mathematics olympiad community around him, where as a teenager I had the joy of learning among curious, highly intellectual, and motivated peers—and of sharing their love for solving purely abstract mathematical problems.

## History

The project evolved from **DSET** to **CARMADIO** to **CAPRMEDIO** as its semantic model became clearer.
